# import telebot
# import requests
#
#
# bot = telebot.TeleBot('1338868375:AAE7QpHzWV4iG8xTcE7FK2nS8InPSU2mhmE')
# links = []
#
#
# @bot.message_handler(commands=['help'])
# def help(message):
#     answer = """
#     Bot has 2 options:
#     1. Type /last to see 10 last URLs.
#     2. Type a valid URL, that you want to short.
#     """
#
#     bot.send_message(message.from_user.id, answer)
#
#
# @bot.message_handler(commands=['last'])
# def last(message):
#
#     if not links:
#         bot.send_message(message.from_user.id, "Your don`t type any links yet.")
#         return
#
#     answer = "Ten last urls:"
#
#     for item in links:
#         answer += f"""
#         Your URL: {item['url']}
#         Short link: {item['short_link']} .
#         """
#
#     bot.send_message(message.from_user.id, f"{answer}")
#
#
# @bot.message_handler(content_types=['text'])
# def send_url(message):
#     print(message.from_user.id, message.text)
#     url = message.text
#
#     urls = [item["url"] for item in links]
#     if url in urls:
#         bot.send_message(message.from_user.id, "You have already have this URL in your ten last links. Please, type /last to see it.")
#         return
#
#     data = {"url": url}
#
#     response = requests.post(url='https://rel.ink/api/links/', json=data)
#     print(response)
#
#     if response.status_code == 400:
#         bot.send_message(message.from_user.id, "Enter a valid URL.")
#         return
#
#     short_link = 'https://rel.ink/' + response.json()["hashid"]
#     time = response.json()["created_at"]
#     data = {"url": url, "short_link": short_link, "time": time}
#
#     if len(links) >= 10:
#         links.pop(0)
#
#     links.append(data)
#
#     bot.send_message(message.from_user.id, f"Short link: {short_link} .")
#
#
# bot.polling(none_stop=True, interval=0)
