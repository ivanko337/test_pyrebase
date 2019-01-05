#coding=utf-8

import core

user1 = ( 'iamloxgigigi@hui.com', '123456' )

app = core.Core(*user1)

t = app.deleteNote('-LUqWGHVlv5XbRM_PytH')
print(t)