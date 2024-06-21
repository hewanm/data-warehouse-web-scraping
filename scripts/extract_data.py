from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import configparser
import pandas as pd

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

message_ids = []
dates = []
sender_ids = []
messages = []

for message in history.messages:
    message_ids.append(message.id)
    dates.append(message.date)
    sender_ids.append(message.from_id)
    messages.append(message.message)
    print(message.id, message.date, message.from_id, message.message)


data = {
    'Message ID': message_ids, 
    'Date': dates, 
    'Sender ID': sender_ids, 
    'Message': messages}
df = pd.DataFrame(data)

df.to_csv('data/telegram_channel_data.csv', index=False)