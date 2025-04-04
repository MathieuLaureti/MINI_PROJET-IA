import os
import subprocess
import shutil
from create_data import create_training_data

# Configurable parameters
MAX_IMAGES_PER_BATCH = 500  # Prevents issues with too large datasets
TRAINING_DATA_DIR = os.path.realpath("training_data")
MISC_DIR = os.path.realpath("training_data/misc")
OUTPUT_DIR = os.path.realpath("trained_data")

def ensure_directory_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Created directory: {dir_path}")

def split_list(lst, batch_size):
    """Splits a list into smaller chunks."""
    for i in range(0, len(lst), batch_size):
        yield lst[i:i + batch_size]

def run_training():
    # User input
    directory = "fonts"
    font_list = os.listdir(directory)
    print("List of available fonts:")
    for i, font in enumerate(font_list):
        print(f"{i+1}. {font}")
    font_input = input("Enter the font digit: ")
    font_path = os.path.join(directory, font_list[int(font_input)-1])
    print(font_path)
    
    image_count = int(input("Enter the number of images to generate: "))
    font_name = os.path.splitext(os.path.basename(font_path))[0]
    default_name = f"{font_name}_{image_count}"
    language_name = input(f"Enter a language name (default: [{default_name}]): ").strip() or default_name
    print("Language Name set to:", language_name)
    
    # Get original working directory to restore later
    original_dir = os.getcwd()
    try:
        os.chdir(TRAINING_DATA_DIR)
        tr_files = [f for f in os.listdir('.') if f.endswith(".tr")]
        if not tr_files:
            print("No .tr files found. Ensure images were generated correctly.")
            return
        
        # Split dataset if too large
        tr_batches = list(split_list(tr_files, MAX_IMAGES_PER_BATCH))
        
        for batch_idx, batch in enumerate(tr_batches):
            print(f"Processing batch {batch_idx+1}/{len(tr_batches)} ({len(batch)} images)")
            os.chdir(MISC_DIR)
            for tr_file in batch:
                shutil.copy(os.path.join(TRAINING_DATA_DIR, tr_file), tr_file)
                print(f"Copied {tr_file} to misc directory for training")
            
            # Run training steps per batch
            subprocess.run(f"shapeclustering -F font_properties -U unicharset {' '.join(batch)}", shell=True)
            subprocess.run(f"mftraining -F font_properties -U unicharset -O {language_name}.unicharset {' '.join(batch)}", shell=True)
            subprocess.run(f"cntraining {' '.join(batch)}", shell=True)
        
        # Combine results into final traineddata file
        os.chdir(MISC_DIR)
        required_files = ["inttemp", "normproto", "pffmtable", "shapetable", "unicharset"]
        missing_files = [f for f in required_files if not os.path.exists(f)]
        if missing_files:
            print(f"⚠️ Missing files before combine_tessdata: {missing_files}")
            return
        
        subprocess.run(f"combine_tessdata {language_name}", shell=True)
        if os.path.exists(f"{language_name}.traineddata"):
            shutil.copy(f"{language_name}.traineddata", os.path.join(OUTPUT_DIR, f"{language_name}.traineddata"))
            print(f"✅ Training completed. {language_name}.traineddata saved to {OUTPUT_DIR}")
        else:
            print(f"❌ Error: {language_name}.traineddata was not created. Check logs for errors.")
    finally:
        os.chdir(original_dir)

run_training()
