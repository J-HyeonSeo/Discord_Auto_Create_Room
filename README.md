<h1>Discord Auto Create Room</h1>
Discord automatic room creation program

This program is an automatic room creation bot program created using the discord.py library.


The bot performs the following functions:

1. If the 'Room-Create' channel does not exist, it is automatically created.

2. When a user enters 'Room-Create', a channel is created.

3. Set the limit previously set by the administrator to the channel.

4. Move the user to the created channel.

5. When all users leave the channel, the channel is removed.

----------------------------------------------------

<h2>Files</h2>

<p>main.py -> Python file that runs the main source code.</p>
<p>config.py -> A file that parses and writes the config.txt file.</p>

----------------------------------------------------

<h2>How to use</h2>

1. Open config.txt and fill in the parameters.

ex)
<p>=========== AUTO CREATE CONFIG ==========</p>
<p>limit=4</p>
<p>token=123412341234123412341234123</p>

2. Run Main.py


<Strong>It's Very Simple!!</Strong>


---------------------------------------------------

<h2>Chat Commands</h2>
<p>/ping : Check that the bot is running.</p>

<p>/admin : Check if the user who started the chat is an administrator.</p>

<p>/limit : Set the occupancy limit for automatically created rooms.</p>

---------------------------------------------------

<h2>Python and library version.</h2>

<img src="https://img.shields.io/badge/Python v.3.8.16-3776AB?style=flat&logo=python&logoColor=white" />  <img src="https://img.shields.io/badge/discord.py v.2.2.3-5865F2?style=flat&logo=discord&logoColor=white" />
