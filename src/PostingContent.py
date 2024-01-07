import time
from Credentials import getCreds, makeApiCall

class PostingContentToInstagram:

    def __init__(self, url):
        self.params = getCreds(url)

    def createMediaObject(self):
        url = self.params['endpointBase'] + self.params['instagram_account_id'] + '/media'
        endpointParams = {
            "ig-user-id": self.params['instagram_account_id'],
            'caption': self.params['caption'],
            'access_token': self.params['access_token'],
            'image_url': self.params['media_url']
        }
        return makeApiCall(url, endpointParams, 'POST')

    def publishMedia(self, imageMediaObjectId):
        url = self.params['endpointBase'] + self.params['instagram_account_id'] + '/media_publish'
        endpointParams = {
            'creation_id': imageMediaObjectId,
            'access_token': self.params['access_token']
        }
        return makeApiCall(url, endpointParams, 'POST')

