from colorama import Fore
import json
import os
import discord


from discord.ext import (
    commands,
    tasks
)



client = discord.Client()
client = commands.Bot(
    command_prefix="logger.",
    self_bot=True
)
client.remove_command('help')

with open('config.json') as f:
    config = json.load(f)
    
token = config.get("token")
os.system('cls')

print(f"{Fore.WHITE}[ {Fore.CYAN}/ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord message logger by {Fore.WHITE}$€a#0001{Fore.LIGHTBLACK_EX}")
print(f"{Fore.WHITE}[ {Fore.CYAN}/ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}CREDITS : {Fore.WHITE}https://github.com/2wz")

print(f"\n{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}ready! to log")
print(f"{Fore.WHITE}[ {Fore.YELLOW}* {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Write {Fore.WHITE}logger.log <number>{Fore.LIGHTBLACK_EX} to log them\n")

def Init():
    if config.get('token') == "token-here":
        os.system('cls')
        print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}put your token into config.json\n\n"+Fore.RESET)
        exit()
    else:
        token = config.get('token')
        try:
            client.run(token, bot=False, reconnect=True)
            os.system(f'Discord message logger')
        except discord.errors.LoginFailure:
            print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Token is incorrect\n\n"+Fore.RESET)
            exit()


@client.command()
async def log(ctx, amount: int):
    f = open(f"logged/{ctx.message.channel}.txt","w+", encoding="UTF-8")
    total = amount
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Logging {Fore.WHITE}{amount}{Fore.LIGHTBLACK_EX} messages to {Fore.WHITE}logged/{ctx.message.channel}.txt{Fore.LIGHTBLACK_EX}!")
    async for message in ctx.message.channel.history(limit=amount):
        attachments = [attachment.url for attachment in message.attachments if message.attachments]
        try:
            if attachments:
                realatt = attachments[0]
                f.write(f"({message.created_at}) {message.author}: {message.content} ({realatt})\n")
                print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}logged message")
            else:
                f.write(f"({message.created_at}) {message.author}: {message.content}\n")
                print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}logged message")
        except Exception as e:
            print(f"{Fore.WHITE}[ {Fore.RED}$ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cannot log message from {Fore.WHITE}{message.author}")
            print(f"{Fore.WHITE}[ {Fore.RED}$ {Fore.WHITE}] {Fore.LIGHTBLACK_EX} {Fore.WHITE}{e}")
            total = total - 1
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Succesfully logged {Fore.WHITE}{total} {Fore.LIGHTBLACK_EX}messages!\n\n{Fore.WHITE}")


@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}error: {error}"+Fore.RESET)    
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}{error_str}"+Fore.RESET)

Init()
