from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.request
from collections import defaultdict

class ScrapeText():
    def __init__(self):
        self.quoteMap = defaultdict(list)
        self.page = 1
        self.numQuotes = 0

    def extractQuotes(self):
        # Good reads to get the lovely quotes
        url = f"https://www.goodreads.com/quotes/tag/inspirational-quotes?page={self.page}"
        website = requests.get(url)
        soup = BeautifulSoup(website.text, "html.parser")

        quoteText = soup.find_all("div", attrs={"class": "quoteText"})

        for quote in quoteText:
            self.numQuotes += 1
            extractedQuote = quote.text.strip().split("\n")[0]
            author = quote.find("span", attrs={"class": "authorOrTitle"}).text.strip()
            if len(f"{extractedQuote} - {author}") > 300:
                continue
            author = author if author[-1] != "," else author[:-1]
            self.quoteMap[author].append(extractedQuote)

    def writeQuotesToTextFile(self):
        self.extractQuotes()
        try:
            with open("quotes.txt", "w", encoding="utf-8") as f:
                for author, quotes in self.quoteMap.items():
                    for quote in quotes:
                        text = quote + author
                        f.write(f"{quote} - {author}\n\n")
        except Exception as e:
            print("Error while writing to file: ", e)

    def setQuoteMap(self):
        self.quoteMap = defaultdict(list)

    def updateQuoteMap(self):
        if len(self.quoteMap) == 0:
            self.page += 1
            self.setQuoteMap()
            self.extractQuotes()

    def getNumQuotes(self):
        return self.numQuotes

obj = ScrapeText()
obj.writeQuotesToTextFile()