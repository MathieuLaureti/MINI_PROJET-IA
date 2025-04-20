import pytesseract
from PIL import Image
import os


models = {
    "Bradley_Hand_ITC",
    "Brush_Script_MT_Italic",
    "Juice_ITC",
    "Stencil",
    "Vladimir_Script_Regular",
}

for model in models:
    # Load the image
    image_path = fr"C:\Users\mathi\OneDrive\Documents\GitHub\MINI_PROJET-IA\TESSTRAIN_SOLUTION\tesstrain\data\test\{model}\sample_0.png"
    image = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(image, lang=model)
    print(model)
    print("text: ", text)