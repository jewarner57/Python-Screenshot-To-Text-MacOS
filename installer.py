import os

# This file installs the necessary libraries to use this application

# update homebrew
os.system("brew update")

# install pillow
os.system("brew install Homebrew/python/pillow")

# install pytesseract
os.system("pip install pytesseract")

# install tesseract binaries
os.system("brew install tesseract")
