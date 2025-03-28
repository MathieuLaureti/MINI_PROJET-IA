import pytesseract
import editdistance
from PIL import Image

import difflib
import time


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

def remove_ponctuation(string):
    return string.replace(",", "").replace(".", "").strip()

def EXTRACT_TRUE_TEXT():
    file_path = r"C:\Users\mathi\OneDrive\Documents\GitHub\MINI_PROJET-IA\test_case_text.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines

def OCR_TEST(name,index):
    path = f"test_cases\\{name}\\case{index}.png"
    text = get_OCR_text(path)
    if text == "":
        return -1
    return text

def word_test(OCR,TRUTH):
    OCR = OCR.split(" ")
    TRUTH = TRUTH.split(" ")
    char_missed = 0
    correct_char = 0 
    word_missed = 0
    correct_word = 0

    if len(OCR) == len(TRUTH):
        for i in range(len(OCR)):
            OCR_WORD = OCR[i]
            TRUTH_WORD = TRUTH[i]
            if OCR_WORD == TRUTH_WORD:
                correct_word+=1
                correct_char+=len(TRUTH_WORD)
            else:
                word_missed+=1
                if len(OCR_WORD) == len(TRUTH_WORD):
                    for i in range(len(TRUTH_WORD)):
                        if OCR_WORD[i] == TRUTH_WORD[i]:
                            correct_char+=1
                        else:
                            char_missed+=1
                else:
                    diff = abs(len(OCR_WORD) - len(TRUTH_WORD))
                    char_missed+=diff
                    for i in range(min(len(OCR_WORD),len(TRUTH_WORD))):
                        if OCR_WORD[i] == TRUTH_WORD[i]:
                            correct_char+=1
                        else:
                            char_missed+=1
    else:
        print(OCR,TRUTH)
        for i in OCR:
            i
        return -1
    
    CER = char_missed/(char_missed+correct_char)

    WER = word_missed/(word_missed+correct_word)

    return ((CER,char_missed,correct_char),(WER,word_missed,correct_word))


# Calculate WER (Word Error Rate)
def calculate_wer(ocr, truth):
    ocr_str = ' '.join(ocr).lower()  # Join words into a string and lowercase
    truth_str = ' '.join(truth).lower()  # Same for ground truth
    error_count = editdistance.eval(ocr_str.split(), truth_str.split())  # Calculate word-level errors
    return error_count / len(truth), error_count, len(truth)

# Calculate CER (Character Error Rate)
def calculate_cer(ocr, truth):
    ocr_str = ''.join(ocr).replace(' ', '')  # Join characters and remove spaces
    truth_str = ''.join(truth).replace(' ', '')  # Same for ground truth
    error_count = editdistance.eval(ocr_str, truth_str)  # Calculate character-level errors
    return error_count / len(truth_str), error_count, len(truth_str)



def test_all_cases_for(name):
    TRUE_TEXT = EXTRACT_TRUE_TEXT()
    ans = []
    for i in range(15):
        OCR_TEXT = OCR_TEST(name,i)
        if OCR_TEXT == -1:
            continue
        else:
            truth = TRUE_TEXT[i]
            test_results = word_test(remove_ponctuation(OCR_TEXT),remove_ponctuation(truth))
            if not test_results == -1:
                ans.append(test_results)
                print(test_results)
    return ans





if __name__ == "__main__":
    ans = test_all_cases_for("Pacifico")
    

    