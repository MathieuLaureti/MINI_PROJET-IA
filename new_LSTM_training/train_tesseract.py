import os
import subprocess
from pathlib import Path

# === CONFIGURATION ===
LANG_NAME = "roboto"  # Short lang name used in final .traineddata
OUTPUT_DIR = Path(f"new_LSTM_training\\languages\\Roboto_20")  # Folder where .lstmf and .box live
CHECKPOINT_PREFIX = OUTPUT_DIR / LANG_NAME
TRAINEDDATA_OUTPUT = OUTPUT_DIR / f"{LANG_NAME}.traineddata"
FINAL_MODEL = OUTPUT_DIR / f"{LANG_NAME}_final.traineddata"

# === PATHS ===
training_files_path = OUTPUT_DIR / "training_files.txt"
unicharset_path = OUTPUT_DIR / "unicharset"

# === STEP 1: Create training_files.txt ===
print("[✓] Generating training_files.txt...")
lstmf_files = sorted(OUTPUT_DIR.glob("*.lstmf"))
with open(training_files_path, "w") as f:
    for file in lstmf_files:
        f.write(str(file.resolve()) + "\n")

print(f"[✓] Found {len(lstmf_files)} .lstmf files")

# === STEP 2: Extract unicharset ===
print("[✓] Extracting unicharset from box files...")
box_files = list(OUTPUT_DIR.glob("*.box"))
print(box_files)
if not box_files:
    raise FileNotFoundError("No .box files found!")
cmd_unicharset = ["unicharset_extractor"] + [str(f) for f in box_files]
subprocess.run(cmd_unicharset, check=True, cwd=OUTPUT_DIR)

# === STEP 3: Create dummy traineddata ===
print("[✓] Creating dummy .traineddata...")
subprocess.run([
    "combine_lang_model",
    "--input_unicharset", str(unicharset_path),
    "--output_dir", str(OUTPUT_DIR),
    "--lang", LANG_NAME,
], check=True)

# === STEP 4: Start training from scratch ===
print("[✓] Starting LSTM training from scratch...")
subprocess.run([
    "lstmtraining",
    "--model_output", str(CHECKPOINT_PREFIX),
    "--continue_from", "",  # training from scratch
    "--traineddata", str(TRAINEDDATA_OUTPUT),
    "--train_listfile", str(training_files_path),
    "--max_iterations", "4000"
], check=True)

# === STEP 5: Finalize model ===
print("[✓] Finalizing traineddata...")
subprocess.run([
    "lstmtraining",
    "--stop_training",
    "--continue_from", str(CHECKPOINT_PREFIX) + "_checkpoint",
    "--traineddata", str(TRAINEDDATA_OUTPUT),
    "--model_output", str(FINAL_MODEL)
], check=True)

print(f"\n✅ Training complete! Your final model is saved as:\n{FINAL_MODEL}")
