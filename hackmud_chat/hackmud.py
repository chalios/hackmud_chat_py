#!/usr/bin/env python
#~*~ coding: utf-8 ~*~

import json
import requests

def send(endpoint, data):
    """ send(string, dict) """

    url = "https://www.hackmud.com/mobile/{}.json".format(endpoint)

    # Here you would check the validity of the data
    res = requests.post(url, json=data)

    if res.status_code == 200:
        res = res.json()
        if res['ok'] == True:
            return res
        else:
            print 'Request Error: {}'.format(res['msg'])
    else:
        print 'Error {code}: {text}'.format(code=res.status_code, text=res.text)

def get_token(passwd):
    return send('get_token', {'pass':passwd})['chat_token']

def get_account_data(token):
    return send('account_data', {'chat_token':token})

def get_chats(token, usernames, before=None, after=None):
    if before and after:
        return send('chats', {
            'chat_token':token,
            'usernames':usernames,
            'before':before,
            'after':after
        })
    elif before:
        return send('chats', {
            'chat_token':token,
            'usernames':usernames,
            'before':before
        })
    elif after:
        return send('chats', {
            'chat_token':token,
            'usernames':usernames,
            'after':after
        })
    else:
        return send('chats', {'chat_token':token, 'usernames':usernames})

def get_history(token, username, before=None, after=None):
    if before and after:
        return send('chat_history', {
            'chat_token':token,
            'username':username,
            'before':before,
            'after':after
        })
    else:
        return send('chat_history', {'chat_token':token, 'username':username})

def create_chat(token, username, msg, channel=None, dest=None):
    if channel and dest:
        msg = '@{}: {}'.format(dest, msg)
        return send('create_chat', {
            'chat_token':token,
            'username':username,
            'channel':channel,
            'msg':msg
        })
    elif channel:
        return send('create_chat', {
            'chat_token':token,
            'username':username,
            'channel':channel,
            'msg':msg
        })
    elif dest:
        return send('create_chat', {
            'chat_token':token,
            'username':username,
            'tell':dest,
            'msg':msg
        })
    else:
        print 'I need someone or somewhere to talk...'
