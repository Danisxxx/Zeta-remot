from pyrogram import Client, filters
from dotenv import load_dotenv
import os
import logging
from datetime import datetime
import requests, re, time
from Templates.chattext import *

load_dotenv(".env")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def zeta(bit):
    nix = Client.on_message(filters.command(bit, ["/", ".", ",", "-", "$", "%"]))
    return nix

def zetabt(bor):
    nox = Client.on_callback_query(filters.regex(bor))
    return nox