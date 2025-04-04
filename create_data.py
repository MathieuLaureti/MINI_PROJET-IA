from PIL import Image, ImageDraw, ImageFont
import random
import os
import shutil
from faker import Faker


def generate_sentence_with_char_count(target_char_count):
    fake = Faker()
    sentence = ''
    while len(sentence) < target_char_count:
        sentence += ' ' + fake.sentence()
    return sentence[:target_char_count]  # Truncate if exceeds target

def generate_random_string(length):
    # Define the characters you want to use (letters and digits only)
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def create_training_data(font_path,num_image):
    FONT_PATH = font_path  # Update this with your actual font path
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
        get_half_probs = random.choice([True,False])
        if get_half_probs:
            text = generate_sentence_with_char_count(80)
        else:
            text = generate_random_string(80)


        # Create a blank white image
        #random size +/- 15% of the original size 
        img = Image.new("L", (700,100), color=255)  # Grayscale mode (L), white background
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype(FONT_PATH, 30)  # Adjust size as needed
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

    print(f"Generated {NUM_IMAGES} training images with {font_path} font in {OUTPUT_DIR}/")

#create_training_data("fonts\\Dancing.ttf",10)