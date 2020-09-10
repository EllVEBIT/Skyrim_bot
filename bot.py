import discord
from discord.ext import commands
import asyncio
import random
import datetime
from datetime import timezone, tzinfo, timedelta
import time
import time as timeModul
import wikipedia
from bs4 import BeautifulSoup
import requests 
import json
import os 
 
token = 'NzUyODM2NDA0MzYyNjA4NjQx.X1dbiQ.MgCR_oeDqgQmjYvbDeknmh9maKQ'
bot = commands.Bot(command_prefix='Скайрим ')
bot.remove_command('help')
 
@bot.command()
async def скажи(ctx, arg: str):
  await ctx.send(arg)
 
@bot.command()
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def бан(ctx, member: discord.Member, *, reason: str = 'Не указана.'):
    await member.ban(reason=reason, delete_message_days=0)
    await ctx.send(embed = discord.
 Embed(description = (f"**{member} забанен**"),color=0xc582ff))
 
 
@bot.command()
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
async def кик(ctx, member: discord.Member, *, reason: str = 'Не указана.'):
    await member.kick(reason=reason)
    await ctx.send(embed = discord.
 Embed(description = (f"**{member} кикнут**"),color=0xc582ff))
 
@bot.command()
async def тест(ctx): 
 await ctx.send(embed = discord.Embed(description = ("**Все прекрасно!**"),color=0xc582ff))
 
@bot.command()
async def инвайт(ctx): 
 await ctx.send( "https://discord.com/api/oauth2/authorize?client_id=707317001047244800&permissions=8&scope=bot")
 
@bot.command()
async def юзер(ctx, Member: discord.Member = None ):
    if not Member:
        Member = ctx.author
    roles = (role for role in Member.roles )
    emb = discord.Embed(title='Инфа о участнике'.format(Member.name), description=f"Присоединился: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
    f"Ник: {Member.name}\n\n"
 
   f"Кастомный ник: {Member.nick}\n\n"
                                                                                      f"Статус: {Member.status}\n\n"
                                                                                      f"ID: {Member.id}\n\n"
                                                                                      f"Наивысшая роль: {Member.top_role}\n\n"
                                                                                      f"Аккаунт создан: {Member.created_at.strftime('%b %#d, %Y')}", 
                                                                                      color=0xc582ff, timestamp=ctx.message.created_at)
 
    emb.set_thumbnail(url= Member.avatar_url)
    emb.set_footer(icon_url= Member.avatar_url)
    emb.set_footer(text='Requested by: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)
 
 
@bot.command()
async def монетка(ctx):
    name = ('Вам выпал орёл', 'Вам выпала решка')
    await ctx.send(embed = discord.Embed(description = (f'**{random.choice(name)}**'), color=0xc582ff))
 
@bot.command()
async def версия(ctx):
 await ctx.send(embed = discord.Embed(description = ("**Версия бота: 2.3\nРаботает на Python**" ),color=0xc582ff))
 
 
@bot.command()
async def  бля(ctx, *, args):
    await ctx.send(embed = discord.Embed(description = (f"{''.join(random.sample(args,len(args)))}"), color=0xc582ff))
 
@bot.event
async def on_ready():
    print('Logged on as Calculator')
@bot.command()
async def посчитай(ctx, operation):
    await ctx.send(embed= discord.Embed(description = (f"Ответ: {eval(operation)}"), color=0xc582ff))
 
@bot.command()
async def очисти(ctx, amount= None):
         await ctx.channel.purge(limit = int(amount) + 1)
         await ctx.send(embed= discord.Embed(description = (f'**Очищено {amount} сообщений!**'), color=0xc582ff))
 
@bot.event
async def on_member_join(member):
    channel = bot.get_channel (715534298509475891)
 
    role = discord.utils.get (member.guild.roles, name = 'Newscomer')
 
    await member.add_roles (role)
    await channel.send (embed = discord.
Embed(description = (f"**{member.mention}  Добро пожаловать на сервер!**"),color=0xc582ff))
 
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'** {ctx.author.name}, данной команды не существует.**', color=0xc582ff))
 
@bot.command()  #help
async def помощь(ctx, *args):
 
    embed = discord.Embed(title= "Навигация по командам", colour=0xc582ff)
    embed.add_field(name= "Модерация",value= "бан, кик, разбан,\nмут")
    embed.add_field(name= "Развлечение",value= "монетка, бля, скажи,\nрулетка, бутылка, эмозя,\nстоит")
    embed.add_field(name= "Утилиты",value= "юзер, тест, версия,\nпосчитай, время, инвайт,\nвики, гривна, коронавирус\nочисти")
 
    await ctx.send(embed= embed)
 
@bot.command()
async def бутылка(ctx):
    gay = random.choice(ctx.guild.members)
    await ctx.send(embed = discord.Embed(description = f'**{gay} у нас на бутылке**', color=0xc582ff))
 
@bot.event
async def on_ready():
    game = discord.Game(r"Скайрим помощь")
    await bot.change_presence(status=discord.Status.online, activity=game)
 
@bot.command()
async def рулетка(ctx):
    name = ('Бум 💥🔫', 'Щелчёк 🔫')
    await ctx.send(embed = discord.Embed(description = (f'**{random.choice(name)}**'), color=0xc582ff))
 
 
@bot.command()
async def время(ctx):
    t = datetime.datetime.now()
    await ctx.send(embed = discord.Embed(description = (t.strftime('**%I часов: %M минут: %S секунд**')), color=0xc582ff)) 
 
 
 
@bot.command()
async def вики(ctx, *, text):
    wikipedia.set_lang("ru")
    new_page = wikipedia.page(text)
    summ = wikipedia.summary(text)
    emb = discord.Embed(
        title= new_page.title,
        description= summ,
         color=0xc582ff
    )
    emb.set_author(name= 'Полная статья', url= new_page.url, icon_url= 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png')
 
    await ctx.send(embed=emb)
 
 
@bot.command()
async def эмозя(ctx, emotie: discord.Emoji):
  color = 0xc582ff
  emb = discord.Embed(title = '**Эмозя**', colour = color)
  emb.set_image(url = emotie.url)
  await ctx.send(embed = emb)
 
 
class Currensy_grn:
    DOLAR_UA = 'https://www.google.com/search?sxsrf=ALeKk03fHfLO2ZLgvH2aCYHyylK169bp7Q%3A1584807405441&ei=7T12Xt69Gsyf6ASQjpvADw&q=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&gs_l=psy-ab.3..0i7i30j0i7i10i30l9.96278.96485..97742...0.2..0.99.195.2......0....1..gws-wiz.......0i71.ruuxORUhmxA&ved=0ahUKEwie6MDT-6voAhXMD5oKHRDHBvgQ4dUDCAs&uact=5'
 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}
 
    def get_currency_price(self):
        full_page = requests.get(self.DOLAR_UA, headers=self.headers)
 
        soup = BeautifulSoup(full_page.content, 'html.parser')
 
        convert = soup.findAll('span', {'class': 'DFlfde', 
                                        'class': 'SwHCTb',
                                        'data-precision': 2})
        global odna 
        odna = convert[0].text
 
@bot.command()
async def гривна(ctx):
    color = 0xc582ff
    cgrn =Currensy_grn()
    cgrn.get_currency_price()
    emb = discord.Embed(title = 'Курс гривны к доллару', colour = color)
    emb.add_field(name = 'Курс', value = f'1$ = {odna}грн')
    await ctx.send(embed = emb)
 
 
@bot.command(aliases=['коронавирус'])
async def корона(ctx, country):
    for item in  json.loads(requests.get("http://covid2019-api.herokuapp.com/v2/current").text)['data']:
        if item['location'] == country: 
            return await ctx.send(embed=discord.Embed(title='Статистика Covid-19', description=f'**Данные по {country}:**\nУмерло: {item["deaths"]}\nВыздоровело: {item["recovered"]}\nЗаражено: {item["confirmed"]}',color=0xc582ff))
 
@bot.command()
@commands.has_permissions( administrator = True )
async def разбан( ctx, *, member = None ):
    if member is None:
        await ctx.send(embed = discord.Embed(description = f'{ ctx.author.name }, обязательно укажите пользователя!', color = 0x4f4db3 ))
    else:
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            await ctx.guild.unban( user )
            await ctx.send(embed = discord.Embed(description = (f"**{member} разбанен**"),color=0xc582ff))
 
 
@bot.command()
async def стоит(ctx, arg):
    name = ('Думаю не стоит', 'Даже не знаю','Плохая идея','Хорошая идея', 'Прекрасная идея', 'Ужасная идея', 'Так себе')
    await ctx.send(embed = discord.Embed(description = (f'**{random.choice(name)}**'), color=0xc582ff))
 
@bot.command()
@commands.has_permissions(administrator = True)
async def мут (ctx, member:discord.Member,time:int,reason):
  muterole = discord.utils.get(ctx.guild.roles, name = 'Muted' )
  emb = discord.Embed(title= "Мут",color=0xc582ff)
  emb.add_field(name="Модератор",value=ctx.message.author.mention,inline=False)
  emb.add_field(name="Нарушитель",value=member.mention,inline=False)
  emb.add_field(name="Причина",value=reason,inline=False)
  emb.add_field(name="Время(секунд)",value=time,inline=False)
  await member.add_roles(muterole)
  await ctx.send(embed = emb)
  await asyncio.sleep(time)
  await member.remove_roles(muterole)
 
import googletrans
from googletrans import Translator
@bot.command()
async def переведи(ctx, lang: str, r: str, *, text):
    t = Translator()
    result = t.translate(text, src = lang, dest = r)
    emb = discord.Embed(title = f'Перевод: \n result.text', colour = discord.Colour.green())
    await ctx.send(embed = emb)
 
@bot.event
async def on_message(message):
 if message:
  print(f'{message.author}:{message.content}')
 await bot.process_commands(message)
 
token = os.environ.get ('BOT_TOKEN')

bot.run(str(token)

