from telethon.sync import TelegramClient, events
from telethon import events, types
import asyncio
import logging
from tgbot import BOT_TOKEN, API_ID, API_HASH

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

bot = TelegramClient('all_bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


def users_list_to_str(users):
    res = " ".join(f"@{i}" for i in users)
    return res


def check_push_user(user, sender_id):
    return not user.deleted and user.id != sender_id and not user.bot


async def get_all_users_in_group_without_sender_and_bots(client, group_id, sender):
    answer = [user.username async for user in client.iter_participants(group_id) if check_push_user(user, sender)]
    return answer


async def get_all_users_in_group(client, group_id):
    answer = [user.username async for user in client.iter_participants(group_id) if not user.deleted]
    return answer


async def get_admins_of_group(client, group_id):
    answer = [user.id async for user in
              client.iter_participants(group_id, filter=types.ChannelParticipantsAdmins)]
    return answer


@bot.on(events.NewMessage(pattern="/all"))
async def handler(event: events.NewMessage):
    group_id = event.chat_id
    sender = event.sender_id
    admins = await get_admins_of_group(bot, group_id)

    if sender not in admins:
        print("Fail")

    else:
        users = await get_all_users_in_group_without_sender_and_bots(bot, group_id, sender)
        response = users_list_to_str(users)
        await event.respond(response)


# @client.on(events.InlineQuery)
# async def handle_inline_query(event):
#     query = event.query
#     sender = await event.get_user()
#     print(f'Получен инлайн-запрос от: {sender.username}')
#     await client.answer_inline_query(
#         event.id,
#         [types.InputTextMessageContent('Пример ответа на инлайн-запрос')]
#     )


def main():
    with bot:
        bot.run_until_disconnected()