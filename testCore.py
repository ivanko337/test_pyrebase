#coding=utf-8

import core
from exceptions import AuthError

user1 = ( 'iamloxgigigi@hui.com', '123456' )
user2 = ( 'v.gritskevich25@gmail.com', 'pisos123' )
user3 = ( 'pisos@pip.com', '123456')
user4 = ( 'blabr@rambler.ru', '123456' )

app = core.Core(*user1)

def stream_handler(message):
    print(message['event'])
    print(message['path'])
    print(message['data'])

my_stream = app.database.child('users').stream(stream_handler)