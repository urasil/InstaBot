from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.request
from collections import defaultdict

class ScrapeText():
    def __init__(self):
        self.quoteMap = defaultdict(list)
        self.page = open("pageInfo.txt", "r", encoding="utf-8").read()
        self.numQuotes = 0

    def extractQuotes(self):
        # Good reads to get the lovely quotes
        url = f"https://www.goodreads.com/quotes/tag/inspirational-quotes?page={self.page}"
        website = requests.get(url)
        soup = BeautifulSoup(website.text, "html.parser")

        quoteText = soup.find_all("div", attrs={"class": "quoteText"})

        for quote in quoteText:
            extractedQuote = quote.text.strip().split("\n")[0]
            author = quote.find("span", attrs={"class": "authorOrTitle"}).text.strip()
            if len(f"{extractedQuote} - {author}") > 300:
                continue
            author = author if author[-1] != "," else author[:-1]
            self.quoteMap[author].append(extractedQuote)
            self.numQuotes += 1

    def writeQuotesToTextFile(self):
        self.extractQuotes()
        try:
            with open("quotes.txt", "w", encoding="utf-8") as f:
                for author, quotes in self.quoteMap.items():
                    for quote in quotes:
                        f.write(f"{quote} - {author}\n")
        except Exception as e:
            print("Error while writing to file: ", e)

    def setQuoteMap(self):
        self.quoteMap = defaultdict(list)

    def updateQuoteMap(self):
        try:
            with open("pageInfo.txt", "w", encoding="utf-8") as f:
                f.write(str(int(self.page)+1))
        except Exception as e:
            print("Error while writing to file: ", e)
    def getNumQuotes(self):
        return self.numQuotes
