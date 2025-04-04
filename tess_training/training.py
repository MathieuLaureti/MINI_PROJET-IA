import os
import subprocess
import random
import string
import shutil
from pathlib import Path

def generate_random_text(num_words=100, allow_numbers=False, allow_punctuation=False):
    """Generate random text for training."""
    words = []
    for _ in range(num_words):
        word_length = random.randint(2, 10)
        chars = string.ascii_lowercase
        if allow_numbers:
            chars += string.digits
        if allow_punctuation:
            chars += string.punctuation
        
        word = ''.join(random.choice(chars) for _ in range(word_length))
        words.append(word)
    
    # Group into sentences
    sentences = []
    while words:
        sentence_length = min(random.randint(3, 8), len(words))
        sentence = ' '.join(words[:sentence_length])
        sentences.append(sentence + '.')
        words = words[sentence_length:]
    
    return ' '.join(sentences)

def create_tesseract_traineddata(font_path, font_size, num_images, lang_name, output_dir=None):
    """
    Automate the process of creating a Tesseract traineddata file for a specific font.
    
    Args:
        font_path (str): Path to the font file (.ttf)
        font_size (int): Font size to use for training
        num_images (int): Number of training images to generate
        lang_name (str): Name for the output language file (e.g., 'eng_arial')
        output_dir (str, optional): Directory to store output files. Defaults to a temp directory.
        
    Returns:
        str: Path to the generated .traineddata file
    """
    # Set up directories
    if output_dir is None:
        output_dir = f"./tesseract_training_{lang_name}"
    
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True, parents=True)
    
    # Temporary working directory
    work_dir = output_dir / "training"
    work_dir.mkdir(exist_ok=True)
    
    try:
        # 1. Generate training text and images
        print(f"Generating {num_images} training images...")
        image_paths = []
        
        for i in range(num_images):
            # Generate random text
            text_content = generate_random_text()
            text_file = work_dir / f"text_{i}.txt"
            with open(text_file, 'w', encoding='utf-8') as f:
                f.write(text_content)
            
            # Generate image from text
            output_base = work_dir / f"train_{i}"
            cmd = [
                'text2image',
                f'--text={text_file}',
                f'--font={font_path}',
                f'--ptsize={font_size}',
                f'--outputbase={output_base}'
            ]
            
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            image_paths.append(f"{output_base}.tif")
            
        # 2. Generate box files for each image
        print("Generating box files...")
        for image_path in image_paths:
            image_base = Path(image_path).stem
            cmd = [
                'tesseract',
                image_path,
                str(work_dir / image_base),
                'batch.nochop',
                'makebox'
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # 3. Create training data
        print("Creating training data...")
        
        # Create list file (training manifest)
        list_file = work_dir / f"{lang_name}.training_files.txt"
        with open(list_file, 'w') as f:
            for i in range(num_images):
                f.write(f"{work_dir}/train_{i}\n")
        
        # Extract and shape features
        cmd = [
            'lstmtraining',
            f'--traineddata={work_dir}/{lang_name}.traineddata',
            '--net_spec=[1,36,0,1Ct3,3,16Mp3,3Lfys64Lfx96Lrx96Lfx512O1c1]',
            f'--model_output={work_dir}/{lang_name}',
            f'--learning_rate=0.001',
            f'--train_listfile={list_file}',
            '--eval_listfile=',  # Empty for now
            f'--max_iterations={50 * num_images}'  # Basic estimate
        ]
        
        # First create an initial traineddata file
        cmd_init = [
            'combine_lang_model',
            '--input_unicharset=',
            f'--script_dir={work_dir}',
            f'--output_dir={work_dir}',
            f'--lang={lang_name}'
        ]
        subprocess.run(cmd_init, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Run training
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Extract the best trained model
        best_model = work_dir / f"{lang_name}_checkpoint"
        
        # Combine into final traineddata file
        output_traineddata = output_dir / f"{lang_name}.traineddata"
        cmd_combine = [
            'lstmtraining',
            f'--model={best_model}',
            f'--traineddata={work_dir}/{lang_name}.traineddata',
            f'--output_traineddata={output_traineddata}',
            '--stop_training'
        ]
        subprocess.run(cmd_combine, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        print(f"Training complete! Traineddata file created at: {output_traineddata}")
        return str(output_traineddata)
        
    except subprocess.CalledProcessError as e:
        print(f"Error during training process: {e}")
        print(f"Command output: {e.stdout}")
        print(f"Command error: {e.stderr}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Example parameters
    font_path = "C:\\Users\\mathi\\OneDrive\\GitHub\MINI_PROJET-IA\\fonts\\Roboto.ttf"
    font_size = 20
    num_images = 50
    lang_name = "Roboto_50"
    
    traineddata_path = create_tesseract_traineddata(
        font_path=font_path,
        font_size=font_size,
        num_images=num_images,
        lang_name=lang_name
    )
    
    if traineddata_path:
        print(f"Success! Copy {traineddata_path} to your Tesseract tessdata directory to use it.")