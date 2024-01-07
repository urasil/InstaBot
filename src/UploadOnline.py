import requests
from dotenv import load_dotenv
import os

class UploadOnline:
    def __init__(self):
        load_dotenv()
        self.apiKey = os.getenv("imgbbApiKey")

    def uploadImage(self, imagePath):
        endpoint = "https://api.imgbb.com/1/upload"
        with open(imagePath, "rb") as f:
            files = {"image": (imagePath, f.read())}
            params = {"key": self.apiKey, "expiration": 120}
            response = requests.post(endpoint, files=files, params=params)
            data = response.json()
            if data["status"] == 200:
                return data
            else:
                return None
            