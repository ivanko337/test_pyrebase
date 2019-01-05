#coding=utf-8

import core
from exceptions import AuthError
import threading

user1 = ( 'iamloxgigigi@hui.com', '123456' )
user2 = ( 'v.gritskevich25@gmail.com', 'pisos123' )
user3 = ( 'pisos@pip.com', '123456')
user4 = ( 'blabr@rambler.ru', '123456' )

app = core.Core(*user1)

def stream_handler(message):
    for i, j in message.items():
    print('{}:{}'.format(i, j))
    
def pip():
    app.database.child('users').stream(stream_handler)

t = threading.Thread(target=pip)
t.daemon = True
t.start()

app.deleteNote('-LUqWIWN5oLpItqr6Pem')
app.writeNote('pgrioeorfg', 'ngireognierg')