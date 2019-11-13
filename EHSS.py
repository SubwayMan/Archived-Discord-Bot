import discord
import env_variables as ev
import data
import asyncio
client = discord.Client()

#check logon
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#adds to database upon joining
@client.event
async def on_member_join(member):
    if not data.isInside(str(member)):
        if len(data.dataholes) == 0: data.postsAdd(str(member), data.totalPosts())
        else: data.postsAdd(str(member), data.dataholes.pop(0))
        print(f'{str(member)} successfully added to the database')
    else: print(f'{str(member)} is already in the database')

#deletes from database upon leaving
@client.event
async def on_member_remove(member):
    if data.isInside(str(member)):
        data.postRemove(str(member))
        print(f'{str(member)} successfully removed from the database')
    else:
        print(f'{str(member)} wasn\'t in the database, hooray!')
#go through messages:
@client.event
async def on_message(message):

    #prevents self from reading own messages
    if message.author == client.user:
        return

    #leaves
    if message.content == '$quit':
        if str(message.author) == ev.admin:
            await message.channel.send('Logging out')
            await client.logout()
        else:
            await message.channel.send('Can only be force logged out by bot admin!')
    #load channelid and allowed channels
    channelid = client.get_guild(ev.ServerIds['EHSS'])
    allowed = ['spam', 'games', 'random', 'contest-discussion', 'ccc-prep', 'bots', 'beginner-questions']
    isValid = True
    try:
        senderID = data.getID(str(message.author))
        data.count(senderID)
    except:
        print(f'{str(message.author)} is not in the database.')
        return
    admincoms = ['$initializeData', '$remove']

    Members = channelid.members
    #swearjar
    for i in ev.swears:
        if i in message.content:
            await message.channel.send(f'{message.author.mention} Woah profanity!')
            data.swearJar(senderID)

    #set data
    if message.content.startswith('$initializeData') and str(message.author) == ev.admin:
        data.nuke()
        for i in range(len(Members)):
            data.postsAdd(Members[i], i)
        await message.channel.send('Database successfully reset.')

    #remove 1
    if message.content.startswith('$remove') and str(message.author) == ev.admin:
        for i in Members:
            if str(i) in message.content:
                data.postRemove(str(i))
                await message.channel.send(f'The user {str(i)} has been t e r m i n a t e d from the database.')
                return
        else:
            await message.channel.send(f'{message.author.mention}: you must specify a user to n u k e!')

    #add 1
    if message.content.startswith('$add') and str(message.author) == ev.admin:
        for i in Members:
            if str(i) in message.content:
                if not data.isInside(str(i)):
                    data.postsAdd(str(i), data.totalPosts())
                    await message.channel.send(f'{message.author.mention}: User successfully added to database')
                    return
        else:
            await message.channel.send(f'{message.author.mention}: Either user is already in database, or user is not in server.')

    #reject non admins
    if message.content in admincoms and str(message.author) != ev.admin:
        await message.channel.send('Only the bot admin can use this command!')

    #basic message sending
    if str(message.channel) in allowed:
        mentioned = message.mentions

        if message.content == '$help':
            embed = discord.Embed(title = 'BOT HELP', description = 'Commands for my bot. Enjoy! -Ty')
            embed.add_field(name = '$hello', value = 'Says hello :)')
            embed.add_field(name = '$truth', value = 'outputs some truth')
            embed.add_field(name = '$realtruth', value = 'outputs some real truth')
            embed.add_field(name = '$bruh', value = 'Says bruh - Bruh.')
            embed.add_field(name = '$stonks', value = 'STONKS')
            embed.add_field(name = '$users', value = 'Outputs number of users, online and offline.')
            embed.add_field(name = '$swearjar', value = 'Outputs number of times tagged users have sworn. If no users have been tagged, outputs number of times you have sworn.')
            embed.add_field(name = '$spamcount', value = 'Outputs number of times tagged users have messaged. If no users have been tagged, outputs number of times you have messaged.')
            embed.add_field(name = '$initializeData, $add, $remove', value = 'Bot owner tools. Contact me if you have a reason to use these - only useable by me on default.')
            await message.channel.send(content = None, embed = embed)
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

        elif message.content.startswith('$truth'):
            await message.channel.send('Tyler is cool')

        elif message.content.startswith('$realtruth'):
            await message.channel.send('Epstein didn\'t kill himself')

        elif message.content.startswith('$bruh'):
            #await message.channel.purge(limit = 1)
            await message.channel.send('bruh')

        elif message.content.startswith('$stonks'):
            #await message.channel.purge(limit = 1)
            await message.channel.send('$STONKS$')

        elif message.content == '$users':
            await message.channel.send(f'number of members: {channelid.member_count}')

        elif message.content.startswith('$swearjar'):
            print(len(mentioned))
            if len(mentioned) == 0:
                await message.channel.send(f'{message.author.mention} has sworn {data.returnSwears(senderID)} times.')
            else:
                for i in message.mentions:
                    senderID = data.getID(str(i))
                    await message.channel.send(f'{i.mention} has sworn {data.returnSwears(senderID)} times.')

        elif message.content.startswith ('$spamcount'):
            if len(mentioned) == 0:
                await message.channel.send(f'{message.author.mention} has sent {data.returnmsg(senderID)} messages.')
            else:
                for i in message.mentions:
                    senderID = data.getID(str(i))
                    await message.channel.send(f'{i.mention} has sent {data.returnmsg(senderID)} messages.')

#accesses bot
client.run(ev.botURL)
