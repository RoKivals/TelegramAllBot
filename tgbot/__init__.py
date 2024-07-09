import yaml
import sys
import os

WORK_DIR = os.path.dirname(__file__)

with open(f'{WORK_DIR}/config.yaml', 'r') as file:
    CONFIG = yaml.load(file, Loader=yaml.CLoader)

API_ID = CONFIG['api_id']
API_HASH = CONFIG['api_hash']
BOT_TOKEN = CONFIG['bot_token']
