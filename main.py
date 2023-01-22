import telebot
import config
import datetime
import sqlite3
import time
from telebot import types
from datetime import datetime, timedelta
from pyqiwip2p import QiwiP2P
from random import randint
from yoomoney import Client, Quickpay, Authorize
import threading

import helpers.messages as messages
import helpers.markups as markups


###  MAIN CONSTANTS  ###
bot = telebot.TeleBot(config.BOT_TOKEN)
p2p = QiwiP2P(auth_key=config.QIWI_TOKEN) #qiwi payment
yooClient = Client(config.YOOMONEY_TOKEN) #yoomoney payment
db = sqlite3.connect('./forexUsers.db', check_same_thread=False)
sql = db.cursor()

creator_id = 1056056149
groupId = -1001871050533
pricePerMonth = 70
pricePer3Months =  170
usdrub = 70
walletAddress = 'TRoha2nsRGVDeDQomuFhtCXBo1uRBqs2W5'


###  START MESSAGE  ###
@bot.message_handler(commands=['start'])
def welcome(message):
    if sql.execute('SELECT * from users WHERE user_id = ?', (message.chat.id,)).fetchone() == None:
        sql.execute('INSERT INTO users VALUES (NULL, ?, ?, ?)', (message.chat.id , 0, 0))
        db.commit()

    if message.chat.id == creator_id:
        bot.send_message(message.chat.id, text=messages.startMessage.format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markups.menuAdminMarkup)
    else:
        bot.send_message(message.chat.id, text=messages.startMessage.format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markups.menuMarkup)


###  BUTTONS HANDLER  ###
@bot.message_handler(content_types=['text'])
def Buttons(message):
    if message.chat.type == 'private':
        if message.text == 'Сколько можно заработать?':
            bot.send_photo(message.chat.id, caption=messages.revenueMsg, parse_mode='html', photo=open('./assets/rate.jpeg', 'rb'))

        elif message.text == '🗞️ Бесплатный канал':
            bot.send_message(message.chat.id, messages.freeChannelMsg, parse_mode='html')

        elif message.text == '☎️ Обратная связь':
            bot.send_message(message.chat.id, messages.feedbackMsg, parse_mode='html')

        elif message.text == 'Бесплатное обучение':
            bot.send_photo(message.chat.id, photo=open('./assets/education.jpg', 'rb'), caption=messages.educationMsg, parse_mode='html')

        elif message.text == '🛒 Тарифы':
            bot.send_message(message.chat.id, '<b>Выберите длительность доступа в ForexDohod VIP SIGNALS 🔒</b>', parse_mode='html', reply_markup=markups.tariffsMarkup)

        elif message.text == '📊 Подписка':
            if sql.execute('SELECT untill from users WHERE user_id = ?', (message.chat.id,)).fetchone()[0] != '0':
                nowTs = time.time()
                untill = str(sql.execute('SELECT untill from users WHERE user_id = ?', (message.chat.id,)).fetchone()).replace("'","").replace("(","").replace(")","").replace(",","")
                untillTs = time.mktime(datetime.strptime(untill, "%Y-%m-%d %H:%M:%S").timetuple())

                if untillTs - nowTs <= 0:
                    sql.execute('UPDATE users SET isSub=?, untill=? WHERE user_id=?', (0,0,message.chat.id))
                    db.commit()
                    markup = types.InlineKeyboardMarkup()
                    subscribeBtn = types.InlineKeyboardButton("🛒 Перейти к покупке", callback_data='backRate')
                    markup.add(subscribeBtn)

                    bot.send_message(message.chat.id, 'Ваша подписка на <b>ForexDohod VIP SIGNALS</b> закончилась\nПерейти к покупке?', parse_mode='html' ,reply_markup=markup)
                
                elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (message.chat.id, 1,)).fetchone() != None:
                    untill = sql.execute('SELECT untill from users WHERE user_id = ?', (message.chat.id,)).fetchone()[0]
                    markup = types.InlineKeyboardMarkup()
                    subscribeBtn = types.InlineKeyboardButton("👉 ForexDohod VIP SIGNALS", callback_data='privateLink')
                    markup.add(subscribeBtn)

                    bot.send_message(message.chat.id, 'Ваша подписка на <b>ForexDohod VIP SIGNALS</b> действует до ' + untill + '\n\n<b>Для получения доступа к каналу нажмите на соответствующую кнопку ниже 👇</b>\n\n⚠ Если у вас появляется ошибка ссылка не действительна или чат не существует или вы не можете войти в сообщество, просто попробуйте ещё раз через пару минут (особенность Telegram)', parse_mode='html' ,reply_markup=markup)

            elif sql.execute('SELECT id from users WHERE user_id = ? and isSub = ?', (message.chat.id, 0,)).fetchone() != None:
                markup = types.InlineKeyboardMarkup()
                subscribeBtn = types.InlineKeyboardButton("🛒 Перейти к покупке", callback_data='backRate')
                markup.add(subscribeBtn)

                bot.send_message(message.chat.id, 'У вас нет активных подписок. Перейти к покупке?', reply_markup=markup)

        ###  FUNCTIONS ONLY FOR CREATOR  ###
        elif message.text == '🟰🟰🟰 АДМИН ПАНЕЛЬ 🟰🟰🟰':
            if message.chat.id == creator_id:
                bot.send_message(message.chat.id, 'Вы перешли в админ панель', reply_markup=markups.adminMarkup)
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

        elif message.text == 'Статистика пользователей':
            if message.chat.id == creator_id:
                users = sql.execute('SELECT * from users').fetchall()
                privateUsers = sql.execute("SELECT * from users WHERE isSub=?", (1,)).fetchall()
                usersId = sql.execute('SELECT user_id from users WHERE isSub=?', (0,)).fetchall()
                privateUsersId = sql.execute('SELECT * from users WHERE isSub=?', (1,)).fetchall()

                bot.send_message(message.chat.id, messages.statisticMsg(users, privateUsers, parseUsers, usersId, privateUsersId), parse_mode='html')
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

        elif message.text == 'Изменить данные пользователя':
            if message.chat.id == creator_id:
                msg = bot.send_message(message.chat.id, 'Введите измененные данные пользователя через пробел (12345678 1 22-22-2022 22:22:22 ) (user_id, isSub, untill) (user_id, 0 - обнулить)')
                bot.register_next_step_handler(msg, changeUserData)
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

        elif message.text == 'Добавить подписчика в секретный канал':
            if message.chat.id == creator_id:
                msg = bot.send_message(message.chat.id, 'Введите id пользователя')
                bot.register_next_step_handler(msg, addPrivateUser)
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

        elif message.text == 'Удалить подписчика с секретного канала':
            if message.chat.id == creator_id:
                msg = bot.send_message(message.chat.id, 'Введите id пользователя, которого хотите удалить')
                bot.register_next_step_handler(msg, deleteUser)
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

        elif message.text == 'Написать сообщение пользователю':
            if message.chat.id == creator_id:
                msg = bot.send_message(message.chat.id, 'Введите id и текст сообщения через "==="')
                bot.register_next_step_handler(msg, writeToUser)
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

        elif message.text == 'Рассылка по пользователям':
            if message.chat.id == creator_id:
                msg = bot.send_message(message.chat.id, 'Введите текст рассылки')
                bot.register_next_step_handler(msg, writeMailing)
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

        elif message.text == '◀ Назад':
            if message.chat.id == creator_id:
                bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=markups.menuAdminMarkup)
            else:
                bot.send_message(message.chat.id, 'Вы в главном меню', reply_markup=markups.menuMarkup)


###  INLINE CALLBACKS  ###
@bot.callback_query_handler(func=lambda call: True)
def InlineCallback(call):
    try:
        if call.message:
            if call.data == 'privateLink':
                subLink = bot.create_chat_invite_link(groupId, member_limit=1, expire_date=(int(time.time())+10))
                markup = types.InlineKeyboardMarkup()
                subscribeBtn = types.InlineKeyboardButton("👉 ВСТУПИТЬ 👈", url=str(subLink.invite_link))
                markup.add(subscribeBtn)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='✅ Вход открыт, ссылка действительна 10 секунд', reply_markup=markup)

            elif call.data == 'addOneMonthUser':
                addUser(call.message.text.split(':')[1], 30)

            elif call.data == 'addThreeMonthsUser':
                addUser(call.message.text, 90)

            elif call.data == "backMenu":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы в главном меню', reply_markup=None) 

            elif call.data == "backRate":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Выберите длительность доступа в ForexDohod VIP SIGNALS 🔒</b>', parse_mode='html', reply_markup=markups.tariffsMarkup)

            elif call.data == 'subsOne':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=messages.paymentMsg(pricePerMonth, 1),reply_markup=markups.paymentMarkup, parse_mode='html')

            elif call.data == 'subsThree':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=messages.paymentMsg(pricePer3Months, 3),reply_markup=markups.paymentMarkup3, parse_mode='html')             
                
            elif call.data == "usdt":
                messages.paymentWayMsg(bot, pricePerMonth, walletAddress, 1, call, None, None)

            elif call.data == "usdt3":
                messages.paymentWayMsg(bot, pricePer3Months, walletAddress, 3, call, None, None)

            elif call.data == 'qiwi':
                comment = str(call.message.chat.id) + '_' + str(randint(1000, 9999))
                bill = p2p.bill(amount=int(pricePerMonth)*int(usdrub), lifetime=15, comment=comment)
                messages.paymentWayMsg(bot, pricePerMonth, None, 1, call, bill.pay_url, bill.bill_id)

            elif call.data == 'qiwi3':
                comment = str(call.message.chat.id) + '_' + str(randint(1000, 9999))
                bill = p2p.bill(amount=int(pricePer3Months)*int(usdrub), lifetime=15, comment=comment)
                messages.paymentWayMsg(bot, pricePer3Months, None, 3, call, bill.pay_url, bill.bill_id)

            elif 'PyQiwiP2P' in call.data:
                data = call.data.split('_')
                if data[1] == '1':
                    if p2p.check(data[0]).status == 'PAID':
                        addUser(call.message.chat.id, 30)
                    elif p2p.check(data[0]).status != 'PAID':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Счет не оплачен, попробуйте повторить попытку.</b>',reply_markup=None, parse_mode='html')  
                elif data[1] == '3':
                    if p2p.check(data[0]).status == 'PAID':
                        addUser(call.message.chat.id, 90)
                    elif p2p.check(data[0]).status != 'PAID':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Счет не оплачен, попробуйте повторить попытку.</b>',reply_markup=None, parse_mode='html')  

            elif call.data == 'yooMoney':
                balance = yooClient.account_info().balance
                quickpay = Quickpay(
                    receiver=config.YOOMONEY_ID,
                    quickpay_form="shop",
                    targets="Sponsor this project",
                    paymentType="SB",
                    sum=int(pricePerMonth)*int(usdrub),
                    label=str(balance)
                    )
                bot.send_message(call.message.chat.id, messages.paymentWayMsg(bot, pricePerMonth, None, 1, call, pay_url=quickpay.redirected_url, bill_id=balance), parse_mode='html')

            elif call.data == 'yooMoney3':
                balance = yooClient.account_info().balance
                quickpay = Quickpay(
                    receiver=config.YOOMONEY_ID,
                    quickpay_form="shop",
                    targets="Sponsor this project",
                    paymentType="SB",
                    sum=int(pricePer3Months)*int(usdrub),
                    label=str(balance)
                    )
                bot.send_message(call.message.chat.id, messages.paymentWayMsg(bot, pricePer3Months, None, 3, call, pay_url=quickpay.redirected_url, bill_id=balance), parse_mode='html')

            elif 'yooP2P' in call.data:
                data = call.data.split('_')
                prevBalance = data[0]
                newBalance = yooClient.account_info().balance
                if data[2] == '1':
                    if (float(newBalance)-float(prevBalance)) > ((float(pricePerMonth)*float(usdrub))-0.05*(float(pricePerMonth)*float(usdrub))):
                        addUser(call.message.chat.id, 30)
                    else:
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Счет не оплачен, попробуйте повторить попытку.</b>',reply_markup=None, parse_mode='html')  
                elif data[2] == '3':
                    if (float(newBalance)-float(prevBalance)) > ((float(pricePer3Months)*float(usdrub))-0.05*(float(pricePer3Months)*float(usdrub))):
                        addUser(call.message.chat.id, 90)
                    else:
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Счет не оплачен, попробуйте повторить попытку.</b>',reply_markup=None, parse_mode='html')

    except Exception as e:
        print(repr(e))


###  NEXT STEP HANDLERS  ###
def checkPayment(message):
    bot.send_message(message.chat.id, '✅ Спасибо! Квитанция отправлена на проверку, вы получите уведомление как только её проверят.')
    if message.text == None:
        bot.send_photo(creator_id, photo=message.photo[0].file_id, caption=message.caption)
        bot.send_message(creator_id, f'Пользователь с айди `{str(message.chat.id)}` приобрёл подписку', parse_mode='MARKDOWN')
    else:
        bot.send_message(creator_id, message.text)

def addPrivateUser(message):
    id = message.text
    if sql.execute('SELECT id from users WHERE user_id = ? and isSub = ?', (id, 0,)).fetchone() != None:
        markup = types.InlineKeyboardMarkup()
        oneMonth = types.InlineKeyboardButton("1 Месяц", callback_data='addOneMonthUser')
        threeMonths = types.InlineKeyboardButton("3 Месяца", callback_data='addThreeMonthsUser')
        markup.add(oneMonth, threeMonths)

        bot.send_message(message.chat.id, 'Выберите период подписки для пользователя с айди:' + id, reply_markup=markup)

    elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (id, 1,)).fetchone() != None:
        bot.send_message(message.chat.id, 'у этого пользователя уже оформлена подписка')
        
    elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (id, 0,)).fetchone() == None:
        bot.send_message(message.chat.id, 'такого пользователя не существует')

def changeUserData(message):
    data = message.text.split(' ')
    if sql.execute('SELECT id from users WHERE user_id = ?', (data[0],)).fetchone() != None:
        if data[1] == '0':
            sql.execute('UPDATE users SET isSub=?, untill=? WHERE user_id=?', (0, 0, data[0]))
            db.commit()
            bot.send_message(message.chat.id, 'данные пользователя успешно изменены')
        else:
            sql.execute('UPDATE users SET isSub=?, untill=? WHERE user_id=?', (data[1], data[2] + ' ' + data[3], data[0]))
            db.commit()
            bot.send_message(message.chat.id, 'данные пользователя успешно изменены')

    else:
        bot.send_message(message.chat.id, 'такого пользователя не существует')

def deleteUser(message):
    data = message.text
    if sql.execute('SELECT id from users WHERE user_id = ? and isSub = ?', (data, 1,)).fetchone() != None:
        sql.execute('UPDATE users SET isSub=?, untill=? WHERE user_id=?', (0, 0, data))
        db.commit()

        bot.kick_chat_member(groupId, data)
        bot.unban_chat_member(groupId, data)

        bot.send_message(data, 'Ваша подписка закончилась', parse_mode='html')
        bot.send_message(message.chat.id, 'Подписка для пользователя с id ' + data + ' теперь окончена')

    elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (data, 0,)).fetchone() != None:
        bot.send_message(message.chat.id, 'у этого пользователя уже закончилась подписка')

    elif sql.execute('SELECT * from users WHERE user_id = ? ', (data,)).fetchone() == None:
        bot.send_message(message.chat.id, 'такого пользователя не существует')

def writeToUser(message):
    data = message.text.split('===')
    if sql.execute('SELECT id from users WHERE user_id = ?', (data[0],)).fetchone() != None:
        bot.send_message(data[0], f'<b>Сообщение от администратора:</b>\n\n{data[1]}', parse_mode='html')
        bot.send_message(message.chat.id, 'Ваше сообщение успешно отправлено пользователю')

    elif sql.execute('SELECT * from users WHERE user_id = ? ', (data[0],)).fetchone() == None:
        bot.send_message(message.chat.id, 'такого пользователя не существует')

def writeMailing(message):
    users = sql.execute('SELECT user_id from users').fetchall()
    if message.photo:
        for userId in users:
            bot.send_photo(userId[0], photo=message.photo[0].file_id, caption=message.caption, parse_mode='MARKDOWN', reply_markup=markups.advertisingMarkup)
        bot.send_message(creator_id, 'Рассылка прошла успешно!', parse_mode='html')
    else:
        for userId in users:
            bot.send_message(userId[0], message.text, parse_mode='MARKDOWN', reply_markup=markups.advertisingMarkup)
        bot.send_message(chat_id=creator_id, text='Рассылка прошла успешно!', parse_mode='html')

###  HELPER FUNCTIONS  ###
def parseUsers(users):
    newArr = []
    for el in users:
        newArr.append(str(el).replace("'","").replace("(","").replace(")","").replace(",",""))
    return "\n".join(newArr)

def addUser(id, duration):
    untill = str(datetime.now() + timedelta(days=duration)).split('.')[0]

    sql.execute('UPDATE users SET isSub=?, untill=? WHERE user_id=?', (1, untill, id))
    db.commit()

    bot.send_message(chat_id=creator_id, text='Подписчику с айди ' + str(id) + ' оформлен доступ в VIP-канал до ' + str(sql.execute('SELECT untill from users WHERE user_id=?', (id,)).fetchone()[0]))
    bot.send_message(chat_id=id, text=f"Ваша подписка успешно активирована <b>до {str(sql.execute('SELECT untill from users WHERE user_id=?', (id,)).fetchone()[0])}.</b> Чтобы получить ссылку доступа, выберите в меню кнопку 'Подписка'.", parse_mode='html')

def checkSubcription(duration: int=60):
    while True:
        usersDates = sql.execute('SELECT untill from users').fetchall()
        for userDate in usersDates:
            if str(userDate[0]) != '0':
                nowTs = time.time()
                userDateTs = time.mktime(datetime.strptime(userDate[0], "%Y-%m-%d %H:%M:%S").timetuple())
                if userDateTs - nowTs <= 0:
                    userId = sql.execute('SELECT user_id from users WHERE untill=?', (userDate[0],)).fetchone()[0]
                    markup = types.InlineKeyboardMarkup()
                    subscribeBtn = types.InlineKeyboardButton("🛒 Перейти к покупке", callback_data='backRate')
                    markup.add(subscribeBtn)
                    bot.send_message(userId, 'Ваша подписка на <b>ForexDohod VIP SIGNALS</b> закончилась\nПерейти к покупке?', parse_mode='html' ,reply_markup=markup)
                    bot.send_message(creator_id, f"Подписка у пользователя с id {userId} истекла",)

                    sql.execute('UPDATE users SET isSub=?, untill=? WHERE untill=?', (0,0,userDate[0]))
                    db.commit()

                    bot.kick_chat_member(groupId, userId)
                    bot.unban_chat_member(groupId, userId)
            else:
                pass
        time.sleep(duration)


if __name__ == '__main__':
    checkSubThread = threading.Thread(target=checkSubcription, args=(60,)).start()
    botThread = threading.Thread(target=bot.polling(none_stop=True)).start()