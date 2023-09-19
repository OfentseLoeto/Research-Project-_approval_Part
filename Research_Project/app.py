#!/usr/bin/python3
"""Setting up a backend server using python with flask."""
import os
from config import DATABASE_URI, EMAIL_USERNAME, EMAIL_PASSWORD
from dotenv import load_dotenv
from flask import Flask, jsonify, request, render_template
from utils import get_github_data
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests


# This method method load the environment variables from Git_token.env file

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    """Rendering index page"""
    return render_template('index.html')

@app.route('/github/stats/<string:username>')

def get_github_stats(username):
    # Getting statistics from a Github user account.
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
    # Getting a list of repositories for a github user.
    data = get_github_data(username)
    if data:
        repos_url = data['repos_url']
        response = requests.get(repos_url)
        repos = response.json()
        repos_names = [repo['name'] for repo in repos]
        return jsonify({'username': username, 'repositories': repos_names})
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/api/data')

def get_data():
    # Return some data from the backend as JSON
    data = some_util_function()
    return jsonify(data)

@app.route('/create_user')

def create_user():
    # Create a new user
    new_user = User(username=USERNAME, email=EMAIL)
    db.session.add(new_user)
    db.session.commit()
    return 'User created!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
