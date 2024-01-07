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
        text = addNewlines(text)
        while True:
            font = ImageFont.load_default(size=self.fontSize)
            print(repr(text))
            left, top, right, bottom  = draw.textbbox((0, 0), text, font=font, spacing=4, align="center")
            textWidth = abs(right - left)
            textHeight = abs(bottom - top)
            if textWidth < image.width and textHeight < image.height:
                break
            self.fontSize -= 5
        text_x = (image.width - textWidth) // 2
        text_y = (image.height - textHeight) // 2
        draw.multiline_text((text_x, text_y), text, font=font, fill="white", stroke_width=2, stroke_fill="black", spacing=4, align="center")
        image.save(outputPath)
        
    def createPosts(self):
        with open(self.textPath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if os.path.isfile(f"imgs\\image{i}.jpg"):
                    self.fontSize = 100
                    imagePath = f"{self.roughImagePath}\\image{i}.jpg"
                    outputPath = f"posts\\image{i}.jpg"
                    self.addTextToImage(imagePath, outputPath, line.strip())

        # After processing all lines, truncate the file to remove its content
        with open(self.textPath, "w", encoding="utf-8") as f:
            f.truncate()
        # Remove all images from the imgs folder
        removeImages(self.roughImagePath)

