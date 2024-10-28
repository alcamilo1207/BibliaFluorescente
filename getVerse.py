import requests
from lxml import html
import json

with open("bible.json", 'r') as file:
    bible = json.load(file)

def verse_text_from_web(b, c, v):
    # URL of the webpage you want to scrape
    url = "https://www.bibliatodo.com/la-biblia/Reina-valera-1960/{}-{}".format(b,c)
    xpath = "//*[@id=\"info_capitulo\"]/p[{}]/text()".format(v)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

    # Send a GET request to the webpage
    response = requests.get(url, headers=headers)

    # Parse the HTML content
    tree = html.fromstring(response.content)

    # Use the XPath to get the desired element
    text = tree.xpath(xpath)

    # text() returns a list, you can access the first item to get the actual text
    if text:
        return text[0]
    else:
        return "Element not found or no text available."

def verse_text(b,c,v):
    return bible[b][str(c)][str(v)]

def get_chapterList(b):
    return list(bible[b].keys())

def get_verseList(b,c):
    #Check chapter number
    if len(bible[b].keys()) < int(c):
        c = 1

    return list(bible[b][str(c)].keys())
