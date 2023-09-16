#!/usr/bin/python3
"""The script performs some utils"""
import requests
import os

def get_github_data(username):
        access_token = os.environ.get('GITHUB_ACCESS_TOKEN')
        headers = {'Authorization': f'token {access_token}'}
        url = f'https://api.github.com/users/{username}'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None
