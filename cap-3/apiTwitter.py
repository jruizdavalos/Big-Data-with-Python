import tweepy

# Replace with your API credentials NUItTHFyakQxN05fc0cxeU1fbkc6MTpjaQ
bearer_token = 'NUItTHFyakQxN05fc0cxeU1fbkc6MTpjaQ'
consumer_key = 'QVcFce00mPusAvRADsNCp9oPB'
consumer_secret = 'j9fxjklYNYSfVVKPgTe4eZSdpIbzPaNRNqgjVXfDtrBpxjBDW5'
access_token = '1803238421797752832-Ig5l4hheP4eZWTDnvVFTQIF17qzoeY'
access_token_secret = 'EEakxfjBeXC40syLrTD87Y14lzFgsXt6XO3nbFH4isPd7'# Authenticate with the Twitter API

# Autenticación
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Crear un objeto API
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Create a tweet
client = tweepy.Client(
    bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
    wait_on_rate_limit=True
)

#media_id=api.media_upload(filename="twitter.jpg").media_id_string
#print(media_id)
text = "Hello Twit!"
client.create_tweet(text=text)