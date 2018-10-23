#!/usr/bin/env python
#~*~ coding: utf-8 ~*~

import hackmud

class Channel(object):
    def __init__(self, name, users):
        self.name = name
        self.users = users

class Message(object):
    def __init__(self, msg_obj):
        self.id        = msg_obj['id']
        self.time      = msg_obj['t']
        self.text      = msg_obj['msg']
        self.from_user = msg_obj['from_user']
        self.to_user   = None
        self.channel   = None
        self.is_join   = None
        self.is_leave  = None

        if 'channel' in msg_obj:
            self.channel   = msg_obj['channel']
        if 'is_join' in msg_obj:
            self.is_join   = msg_obj['is_join']
        if 'is_leave' in msg_obj:
            self.is_leave  = msg_obj['is_leave']
        if 'to_user' in msg_obj:
            self.to_user = msg_obj['to_user']

class User(object):
    def __init__(self, name, chan_obj, account):
        self.name = name
        self.account = account
        self.channels = []
        self.messages = []

        for chan_name, users in chan_obj.items() :
            self.channels.append(Channel(chan_name, users))

        self.update_history()

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<hackmud_chat.User name={}>'.format(self.name)

    def update_history(self):
        self.messages = [Message(m) for m in
                         sorted(hackmud.get_chats(self.account.token,
                                                  [self.name])['chats'][self.name],
                                key=lambda msg: msg['t'])]

    def messages_since(self, time):
        target_i = 0
        for i in xrange(len(self.messages)):
            if self.messages[i].time == time:
                target_i = i
                break
        return (len(self.messages) - 1) - target_i

    def tell(self, to, msg):
        hackmud.create_chat(self.account.token, self.name, msg, dest=to)

    def say(self, channel, msg):
        hackmud.create_chat(self.account.token, self.name, msg, channel=channel)

    def say_to(self, channel, to, msg):
        hackmud.create_chat(self.account.token, self.name, msg, channel=channel, dest=to)

class Account(object):
    def __init__(self, passwd="", token=""):
        self.users = []
        if token:
            self._login(token=token)
        elif passwd:
            self._login(passwd=passwd)

    def __repr__(self):
        users = '['
        l = len(self.users)
        for i in xrange(l):
            if i == l - 1:
                users += self.users[i].name
            else:
                users += self.users[i].name +', '
        users += ']'
        return '<hackmud_chat.Account token={}, users={}>'.format(self.token, users)

    def _login(self, token="", passwd=""):
        def parseUsers(response):
            for username, channels in response['users'].items():
                user = User(username, channels, self)
                self.users.append(user)

        if token:
            self.token = token
            parseUsers(hackmud.get_account_data(token))
        elif passwd:
            self.token = hackmud.get_token(passwd)
            parseUsers(hackmud.get_account_data(token))
            print 'Got account token: ' + self.token
            print 'Now you can directly use it instead of generating new pass'

    def get_user(self, username):
        for user in self.users:
            if user.name == username:
                return user
