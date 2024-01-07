# InstaBot - Your favourite motivational quote with nature background poster on instagram.
![image](https://github.com/urasil/InstaBot/assets/114501016/dc5c5611-4ff8-47c1-bd14-45d931f8ecf3)
## How does the bot work?
The bot scrapes the goodreads website for motivational quotes as well as scraping google images under nature search. It then combines a motivational quote with an image, 
which is the post that is going to be made to instagram.

Instagram Graph API only accepts URL's of images therefore, the posts created have to be uploaded online. imgbb API is used for this purpose. The posts are put online
to imgbb and the URL's of the posts are then used to post the images to Instagram using the Graph API.

This bot is motivational, however you can easily change the purpose of the bot by finding something else it can scrape.

#### Things to consider
To use the bot, an instagram business account is required. Then you need to connect this instagram account to a facebook account by creating a "Page".
To be careful of which permissions are required to post content because I wasn't and ended up spending a shameful amount of time.
