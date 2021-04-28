## Grab Text for Mac OS
* * *

## Install dependencies
* ### You need homebrew and pip already installed
* You can run installer.py to automatically install necessary dependencies

* Or you can run these commands to manually install dependencies.
    * Make sure homebrew is up to date
      * ``` brew update ```

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
* You can cancel a screenshot by pressing escape. This will print the previous text that was grabbed.

## Tips for Easy Use
* I recommend adding an alias for this app to your .bashrc 
* Here's the alias I use, don't forget to update the file path:
  * ``` alias grab-text="python3 pathToAppDirectory/app.py"  ```
* Once you have pasted that line in your .bashrc and restarted your terminal you can run the command ``` grab-text ``` to start the app.