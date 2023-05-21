AUTO_CREATE

This program is an automatic room creation bot program created using the discord.py library.


The bot performs the following functions:

1. If the 'Room-Create' channel does not exist, it is automatically created.

2. When a user enters 'Room-Create', a channel is created.

3. Set the limit previously set by the administrator to the channel.

4. Move the user to the created channel.

5. When all users leave the channel, the channel is removed.

----------------------------------------------------

files

main.py -> Python file that runs the main source code.
config.py -> A file that parses and writes the config.txt file.

----------------------------------------------------

how to use

limit=
token=

All you have to do is fill in the values for the parameters.

ex)

limit=4
token=123412341234123412341234

---------------------------------------------------

Python and library version.

python = v.3.8.16
discord.py = v.2.2.3

