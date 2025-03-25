import pytesseract

from PIL import Image
import difflib

import difflib

def align_texts(OCR_TEXT,TRUE_TEXT):
    return OCR_TEXT,TRUE_TEXT
def get_OCR_text(image_path):
    """
    Extracts text from an image using Tesseract OCR.
    
    Args:
    - image_path (str): The path to the image file.
    
    Returns:
    - str: The extracted text.
    """
    # Load the image from the specified file
    img = Image.open(image_path)
    
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    
    return text

def compare_words(OCR_WORDS,TRUE_WORDS):
    print(len(OCR_WORDS),len(TRUE_WORDS))
    for i in range(max(len(OCR_WORDS),len(TRUE_WORDS))):
        print(i,OCR_WORDS[i],TRUE_WORDS[i])	
        
def EXTRACT_TRUE_TEXT():
    file_path = r"C:\Users\mathi\OneDrive\Documents\GitHub\MINI_PROJET-IA\test_case_text.txt"

# Step 1: Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

# Step 2: Split the text into words
    return text.split()

def OCR_TEST(name):
    path = f"test_cases\\{name}.png"
    text = get_OCR_text(path)
    return text.split()

if __name__ == "__main__":
    aligned_true, aligned_ocr = align_texts(OCR_TEST("Pacifico"),EXTRACT_TRUE_TEXT())
    compare_words(aligned_true, aligned_ocr)
    OCR_TEST("Pacifico")
    print(EXTRACT_TRUE_TEXT())
    