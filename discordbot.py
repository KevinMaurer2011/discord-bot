import random
import asyncio
import aiohttp
import json
import requests
import praw
import discord
from discord import Game
from discord.ext.commands import Bot
# from bs4 import BeautifulSoup
from discord.ext import commands
import os

# TOKEN = open('C:/Users/kevin/OneDrive/Documents/discord_token.txt', 'r').readline()  # used when hosting locally
# client_id, client_secret, user_agent = open('C:/Users/kevin/OneDrive/Documents/reddit-info.txt',
#                                             'r').read().splitlines()  # reddit info, hosting locally

client_id = os.getenv('client_id') # heroku
client_secret = os.getenv('client_secret') # heroku
user_agent = 'meme-bot' # heroku


client = Bot(command_prefix='!')

print(discord.__version__)


@client.command(name='hello', description="You will get a nice greeting and be mentioned", brief="Says hello!!!",
                aliases=['hi', 'hey'], pass_context=True)
async def hello(ctx):
    possible_responses = ['Well, hello there ',
                          'Hey, how are you ',
                          'What\'s kicking ']
    await ctx.send(random.choice(possible_responses) + ctx.message.author.mention)


@client.command(name='youthere', decription='You will know if they are there!', brief='You there?',
                alises=[], pass_context=True)
async def you_there(ctx):
    possible_responses = ['OHHHHH YEAHHHH SON!!!',
                          'Where else would I be?']
    await ctx.send(random.choice(possible_responses))


@client.command(name='meme', decription='Gets you a nice meme from reddit!', brief='More meme?',
                alises=[], pass_context=True)
async def reddit_meme(ctx):
    reddit_memes = praw.Reddit(client_id=client_id,
                              client_secret=client_secret,
                              user_agent=user_agent)

    subreddit_choices = ['memes', 'offensivememes', 'dankmemes', 'blackpeopletwitter', 'MemeEconomy', 'wholesomememes',
                         'AdviceAnimals', 'trippinthroughtime', 'WhitePeopleTwitter', 'boottoobig', 'bonehurtingjuice',
                         'dankchristianmemes', 'fakehistoryporn', 'HistoryMemes', 'musicmemes', 'MEOW_IRL', 'woof_irl',
                         'youdontsurf', 'starterpacks', 'wheredidthesodago', 'coaxedintoasnafu', 'lewronggeneration',
                         'im14andthisisdeep', 'ImGoingToHellForThis', 'surrealmemes', 'BikiniBottomTwitter', 'ahegao']

    random_choice = random.choice(subreddit_choices)
    memes_submissions = reddit_memes.subreddit(random_choice).new()
    post_to_pick = random.randint(1, 30)
    await ctx.send(
        f'This pic is from : https://reddit.com/r/{random_choice}/new/, it is post number {str(post_to_pick)}.'
        f' Sorted by New ')

    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)


# @bot.command(name='urban')
# async def urban_dictionary(*ctx):
#     search = ' '.join(str(c) for c in ctx)
#     r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(search))
#     soup = BeautifulSoup(r.content)
#
#     try:
#         await bot.say(soup.find("div", attrs={"class": "meaning"}).text)
#
#     except AttributeError:
#         await bot.say('Search returned no results, try something else, or be more broad.')


@client.command(name='youtube', description='Get a result from youtube', brief='YouTube result',
                aliases=['yt'])
async def youtube(*ctx):
    string = '+'.join(str(c) for c in ctx)
    await ctx.send(f'https://youtube.com/results?search_query={string}')


@client.command(name='serverinfo', description='Information about the current server', brief='Server info',
                aliases=['servinfo', 'sinfo', 'server'], pass_context=True)
async def server_info(ctx):
    embed = discord.Embed(name='{}\'s info'.format(ctx.message.server.name), description='Here\'s what I could find.',
                          color=0x00ff00)
    embed.set_author(name='ItsKraZyKev')
    embed.add_field(name='Name', value=ctx.message.server.name, inline=True)
    embed.add_field(name='ID', value=ctx.message.server.id, inline=True)
    embed.add_field(name='Roles', value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name='Members', value=len(ctx.message.server.members), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await ctx.send(embed=embed)


@client.command(name='info', description='Get detailed info on the user who called me (you!)', brief='User info',
                aliases=['myinfo', 'meinfo'], pass_context=True)
async def info(ctx):
    embed = discord.Embed(name='', description='Here\'s what I could find.',
                          color=0x00ff00)
    embed.set_author(name='ItsKraZyKev')
    embed.add_field(name="Name", value=discord.User.name, inline=True)
    embed.add_field(name="ID", value=discord.User.id, inline=True)
    embed.add_field(name="Status", value=discord.Member.status, inline=True)
    embed.add_field(name="Highest role", value=discord.Member.top_role)
    embed.add_field(name="Joined", value=discord.Member.joined_at)
    # embed.set_thumbnail(url=)
    await ctx.send(embed=embed)


@client.command(name='8ball', description="Answers a yes/no question", brief="Answers from the beyond",
                aliases=['eight_ball', 'eightball', '8-ball'], pass_context=True)
async def eight_ball():
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.send(random.choice(possible_responses))


@client.command(name='roll')
async def role_dice(num_dice, num_side):
    if num_dice.isalpha() or num_side.isalpha():
        await client.send(' Numbers only boys')

    num_dice = int(num_dice)
    num_side = int(num_side)

    if num_dice > 1000000000 or num_side > 1000000000:
        await client.send('Nice try there bud, maybe use a number less than 1 billion? XD ')

    if num_dice < 1 or num_side < 6:
        await client.send('No, you can\'t roll less than 1 die, or a die with less than 6 sides!')


    else:
        rolled_list = []
        for i in range(0, int(num_dice)):
            rolled_list.append(random.randint(1, int(num_side)))
        await client.send(rolled_list)


@client.command(name='test')
async def test_test(ctx):
    # await client.send('I\'m here good buddy! All is well!')
    await ctx.send('I\'m here good buddy! All is well!')

@client.command(name='troll')
async def troll_troll(ctx):
    await ctx.send('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░\n'
                   '░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░\n'
                   '░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░\n'
                   '░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░\n'
                   '░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░\n'
                   '█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█\n'
                   '█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█\n'
                   '░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░\n'
                   '░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░\n'
                   '░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░\n'
                   '░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░\n'
                   '░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░\n'
                   '░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░\n'
                   '░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░\n'
                   '░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░')


@client.command(name='spamtroll')
async def troll_troll(ctx):
    await ctx.send('░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░\n'
                   '░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░\n'
                   '░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░\n'
                   '░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░\n'
                   '░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░\n'
                   '█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█\n'
                   '█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█\n'
                   '░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░\n'
                   '░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░\n'
                   '░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░\n'
                   '░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░\n'
                   '░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░\n'
                   '░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░\n'
                   '░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░\n'
                   '░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░\n' * 3)


@client.command(name='killme', description="You will die.", brief="You die.",
                aliases=['kill me'], pass_context=True)
async def kill_me(ctx):
    possible_responses = ['I\'ve heard you\'re a low-down Yankee liar.',
                          'Fill your hand, you son of a bitch.',
                          'You gotta ask yourself a question, "Do I feel lucky?". Well, do you punk?',
                          'Smile, you son of a bitch.',
                          'Say hello to my little friend.',
                          'Remember Sully, when I promised to kill you last? I lied.',
                          'You\'re disease, and I\'m the cure.',
                          'My name is Inigo Montoya. You killed my father. Prepare to die.',
                          'I have come here to chew bubblegum and kick ass. And I\'m all out of bubblegum.',
                          'You\'re out of bullets. And you know what that means, you\'re shit out of luck.',
                          'I come in peace. And you go in pieces.',
                          'There must be a hundred reasons why I don\'t blow you away. Right now,'
                          ' I can\'t think of one.',
                          'Yippee-ka-yay motherf--ker.',
                          'Hasta La Vista, Baby.',
                          'Long Live The King',
                          '...And you will know my name is the Lord, when I lay my vengeance upon thee.',
                          'You\'re fired!',
                          'Resistance is futile.',
                          'Dodge this.',
                          'You Shall Not Pass.']
    await ctx.send(random.choice(possible_responses) + ':gun:')


@client.command(name='eat', description="Need to know where to eat?", brief="FOOD!",
                aliases=[], pass_context=True)
async def food_eat(ctx):
    possible_responses = ['Applebees',
                          'McDonalds bitchhhhhhh',
                          'Taco Bell']

    await ctx.send(random.choice(possible_responses))


@client.command(name='picofkevdick', description="This is my Dick", brief="DicK!",
                aliases=[], pass_context=True)
async def dick_pic(ctx):
    await ctx.send('https://pics.me.me/mall-hiro-trolled-xd-16312171.png')


@client.command(name='roastme', description="This will roast you", brief="You will get roasted!",
                aliases=['roast', 'roast_me'], pass_context=True)
async def roast_me(ctx):
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

    await ctx.send(random.choice(possible_responses))


@client.command(name='dick', description='You will get some dick art!', brief='Dicks, man...',
                aliases=[], pass_context=True)
async def dick_art(ctx):
    dick_list = [' ░░░░█─────────────█──▀──\n'
                 ' ░░░░▓█───────▄▄▀▀█──────\n'
                 ' ░░░░▒░█────▄█▒░░▄░█─────\n'
                 ' ░░░░░░░▀▄─▄▀▒▀▀▀▄▄▀─────\n'
                 ' ░░░░░░░░░█▒░░░░▄▀───────\n'
                 ' ▒▒▒░░░░▄▀▒░░░░▄▀────────\n'
                 ' ▓▓▓▓▒░█▒░░░░░█▄─────────\n'
                 ' █████▀▒░░░░░█░▀▄────────\n'
                 ' █████▒▒░░░▒█░░░▀▄───────\n'
                 ' ███▓▓▒▒▒▀▀▀█▄░░░░█──────\n'
                 ' ▓██▓▒▒▒▒▒▒▒▒▒█░░░░█─────\n'
                 ' ▓▓█▓▒▒▒▒▒▒▓▒▒█░░░░░█────\n'
                 ' ░▒▒▀▀▄▄▄▄█▄▄▀░░░░░░░█───\n',
                 '———————————————\n'
                 ' ────────▄▀▀▀▀▀▀▀▄───────\n'
                 ' ───────█▒▒▒▒▒▒▒▒▒█──────\n'
                 ' ──────█▒▒▒▒▒▒▒▒▒▒█──────\n'
                 ' ──────█▒▒▀▄▄▒▄▄▀▒█──────\n'
                 ' ─▄▄▄──█▒▒─▀─▒─▀─▒█──────\n'
                 ' █░░░▀▄█▒▒▒▒▒▒▒▒▒▒█──────\n'
                 ' ▀▄░░░▄▀▀▄▒▀▀▀▀▀▒▒▒▒▀▀▄───\n'
                 ' ─▀▄▄▀░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄─\n'
                 ' ─█▒▀▄░░░░░░▀▄▒▒▒▒▒▒█▒▒█─\n'
                 ' ─▀▄▀▒▀▄░░░░░░▀▄▄▒▒▒▒▀▄▀─\n'
                 ' ───█▌▌▄▀░░░░░░░░░▀▄▌▌█───\n'
                 ' ───▀█▌█░░░░░▄░░░░░██▀───\n'
                 ' ─────██▀▄▄▄▄▀▄▄▄▄▀██───\n']
    await ctx.send(random.choice(dick_list))


@client.command(name='serverinv', description='Will give you a link for server invite', brief='Creates server invite',
                aliases=['invite', 'serverinvite'], pass_context=True)
async def serverinv(ctx):
    await ctx.send('https://discord.gg/yveXcD6')


@client.command(name='square', description='Will square whatever number you give me!', brief='Squares number',
                aliases=[])
async def square(ctx, number):
    squared_value = int(number) * int(number)
    await ctx.send(str(number) + " squared is " + str(squared_value))


@client.command(name='cube', description='Will cube whatever number you give me!', brief='Cubes number',
                aliases=[])
async def cube_number(ctx, number):
    triple_value = int(number) * int(number) * int(number)
    await ctx.send(f'{str(number)} cubed is {str(triple_value)}')


@client.command(name='bitcoin', description='Current price of Bitcoin in $USD', brief='$bitcoin',
                pass_context=True)
async def bitcoin(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])


@client.command(name='weather', description="You will get the weather", brief="Weather details", aliases=[], )
async def weather(ctx, zip_code):
    try:
        zip_search = str(zip_code)
        api_key = 'appid=7a03b00d0882aebb22319016022eb33d'
        search_data = zip_search + ',us&'

        api_address = 'https://api.openweathermap.org/data/2.5/weather?&units=imperial&zip=' + search_data + api_key
        json_data = requests.get(api_address).json()
        await ctx.send((f"The current weather is {json_data['weather'][0]['description'].title()}. \nThe min temp"
                        f" is {json_data['main']['temp_min']}°F with a max temp of {json_data['main']['temp_max']}°F.\n"
                        f"The wind speed is: {json_data['wind']['speed']}mph, with a humidity of {json_data['main']['humidity']}%\n"
                        f"This weather information is provided for the following area code: {zip_search}"))
    except:
        await ctx.send('This doesn\'t seem to be a valid zip. Give that another go :)')


@client.command(name='forecast', decription='Weather forecast', brief='Forecast',
                aliases=[], pass_context=True)
async def forecast(ctx):
    zip_search = '63389'
    api_key = 'appid=7a03b00d0882aebb22319016022eb33d'
    search_data = zip_search + ',us&'

    api_address = 'https://api.openweathermap.org/data/2.5/forecast?&units=imperial&zip=' + search_data + api_key
    json_data = requests.get(api_address).json()
    await ctx.send(
        f"The weather for {json_data['list'][3]['dt_txt']}<--(3pm) will be {json_data['list'][3]['weather'][0]['description']}, a min temp of {json_data['list'][3]['main']['temp_min']}°F, and a max temp of {json_data['list'][3]['main']['temp_max']}°F.\n"
        f"The weather for {json_data['list'][11]['dt_txt']}<--(3pm) will be {json_data['list'][11]['weather'][0]['description']}, a min temp of {json_data['list'][11]['main']['temp_min']}°F, and a max temp of {json_data['list'][11]['main']['temp_max']}°F.\n"
        f"The weather for {json_data['list'][19]['dt_txt']}<--(3pm) will be {json_data['list'][19]['weather'][0]['description']}, a min temp of {json_data['list'][19]['main']['temp_min']}°F, and a max temp of {json_data['list'][19]['main']['temp_max']}°F.\n"
        f"The weather for {json_data['list'][27]['dt_txt']}<--(3pm) will be {json_data['list'][27]['weather'][0]['description']}, a min temp of {json_data['list'][27]['main']['temp_min']}°F, and a max temp of {json_data['list'][27]['main']['temp_max']}°F.\n"
        f"The weather for {json_data['list'][35]['dt_txt']}<--(3pm) will be {json_data['list'][35]['weather'][0]['description']}, a min temp of {json_data['list'][35]['main']['temp_min']}°F, and a max temp of {json_data['list'][35]['main']['temp_max']}°F.\n")


@client.event
async def on_ready():
    game = discord.Game("with the API")
    await client.change_presence(status=discord.Status.idle, activity=game, afk=False)
    print("Logged in as " + client.user.name)


# async def list_servers():
#     await ctx.wait_until_ready()
#     while not ctx.is_closed:
#         print("Current servers:")
#         for server in ctx.guilds:
#             print(server.name)
#         await asyncio.sleep(600)


# bot.loop.create_task(list_servers())
client.run(os.getenv('TOKEN'))  # for  hosting on Heroku...
# client.run(TOKEN)  # for running locally
