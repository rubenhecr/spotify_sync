#!/usr/bin/env python
# coding: utf-8

import base64
import datetime
import webbrowser
from urllib.parse import urlencode

import requests
from requests_oauthlib import OAuth2Session


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    auth_url = "https://accounts.spotify.com/authorize"
    redirect_uri = 'https://www.spotify.com/'
    response_type = 'code'
    scope = ''

    def __init__(self, client_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
    
    def perform_auth(self):
        oauth = OAuth2Session(self.client_id, redirect_uri=self.redirect_uri, scope = self.scope)
        authorization_url, state = oauth.authorization_url( self.auth_url, access_type = self.response_type )
        
        webbrowser.open(authorization_url)
        authorization_response = input('Please paste whole callback:')


