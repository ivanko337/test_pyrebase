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
        self.user = self.authUser(email, passw)
        self.database = firebase.database()

    def getNotes(self, noteId=None):
        if noteId == None:
            return self.database.child('users').child(self.user['localId']).child('notes').get().val()
        else:
            return self.database.child('users').child(self.user['localId']).child('notes').child(noteId).get().val()

    def writeNote(self, title, text):
        note = { 'title':title, 'text':text }
        return self.database.child('users').child(self.user['localId']).child('notes').push(note, self.user['idToken'])

    def authUser(self, email, passw): # если email и passw равно None, то будет возвращено None
        try:
            if not email and not passw:
                return None
            return self.auth.sign_in_with_email_and_password(email, passw)
        except Exception as e:
            msg = self.getExceptionMessage(e.args)
            raise Exception(msg)

    def logOut(self):
        if not self.user:
            self.user = None

    def getExceptionMessage(self, args):
        emsg = args[1]
        s = emsg.find('"message":')
        s = emsg.find(': "', s) + 3
        e = emsg.find(',', s) - 1
        return emsg[s:e]

    def register(self, email, passw):
        try:
            response = self.auth.create_user_with_email_and_password(email, passw)
        except Exception as e:
            msg = self.getExceptionMessage(e.args)
            raise Exception(msg)
        self.user = response
        return response

    def deleteNote(self, noteId):
        if not isinstance(noteId, str):
            raise TypeError('noteId must be a str')
        note = self.database.child('users').child(self.user['localId']).child('notes').child(noteId).get().val()
        if not note:
            raise Exception('Selected note does not exist')
        note = dict(note.items())
        self.database.child('users').child(self.user['localId']).child('notes').child(noteId).remove(self.user['idToken'])
        return self.database.child('users').child(self.user['localId']).child('removed').push(note, self.user['idToken'])

    def redactNote(self, noteId, text=None, titlte=None):
        if not text and not titlte:
            raise Exception('You must specify at least one of the optional arguments')
        note = self.database.child('users').child(self.user['localId']).child('notes').child(noteId).get().val()
        if not note:
            raise Exception('Selected note does not exist')
        note = list(note.items())
        newNote = { 'text':note[0][1], 'title':note[1][1] }
        if text:
            newNote['text'] = text
        if titlte:
            newNote['title'] = titlte
        return self.database.child('users').child(self.user['localId']).child('notes').child(noteId).update(newNote)

    def restoreNote(self, noteId):
        note = self.database.child('users').child(self.user['localId']).child('removed').child(noteId).get().val()
        if not note:
            raise Exception('Selected note does not exist')
        rNote = list(note.items())
        newNote = { 'text': rNote[0][1], 'title': rNote[1][1] }
        return self.database.child('users').child(self.user['localId']).child('notes').push(newNote)