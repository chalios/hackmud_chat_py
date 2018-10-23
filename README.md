hackmud_chat (Unofficial)
-------------------------

###### Installation
Just `pip install hackmud_chat`

Learn by example:
``` python
     >>> from hackmud_chat import Account

     # 'Login' to the hackmud chat API
     >>> account = Account(token='yourtokenhere')

     # Don't have a token? No panic...
     # Get into your hackmud client and enter the command chat_pass
     >>> account = Account(passwd='thegivenpass')

     # Account's properties:
     >>> account.users
     >>> account.token

     # Get the user you want to interact with
     >>> user1 = account.get_user('user1')

     # User's properties:
     >>> user1.messages
     >>> user1.channels

     # Deeper, inside channels:
     >>> user1.channels[0].users # The list of channel's members

     # Access user's messages (sorted by time [latest == earliest])
     >>> last = user1.messages[-1]

     # Message object:
     >>> last.id
     >>> last.time
     >>> last.from_user
     >>> last.text
     >>> last.to_user  # Optional
     >>> last.channel  # Optional
     >>> last.is_join  # Optional
     >>> last.is_leave # Optional

     # Update messages:
     >>> user1.update_history() # Updates user1.messages

     # User's actions:
     >>> user1.tell('user2', 'Hello')                   # Send a private message to user2
     >>> user1.say('0000', 'H1 3vry0ne!')               # Send a message to channel 0000
     >>> user1.sayTo('0000', 'user2', "You're a noob!") # Send a message to chan 0000 formated like:
                                                        # @user2: You're a noob!
```

See some examples in [examples/](./examples/)

Documentation is coming...
