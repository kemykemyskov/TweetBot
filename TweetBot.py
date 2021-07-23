import tweepy
from time import sleep
from keys import *
from time import sleep

import json
from urllib import request
from urllib.error import HTTPError


WEBHOOK_URL = 'https://discord.com/api/webhooks/867543338499571753/6kf0gf3bn17YzAalihjvM0dlqYz8MgLFbtQF_4cHfMytDiIDJY1h2hCRTyuxrPawpGMe'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
last_1 = 0


userID = "kemyskov"
while True:
    tweets = api.user_timeline(screen_name=userID, 
                            # 200 is the maximum allowed count
                            count=10,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )
    # for info in tweets[:1]:
    #     #api.retweet(info.id)
    #     print("ID: {}".format(info.id))
    #     print(info.created_at)
    #     print(info.full_text)
    #     print(tweets[0].created_at)
       
    if  last_1 != tweets[0].created_at:

        payload = {
            'embeds': [
                {
                    'title': 'Une nouvelle release',  # Le titre de la carte
                    'description': tweets[0].full_text,  # Le corps de la carte
                # 'url': 'https://zestedesavoir.com/on-peut-aussi-mettre-une-url',  # Si vous voulez faire un lien
                # 'timestamp': info.created_at,  # Si vous voulez horodater le contenu
                    'author': {'name': tweets[0].id},  # Pourquoi pas mettre des auteurs ?
                },
            ]
        }


        # Les paramètres d'en-tête de la requête
        headers = {
            'Content-Type': 'application/json',
            'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
        }

        # Enfin on construit notre requête
        req = request.Request(url=WEBHOOK_URL,
                            data=json.dumps(payload).encode('utf-8'),
                            headers=headers,
                            method='POST')

        response = request.urlopen(req)
    last_1 = tweets[0].created_at
