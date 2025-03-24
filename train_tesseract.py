import os
import subprocess
import shutil
from create_data import create_training_data
import datetime
directory = "fonts"
font_list = os.listdir(directory)
font_name = None
print("List of available fonts:")
for i, font in enumerate(font_list):
    print(f"{i+1}. {font}")
font_input = input("Enter the font digit : ")


font_path = os.path.join(directory, font_list[int(font_input)-1])

print(font_path)

data_size = input("Enter the number of images to generate : ")

font_name = os.path.splitext(os.path.basename(font_path))[0]

default_name = f"{font_name}_{data_size}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-1%S')}"
name = input(f"Enter a language name (default : [{default_name}]) ").strip() or default_name
print("Language Name set to:", name)


# Path to training data (images and ground truth files)
TRAINING_DATA_DIR = os.path.realpath("training_data")
MISC_DIR = os.path.join("C:\\Users\\mathi\\OneDrive\\Documents\\GitHub\\MINI_PROJET-IA\\training_data\\misc")
OUTPUT_DIR = os.path.realpath("trained_data")  # Directory to store final traineddata file
LANGUAGE = name  # Language name (can be anything, e.g., "mylang")

# Ensure directory exists
def ensure_directory_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Created directory: {dir_path}")

# Generate training files (box files and other necessary files)
def generate_training_files():
    # Get original working directory to restore later
    original_dir = os.getcwd()
    
    # Ensure the necessary directories exist
    ensure_directory_exists(MISC_DIR)
    ensure_directory_exists(OUTPUT_DIR)
    
    try:
        # Change to training data directory for processing
        os.chdir(TRAINING_DATA_DIR)
        
        # Run tesseract to generate box files and training files
        for image_file in os.listdir('.'):
            if image_file.endswith(".tif"):
                base_name = os.path.splitext(image_file)[0]
                
                # Generate box files
                command = f"tesseract {image_file} {base_name} batch.nochop makebox"
                subprocess.run(command, shell=True)
                
                # Generate tr files (kept in training_data directory)
                if os.path.exists(f"{base_name}.box"):
                    command = f"tesseract {image_file} {base_name} box.train"
                    subprocess.run(command, shell=True)
                    print(f"Generated training file: {base_name}.tr")
    finally:
        # Restore original directory when done
        os.chdir(original_dir)

# Run training commands
def run_training():
    # Get original working directory to restore later
    original_dir = os.getcwd()
    
    try:
        # First extract unicharset in the training data directory
        os.chdir(TRAINING_DATA_DIR)
        
        # Get all box files
        box_files = [f for f in os.listdir('.') if f.endswith(".box")]
        if box_files:
            # Extract unicharset
            command = f"unicharset_extractor {' '.join(box_files)}"
            subprocess.run(command, shell=True)
            
            # Copy (not move) the unicharset to misc directory
            if os.path.exists("unicharset"):
                shutil.copy("unicharset", os.path.join(MISC_DIR, "unicharset"))
                print("Copied unicharset to misc directory")
        
        # Get all tr files
        tr_files = [f for f in os.listdir('.') if f.endswith(".tr")]
        if not tr_files:
            print("No .tr files found. Make sure to generate them first.")
            return
        
        # Switch to misc directory for remaining training operations
        os.chdir(MISC_DIR)
        
        # Copy tr files to misc for training (but don't remove from original)
        for tr_file in tr_files:
            source_path = os.path.join(TRAINING_DATA_DIR, tr_file)
            shutil.copy(source_path, tr_file)
            print(f"Copied {tr_file} to misc directory for training")
        
        # Create font properties file (can be customized)
        # Extract font name from tr files
        font_name = tr_files[0].split('.')[0] if tr_files else "default"
        font_properties = f"{font_name} 0 0 0 0 0\n"
        with open("font_properties", "w") as f:
            f.write(font_properties)
        
        # Create shapetable file
        print("Creating shapetable file...")
        shapeclustering_cmd = f"shapeclustering -F font_properties -U unicharset {' '.join(tr_files)}"
        subprocess.run(shapeclustering_cmd, shell=True)
        
        # Run mftraining
        print("Running mftraining...")
        mftraining_command = f"mftraining -F font_properties -U unicharset -O {LANGUAGE}.unicharset {' '.join(tr_files)}"
        subprocess.run(mftraining_command, shell=True)
        
        # Run cntraining
        print("Running cntraining...")
        cntraining_command = f"cntraining {' '.join(tr_files)}"
        subprocess.run(cntraining_command, shell=True)
        
        # Rename the output files to have the language prefix
        print("Renaming output files...")
        if os.path.exists("inttemp"):
            shutil.copy("inttemp", f"{LANGUAGE}.inttemp")
        if os.path.exists("normproto"):
            shutil.copy("normproto", f"{LANGUAGE}.normproto")
        if os.path.exists("pffmtable"):
            shutil.copy("pffmtable", f"{LANGUAGE}.pffmtable")
        if os.path.exists("shapetable"):
            shutil.copy("shapetable", f"{LANGUAGE}.shapetable")
            
        # List all files for debugging
        print("Files in directory before combine_tessdata:")
        for file in os.listdir('.'):
            print(f"  {file}")
        
        # Combine all the files into a single traineddata file
        print("Combining tessdata files...")
        combine_tessdata_command = f"combine_tessdata {LANGUAGE}"
        result = subprocess.run(combine_tessdata_command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        print(result.stderr)
        
        # Move trained data to the output directory if created
        if os.path.exists(f"{LANGUAGE}.traineddata"):
            output_path = os.path.join(OUTPUT_DIR, f"{LANGUAGE}.traineddata")
            shutil.copy(f"{LANGUAGE}.traineddata", output_path)
            print(f"Training completed. {LANGUAGE}.traineddata saved to {OUTPUT_DIR}")
        else:
            print(f"Error: {LANGUAGE}.traineddata was not created. Check previous steps for errors.")
    finally:
        # Restore original directory
        os.chdir(original_dir)

# Run everything
generate_training_files()
run_training()