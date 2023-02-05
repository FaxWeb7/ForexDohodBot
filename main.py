import telebot
import config
import sqlite3
from telebot import types
import helpers.messages as messages
import helpers.markups as markups

bot = telebot.TeleBot(config.BOT_TOKEN)
db = sqlite3.connect('./forexUsers.db', check_same_thread=False)
sql = db.cursor()
creator_id = 1056056149

priceGold = '100.000'
priceGoldMini = '40.000'

@bot.message_handler(commands=['start'])
def welcome(message):
    if sql.execute('SELECT * from users WHERE user_id = ?', (message.chat.id,)).fetchone() == None:
        sql.execute('INSERT INTO users VALUES (NULL, ?, ?, ?)', (message.chat.id , 0, 0))
        db.commit()

    if message.chat.id == creator_id:
        bot.send_message(message.chat.id, text=messages.startMessage.format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markups.menuAdminMarkup)
    else:
        bot.send_message(message.chat.id, text=messages.startMessage.format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markups.menuMarkup)


@bot.message_handler(content_types=['text'])
def Buttons(message):
    if message.chat.type == 'private':
        if message.text == 'Статистика доходности':
            bot.send_photo(message.chat.id, caption=messages.profitabilityMsg, parse_mode='html', photo=open('./assets/rate.jpg', 'rb'))
            bot.send_document(message.chat.id, document=open('./assets/GOLD.htm', 'rb'))
            bot.send_document(message.chat.id, document=open('./assets/GOLD.gif', 'rb'))
            bot.send_document(message.chat.id, document=open('./assets/GOLDmini.htm', 'rb'))
            bot.send_document(message.chat.id, document=open('./assets/GOLDmini.gif', 'rb'))

        elif message.text == '🗞️ Бесплатный канал':
            bot.send_message(message.chat.id, messages.freeChannelMsg, parse_mode='html')

        elif message.text == '☎️ Обратная связь':
            bot.send_message(message.chat.id, messages.feedbackMsg, parse_mode='html')

        elif message.text == 'Что за робот?':
            bot.send_photo(message.chat.id, photo=open('./assets/faq.jpg', 'rb'), caption=messages.faqMsg, parse_mode='html')

        elif message.text == '🤖 Купить Торгового Робота':
            bot.send_message(message.chat.id, '<b>Выберите подходящяй для вас вариант Торгового робота.</b>', parse_mode='html', reply_markup=markups.tariffsMarkup)
            
        elif message.text == '◀ Назад':
            if message.chat.id == creator_id:
                bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=markups.menuAdminMarkup)
            else:
                bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=markups.menuMarkup)

        ### FUNCTIONS ONLY FOR ADMINS ###
        elif message.text == '🟰🟰🟰 АДМИН ПАНЕЛЬ 🟰🟰🟰':
            if message.chat.id == creator_id:
                bot.send_message(message.chat.id, 'Вы перешли в админ панель', reply_markup=markups.adminMarkup)
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

        elif message.text == 'Статистика пользователей':
            if message.chat.id == creator_id:
                users = sql.execute('SELECT * from users').fetchall()
                bot.send_message(message.chat.id, messages.statisticMsg(users), parse_mode='html')
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

        elif message.text == 'Рассылка по пользователям':
            if message.chat.id == creator_id:
                msg = bot.send_message(message.chat.id, 'Введите текст рассылки (parse_mode=markdown)\n*text* - bold\n[Link text](https://link-url-here.org)')
                bot.register_next_step_handler(msg, writeMailing)
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')



###  INLINE CALLBACKS  ###
@bot.callback_query_handler(func=lambda call: True)
def InlineCallback(call):
    try:
        if call.message:
            if call.data == "backMenu":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы в главном меню', reply_markup=None) 

            elif call.data == "backRate":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Выберите подходящяй для вас вариант Торгового робота.</b>', parse_mode='html', reply_markup=markups.tariffsMarkup)

            elif call.data == 'subsGold':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=messages.paymentMsg(priceGold, 'gold'), parse_mode='html', reply_markup=markups.paymentMarkup)

            elif call.data == 'subsGoldMini':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=messages.paymentMsg(priceGoldMini, 'goldMini'), parse_mode='html', reply_markup=markups.paymentMarkup)

            elif call.data == 'docBtn':
                bot.send_message(creator_id, f'Пользователь с айди <b>{call.message.chat.id}</b> открыл чат с DOC по поводу покупки торгового робота', parse_mode='html')

    except Exception as e:
        print(repr(e))


### NEXT STEP MESSAGE HANDLERS ###
def writeMailing(message):
    users = sql.execute('SELECT user_id from users').fetchall()
    if message.text != '◀ Назад' and message.text != 'Статистика пользователей' and message.text != 'Рассылка по пользователям':
        if message.photo:
            for userId in users:
                bot.send_photo(userId[0], photo=message.photo[0].file_id, caption=message.caption, parse_mode='markdown')
            bot.send_message(creator_id, 'Рассылка прошла успешно!', parse_mode='html')
        else:
            for userId in users:
                bot.send_message(userId[0], message.text, parse_mode='markdown')
            bot.send_message(chat_id=creator_id, text='Рассылка прошла успешно!', parse_mode='html')
    else:
        bot.send_message(creator_id, 'Рассылка отменена', parse_mode='html')

if __name__ == '__main__':
    bot.polling(none_stop=True)
