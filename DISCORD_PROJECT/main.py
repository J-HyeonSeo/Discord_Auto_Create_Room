import discord
from discord.ext import commands
import settings

target_name = "ROOM-CREATE"
target_channel = None
new_room_name = "Personal Voice Room"
limit = 4
discord_bot_token = settings.get_token()

bot_channels = [] #This list contains the channels created by the bot.

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready(): #bot initialize.
    global target_channel
    global limit
    limit = settings.get_limit()
    print("limit:", limit)
    print('Bot: {}'.format(bot.user))
    print(bot.user.name)
    print(bot.user.id)

    #load channels created by bot.
    ids = settings.get_channel_ids()
    keep_channel = []
    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.id in ids:
                if len(channel.members) > 0:
                    bot_channels.append(channel)
                    keep_channel.append(str(channel.id))
                else:
                    await channel.delete()
    settings.reset_channel_ids() #reset candidate ids.

    '''
    The channel id where the user exists is added back to the text file.
    '''
    for channel in keep_channel:
        settings.add_channel_ids(channel)

    #make main room.
    for guild in bot.guilds:
        for channel in guild.channels:
            if channel.name == target_name:
                target_channel = channel
                break

        if target_channel: #already exists main channel(create room channel).
            pass
        else:
            channel = await guild.create_voice_channel(target_name)
            target_channel = channel


@bot.event
async def on_guild_channel_delete(channel): #Event that occurs when a chat room is deleted

    if channel.name == target_name:
        for guild in bot.guilds:
            new_channel = await guild.create_voice_channel(target_name)
            target_channel = new_channel
            print(new_channel)

@bot.event
async def on_voice_state_update(member, before, after): #Changes occurred in the voice chat room

    if before.channel is not None:
        if before.channel in bot_channels: #before is not main room.
            if len(before.channel.members) == 0:
                bot_channels.remove(before.channel)
                await before.channel.delete()


    #enter 'create voice room', make channel -> player move to channel

    if after.channel is not None:
        if after.channel.name == target_name:
            for guild in bot.guilds:
                #create channel
                channel = await guild.create_voice_channel(name = new_room_name, user_limit = limit)

                #move channel position.
                parent_category = target_channel.category
                parent_position = target_channel.position + 1
                await channel.edit(category=parent_category, position=parent_position)

                #Authorize the channel.
                overwrite = discord.PermissionOverwrite()

                overwrite.manage_channels = True
                overwrite.send_messages = True
                await channel.set_permissions(member, overwrite=overwrite)

                #Move the player who changed the channel to the new channel to be created.
                await member.move_to(channel)
                bot_channels.append(channel) #add channel to bot created channel list.
                settings.add_channel_ids(str(channel.id)) #write the settings.txt


@bot.command()
async def ping(ctx): #bot test command.
    await ctx.send(ctx.author.mention)

@bot.command(name='admin') #check the administrator.
async def managerCheck(ctx):
    if ctx.guild:
        if ctx.message.author.guild_permissions.administrator:
            await ctx.send('you are administrator in this guild')
        else:
            await ctx.send('you are not administrator in this guild')

@bot.command(name='limit') #set the room limit.
async def limit(ctx, value):
    if ctx.guild:
        if ctx.message.author.guild_permissions.administrator:
            try:
                settings.set_limit(int(value), discord_bot_token)
                if 1 <= int(value) <= 99:
                    await ctx.send("Room occupancy limit set to "+ str(value) +" people.")
                    global limit
                    limit = int(value)
                else:
                    await ctx.send("Please enter an integer from 1 to 99!!")
            except:
                await ctx.send("Please enter an integer value!")

bot.run(discord_bot_token)