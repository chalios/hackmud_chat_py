#!/usr/bin/env python
#~*~ coding: utf-8 ~*~

from hackmud_chat import Account
from time import sleep

acct = Account(token='yourtoken')
user = acct.get_user('user')

channel = user.channels[0].name

message = '''Message Of The Day:
    The sky is blue and the sun is shining.
'''

try:
    while True:
        user.say(channel, message)
        sleep(60)
except KeyboardInterrupt:
    pass
