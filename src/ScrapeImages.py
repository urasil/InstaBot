from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
from PIL import Image
import time
from Helpers import isLineInFile

class ScrapeImages:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.imageURLs = set()
        self.natureURL = "https://www.google.com/search?q=nature&tbm=isch&ved=2ahUKEwjlh-_AqcKDAxWf_7sIHbG4CWQQ2-cCegQIABAA&oq=nature&gs_lcp=CgNpbWcQAzIKCAAQgAQQigUQQzINCAAQgAQQigUQQxCxAzIFCAAQgAQyCggAEIAEEIoFEEMyBQgAEIAEMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgjECc6BwgAEIAEEBM6CAgAEAgQHhATUNYGWNYGYIUKaABwAHgAgAGMAYgBjwKSAQMwLjKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=ROeVZeXVGZ__7_UPsfGmoAY&bih=631&biw=1280&rlz=1C1ONGR_en-GBUS1087US1087"
        self.skips = 0

    def downloadImages(self, downloadPath, url, fileName):
        try:
            imageContent = requests.get(url).content
            imageFile = io.BytesIO(imageContent)
            image = Image.open(imageFile)
            filePath = downloadPath + fileName

            with open(filePath, "wb") as f:
                image.save(f, "JPEG")
        except Exception as e:
            print("Error while downloading image: ", e)

    def imagesFromGoogle(self, delay, maxImages):
        
        def scrollDown():
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(delay)

        self.driver.get(self.natureURL)
        while len(self.imageURLs) + self.skips < maxImages:
            scrollDown()
            thumbnails = self.driver.find_elements(By.CLASS_NAME, "Q4LuWd")
            for thumbnail in thumbnails[len(self.imageURLs) + self.skips: maxImages]:
                try:
                    thumbnail.click()
                    time.sleep(delay)
                except Exception as e:
                    print("Error while clicking image")
                    continue
                images = self.driver.find_elements(By.CLASS_NAME, "iPVvYb")
                for image in images:
                    if image.get_attribute('src') in self.imageURLs or isLineInFile("imageURLs.txt", image.get_attribute('src')):
                        maxImages += 1
                        self.skips += 1
                        break
                    
                    if image.get_attribute("src") and "http" in image.get_attribute("src"):
                        self.imageURLs.add(image.get_attribute("src"))
                        with open("imageURLs.txt", "a", encoding="utf-8") as f:
                            f.write(f"{image.get_attribute('src')}\n")
                        print("success")
                        break
    def getImages(self, delay, requiredNum):
        self.imagesFromGoogle(delay, requiredNum)
        for i, url in enumerate(self.imageURLs):
            self.downloadImages("imgs\\", url, f"image{i}.jpg")
        
obj = ScrapeImages()
obj.getImages(1, 7)