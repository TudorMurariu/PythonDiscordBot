import asyncio
import discord
from discord.ext import commands

token = ''
sender_email = ''
parola = ''
with open('C:\\Users\\tudor\\OneDrive\\Desktop\\Discord Bots\\input.txt','r') as f:
    args = f.readlines()
    token = args[0]
    sender_email = args[1]
    parola = args[2]

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print("redy")

@bot.command()
async def sex(ctx,member = discord.Member):
    print("pistol")
    await ctx.send("pistol "+ str(bot.latency * 100))

@bot.command()
async def clear(ctx , ammount = 5):
    if ammount == 0:
        await ctx.send("Zero messeges deleted")
    else:
        await ctx.channel.purge(limit = ammount + 1)

@bot.command()
async def kick(ctx, member : discord.Member, *, reson=None):
    await member.kick(reson)

@bot.command()
async def ban(ctx, member : discord.Member, *, reson=None):
    await member.ban(reson)

@bot.command()
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for banned_entry in banned_users:
        user = banned_entry.user
        if user.name == member.name and user.discriminator == member.discriminaotr:
            await ctx.guild.unban(user)
            return

text = "يلحق  ضررًا جسديًا لجميع الأعداء القريبين ، ويزيد بنسبة 20٪ لكل هجوم يتم تفاديه ، وزيادة تصل إلى 01010010 01100101 01110100 01100101 01110100 01100001 00100000 01000100 01100101 01110011 01100101 01110010 01110100 00100000 01100011 01101000 01100101 01100011 00100000 01110000 01110101 01100110 01101111 01110011 00100000 01100011 01110101 00100000 01100011 01100001 01100011 01100001 01101111 00100000 00101101 00100000 01000010 01110101 01100011 01100001 01110100 01100001 01110010 01100001 01110011 00001010 01101001 01101110 00100000 01110000 01101100 01110101 01110011 00100000 00111010 00100000 00001010 01000001 01000011 01010100 01001001 01010110 01000101 00111010 00100000 01001010 01100001 01111000 00100000 01100101 01101110 01110100 01100101 01110010 01110011 00100000 01000101 01110110 01100001 01110011 01101001 01101111 01101110 00101100 00100000 01100001 00100000 01100100 01100101 01100110 01100101 01101110 01110011 01101001 01110110 01100101 00100000 01110011 01110100 01100001 01101110 01100011 01100101 00101100 00100000 01100110 01101111 01110010 00100000 00110010 00100000 01110011 01100101 01100011 01101111 01101110 01100100 01110011 00101100 00100000 01100011 01100001 01110101 01110011 01101001 01101110 01100111 00100000 01100001 01101100 01101100 00100000 01101110 01101111 01101110 00101101 01110100 01110101 01110010 01110010 01100101 01110100 00100000 01100010 01100001 01110011 01101001 01100011 00100000 01100001 01110100 01110100 01100001 01100011 01101011 01110011 00100000 01100001 01100111 01100001 01101001 01101110 01110011 01110100 00100000 01101000 01101001 01101101 00100000 01110100 01101111 00100000 01100010 01100101 00100000 01100100 01101111 01100100 01100111 01100101 01100100 00101110 00100000 01001010 01100001 01111000 00100000 01100001 01101100 01110011 01101111 00100000 01110100 01100001 01101011 01100101 01110011 00100000 00110010 00110101 00100101 00100000 01110010 01100101 01100100 01110101 01100011 01100101 01100100 00100000 01100100 01100001 01101101 01100001 01100111 01100101 00100000 01100110 01110010 01101111 01101101 00100000 01100001 01101100 01101100 00100000 01100011 01101000 01100001 01101101 01110000 01101001 01101111 01101110 00100000 01100001 01110010 01100101 01100001 00100000 01101111 01100110 00100000 01100101 01100110 01100110 01100101 01100011 01110100 00100000 01100001 01100010 01101001 01101100 01101001 01110100 01101001 01100101 01110011 00101110 00100000 01000011 01101111 01110101 01101110 01110100 01100101 01110010 00100000 01010011 01110100 01110010 01101001 01101011 01100101 00100000 01100011 01100001 01101110 00100000 01100010 01100101 00100000 01110010 01100101 01100011 01100001 01110011 01110100 00100000 01100001 01100110 01110100 01100101 01110010 00100000 00110001 00100000 01110011 01100101 01100011 01101111 01101110 01100100 00101110 00001010 01000001 01110100 00100000 01110100 01101000 01100101 00100000 01100101 01101110 01100100 00100000 01101111 01100110 00100000 01110100 01101000 01100101 00100000 01100100 01110101 01110010 01100001 01110100 01101001 01101111 01101110 00101100 00100000 01001010 01100001 01111000 00100000 01110011 01110100 01110101 01101110 01110011 00100000 01100001 01101100 01101100 00100000 01101110 01100101 01100001 01110010 01100010 01111001 00100000 01100101 01101110 01100101 01101101 01101001 01100101 01110011 00100000 01100110 01101111 01110010 00100000 00110001 00100000 01110011 01100101 01100011 01101111 01101110 01100100 00100000 01100001 01101110 01100100 00100000 01100100 01100101 01100001 01101100 01110011 00100000 01110000 01101000 01111001 01110011 01101001 01100011 01100001 01101100 00100000 01100100 01100001 01101101 01100001 01100111 01100101 00100000 01110100 01101111 00100000 01110100 01101000 01100101 01101101 00101100 00100000 01101001 01101110 01100011 01110010 01100101 01100001 01110011 01100101 01100100 00100000 01100010 01111001 00100000 00110010 00110000 00100101 00100000 01100110 01101111 01110010 00100000 01100101 01100001 01100011 01101000 00100000 01100001 01110100 01110100 01100001 01100011 01101011 00100000 01100100 01101111 01100100 01100111 01100101 01100100 00101100 00100000 01110101 01110000 00100000 01110100 01101111 00100000 01100001 00100000 00110001 00110000 00110000 00100101 00100000 01101001 01101110 01100011 01110010 01100101 01100001 01110011 01100101 00101110"

@bot.command()
async def send(ctx,yahoo = "idk_bruh@yahoo.com",x = 1):
    from email import message
    from multiprocessing import context
    import smtplib
    global text

    import smtplib
    import ssl
    from email.message import EmailMessage

    for i in range(x):
        subiect = "Ti-ai luat virus fraiere"
        body = text
        global sender_email
        receiver_email = yahoo
        global parola

        message1 = EmailMessage()
        message1['From'] = sender_email
        message1['To'] = receiver_email
        message1['Subject'] = subiect
        message1.set_content(body)  

        context1 = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context1) as server:
            server.login(sender_email, parola)
            server.sendmail(sender_email, receiver_email, message1.as_string())

@bot.command()
async def setText(ctx, newText):
    global text
    text = newText


@bot.command()
async def showText(ctx):
    global text
    print(text)
    if len(text) < 4000:
        await ctx.send(text)
    else:
        await ctx.send("Textul este prea lung.")
        

bot.run(token)