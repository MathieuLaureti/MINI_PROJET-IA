import pytesseract
import editdistance
from PIL import Image

import difflib
import time


def get_OCR_text(image_path,filename):
    """
    Extracts text from an image using Tesseract OCR.
    
    Args:
    - image_path (str): The path to the image file.
    
    Returns:
    - str: The extracted text.
    """
    # Load the image from the specified file
    img = Image.open(image_path)
    
    if not filename == -1:
        # Use Tesseract to do OCR on the image
        text = pytesseract.image_to_string(img,lang=f"{filename}")
    
        return text
    else:
        text = pytesseract.image_to_string(img,lang=f"eng")
    
        return text


def remove_ponctuation(string):
    return string.replace(",", "").replace(".", "").strip()

def EXTRACT_TRUE_TEXT():
    file_path = r"C:\Users\mathi\OneDrive\Documents\GitHub\MINI_PROJET-IA\test_case_text.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines

def OCR_TEST(name,index,filename):
    path = f"test_cases\\{name}\\case{index}.png"
    text = get_OCR_text(path,filename)
    if text == "":
        return -1
    return text

# Calculate WER (Word Error Rate)
def calculate_wer(ocr: str, truth: str):
    ocr_words = ocr.lower().split()  # Convert to lowercase & split into words
    truth_words = truth.lower().split()  # Same for ground truth
    error_count = editdistance.eval(ocr_words, truth_words)  # Compute edit distance
    return error_count / len(truth_words) if truth_words else 0, error_count, len(truth_words)

# Calculate CER (Character Error Rate)
def calculate_cer(ocr: str, truth: str):
    ocr_chars = ocr.replace(' ', '').lower()  # Remove spaces & normalize case
    truth_chars = truth.replace(' ', '').lower()  # Same for ground truth
    error_count = editdistance.eval(ocr_chars, truth_chars)  # Compute edit distance
    return error_count / len(truth_chars) if truth_chars else 0, error_count, len(truth_chars)

# Calculate MER (Match Error Rate) - Based on OCR output words instead of truth words
def calculate_mer(ocr: str, truth: str):
    ocr_words = ocr.lower().split()  # Normalize case & split words
    truth_words = truth.lower().split()  # Same for ground truth
    error_count = editdistance.eval(ocr_words, truth_words)  # Compute edit distance
    return error_count / len(ocr_words) if ocr_words else 0, error_count, len(ocr_words)




def test_all_cases_for(name,filename):
    TRUE_TEXT = EXTRACT_TRUE_TEXT()
    ans = []
    for i in range(15):
        OCR_TEXT = OCR_TEST(name,i,filename)
        if OCR_TEXT == -1:
            continue
        else:
            truth = TRUE_TEXT[i]

            CER_test_results = calculate_cer(remove_ponctuation(OCR_TEXT),remove_ponctuation(truth))
            WER_test_results = calculate_wer(remove_ponctuation(OCR_TEXT),remove_ponctuation(truth))
            MER_test_results = calculate_mer(remove_ponctuation(OCR_TEXT),remove_ponctuation(truth))
            ans.append((CER_test_results,WER_test_results,MER_test_results))
            print(CER_test_results,WER_test_results,MER_test_results)

    return ans





if __name__ == "__main__":
    ans = test_all_cases_for("Dancing","Dancing_100")
    print("___________________________________________________________________________________________")
    ans = test_all_cases_for("Dancing","Dancing_500")
    print("___________________________________________________________________________________________")
    ans = test_all_cases_for("Dancing",-1)

    

    