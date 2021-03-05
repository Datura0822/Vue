# -*- coding: utf-8 -*-

def onQQMessage(bot, contact, member, content):
    if contact.ctype == "buddy":
        with open('test.txt', 'a+') as f:
            f.write( "www.runoob.com!Very good site!\n")