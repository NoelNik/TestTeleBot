import random, os, telebot, logging
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    print(message)
    print(message.text)
    sti = open('stickers/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton('Показать Феликса')
    item2 = types.KeyboardButton('Посмотреть милые видео')
    item3 = types.KeyboardButton('Прослушать твои любимые песни')
    item4 = types.KeyboardButton('Cекрет')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,
                     f'Дарова <b>{message.chat.first_name}</b>, я написал простенького бота специалльно для тебя',
                     parse_mode='html', reply_markup=markup, )


@bot.message_handler(content_types=['text'])
def message_echo(mesage):
    print(mesage)
    print(mesage.text)
    if mesage.text == 'Показать Феликса':
        im = open('Felix/photo_2022-07-06_09-05-09.jpg', 'rb')
        bot.send_photo(mesage.chat.id, im)

    if mesage.text == 'Посмотреть милые видео':
        with open('web_for_video/web') as f:
            f = [elem for elem in f]
        bot.send_message(mesage.chat.id, random.choice(f))

    if mesage.text == 'Прослушать твои любимые песни':
        song = open('songs/Stray Kids - Red Lights.mp3', 'rb')
        bot.send_audio(mesage.chat.id, song)

    if mesage.text == 'Cекрет':
        sti = open('stickers/sticker1.webp', 'rb')
        bot.send_message(mesage.chat.id, 'Люблю тя <3')
        bot.send_sticker(mesage.chat.id, sti)


bot.infinity_polling()
