#!/usr/bin/env python
#~*~ coding: utf-8 ~*~

from hackmud_chat import Account
from time import sleep

# 'Login' to hackmud chat API
acct = Account(token='yourtoken')
# OR
# acct = Account(passwd='yourpasshere')

# Get the user from which you want to monitor chat
user = acct.get_user('user')

# Setup a last index for monitoring new messages
last = 0
try:
    while True:

        # Get the number of messages received since last
        new_msgs = user.messages_since(last)

        # If we received new messages
        if  new_msgs > 0:
            # Get the time of last message
            current = user.messages[-1].time

            # Extract new messages since last index
            for message in user.messages[-new_msgs:]:
                # Format text then output to stdout.
                to = ''
                if message.to_user:
                    to = ' -> {}'.format(message.to_user)
                print '{time} - {_from}{to}: {msg}'.format(time=message.time,
                                                      _from=message.from_user,
                                                      to=to,
                                                      msg=message.text)
            # Update the last message time
            last = current

        # Avoid overloading hackmud's server
        sleep(1.5)

        # Reload user's history
        user.update_history()

except KeyboardInterrupt:
    # Gracefully handle <ctrl+c> exit
    pass
