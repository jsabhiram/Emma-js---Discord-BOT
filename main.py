#application-id 1378392697907187852
#public key 0883ddcf91c81b6de90996b272a8603985b253e0b41aed97a981e34ce984653a


# This example requires the 'message_content' intent.

import discord
import os

import google.generativeai as genai
token = os.environ["KEY"]


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        with open("history.txt","w+") as f:
            f.close()

    async def on_message(self, message):
        api = os.environ["gemini_api"]

        print(f'Message from {message.author}: {message.content}')
        if self.user != message.author and self.user in message.mentions:

            genai.configure(api_key=api)

            model = genai.GenerativeModel('gemini-2.0-flash')

            response = await model.generate_content_async("Be sweet and answer understanding the tone of user,also make the response feel like from a compassionate human,though keeping it short response not exceeding 5 sentences:"+message.content)
            with open("history.txt","a") as fd:
                
                fd.write(message.content+"\nResponse:"+response.text+"\n")
                fd.close()
            await message.channel.send(response.text)

            

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
