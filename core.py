#coding=utf-8

import pyrebase

class Core:
    def __init__(self, email, passw):    
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
        self.auth = firebase.auth()
        self.user = self.auth.sign_in_with_email_and_password(email, passw)
        self.database = firebase.database()

    def getNotes(self, noteId=None):
        if noteId:
            return self.database.child('users').child(self.user['localId']).child('notes').get()
        else:
            return self.database.child('users').child(self.user['localId']).child('notes').child(noteId).get()

    def writeNote(self, title, text):
        note = { 'title':title, 'text':text }
        return self.database.child('users').child(self.user['localId']).child('notes').push(note, self.user['idToken'])