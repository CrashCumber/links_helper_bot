import requests

from config import TOKEN, DB, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
from models import User, Link
import telebot
from database import SqlOrmConnection

db = SqlOrmConnection(MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, DB)
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    if db.session.query(User).get(message.from_user.id):
        bot.send_message(message.from_user.id, "Your have already used bot.")
        return

    user = User(id=message.from_user.id)
    db.session.add(user)
    db.session.commit()


@bot.message_handler(commands=['help'])
def help(message):
    answer = """
    Bot has 2 options: 
    1. Type /last to see 10 last URLs.
    2. Type a valid URL, that you want to short.
    """

    bot.send_message(message.from_user.id, answer)


@bot.message_handler(commands=['last'])
def last(message):
    links = db.session.query(Link).filter_by(user_id=message.from_user.id).all()

    if not links:
        bot.send_message(message.from_user.id, "Your don`t type any links yet.")
        return

    answer = "Ten last urls:"

    for item in links:
        answer += f"""
        Your URL: {item.url}
        Short link: {item.short_link} .
        """

    bot.send_message(message.from_user.id, f"{answer}")


@bot.message_handler(content_types=['text'])
def send_url(message):
    url = message.text

    if db.session.query(Link).filter_by(user_id=message.from_user.id, url=url).first():
        bot.send_message(message.from_user.id, "You have already have this URL in your ten last links. Please, type /last to see it.")
        return
    data = {"url": url}

    response = requests.post(url='https://rel.ink/api/links/', json=data)

    if response.status_code == 400:
        bot.send_message(message.from_user.id, "Enter a valid URL.")
        return

    short_link = 'https://rel.ink/' + response.json()["hashid"]
    data = {"url": url, "short_link": short_link, "user_id": message.from_user.id}

    links = db.session.query(Link).filter_by(user_id=message.from_user.id).all()
    if len(links) >= 10:
        delete_link = db.session.query(Link).filter_by(user_id=message.from_user.id).first()
        db.session.delete(delete_link)

    link = Link(**data)

    db.session.add(link)
    db.session.commit()

    bot.send_message(message.from_user.id, f"Short link: {short_link} .")


bot.polling(none_stop=True, interval=0)
