from PIL import Image, ImageDraw, ImageFont
import random
import os
import shutil


def create_training_data(font_name,num_image):
    # Path to Seriffi Morgan Regular font file (.ttf or .otf)
    FONT_PATH = f"fonts/{font_name}.ttf"  # Update this with your actual font path
    OUTPUT_DIR = "training_data"
    NUM_IMAGES = num_image  # Number of training samples
    TEXT_LENGTH = 25  # Characters per image

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

    # Define characters for random text (modify as needed)
    CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    for i in range(NUM_IMAGES):
        # Generate a random text sequence
        text = ''.join(random.choices(CHARACTERS, k=TEXT_LENGTH))

        # Create a blank white image
        img = Image.new("L", (700, 100), color=255)  # Grayscale mode (L), white background
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype(FONT_PATH, 40)  # Adjust size as needed
        except IOError:
            print(f"Error: Could not load font at {FONT_PATH}")
            break

        # Draw text in black
        draw.text((20, 20), text, font=font, fill=0)  # Position (20,20), black text
        
        # Save image and ground truth text file
        img_path = os.path.join(OUTPUT_DIR, f"train{i}.tif")
        text_path = os.path.join(OUTPUT_DIR, f"train{i}.gt.txt")

        img.save(img_path)
        with open(text_path, "w") as f:
            f.write(text)

    print(f"Generated {NUM_IMAGES} training images with {font_name} font in {OUTPUT_DIR}/")


if __name__ == "__main__":
    create_training_data("Roboto",100)  # Change font name and number of images as needed