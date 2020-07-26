import dbConfig
from utils.user_manager import user_manager

from flask import Flask, Response

from scripts.signin_user import signin_user
from scripts.signup_user import signup_user
from scripts.get_user_profile import get_user_profile

import mysql.connector
import sys
import boto3
import os

from utils.videoTranscoder import transcodeVideo

app = Flask(__name__)

# testing purposes
@app.route('/')
def hello_world(): 
    return "You've hit VIBE backend"

# signing up a user
@app.route('/signup')
def signup_script():
    username = '' # need to parse from frontend
    email = ''
    password = '' # need to parse from frontend
    return user_manager.signup_user(username, email, password)

# signing in user
@app.route('/signin')
def signin_script():
    username = '' # need to parse from frontend
    password = '' # need to parse from frontend
    return user_manager.signin_user(username, password)

# get using profile info - for user profile page
@app.route('/get_user_profile_info')
def get_user_profile_info():
    user_id = ''
    return get_user_profile(user_id=user_id)

@app.route('/testU')
def s3UploadTest():
    transcodeVideo("testMkv.mkv", "newOutputVideo.mkv")
    return "video transcoded"

@app.route('/testD')
def s3DownloadTest():
    client = boto3.client('s3', region_name=dbConfig.REGION, aws_access_key_id=dbConfig.ACCESS_KEY, aws_secret_access_key=dbConfig.SECRET_ACCESS_KEY)
    file = client.get_object(Bucket='vibe-test-bucket', Key='testMkv.mkv')
    file = client.get_object(Bucket='vibe-test-bucket', Key='testMkv.mkv')
    return Response(
        file['Body'].read(),
        mimetype='video/quicktime',
        headers={"Content-Disposition": "attachment;filename=newName.mkv"}
    )