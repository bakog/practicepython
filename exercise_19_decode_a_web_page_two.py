# coding=utf-8
"""
 Decode A Web Page Two
Exercise 19 (and Solution)

Using the requests and BeautifulSoup Python libraries,
print to the screen the full text of the article on this website:
 http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages.
Your task is to print out the text to the screen so that you
can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the
BeautifulSoup and requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to
the screen. It will not make it easy to read, so next exercise we
will learn how to write this text to a .txt file.
Discussion
Inspecting HTML on a web page

If you have forgotten how to inspect the HTML of a web page,
look at the detailed solution to the previous exercise for a very detailed explanation. In brief:

    Open the web page in Chrome.
    Right-click the page and click “Inspect Element”
    Use the magnifying glass on the bottom-left of the page
    to click on elements of the page and look at their properties.

"""

import requests
from bs4 import BeautifulSoup
import sys

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
page = requests.get(url)
soup = BeautifulSoup(page.content,"lxml")

#print(soup.prettify())

#szűrés a teljes szöveget tartalmazó div-re
c1=soup.find("div", class_="content paywall drop-cap")
#print (c1)

#szűrés az egyes szekciókra, melyek a bekezdéseket tartalmazzák
c2=c1.find_all("section", class_="content-section")
#print (c2)


for c in c2:
    bekezdes=c.find_all("p")
    for b in bekezdes:
        print (b.get_text())

