import telebot
from telebot import types

bot = telebot.TeleBot('YOUR API')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'hello <b>{message.from_user.first_name}</b>! \nПриятного пользования нашим ботом! :)'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['hello'])
def start(message):
    mess = f'hello <b>{message.from_user.first_name}</b>!'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['youtube'])
def youtube(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт", "https://youtube.com"))
    bot.send_message(message.chat.id, 'Go to YouTube', reply_markup=markup)


@bot.message_handler(commands=['btn'])
def btn(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    website = types.KeyboardButton('Website')
    photo = types.KeyboardButton('Photo')
    help = types.KeyboardButton('Help')
    all = types.KeyboardButton('ALL')
    id = types.KeyboardButton('ID')
    insta = types.KeyboardButton('Instagram')
    markup.add(website, photo, help, all, id, insta)
    bot.send_message(message.chat.id, 'buttons:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, "Hi!", parse_mode='html')
    elif message.text == 'ID':
        bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}", parse_mode='html')
    elif message.text == 'ALL':
        bot.send_message(message.chat.id, message, parse_mode='html')
    elif message.text == 'Help':
        bot.send_message(message.chat.id, 'Admin: <b>@???</b>', parse_mode='html')
    elif message.text == 'Photo':
        photo = open('img/photo.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'location':
        bot.send_location(message.chat.id, 59.4497585, 24.8502119)
    elif message.text == 'Website':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Посетить сайт", "https://youtube.com"))
        bot.send_message(message.chat.id, 'Go to YouTube', reply_markup=markup)
    elif message.text == 'Instagram':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Go to Instagram", "https://www.instagram.com/"))
        bot.send_message(message.chat.id, 'Our Instagram', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'nice photo bro!')


bot.polling(none_stop=True)
