import os
import subprocess
import random
import re
from pathlib import Path

# === CONFIGURABLE PARAMETERS ===
NUM_IMAGES = 20
FONT_NAME = "Roboto"
FONT_PATH = f"new_LSTM_training\\fonts\\{FONT_NAME}.ttf"  # Path to the font file
FONT_SIZE = 32
LANG_NAME = FONT_NAME + "_" + str(NUM_IMAGES)
CORPUS_PATH = "new_LSTM_training\\text.txt"  # Large input text
RESOLUTION = 300
OUTPUT_DIR = f"new_LSTM_training\\languages\\{LANG_NAME}"  # Output directory for generated images

# === HELPERS ===

def extract_random_lines(corpus_path, count):
    with open(corpus_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Clean text and split into sentences
    text = re.sub(r'\s+', ' ', text)
    sentences = re.split(r'(?<=[.!?]) +', text)

    if len(sentences) < count:
        raise ValueError("Not enough unique sentences in corpus to generate desired images.")

    return random.sample(sentences, count)

def normalize_gt_line(text):
    """Normalize whitespace and ensure literal spaces are preserved for .box compatibility."""
    return text.replace("\u00A0", " ")  # No \u0020 – keep as real space

def clean_box_file(box_path):
    cleaned_lines = []
    with open(box_path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 6 and parts[0].strip():  # Skip lines with no visible character
                cleaned_lines.append(" ".join(parts))
            else:
                print(f"⚠️ Removed invalid line in {box_path.name}: {repr(line.strip())}")
    with open(box_path, "w", encoding="utf-8") as f:
        f.write("\n".join(cleaned_lines) + "\n")

# === SETUP OUTPUT DIR ===
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === WRITE font_properties FILE ===
with open(os.path.join(OUTPUT_DIR, "font_properties"), "w") as f:
    f.write(f"{FONT_NAME} 0 0 0 0 0\n")

# === GET RANDOM TEXT SNIPPETS ===
lines = extract_random_lines(CORPUS_PATH, NUM_IMAGES)

# === GENERATE IMAGES AND .lstmf ===
for i, line in enumerate(lines):
    base_name = f"{LANG_NAME}.{i}"
    base_path = os.path.join(OUTPUT_DIR, base_name)

    # Normalize and write ground truth text
    cleaned_text = normalize_gt_line(line)
    with open(base_path + ".gt.txt", "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    # Generate image using text2image
    fontconfig_tmpdir = os.path.join(OUTPUT_DIR, 'fc_tmp')
    os.makedirs(fontconfig_tmpdir, exist_ok=True)

    cmd_text2image = [
        "text2image",
        f"--font={FONT_NAME}",
        f"--fonts_dir={str(Path(FONT_PATH).parent)}",
        f"--text={base_path}.gt.txt",
        f"--outputbase={base_path}",
        f"--ptsize={FONT_SIZE}",
        f"--resolution={RESOLUTION}",
        f"--fontconfig_tmpdir={fontconfig_tmpdir}",
    ]

    print(f"[+] ({i+1}/{NUM_IMAGES}) Generating .tif/.box for {base_name}")
    try:
        subprocess.run(cmd_text2image, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError as e:
        print(f"🚨 text2image failed for {base_name}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        raise

    # Create .lstmf file using Tesseract
    cmd_tesseract = [
        "tesseract",
        base_path + ".tif",
        base_path,
        "--psm", "6", "lstm.train"
    ]
    print(f"[+] ({i+1}/{NUM_IMAGES}) Creating .lstmf for {base_name}")
    subprocess.run(cmd_tesseract, check=True)

# === CLEAN .box FILES ===
print("\n🧼 Cleaning .box files...")
box_dir = Path(OUTPUT_DIR)
for box_file in box_dir.glob("*.box"):
    clean_box_file(box_file)
    print(f"[✓] Cleaned {box_file.name}")

print("\n✅ All data (.lstmf, .tif, .box, .gt.txt) generated and cleaned in:", OUTPUT_DIR)
