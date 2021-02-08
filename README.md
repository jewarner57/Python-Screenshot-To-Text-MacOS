## URL Screenshotter for Mac OS
* * *

## Install dependencies
* ### You need homebrew and pip already installed
* You can run installer.py to automatically install necessary dependencies

    * Install tesseract Binaries Using Homebrew- 
        * ``` brew install tesseract ```

    * Install pytesseract Using pip
        * ``` pip install pytesseract ```

    * Install pillow using homebrew
        * ``` brew install Homebrew/python/pillow ```

## How to use
* Once you've installed the dependencies you can navigate to the project directory and run: 
    * ``` python3 ./app.py ```
* A screenshot will start and you should be able to drag the screenshot area selector around the text you would like to copy.
* The text will be read from the image and printed to the terminal