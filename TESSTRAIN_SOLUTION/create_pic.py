import os
import subprocess
from pathlib import Path
from PIL import Image
import shutil

# ==== CONFIGURATION ====
FONT_NAME = "Vladimir Script Regular"  # Change this to your desired font name
name = f"test\{FONT_NAME.replace(' ', '_')}"	
OUTPUT_DIR = Path(fr"C:\Users\mathi\OneDrive\Documents\GitHub\MINI_PROJET-IA\TESSTRAIN_SOLUTION\tesstrain\data\{name}")
MISC_DIR = Path(r"C:\Users\mathi\OneDrive\Documents\GitHub\MINI_PROJET-IA\TESSTRAIN_SOLUTION\tesstrain\misc")
PHRASESS = [
    "The quick brown fox jumps over the lazy dog.",
    "Tesseract OCR is amazing.",
    "0123456789 are digits.",
    "Can it read punctuation? Yes!",
    "This is a single-line example.",
    "This is a multi-phrase example. It has two phrases.",
    "Can it read special characters? Yes!",
    "abcdefghijklmnopqrstuvwxyz are lowercase letters.",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ are uppercase letters.",
    "She sells seashells by the seashore.",
    "How much wood would a woodchuck chuck?",
    "A journey of a thousand miles begins with a single step.",
    "Better late than never.",
    "Birds of a feather flock together.",
    "Actions speak louder than words.",
    "All that glitters is not gold.",
    "Practice makes perfect.",
    "You can lead a horse to water, but you can't make it drink.",
    "Beauty is in the eye of the beholder.",
    "The early bird catches the worm.",
    "Every cloud has a silver lining.",
    "Don't count your chickens before they hatch.",
    "A picture is worth a thousand words.",
    "When in Rome, do as the Romans do.",
    "The pen is mightier than the sword.",
    "Two wrongs don't make a right.",
    "The grass is always greener on the other side.",
    "Don't bite the hand that feeds you.",
    "Too many cooks spoil the broth.",
    "A watched pot never boils.",
    "Honesty is the best policy.",
    "Look before you leap.",
    "You can't judge a book by its cover.",
    "Rome wasn’t built in a day.",
    "The squeaky wheel gets the grease.",
    "Let sleeping dogs lie.",
    "Don't put all your eggs in one basket.",
    "Many hands make light work.",
    "Time flies when you're having fun.",
    "There's no place like home.",
    "Fortune favors the bold.",
    "Out of sight, out of mind.",
    "What goes around comes around.",
    "A stitch in time saves nine.",
    "Barking dogs seldom bite.",
    "Still waters run deep.",
    "Necessity is the mother of invention.",
    "Silence is golden.",
    "Knowledge is power."
]
PHRASES = [	
    "Hello, World! Is this a test?",
]

FONT_SIZE = 12
DPI = 600

# ==== SETUP ====
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(MISC_DIR, exist_ok=True)

for idx, phrase in enumerate(PHRASES):
    base_name = f"sample_{idx}"
    txt_file = OUTPUT_DIR / f"{base_name}.gt.txt"
    tif_file = OUTPUT_DIR / f"{base_name}.tif"
    png_file = OUTPUT_DIR / f"{base_name}.png"

    # Write GT text
    with open(txt_file, "w", encoding="utf-8") as f:
        f.write(phrase)

    # Generate image using text2image (outputs .tif)
    cmd = (
        f'text2image '
        f'--text="{txt_file}" '
        f'--outputbase="{OUTPUT_DIR / base_name}" '
        f'--font="{FONT_NAME}" '
        f'--ptsize={FONT_SIZE} '
        f'--resolution={DPI} '
        f'--degrade_image=false '
        f'--xsize=3000 '
        f'--ysize=300 '
        f'--leading=32 '
        f'--margin=50 '
        f'--max_pages=1'
    )
    subprocess.run(cmd, shell=True, check=True)

    # Convert TIF to PNG
    if tif_file.exists():
        with Image.open(tif_file) as im:
            im.save(png_file)
        tif_file.unlink()

# ==== MOVE NON-PNG and NON-GT FILES TO MISC ====
for file in OUTPUT_DIR.iterdir():
    if file.is_file() and not (file.suffix == ".png" or file.suffix == ".txt"):
        shutil.move(str(file), str(MISC_DIR / file.name))

print(f"\n✅ Done! PNG and GT files are saved in:\n{OUTPUT_DIR}\n📁 All other files are in: {MISC_DIR}")
