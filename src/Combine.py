from Helpers import addNewlines, removeImages
from PIL import Image, ImageDraw, ImageFont
import os

class CreatingPosts:
    def __init__(self):
        self.roughImagePath = "imgs"
        self.textPath = "quotes.txt"
        self.fontSize = 100

    def addTextToImage(self, imagePath, outputPath, text):
        image = Image.open(imagePath)
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default(size=self.fontSize)
        width, height = image.size
        text = addNewlines(text)
        left, top, right, bottom  = draw.textbbox((0, 0), text, font=font)
        textWidth = abs(right - left)
        textHeight = abs(bottom - top)
        width, height = image.size
        text_x = (width - textWidth) // 2
        text_y = (height - textHeight) // 2

        draw.multiline_text((text_x, text_y), text, font=font, fill="white", stroke_width=2, stroke_fill="black", spacing=4, align="center")  # You can adjust the text color if needed

        
        image.save(outputPath)
    #TODO:: 
    def createPosts(self):
        with open(self.textPath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                imagePath = f"{self.roughImagePath}\\image{i}.jpg"
                outputPath = f"posts\\image{i}.jpg"
                self.addTextToImage(imagePath, outputPath, line.strip())

        # After processing all lines, truncate the file to remove its content
        with open(self.textPath, "w", encoding="utf-8") as f:
            f.truncate()
        # Remove all images from the imgs folder
        removeImages(self.roughImagePath)

#TODO:: now make sure that there are the same number of quotes and images

text = '"Accept yourself, love yourself, and keep moving forward. If you want to fly, you have to give up what weighs you down." - Roy T. Bennett'

post = CreatingPosts()
#post.addTextToImage("imgs\\image0.jpg", "posts\\image0.jpg", text)
post.createPosts()
