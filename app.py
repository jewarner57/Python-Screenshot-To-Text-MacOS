from PIL import Image
import pytesseract
import os

filepath = os.path.dirname(os.path.realpath(__file__))

# tell the user a screenshot is active
os.system("echo \" Screenshot In Progress - Select screenshot area. \"")
# start a new select area screenshot
os.system(f'screencapture -s {filepath}/images/screenshot.png')


def get_image_text(filename):
    """This function reads text from the image and return it"""
    text = pytesseract.image_to_string(Image.open(filename))
    return text


# get text from the image
text = get_image_text(f'{filepath}/images/screenshot.png')

# echo the text to the terminal
os.system(f"echo \"{text}\"")
