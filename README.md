# Print a book from VitalSource Bookshelf to PDF

This script automates the mouse click of the next page button and takes screenshot of the current page in the opened book. It could probably be used in programs other than VitalSource's desktop app, but I haven't tested them.

Tested on Python 3.5+


## Usage

This script looks for coordinates as inputs in order to cut the page out of each screenshot. Use a program like Greenshot to find the coordinates you need for the top left and bottom right of the page, as well as the next button. Generally, the top left of the monitor is 0,0.

Start it up and let it run its course through the book. If your computer has trouble loading the pages fast enough, change the amount of time the script sleeps between screenshots on line 20.

```bash
pip install -r requirements.txt
python vitalprinter.py leftX topY rightX bottomY next_buttonX next_buttonY total_page
# Ex: python vitalprinter.py 1162 142 1871 1030 1900 130 195
```
