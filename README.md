# OCMC's Not Scantron 1.0
## Description
This script uses OpenCV to automatically pick up page contour, detect contestant input, and outputs their mark and tiebreaker score in a convenient `.csv` format. Hand marking bubblesheets is now officially a thing of the past woohoo!!!

## Library Dependencies
This script uses the following external libraries:
```bash
imutils
pdf2image
dynamsoft_barcode_reader_bundle
numpy
openCV-python
```
If you have any trouble using the `dynamsoft_barcode_reader_bundle`, either talk to me (if I'm still here) or go get the API yourself by searching it up on google. They have pretty clear instructions.

### Setting up
Run the following commands in your console before using this script
```bash
python 3 -m venv venv
source venv/bin/activate
pip install imutils pdf2image dynamsoft-barcode-reader opencv-python
```
Then make sure that you are using the virtual environment that we have set up by using the shortcut `Ctrl + Shift + P` (Windows) or `Cmd + Shift + P` (MacOS) to open Command Palette. Then select `Python: Select Interpreter` and then something like `Python 3.13.2 ('venv')` (your python might have a different version, so just look for the `('venv')` at the end) and you are good to go.

## Usage
### Mark Scheme Setup
Before running the `not_scantron.ipynb`, make sure that the answer key is up to date by running `update_mark_scheme.py`. It will ask you to enter as a column, just... put the answers in a column in Google Sheet or MS Excel, and then copy paste into the terminal. Saves you a lot of troubles. If your answer key was in one row uhhh... tough luck, go learn how to use Excel or smth.

Just kidding, here's what you need to do:
>If all of your answers are in a row, so if it looks like `ABCDEFG...`, copy paste it into the `A1` cell, then type this into the `B1` cell `=MID($A$1, ROW(A1), 1)` and then drag it down until you reach an empty cell. Will this work? Who knows. Good luck!!!  
\- Love, ChatGPT ;)

If you need to update the mark scheme, i.e. how many marks a correct, incorrect, or blank question is worth. (idk why you would ever do that, I thought we had an agreement going T-T) Delete the `mark_scheme.json` file in `./config`, change the `DEFAULT_CORRECT`, `DEFAULT_NONE`, and `DEFAULT_INCORRECT`, and run the code like you're just updating the answer key.
### Running the Main Program
Put every submission you got into the `./fileIn` folder, `.pdf`s, `.jpg`s, `png`s, or wtv doesn't matter. File name? Doesn't matter. You can stop bothering the proctors about naming things wrong.
Run each cell of `not_scantron.ipynb`. That's it. Idk what else you expected. There will be a log behind most cells, which will tell you what has happened. Some cells take longer than others. Don't worry that's just how it is. Your program is not crashing. Stop being ADHD and go touch some grass while you wait or smth.
Read the log if you're interested, if not, just to go the `./fileOut` folder at the end, and open the `result.csv`. Every line that says smth like
```
sm_id,scan failed,,,,,,,,,,,,,,,,,,,,,,,,,,
```
just means that the contestant probably coloured some bubble really poorly, or the proctor is being a dummy and can't take a proper scan of the bubble sheet. Oh well, go mark those sheets by hand like your forebears. You might even find the ancient grading tools they once used hidden in some behind a waterfall in the OCMC Google Drive (if that still exists). Have fun, and good luck releasing the results to the students in a few days!

## Acknowledgment
Big thanks to Vishal Turkar ([Vishal1999-33](https://github.com/Vishal1999-33) on GitHub), I stole a bunch of code from his bubble sheet scanner project. Couldn't have done it without you man, although I think it helps on a poorly lit photo if you apply Otsu's thresholding method *before* detecting the edge contour. This made edge detection more reliable in my experience of copying from you :)  
I stole some code from someone else, so feel free to steal from me if you can read my messy code ¯\\\_(ツ)\_/¯  
Byeeeeee (\^o\^)/\~\~\~
