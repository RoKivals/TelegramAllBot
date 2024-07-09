import requests
import json

BOT_API = '6340884843:AAGcQK17XIbFj1qI_JrsCZG_zNJYRXGdUIQ'


def get_group_id(group_name: str):
    responce = requests.get(f'https://api.telegram.org/bot{BOT_API}/getUpdates')
    json_responce = json.loads(responce.text)
    list_of_results = json_responce["result"]

    if len(list_of_results) == 0:
        return None

    chat_id = None
    for update in list_of_results:
        try:
            chat_info = update["my_chat_member"]["chat"]
        except KeyError:
            chat_info = update["message"]["chat"]
        if chat_info["title"] == group_name:
            chat_id = chat_info['id']
            break

    return chat_id


def main():
    get_group_id('test')


if __name__ == '__main__':
    main()
