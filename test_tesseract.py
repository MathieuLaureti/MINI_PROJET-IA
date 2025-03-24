import pytesseract

from PIL import Image


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

def compare_words(OCR_TEXT,TRUE_TEXT):
    """
    Compares the OCR text to the true text and returns the number of words that match.
    
    Args:
    - OCR_TEXT (str): The text extracted by OCR.
    - TRUE_TEXT (str): The true text to compare against.
    
    Returns:
    - int: The number of words that match between the two texts.
    """
    # Split the text into words
    OCR_words = OCR_TEXT.split()
    TRUE_words = TRUE_TEXT.split()
    
    # Count the number of matching words
    match_count = 0
    for word in OCR_words:
        if word in TRUE_words:
            match_count += 1
    
    return match_count

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
    print(text)

if __name__ == "__main__":
    OCR_TEST("Pacifico")
    print(EXTRACT_TRUE_TEXT())
    