from PIL import Image, ImageDraw, ImageFont
import random
import os
import shutil


def create_test_case(font_path,output_dir):
    FONT_PATH = font_path  # Update this with your actual font path
    OUTPUT_DIR = output_dir


    if os.path.exists(OUTPUT_DIR):
        for filename in os.listdir(OUTPUT_DIR):
            file_path = os.path.join(OUTPUT_DIR, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)  # Delete file
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
    else:
        os.makedirs(OUTPUT_DIR, exist_ok=True)  

    test_phrases = [
    "The sun shines brightly in the sky, and the warmth makes everything feel alive.",
    "A cat sat lazily on the mat, enjoying the afternoon sun as it streamed through the window.",
    "Coffee is best when brewed fresh in the morning, giving you the energy to start your day right.",
    "This is a simple test, designed to challenge the mind and improve your problem-solving skills.",
    "The quick brown fox jumps over the lazy dog, showing off its agility and speed in the meadow.",
    "Life is full of surprises, and each day brings something new that can change the course of events.",
    "Water is essential for life, and without it, no living creature could survive for long in any environment.",
    "Reading books is a relaxing way to escape into another world and learn new things along the way.",
    "The train arrives at noon, just in time for the passengers to board and begin their afternoon journey.",
    "Keep moving forward, no matter how difficult the road may seem, and never look back with regret.",
    "A journey begins with a step, and every small step leads you closer to your destination and your goals.",
    "The sky is blue today, with only a few clouds drifting lazily across the expanse as the sun shines brightly.",
    "Learning never stops, and every experience brings valuable lessons that help you grow and improve.",
    "Time waits for no one, and each passing moment brings us closer to new opportunities and challenges.",
    "Hard work pays off, and through perseverance and determination, you can achieve even your most difficult goals."
]
    for index,i in enumerate(test_phrases):

        # Create a blank white image
        img = Image.new("L", (1500, 100), color=255)  # Grayscale mode (L), white background
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype(FONT_PATH, 30)  # Adjust size as needed
        except IOError:
            print(f"Error: Could not load font at {FONT_PATH}")
            break

        # Draw text in black
        draw.text((20, 20), i, font=font, fill=0)  # Position (20,20), black text
        
        # Save image and ground truth text file
        img_path = os.path.join(OUTPUT_DIR, f"case{index}.png")

        img.save(img_path)

def creation_handler(name):
    create_test_case(f"fonts\\{name}.ttf",f"test_cases\\{name}")

if __name__ == "__main__":
    name = "Shadows"

    creation_handler(name)