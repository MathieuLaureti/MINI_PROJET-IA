import subprocess
import re
import csv
from pathlib import Path

# === CONFIGURATION ===
CHECKPOINT_DIR = Path(r"C:\Users\mathi\OneDrive\Documents\GitHub\MINI_PROJET-IA\TESSTRAIN_SOLUTION\tesstrain\data\Vladimir_Script_Regular\checkpoints")
TRAINEDDATA_PATH = Path(r"C:\Users\mathi\OneDrive\Documents\GitHub\MINI_PROJET-IA\TESSTRAIN_SOLUTION\tesstrain\data\Vladimir_Script_Regular\Vladimir_Script_Regular.traineddata")
OUTPUT_CSV = "checkpoint_metrics.csv"

# === MAIN ===
metrics = []

for ckpt in sorted(CHECKPOINT_DIR.glob("*_checkpoint_*")):
    print(f"🔍 Checking: {ckpt.name}")
    try:
        result = subprocess.run([
            "lstmtraining",
            "--debug_interval", "-1",
            "--stop_training",
            "--continue_from", str(ckpt),
            "--traineddata", str(TRAINEDDATA_PATH),
            "--model_output", "dummy_output"
        ], capture_output=True, text=True, check=True)

        for line in result.stdout.splitlines():
            if "Iteration" in line and "Training" in line:
                print("   ↳ ", line.strip())
                match = re.search(r"Iteration (\d+),.*?Training accuracy=(\d+\.\d+)", line)
                if match:
                    iteration = int(match.group(1))
                    accuracy = float(match.group(2))
                    metrics.append((iteration, accuracy))
    except subprocess.CalledProcessError:
        print(f"⚠️ Failed to process {ckpt.name}")

# === SAVE TO CSV ===
with open(OUTPUT_CSV, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["iteration", "training_accuracy"])
    writer.writerows(metrics)

print(f"\n✅ Done! {len(metrics)} entries saved to {OUTPUT_CSV}")
