import tweepy
from time import sleep
from keys import *

import json
from urllib import request
from urllib.error import HTTPError


WEBHOOK_URL = 'https://discord.com/api/webhooks/867543338499571753/6kf0gf3bn17YzAalihjvM0dlqYz8MgLFbtQF_4cHfMytDiIDJY1h2hCRTyuxrPawpGMe'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

userID = "kemyskov"

tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=10,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
for info in tweets[:1]:
     #api.retweet(info.id)
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")

payload = {
    'embeds': [
        {
            'title': 'Une nouvelle release',  # Le titre de la carte
            'description': info.full_text,  # Le corps de la carte
           # 'url': 'https://zestedesavoir.com/on-peut-aussi-mettre-une-url',  # Si vous voulez faire un lien
           # 'timestamp': info.created_at,  # Si vous voulez horodater le contenu
            'author': {'name': info.id},  # Pourquoi pas mettre des auteurs ?
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

# Puis on l'émet !
try:
    response = request.urlopen(req)
    print(response.status)
    print(response.reason)
    print(response.headers)
except HTTPError as e:
    print('ERROR')
    print(e.reason)
    print(e.hdrs)
    print(e.file.read())