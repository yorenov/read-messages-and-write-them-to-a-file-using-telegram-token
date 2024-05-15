import json
from telethon import TelegramClient, events

# https://my.telegram.org/auth?to=apps 
# 1)_ Заходишь по этой ссылке, авторизуешься и создаешь приложение(много гайдов в ютубе, не сложно, за минуту делается),
# 2)_ Затем устанавливаешь библиотеку telethon - 
# pip install telethon 
# 3)_ Полученные данные после созд. приложения вводишь в файл, там расписано что-куда, так-же токен туда вводишь от бота.
# Запускаешь, только не забудь в файле указать путь, где должен будет сохраняться файл с сообщениями.

api_id = '' #Впиши сюда аппи ид взятый с телеграмма после создания приложения
api_hash = '' #Впиши сюда аппи хеш взятый с телеграмма после создания приложения
bot_token = '' #Впиши сюда токен бота
path_to_json = 'C:\\Users\\admin\\Desktop\\projects\\messages.json' #Впиши сюда путь куда должен сохраниться файл с сообщениями

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(outgoing=True))
async def handle_outgoing_message(event):
    # Логирование исходящих сообщений
    message_data = {
        'id': event.id,
        'text': event.text,
        'to_user_id': event.peer_id.user_id if hasattr(event.peer_id, 'user_id') else 'unknown'
    }
    
    with open(path_to_json, 'a', encoding='utf-8') as file:
        json.dump(message_data, file, ensure_ascii=False)
        file.write('\n') 

client.start()
client.run_until_disconnected()
