import telebot
import json
from telebot import types
from random import randint
TOKEN = "6325118238:AAEd9dSQRJGVlZOY9114xn0dhCqDAJj5YVk"
bot = telebot.TeleBot(TOKEN)
STATE_MENU = "menu"
STATE_BREAKFAST = "breakfast"
STATE_LUNCH = "lunch"
STATE_DINNER = "dinner"
STATE_RANDOM = "random"
user_states = {}
@bot.message_handler(commands=['start', 'назад'])
def send_greeting(message):
    user_states[message.chat.id] = STATE_MENU
    bot.send_photo(message.chat.id, 'https://png.pngtree.com/png-vector/20210826/ourlarge/pngtree-chef-and-knifes-png-image_3829141.jpg')
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('подобрать случайное блюдо')
    btn2 = types.KeyboardButton('рекомендуемое блюдо на завтрак')
    btn3 = types.KeyboardButton('рекомендуемое блюдо на обед')
    btn4 = types.KeyboardButton('рекомендуемое блюдо на ужин')
    btn5 = types.KeyboardButton('donat')
    btn6 = types.KeyboardButton('Купить премиум версию')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, 'Добро пожаловать!\nЯ могу вам порекомендовать блюдо', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def choose_mode(message):
    if message.text == 'рекомендуемое блюдо на завтрак':
        user_states[message.chat.id] = STATE_BREAKFAST
        with open('file_breakfast.json', 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
        i = randint(0, 27)
        dish = data[i]
        title = dish.get('title')
        description = dish.get('description')
        image = dish.get('image')
        recipe = dish.get('recipe')
        bot.send_message(message.chat.id, text=image)
        bot.send_message(message.chat.id, text=title)
        bot.send_message(message.chat.id, text=description)
        bot.send_message(message.chat.id, text=recipe)
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn3 = types.KeyboardButton('рекомендуемое блюдо на обед')
        btn4 = types.KeyboardButton('рекомендуемое блюдо на ужин')
        btn5 = types.KeyboardButton('Назад')
        markup.add(btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Что вы хотели бы сделать дальше?', reply_markup=markup)
    elif message.text == 'рекомендуемое блюдо на обед':
        user_states[message.chat.id] = STATE_LUNCH
        with open('file_lunch.json', 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
        i = randint(0, 27)
        dish = data[i]
        title = dish.get('title')
        description = dish.get('description')
        image = dish.get('image')
        recipe = dish.get('recipe')
        bot.send_message(message.chat.id, text=image)
        bot.send_message(message.chat.id, text=title)
        bot.send_message(message.chat.id, text=description)
        bot.send_message(message.chat.id, text=recipe)
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn3 = types.KeyboardButton('рекомендуемое блюдо на завтрак')
        btn4 = types.KeyboardButton('рекомендуемое блюдо на ужин')
        btn5 = types.KeyboardButton('Назад')
        markup.add(btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Что вы хотели бы сделать дальше?', reply_markup=markup)
    elif message.text == 'рекомендуемое блюдо на ужин':
        user_states[message.chat.id] = STATE_DINNER
        with open('file_dinner.json', 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
        i = randint(0, 27)
        dish = data[i]
        title = dish.get('title')
        description = dish.get('description')
        image = dish.get('image')
        recipe = dish.get('recipe')
        bot.send_message(message.chat.id, text=image)
        bot.send_message(message.chat.id, text=title)
        bot.send_message(message.chat.id, text=description)
        bot.send_message(message.chat.id, text=recipe)
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn3 = types.KeyboardButton('рекомендуемое блюдо на завтрак')
        btn4 = types.KeyboardButton('рекомендуемое блюдо на обед')
        btn5 = types.KeyboardButton('Назад')
        markup.add(btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Что вы хотели бы сделать дальше?', reply_markup=markup)
    elif message.text == 'подобрать случайное блюдо':
        user_states[message.chat.id] = STATE_RANDOM
        with open('file_random.json', 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
        i = randint(0, 81)
        dish = data[i]
        title = dish.get('title')
        description = dish.get('description')
        image = dish.get('image')
        recipe = dish.get('recipe')
        bot.send_message(message.chat.id, text=image)
        bot.send_message(message.chat.id, text=title)
        bot.send_message(message.chat.id, text=description)
        bot.send_message(message.chat.id, text=recipe)
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn3 = types.KeyboardButton('рекомендуемое блюдо на завтрак')
        btn4 = types.KeyboardButton('рекомендуемое блюдо на обед')
        btn5 = types.KeyboardButton('Назад')
        markup.add(btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Что вы хотели бы сделать дальше?', reply_markup=markup)
    elif message.text == 'donat':
        bot.send_message(message.chat.id, f'Mbank:{770200017}')
    elif message.text == 'Купить премиум версию':
        bot.send_message(message.chat.id, 'Еще в разработке')
    elif message.text == 'Назад':
        current_state = user_states.get(message.chat.id, STATE_MENU)
        if current_state == STATE_MENU:
            send_greeting(message)
        elif current_state == STATE_BREAKFAST:
            user_states[message.chat.id] = STATE_MENU
            send_greeting(message)
        elif current_state == STATE_LUNCH:
            user_states[message.chat.id] = STATE_MENU
            send_greeting(message)
        elif current_state == STATE_DINNER:
            user_states[message.chat.id] = STATE_MENU
            send_greeting(message)
        elif current_state == STATE_RANDOM:
            user_states[message.chat.id] = STATE_MENU
            send_greeting(message)
    else:
        bot.send_message(message.chat.id, 'Такая команда не найдена')
bot.polling()