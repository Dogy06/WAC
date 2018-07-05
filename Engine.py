import wolframalpha
import json
import discord
import asyncio

client = discord.Client()



@client.event
async def on_message(message):

    if message.author == client.user:
        return


    input = str(message.content)

    print('User:', input)

    inputs = input

    app_id = "2AEKHJ-4JTQH4AUK3"

    client1 = wolframalpha.Client(app_id)

    result = client1.query(inputs)

    answer = next(result.results).text

    print("Smart:", answer)

    out = answer

    output = out

    await client.send_message(message.author, output)







@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDY0Mzc1NjgzNzUwMTY2NTM4.Dh-GCg.o7zJ0DZBPKqQsgAU5ELrsD5E7yE')

data = {}


def writeToJSONFile(path, fileName, data):

    filePathNameWExt = './' + path + '/' + fileName + '.json'

    with open(filePathNameWExt, 'w') as fp:

        json.dump(data, fp)





