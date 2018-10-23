#!/usr/bin/env python
#~*~ coding: utf-8 ~*~

from hackmud_chat import Account

acct = Account(token='yourtoken')
user = acct.get_user('user')
other = acct.get_user('other')

channel = user.channels[0].name # The user must have joined the channel before

# Send message to the other user:
user.tell(other.name, 'Hello!')

# Send a message to a channel
user.say(channel, 'Hello everyone!')

# Send a public  message in channel that target specific user
user.sayTo(channel, other.name, 'Hello!')
