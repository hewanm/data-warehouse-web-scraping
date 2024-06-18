from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import configparser

# Access credentials
config = configparser.ConfigParser()
config.read('./config.ini')

api_id = config.get('default', 'api_id')
api_hash = config.get('default', 'api_hash')

client = TelegramClient('anon', api_id, api_hash)

client.start()

channel = client.get_entity('DoctorsET')
chat_id = channel.id

history = client(GetHistoryRequest(
    peer=chat_id,
    limit=10000,
    offset_id=0,
    offset_date=None,
    add_offset=0,
    max_id=0,
    min_id=0,
    hash=0
))
for message in history.messages:
    print(message.id, message.date, message.from_id, message.message)