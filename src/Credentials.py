import requests
import json
from dotenv import load_dotenv
import os

def getCreds(url) :

	"""
	Getting the long lived access token
	$uri = "https://graph.facebook.com/v18.0/oauth/access_token?grant_type=fb_exchange_token&client_id={app id}&client_secret={app secret}&fb_exchange_token={short lived access token}"
	$response = Invoke-WebRequest -Uri $uri -Method Get
	$response.Content	
	"""

	#17841464013746209/media?image_url=https://media.istockphoto.com/id/1283504873/photo/mosque-and-bosphorus-bridge.jpg?s=612x612&w=0&k=20&c=UHyYLC4VVJef9V8vzdJsVwqSjX3N06D2-975j3VoajY=&access_token=EAA0UfPi8NDMBO7GBwxcyYHldoR7TBptpdTGrxEJXem0bMiAGLonkZAjqrEsz1s6lFzZARfXS6OlwZAFv12xJq1ZC1L2lBZBxnFrcYdsOT0UTFh9XbtRZAqZCol0YszMXjfqy6wlhohiqABXAZCXMKUz0U5OZCcZCnxXulCVo8HqF3SU0Mrazh7H3HSfM089jGxQr8qBL8pWXEVsAw6NePppKBGWNZCZBqCpcjwp5psYZD
	load_dotenv()
	creds = dict() 
	#access token is long lived
	creds['access_token'] = os.getenv("graphApiKey")
	creds['graphDomain'] = 'https://graph.facebook.com/' 
	creds['graphVersion'] = 'v18.0'
	creds['endpointBase'] = creds['graphDomain'] + creds['graphVersion'] + '/' 
	creds['instagram_account_id'] = "17841464013746209" #make sure this is the busness account id
	creds['media_type'] = 'IMAGE' 
	creds['media_url'] = url
	creds['caption'] = "#motivasyon #motivation #motivationalquotes #motivationmonday #motivational #motivationquotes\n"
	creds['caption'] += "#motivationquote #motivationalquote #motivationalwords #motivationmondays #motivationalquoteoftheday\n"
	creds['caption'] += "#motivationalpost #motiv"

	return creds

def makeApiCall(url, endpointParams, type):
	"""
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters


	Returns:
		object: data from the endpoint
	"""

	if type == 'POST' :
		data = requests.post(url, endpointParams)
	else :
		data = requests.get(url, endpointParams)

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpointParams'] = endpointParams #parameters for the endpoint
	response['jsonData'] = json.loads(data.content) # response data from the api

	return response