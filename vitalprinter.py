import argparse
import os
import tempfile

import img2pdf
import pyautogui
import time

def screenshot(leftx, topy, width, height, nextx, nexty, total_page):
    images = []
    temp_dir = tempfile.mkdtemp()
    for i in range(total_page):
        page_num = "{}".format(i).zfill(len(str(total_page)))
        file_name = os.path.join(temp_dir, 'book-page-{}.png'.format(page_num))
        images.append(file_name)

        pyautogui.screenshot(region=(leftx,topy, width, height)).save(file_name)
        pyautogui.moveTo(nextx, nexty)
        pyautogui.click()
        time.sleep(.3)

    return images


def image2pdf(images):
    with open("book.pdf", "wb") as f:
        f.write(img2pdf.convert(images))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Take book screenshots.')
    parser.add_argument('leftx', type=int)
    parser.add_argument('topy', type=int)
    parser.add_argument('rightx', type=int)
    parser.add_argument('bottomy', type=int)
    parser.add_argument('next_buttonx', type=int)
    parser.add_argument('next_buttony', type=int)
    parser.add_argument('total_page', type=int)

    args = parser.parse_args()

    leftx = args.leftx
    topy = args.topy
    rightx = args.rightx
    bottomy = args.bottomy
    nextx = args.next_buttonx
    nexty = args.next_buttony
    total_page = args.total_page
	
    width = rightx - leftx
    height = bottomy - topy
	

    print("Take book screenshots from ({},{}) to ({},{}) with next button at ({},{}) for {} pages".format(
        leftx, topy, rightx, bottomy, nextx, nexty, total_page
    ))

    images = screenshot(leftx, topy, width, height, nextx, nexty, total_page)
    image2pdf(images)

    print("Done, book saved in the local directory as book.pdf.")
