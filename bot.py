import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está online: {bot.user.name}')
    check_roles.start() 

@tasks.loop(seconds=0)  
async def check_roles():
    guild_id = 123  # ID do seu servidor
    role_id = 123  # ID do cargo que deseja atribuir
    user_id = 123  # ID do usuário que deve receber o cargo
    guild = bot.get_guild(guild_id)
    role = guild.get_role(role_id)
    user = guild.get_member(user_id)
    
    if role and user:
        if role not in user.roles:
            await user.add_roles(role)
            print(f'{user.display_name} recebeu o cargo {role.name}.')



bot.run('sua token')
