import random
import asyncio
import aiohttp
import json
import requests
import os
from discord import Game
from discord.ext.commands import Bot


BOT_PREFIX = "!"


client = Bot(command_prefix=BOT_PREFIX)


# @client.event
# async def on_message(message):
#     # we do not want the bot to reply to itself
#     if message.author == client.user:
#         return
#
#     if message.content.startswith('!hello'):
#         msg = 'Hello {0.author.mention}'.format(message)
#         f'Hello {message.author.mention}
#         await client.send_message(message.channel, msg)


@client.command(name='hello', description="You will get a nice greeting", brief="Says hello",
                aliases=['hi', 'hey'], pass_context=True)
async def hello(message):
    possible_responses = [f'Well, hello there ',
                          f'Hey, how are you ',
                          f'What\'s kicking ']

    await client.say(random.choice(possible_responses + message.author.mention))


@client.command(name='8ball', description="Answers a yes/no question.", brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'], pass_context=True)
async def eight_ball():
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses))


@client.command(name='roastme', description="This will roast you", brief="You will get roasted!",
                aliases=['roast', 'roast_me'], pass_context=True)
async def roast_me():
    possible_responses = ['If laughter is the best medicine, your face must be curing the world.',
                          'You\'re so ugly, you scared the crap out of the toilet.',
                          'Your family tree must be a cactus because everybody on it is a prick.',
                          'No I\'m not insulting you, I\'m describing you.',
                          'It\'s better to let someone think you are an Idiot than to open your mouth and prove it.',
                          'If I had a face like yours, I\'d sue my parents.',
                          'Your birth certificate is an apology letter from the condom factory.',
                          'I guess you prove that even god makes mistakes sometimes.',
                          'The only way you\'ll ever get laid is if you crawl up a chicken\'s ass and wait.',
                          'You\'re so fake, Barbie is jealous.',
                          'I’m jealous of people that don’t know you!',
                          'My psychiatrist told me I was crazy and I said I want a second opinion. He said okay,'
                          ' you\'re ugly too.',
                          'You\'re so ugly, when your mom dropped you off at school she got a fine for littering.',
                          'If I wanted to kill myself I\'d climb your ego and jump to your IQ.',
                          'You must have been born on a highway because that\'s where most accidents happen.',
                          'Brains aren\'t everything. In your case they\'re nothing.',
                          'I don\'t know what makes you so stupid, but it really works.',
                          'I can explain it to you, but I can’t understand it for you.',
                          'Roses are red violets are blue, God made me pretty, what happened to you?',
                          'Behind every fat woman there is a beautiful woman.No seriously, your in the way.',
                          'Calling you an idiot would be an insult to all the stupid people.',
                          'You, sir, are an oxygen thief!',
                          'Some babies were dropped on their heads but you were clearly thrown at a wall.',
                          'Don\'t like my sarcasm, well I don\'t like your stupid.',
                          'Why don\'t you go play in traffic.',
                          'Please shut your mouth when you’re talking to me.',
                          'I\'d slap you, but that would be animal abuse.',
                          'They say opposites attract. I hope you meet someone who is good-looking,'
                          ' intelligent, and cultured.',
                          'Stop trying to be a smart ass, you\'re just an ass.',
                          'The last time I saw something like you, I flushed it.',
                          'I\'m busy now. Can I ignore you some other time?',
                          'You have Diarrhea of the mouth; constipation of the ideas.',
                          'If ugly were a crime, you\'d get a life sentence.',
                          'Your mind is on vacation but your mouth is working overtime.',
                          'I can lose weight, but you’ll always be ugly.',
                          'Why don\'t you slip into something more comfortable...like a coma.',
                          'Shock me, say something intelligent.',
                          'If your gonna be two faced, honey at least make one of them pretty.',
                          'Keep rolling your eyes, perhaps you\'ll find a brain back there.',
                          'You are not as bad as people say, you are much, much worse.',
                          'I don\'t know what your problem is, but I\'ll bet it\'s hard to pronounce.',
                          'You get ten times more girls than me? ten times zero is zero...',
                          'There is no vaccine against stupidity.',
                          'You\'re the reason the gene pool needs a lifeguard.',
                          'Sure, I\'ve seen people like you before - but I had to pay an admission.',
                          'How old are you? - Wait I shouldn\'t ask, you can\'t count that high.',
                          'Have you been shopping lately? They\'re selling lives, you should go get one.',
                          'You\'re like Monday mornings, nobody likes you.',
                          'Of course I talk like an idiot, how else would you understand me?',
                          'All day I thought of you... I was at the zoo.',
                          'To make you laugh on Saturday, I need to you joke on Wednesday.',
                          'You\'re so fat, you could sell shade.',
                          'I\'d like to see things from your point of view but I can\'t seem to get my head '
                          'that far up my ass.',
                          'Don\'t you need a license to be that ugly?',
                          'My friend thinks he is smart. He told me an onion is the only food that makes you cry,',
                          ' so I threw a coconut at his face.',
                          'Your house is so dirty you have to wipe your feet before you go outside.',
                          'I\'f you really spoke your mind, you\'d be speechless.',
                          'Stupidity is not a crime so you are free to go.',
                          'You are so old, when you were a kid rainbows were black and white.',
                          'If I told you that I have a piece of dirt in my eye, would you move?',
                          'You so dumb, you think Cheerios are doughnut seeds.',
                          'So, a thought crossed your mind? Must have been a long and lonely journey.',
                          'You are so old, your birth-certificate expired.',
                          'Every time I\'m next to you, I get a fierce desire to be alone.',
                          'You\'re so dumb that you got hit by a parked car.',
                          'Keep talking, someday you\'ll say something intelligent!',
                          'You\'re so fat, you leave footprints in concrete.',
                          'How did you get here? Did someone leave your cage open?',
                          'Pardon me, but you\'ve obviously mistaken me for someone who gives a damn.',
                          'Wipe your mouth, there\'s still a tiny bit of bullshit around your lips.',
                          'Don\'t you have a terribly empty feeling - in your skull?',
                          'As an outsider, what do you think of the human race?',
                          'Just because you have one doesn\'t mean you have to act like one.',
                          'We can always tell when you are lying. Your lips move.',
                          'Are you always this stupid or is today a special occasion?']

    await client.say(random.choice(possible_responses))


@client.command(name='serverinv', description='Will give you a link for server invite', brief='Creates server invite',
                aliases=['invite', 'serverinvite'], pass_context=True)
async def serverinv():
    await client.say('https://discord.gg/yveXcD6')


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.command(name='bitcoin', description='Current price of Bitcoin in $USD', brief='$bitcoin',
                pass_context=True)
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])


@client.command(name='weather', description="You will get the weather", brief="Weather details",
                aliases=[], pass_context=True)
async def weather():
    zip_search = '63389'
    api_key = 'appid=7a03b00d0882aebb22319016022eb33d'
    search_data = zip_search + ',us&'

    api_address = 'https://api.openweathermap.org/data/2.5/weather?&units=imperial&zip=' + search_data + api_key
    json_data = requests.get(api_address).json()
    await client.say((f"The current weather is {json_data['weather'][0]['description'].title()}. \nThe min temp"
                      f" is {json_data['main']['temp_min']}°F with a max temp of {json_data['main']['temp_max']}°F.\n"
                      f"The wind speed is: {json_data['wind']['speed']}mph, with a humidity of {json_data['main']['humidity']}%\n"
                      f"This weather information is provided for the following area code: {zip_search}"))


@client.command(name='forecast', decription='Weather forecast', brief='Forecast',
                aliases=[], pass_context=True)
async def forecast():
    zip_search = '63389'
    api_key = 'appid=7a03b00d0882aebb22319016022eb33d'
    search_data = zip_search + ',us&'

    api_address = 'https://api.openweathermap.org/data/2.5/forecast?&units=imperial&zip=' + search_data + api_key
    json_data = requests.get(api_address).json()
    await client.say(
        f"The weather for {json_data['list'][3]['dt_txt']}<--(3pm) will be {json_data['list'][3]['weather'][0]['description']}, a min temp of {json_data['list'][3]['main']['temp_min']}°F, and a max temp of {json_data['list'][3]['main']['temp_max']}°F.\n"
        f"The weather for {json_data['list'][11]['dt_txt']}<--(3pm) will be {json_data['list'][11]['weather'][0]['description']}, a min temp of {json_data['list'][11]['main']['temp_min']}°F, and a max temp of {json_data['list'][11]['main']['temp_max']}°F.\n"
        f"The weather for {json_data['list'][19]['dt_txt']}<--(3pm) will be {json_data['list'][19]['weather'][0]['description']}, a min temp of {json_data['list'][19]['main']['temp_min']}°F, and a max temp of {json_data['list'][19]['main']['temp_max']}°F.\n"
        f"The weather for {json_data['list'][27]['dt_txt']}<--(3pm) will be {json_data['list'][27]['weather'][0]['description']}, a min temp of {json_data['list'][27]['main']['temp_min']}°F, and a max temp of {json_data['list'][27]['main']['temp_max']}°F.\n"
        f"The weather for {json_data['list'][35]['dt_txt']}<--(3pm) will be {json_data['list'][35]['weather'][0]['description']}, a min temp of {json_data['list'][35]['main']['temp_min']}°F, and a max temp of {json_data['list'][35]['main']['temp_max']}°F.\n")


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans! Mwuahah"))
    print("Logged in as " + client.user.name)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(os.getenv('TOKEN'))
