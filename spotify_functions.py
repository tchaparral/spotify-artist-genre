'''Module providing spotify functions'''
import base64
import os

import requests
from dotenv import load_dotenv

load_dotenv()

# getting client and secret from env
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_access_token():
    '''
    Function to get access token from Spotify
    '''
    credentials = f'{CLIENT_ID}:{CLIENT_SECRET}'
    credentials_b64 = base64.b64encode(credentials.encode()).decode()

    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {credentials_b64}'    
    }
    data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(token_url, headers = headers, data = data, timeout = 500)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        print(f'Error: {response.status_code}')
        return None

# creating a token
SPOTIFY_API_URL = 'https://api.spotify.com/v1'
ACCESS_TOKEN = get_access_token()

def get_artist_genre(artist_name):
    '''
    Function to get artist genre from Spotify
    '''
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    params = {
        'q': artist_name,
        'type': 'artist',
        'limit': 1
    }
    response = requests.get(f'{SPOTIFY_API_URL}/search',
                            headers = headers,
                            params = params,
                            timeout = 500)

    if response.status_code == 200:
        data = response.json()
        if data['artists']['items']:
            return data['artists']['items'][0]['genres']
    return []

# End-of-file (EOF)
