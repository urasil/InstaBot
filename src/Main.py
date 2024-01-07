from ScrapeImages import ScrapeImages
from ScrapeText import ScrapeText
from Helpers import checkForScraping
from UploadOnline import UploadOnline
from PostingContent import PostingContentToInstagram
from CreatingPosts import CreatingPosts
import os
import time

def scrapeChecking(textScraper, imageScraper):
    try:
        checkForScraping(textScraper, imageScraper)
    except Exception as e:
        print("Error while checking for scraping: ", e)
        return
    
def uploadingImageOnline(uploader):
    imageToPost = os.listdir("posts")[0]
    imageToPostPath = os.path.join("posts", imageToPost)
    data = uploader.uploadImage(imageToPostPath)
    time.sleep(1)
    if data:
        os.remove(imageToPostPath)
        return data

def main():
    textScraper = ScrapeText()
    imageScraper = ScrapeImages()   
    uploader = UploadOnline()

    print("Checking if there is an available post to post...")
    time.sleep(1)

    if scrapeChecking(textScraper, imageScraper):
        print("There is no available post to post, creating posts...")
        time.sleep(1)
        postCreater = CreatingPosts()
        postCreater.createPosts()

    print("Uploading image online...")
    time.sleep(1)
    data = uploadingImageOnline(uploader)

    print("Posting image to Instagram...")
    time.sleep(1)
    post = PostingContentToInstagram(data["data"]["url"])
    imageMediaObjectResponse = post.createMediaObject()
    if 'error' in imageMediaObjectResponse['jsonData']:
        print(f"Error creating media object: {imageMediaObjectResponse['jsonData']['error']}")
    else:
        imageMediaObjectId = imageMediaObjectResponse['jsonData'].get('id')
        if imageMediaObjectId:
            time.sleep(1)
            publishImageResponse = post.publishMedia(imageMediaObjectId)
            if 'error' in publishImageResponse['jsonData']:
                print(f"Error publishing media: {publishImageResponse['jsonData']['error']}")
                exit()
            print("Success!")

if __name__ == "__main__":
    main()


