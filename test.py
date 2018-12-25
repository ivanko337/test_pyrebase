#!/usr/bin/python3
#coding=utf-8

import pyrebase

config = {
    'apiKey': "AIzaSyATCyEnI5lObVL3ktgeuJ8tGw7CclYfjwM",
    'authDomain': "pisos-test-pyrebase.firebaseapp.com",
    'databaseURL': "https://pisos-test-pyrebase.firebaseio.com",
    'projectId': "pisos-test-pyrebase",
    'storageBucket': "pisos-test-pyrebase.appspot.com",
    'messagingSenderId': "771854574757",
    'serviceAccount': 'E:\\pisos-test-pyrebase-firebase-adminsdk-lucom-4e6ef771c9.json'
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

user1 = ( 'iamloxgigigi@hui.com', '123456' )
user2 = ( 'v.gritskevich25@gmail.com', 'pisos123' )
user3 = ( 'pisos@pip.com', '123456')

try:
    user = auth.sign_in_with_email_and_password(*user1)
    for i, j in user.items():
        print('{}:{}'.format(i, j))
except:
    print('Invalid email or password')

db = firebase.database()

title = input('Enter note\'s title: ')
note_text = input('Enter note: ')

current_note = {
    'title': title,
    'text': note_text
}

db.child('users').child(user['localId']).child('notes').push(current_note, user['idToken'])

result = db.child('users').child(user['localId']).child('notes').get() # idToken localId

for i, j in result.val().items():
    print('{}:{}'.format(i, j))