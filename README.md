# Print a book from VitalSource Bookshelf to PDF

This script simulates mouse click in the next page button and takes screenshot of current page in the opened book. It could be used in programs other than VitalSource's desktop app, but I haven't tested them.

Tested on Python 3.5+


## Usage

This script looks for coordinates as inputs in order to cut the page out of each screenshot. Use a program like Greenshot to find the coordinates you need. Generally, the top left of the monitor is 0,0.

```bash
pip install -r requirements.txt
python vitalprinter.py leftX topY rightX bottomY next_buttonX next_buttonY total_page
# Ex: python vitalprinter.py 1162 142 1871 1030 1900 130 195
```
