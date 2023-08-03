#!/usr/bin/python3
"""Setting up a backend server using pyhton with flask."""
import os
from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

#This function fetches Github data using the provided token
def get_github_data(username):
    token = os.environ.get('GITHUB_ACCESS_TOKEN')
    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/users/{username}'
    response = request.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def index():
    """Rendering index page"""
    return render_template('index.html')

@app.route('/github/stats/<string:username>')

def get_github_stats(username):
    """Getting statistics from a Github user account."""
    data = get_github_data(username)
    if data:
        stats = {
                'username': data['login'],
                'name': data['name'],
                'followers': data['followers'],
                'following': data['following'],
                'public_repos': data['public_repos']
                }
        return jsonify(stats)
    else:
        return jsonify({'error': 'User not found'}), 404


@app.route('/github/repos/<string:username>')

def get_github_repos(username):
    """Getting a list of repositories for a github user"""
    data = get_github_data(username)
    if data:
        repos_url = data['repos_url']
        response = requests.get[repos_url]
        repos = response.json()
        repos_names = [repos['name'] for repo in repos]
        return jsonify({'username': username, 'repositories': repo_names})
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
