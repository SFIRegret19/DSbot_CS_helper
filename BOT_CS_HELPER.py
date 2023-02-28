#from email import message
from discord_components import Select,SelectOption,ComponentsBot
from credits import bot_token_ds
import discord, random, time, asyncio,os,os.path
from discord.ext import commands
"""
guild_welcome = {957270765739311225}

intents = discord.Intents.all()

client = discord.Client(intents=intents)
"""
client = discord.Client()
token = bot_token_ds

#bot = commands.Bot(command_prefix="!", intents=intents)

#bot = commands.Bot(command_prefix="!")
bot = ComponentsBot('!')
"""
@bot.event
async def on_member_join(member):
    welcome = bot.get_channel(guild_welcome[member.guild.id]) #Получение канала для приветствия
    embed=discord.Embed(title="Добро пожаловать!", description=f"К нам в {member.guild.name} приехал {member.mention}!", color=0xCC974F) #Embed
    await welcome.send(embed=embed)
      #  await bot.process_commands(message)
"""
#-----------------------------------------------SELECT-------------------------------------------------------------------
async def selectBox(ctx):
    await ctx.send(content = 'Select an option!',components = [Select(
                                                            placeholder = 'Select something!',
                                                            options=[
                                                                SelectOption(label='Option 1',value = '1'),
                                                                SelectOption(label='Option 2',value = '2'),
                                                                SelectOption(label='Option 3',value = '3'),
                                                                SelectOption(label='Cancel Option',value = 'Cancel'),
                                                            ],
                                                            custom_id = 'SelectTesting'
    )])

    interaction = await bot.wait_for('select_option',check=lambda inter: inter.custom_id == 'SelectTesting' and inter.user == ctx.author)
    print(interaction)
    res = interaction.values[0]
    print(res)
    if res == 'Cancel':
        await interaction.send('You have canceled option')
    if res == '3':
        await interaction.send('3')

@bot.command(name = 'test')
async def testing(ctx):
    await selectBox(ctx)

#--------------------------------------------------------------------------------------------------------
@bot.event
async def on_ready():
    print('BOT ACTIVATED !!!')

@bot.event
async def on_guild_join(guild):
    text_channels = guild.text_channels
    
    if text_channels:
        channel = text_channels[0]
    await channel.send('Привет я бот помощник по конфигам в кс.\nДля того что я могу введи команду << !info >> ')


@bot.command(name='info')
async def inf(ctx):
        await ctx.send('Привет я бот помощник по конфигам в кс.\nВот что я могу: ')
        embed = discord.Embed(colour=ctx.author.color,timestamp=ctx.message.created_at)
        embed.add_field(name='!info',value='۞ Информация о всех командах бота', inline=False),
        embed.add_field(name='!whois',value='֎ Выдаёт информацию о пользователе', inline=False),
        embed.add_field(name='!configs_info',value='۞ Все конфиги пользователей сервера', inline=False),
        embed.add_field(name='!send_config "твоё название конфига" + файл с расширением .cfg (твой конфиг)',value='֎ Добавляет конфиг пользователя на сервер', inline=False),
        embed.add_field(name='!get_config "@имя создателя конфига" "название конфига"',value='۞ Выдаёт конфиг пользователя', inline=False),
        embed.add_field(name='!how_get_config',value='֎ Даёт полную информацию по получению конфига из CS:GO', inline=False),
        embed.add_field(name='!get_help_ph',value='۞ Скидывает скриншоты с поиском конфига', inline=False),
        embed.add_field(name='!spam "@кому" "сколько сообщений" "текст сообщения"',value='֎ Спам сообщениями', inline=False),
        embed.add_field(name='!roll "ваш вариант выпадения числа (от 1 до 6)"',value='۞ Миниигра с кубиком', inline=False),
        embed.add_field(name='!clear "сколько сообщений удалить" << ONLY FOR ADMIN >>',value='֎ Удаляет несколько последних сообщений', inline=False),
        await ctx.send(embed=embed)
        await ctx.send('Приятного использования :heart:')

@bot.command(name = 'whois') #Функция проверки пользователя
async def who(ctx, user:discord.Member=None):
    if user == None:
        user=ctx.author #если пользователь не ввел ничье имя, то проверяем автора сообщения
    #Генерируем сообщение с инфой о пользователе
    embed = discord.Embed(colour=user.color,timestamp=ctx.message.created_at)
    embed.set_author(name=f"User info - {user}"),
    embed.set_thumbnail(url=user.avatar_url),
    embed.add_field(name='ID: ', value=str(user.id)+"#"+str(user.discriminator), inline=False)
    embed.add_field(name='Name: ', value=user.display_name, inline=False)
    embed.add_field(name='Created at: ', value=user.created_at, inline=False)
    embed.add_field(name='Joined at: ', value=user.joined_at, inline=False)
    embed.add_field(name='Top role: ', value=user.top_role.mention, inline=False)
    #Отправляем сгенерированное сообщение
    await ctx.send(embed=embed)

@bot.command(name='how_get_config')
async def hgc(ctx):
    embed = discord.Embed(colour=ctx.author.color,timestamp=ctx.message.created_at)
    embed.add_field(name='1. Введи эти команды в консоли в CS:GO (без ~ ~):',value='۞۞۞',inline=False),
    embed.add_field(name='~ host_writeconfig "название вашего конфига" ~',value='Cохранить конфиг кс го', inline=False),
    embed.add_field(name='2. Далее надо найти и открыть папку ~ Steam ~',value='Введи ~ !get_help_ph ~ в чат бота, чтобы он выдал сакриншоты с папками и файлами для установки конфига', inline=False),
    embed.add_field(name='3. Далее надо найти и открыть папку ~ userdata ~',value='۩۩۩', inline=False),
    embed.add_field(name='4. Открываем папку с цифрами (SteamID) ~ (твои цифры) ~',value='₪₪₪', inline=False),
    embed.add_field(name='5. Далее надо найти и открыть папку ~ 730 ~',value=':sunglasses: :sunglasses: :sunglasses:', inline=False),
    embed.add_field(name='6. Далее надо найти и открыть папку ~ local ~',value='▬▬▬', inline=False),
    embed.add_field(name='7. Далее надо найти и открыть папку ~ cfg ~',value='֎֎֎', inline=False),
    embed.add_field(name='8. Поздравляю !!!',value='Здесь все твои конфиги', inline=False),
    await ctx.send(embed=embed)

@bot.command(name='get_help_ph')
async def ghp(ctx):
    my_files = [
        discord.File('./ScreenHelpForBot/1.png'),
        discord.File('./ScreenHelpForBot/2.png'),
        discord.File('./ScreenHelpForBot/3.png'),
        discord.File('./ScreenHelpForBot/4.png'),
        discord.File('./ScreenHelpForBot/5.png'),
        discord.File('./ScreenHelpForBot/6.png')
    ]
    await ctx.author.send(files=my_files)
    await ctx.send('Отправил в личку!')

@bot.command(name = 'spam')
async def sending(ctx, user:discord.Member, ints, *args):
    if str(user.top_role) != 'ADMIN':
        strt=''
        for a in range(len(args)):
            strt+=str(" "+args[a])
        embed = discord.Embed(colour=ctx.author.color, timestamp=ctx.message.created_at)
        embed.add_field(name="Внимание!", value=strt, inline=False)
        for _ in range(int(ints)):
            await user.send(embed=embed)
        await ctx.send(f'Сообщение: {strt} было отправлено пользователю {user.name} - {ints} раз(a)')
    else:
        await ctx.send('Нельзя так делать !!!')

@bot.command(name = 'clear')
async def delt(ctx, *args):
    if str(ctx.author.top_role) == 'ADMIN':    
        await ctx.channel.purge(limit=int(args[0])+1)
    else:
        await ctx.send('У вас недостаточно прав')   

@bot.command(name="configs_info") 
async def cfginf(ctx):
    global default_folder
    id_serv = str(ctx.message.guild.id)
    embed = discord.Embed(colour=ctx.author.color, timestamp=ctx.message.created_at)
    embed.set_author(name='Все конфиги пользователей на этом сервере:')
    files_in_serv = [f for f in os.listdir(f'./{default_folder}/{id_serv}')]
    users_in_serv = [(await bot.fetch_user(int(u))).name for u in files_in_serv]
#    print(files_in_serv) - файлы с id пользователей на сервере
#    print(ctx.message.guild.member_count) - количество пользователей на сервере
#    print(users_in_serv) - имена пользователей по файлам с id на сервере
    for i in files_in_serv:
        for j in users_in_serv:
            configs_user = [k for k in os.listdir(f'./{default_folder}/{id_serv}/{i}')]
            cfg_prod = ''
            for l in configs_user:
                cfg = str(l)[:len(str(l))-4] + ' - ' + str(l)
                cfg_prod += cfg + '\n'
            embed.add_field(name=j,value=cfg_prod,inline=True)
        
    await ctx.send(embed=embed)
#--------------------------получение и выдача конфига пользователя-----------------------------
default_folder = 'CONFIGS_POL'

@bot.command(name='send_config')
async def send_cfg(ctx,*args):
    global default_folder
    id_serv = str(ctx.message.guild.id)
    id_polz = str(ctx.message.author.id)
    conf = ctx.message.attachments[0]
    if str(conf)[-4:] == '.cfg':
        if not os.path.exists(default_folder + '/' + id_serv):
            os.mkdir(default_folder + '/' + id_serv)
            if not os.path.exists(default_folder + '/' + id_serv + "/" + id_polz):
                os.mkdir(default_folder + '/' + id_serv + "/" + id_polz)

        if not os.path.exists(f'./{default_folder}/{id_serv}/{id_polz}/{args[0]}.cfg'):
            await conf.save(f'./{default_folder}/{id_serv}/{id_polz}/{args[0]}.cfg')
            await ctx.send(f'Конфиг << {args[0]}.cfg >> добавлен на сервер')
        else:
            await ctx.send('Такой конфиг уже есть. Либо у тебя есть конфиг с таким названием :smile:')
    else:
        await ctx.send('Можно отправлять файлы только с разрешением << .cfg >>')

@bot.command(name='get_config')
async def get(ctx,user:discord.Member,*args):
    global default_folder
    id_polz = user.id
    id_serv = str(ctx.message.guild.id)
    path = (f'./{default_folder}/{id_serv}/{id_polz}')
    await ctx.send(f'Конфиг << {args[0]}.cfg >> пользователя {user.name} выдан:',file=discord.File(f'./{default_folder}/{id_serv}/{id_polz}/{args[0]}.cfg'))

#   print(num_files,files_in_folder) # кол-во файлов в папке пользователя и какие файлы там лежат
#---------------------МИНИ ИГРЫ----------------------------------------
@bot.command(name='roll')
async def roll(ctx,*args):
    bet = args[0]
    dice = random.randint(1,6)
    await ctx.send('Вы бросили кубик')
    if int(bet) == dice:
        await asyncio.sleep(1)
        await ctx.send('Поздравляю !!! Ты угадал.\nВам выпало число '+ str(dice) + ':medal:')
    else: 
        await asyncio.sleep(1)
        await ctx.send('Увы. Ты не угадал.\nВам выпало число '+ str(dice))

#--------------------секретки-----------------
@bot.event
async def on_message(message):
    if message.content == 'налей пиво':
        if message.author.name != 'CS_HELPER':
            await asyncio.sleep(1)
            await message.channel.send('Держи :beer:')
            await bot.process_commands(message)
        await bot.process_commands(message)
    await bot.process_commands(message)

@bot.command(name='hello')
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Приветствую тебя, {author.mention}!')
   # print(ctx.message.channel.id)

bot.run(token)