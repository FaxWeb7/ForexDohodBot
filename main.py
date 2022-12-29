import telebot
import config
import datetime
import sqlite3
import time
from telebot import types


###  MAIN CONSTANTS  ###
bot = telebot.TeleBot(config.TOKEN)
db = sqlite3.connect('./privateUsers.db', check_same_thread=False)
sql = db.cursor()

creator_id = 1056056149
pricePerMonth = '70'
pricePer3Months =  '170'
walletAddress = 'TRoha2nsRGVDeDQomuFhtCXBo1uRBqs2W5'
cardNumber = '2200700408479524'
qiwiNumber = '+79260534553'


###  START MESSAGE  ###
@bot.message_handler(commands=['start'])
def welcome(message):
    if sql.execute('SELECT * from users WHERE user_id = ?', (message.chat.id,)).fetchone() == None:
        sql.execute('INSERT INTO users VALUES (NULL, ?, ?, ?)', (message.chat.id , 0, 0))
        db.commit()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    rates = types.KeyboardButton("🛒 Тарифы")
    subscribe = types.KeyboardButton("📊 Подписка")
    education = types.KeyboardButton("Бесплатное обучение")
    revenue = types.KeyboardButton("Сколько можно заработать?")
    freeChannel = types.KeyboardButton("Бесплатный канал")
    feedback = types.KeyboardButton("Обратная связь")
    changeUserData = types.KeyboardButton("Статистика пользователей")
    statistic = types.KeyboardButton("Изменить данные пользователя")
    deleteSub = types.KeyboardButton("Удалить подписчика с секретного канала")
    writeToSub = types.KeyboardButton("Написать сообщение пользователю")
    privateSub = types.KeyboardButton("Добавить подписчика в секретный канал")

    if message.chat.id == creator_id:
        markup.add(rates, subscribe, education, revenue, freeChannel, feedback, statistic, changeUserData, deleteSub, writeToSub, privateSub)
    else:
        markup.add(rates, subscribe, education, revenue, freeChannel, feedback)

    bot.send_message(message.chat.id, 
    """
        👋 <b>Добро пожаловать в ForexDohodBot, {0.first_name}!</b>\n\nМеня зовут Артём! <b>В этом боте вы можете пройти бесплатное 📘обучение</b>, узнать все о моем <b>🤖Роботе</b> , а также приобрести подписку на <b>🔒Секреный канал</b>.\n\nПосле покупки доступа в 🔒Секретный канал, вам будут доступны <b>абсолютно все сигналы от моего робота по Золоту, а также в ближайшем будущем и по валютным парам 💹</b>. 
    """
    .format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)


###  BUTTONS HANDLER  ###
@bot.message_handler(content_types=['text'])
def Buttons(message):
    if message.chat.type == 'private':
        if message.text == 'Сколько можно заработать?':
            bot.send_photo(message.chat.id, caption="""
            <b>Сколько можно заработать? 🧐</b>\n\nПеред тем, как узнать ответ на этот вопрос - <b>обязательно пройдите обучение в нашем боте</b>, либо сделайте это после прочтения этого сообщения.\n\nКонечно все зависит от вашего депозита, опыта, терпения и так далее, но <b>в среднем данная цифра варьируется от 15% до 30% в месяц к депозиту.</b>\n\n<b>В среднем можно зарабатывать по 0.5-1% в день к депозиту</b>. Если вы знакомы с понятием <b>сложного процента</b>, то знаете, что с депозитом всего в 1000$ и ежедневным приростом в размере хотябы 0.7% можно в по истечение двух лет иметь на счету порядка 80 000$, что является огромной прибылью.\n\nНо трейдинг так и работает, <b>тут важно зарабатывать постоянно</b>, хоть и небольшие проценты. В противном случае жадность может привести вас к потере денег.\n\n✅ <b><u>На данном этапе я бы вам посоветовал:</u></b>\n\n<b>1.</b> Начать бесплатное обучение в этом боте\n<b>2.</b> Подписаться на <a href="https://t.me/ForexDohod">мой Телеграм канал</a>, чтобы не пропускать бесплатные сигналы, новости и мои мысли\n<b>3.</b> Приобрести доступ в мой закрытый канал и зарабатывать намного больше вместе с нами
            """, parse_mode='html', photo=open('./assets/rate.jpg', 'rb'))

        elif message.text == 'Бесплатный канал':
            bot.send_message(message.chat.id, """
            <b>Еще не подписаны на мой Телеграм канал "ForexDohod"? 🙈</b>\n\n<b><u>В нём вы сможете найти:</u></b>\n\n▪️Бесплатные сигналы\n▪️Обзор рынка\n▪️Важные новости и другое!\n\n<a href="https://t.me/ForexDohod"><b>✅Ссылка на канал✅</b></a>
            """, parse_mode='html')

        elif message.text == 'Обратная связь':
            bot.send_message(message.chat.id, """
            Если у вас возникли вопросы, то свяжитесь с <a href="t.me/@faxweb_w">админом</a>, он ответит вам в ближайшее время.
            """, parse_mode='html')

        elif message.text == 'Бесплатное обучение':
            bot.send_photo(message.chat.id, photo=open('./assets/education.jpg', 'rb'), caption="""‍Отлично, я рад, что <b>вы выбрали путь обучения, это совершенно бесплатно и поможет сохранить ваши деньги!</b>\n\nПоэтому <b>изучить все короткие обучающие статьи ниже очень важно!</b>\n\nЯ постараюсь ответить на максимальное количество ваших вопросов с помощью статей ниже:\n\n<b>1.</b> Проверенные Форекс-Брокеры: <a href="https://roboforex.com">RoboForex</a>, <a href="https://pocketoption.com">PocketOption</a>, <a href="https://amarkets.org">AMarkets</a>.\n<b>2.</b> <a href="https://telegra.ph/Registraciya-i-Verifikaciya-na-RoboForex-12-18">Как зарегистрироваться и верифицировать аккаунт у Форекс-Брокера?</a>\n<b>3.</b> <a href="https://telegra.ph/Kak-otkryt-i-popolnit-schet-u-brokera-RoboForex-12-18">Как открыть и пополнить счет у брокера RoboForex?</a>\n<b>4.</b> <a href="https://telegra.ph/Kak-skachat-terminal-MetaTrader4-i-zajti-na-torgovyj-schet-vashego-brokera-12-18">Как скачать терминал MetaTrader4 и зайти на счет вашего брокера?</a>\n<b>5.</b> <a href="https://telegra.ph/Osnovy-tehnicheskogo-analiza-12-18">Основы технического анализа</a>.\n<b>6.</b> <a href="https://telegra.ph/Manimenedzhment-i-usrednenie-pozicii-12-18">Манименеджмент и усреднение позиции</a>.\n<b>7.</b> <a href="https://telegra.ph/Vsyo-o-moem-robote-Kak-on-rabotaet-torguet-i-daet-signaly-12-18">Как мой робот дает сигналы, и как их повторить без потерь.</a>\n<b>8.</b> <a href="https://telegra.ph/Poleznye-servisy-12-18">Полезные сервисы</a>.\n\nНапоминаю, что <b>изучение этих моментов очень важно для того, чтобы вы сохранили свои деньги и начали их преумножать!</b>""", parse_mode='html')

        elif message.text == '🛒 Тарифы':
            markup = types.InlineKeyboardMarkup(row_width=1)
            subsOne = types.InlineKeyboardButton("1 Месяц", callback_data='subsOne')
            subsThree = types.InlineKeyboardButton("3 Месяца (-20%)", callback_data='subsThree')
            backMenu = types.InlineKeyboardButton("🔙 Назад", callback_data='backMenu')
            markup.add(subsOne, subsThree, backMenu)

            bot.send_message(message.chat.id, '<b>Выберите длительность доступа в 🔒Секретный Канал</b>', parse_mode='html', reply_markup=markup)

        elif message.text == '📊 Подписка':
            if sql.execute('SELECT untill from users WHERE user_id = ?', (message.chat.id,)).fetchone()[0] != '0':
                nowTs = time.time()
                untill = str(sql.execute('SELECT untill from users WHERE user_id = ?', (message.chat.id,)).fetchone()).replace("'","").replace("(","").replace(")","").replace(",","")
                untillTs = time.mktime(datetime.datetime.strptime(untill, "%d-%m-%Y %H:%M").timetuple())

                if untillTs - nowTs <= 0:
                    sql.execute('UPDATE users SET isSub=?, untill=? WHERE user_id=?', (0,0,message.chat.id))
                    db.commit()
                    markup = types.InlineKeyboardMarkup()
                    subscribeBtn = types.InlineKeyboardButton("🛒 Перейти к покупке", callback_data='backRate')
                    markup.add(subscribeBtn)

                    bot.send_message(message.chat.id, 'Ваша подписка на <b>Секретный Канал ForexDohod</b> закончилась\nПерейти к покупке?', parse_mode='html' ,reply_markup=markup)
                
                elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (message.chat.id, 1,)).fetchone() != None:
                    untill = sql.execute('SELECT untill from users WHERE user_id = ?', (message.chat.id,)).fetchone()[0]
                    markup = types.InlineKeyboardMarkup()
                    subscribeBtn = types.InlineKeyboardButton("👉 Секретный Канал ForexDohod", callback_data='privateLink')
                    markup.add(subscribeBtn)

                    bot.send_message(message.chat.id, 'Ваша подписка на <b>Секретный Канал ForexDohod</b> действует до ' + untill + '\n\n<b>Для получения доступа к каналу нажмите на соответствующую кнопку ниже 👇</b>\n\n⚠ Если у вас появляется ошибка ссылка не действительна или чат не существует или вы не можете войти в сообщество, просто попробуйте ещё раз через пару минут (особенность Telegram)', parse_mode='html' ,reply_markup=markup)

            elif sql.execute('SELECT id from users WHERE user_id = ? and isSub = ?', (message.chat.id, 0,)).fetchone() != None:
                markup = types.InlineKeyboardMarkup()
                subscribeBtn = types.InlineKeyboardButton("🛒 Перейти к покупке", callback_data='backRate')
                markup.add(subscribeBtn)

                bot.send_message(message.chat.id, 'У вас нет активных подписок. Перейти к покупке?', reply_markup=markup)

        ###  FUNCTIONS ONLY FOR CREATOR  ###
        elif message.text == 'Статистика пользователей':
            if message.chat.id == creator_id:
                users = sql.execute('SELECT * from users').fetchall()
                privateUsers = sql.execute("SELECT * from users WHERE isSub=?", (1,)).fetchall()
                usersId = sql.execute('SELECT user_id from users WHERE isSub=?', (0,)).fetchall()
                privateUsersId = sql.execute('SELECT * from users WHERE isSub=?', (1,)).fetchall()

                bot.send_message(message.chat.id, f'<b>Статистика пользователей ForexDohodBot</b>\n\nКоличество пользователей: {str(len(users))}\nКоличество пользоватей с подпиской: {str(len(privateUsers))}\nПроцент пользователей с подпиской: {round((len(privateUsers)/len(users))*100, 2)}%\n\nИнформация о пользователях без подписки:\n{parseUsers(usersId)}\n\nИнформация о пользователях с подпиской (id, user_id, isSub, untill):\n{parseUsers(privateUsersId)}\n\nИнформация о всех пользователях (id, user_id, isSub, untill):\n{parseUsers(users)}', parse_mode='html')
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

        elif message.text == 'Изменить данные пользователя':
            if message.chat.id == creator_id:
                msg = bot.send_message(message.chat.id, 'Введите измененные данные пользователя через пробел (12345678 1 22-22-2022 22:22 ) (user_id, isSub, untill) (user_id, 0 - обнулить)')
                bot.register_next_step_handler(msg, changeUserData)
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

        elif message.text == 'Добавить подписчика в секретный канал':
            if message.chat.id == creator_id:
                msg = bot.send_message(message.chat.id, 'Введите данные для private-user через пробел (12345678 22-22-2022 22:22)')
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
                msg = bot.send_message(message.chat.id, 'Введите id и сообщение пользователю через пробел, я ему все передам')
                bot.register_next_step_handler(msg, writeToUser)
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')


###  INLINE CALLBACKS  ###
@bot.callback_query_handler(func=lambda call: True)
def InlineCallback(call):
    try:
        if call.message:
            if call.data == 'privateLink':
                subLink = bot.create_chat_invite_link(-1001871050533, member_limit=1, expire_date=(int(time.time())+10))
                markup = types.InlineKeyboardMarkup()
                subscribeBtn = types.InlineKeyboardButton("👉 ВСТУПИТЬ 👈", url=str(subLink.invite_link))
                markup.add(subscribeBtn)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='✅ Вход открыт, ссылка действительна 10 секунд', reply_markup=markup)

            elif call.data == "backMenu":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы в главном меню', reply_markup=None) 

            elif call.data == "backRate":
                markup = types.InlineKeyboardMarkup(row_width=1)
                subsOne = types.InlineKeyboardButton("1 Месяц", callback_data='subsOne')
                subsThree = types.InlineKeyboardButton("3 Месяца (-20%)", callback_data='subsThree')
                backMenu = types.InlineKeyboardButton("🔙 Назад", callback_data='backMenu')
                markup.add(subsOne, subsThree, backMenu)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Выберите длительность доступа в 🔒Секретный Канал</b>', parse_mode='html', reply_markup=markup)

            elif call.data == 'subsOne':
                markup = types.InlineKeyboardMarkup(row_width=1)
                usdt = types.InlineKeyboardButton("USDT TRC20", callback_data='usdt')
                card = types.InlineKeyboardButton("По номеру карты", callback_data='card')
                qiwi = types.InlineKeyboardButton("Qiwi", callback_data='qiwi')
                backRate = types.InlineKeyboardButton("🔙 Назад", callback_data='backRate')
                markup.add(usdt, card, qiwi, backRate)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>1 Месяц\nЦена: {pricePerMonth} USD\nСрок подписки: 30 дней\n\nВы получите приглашение в Секретный Канал ForexDohod на 30 дней, в котором выкладываются абсолютно все сигналы без ограничений.</b>",
                reply_markup=markup, parse_mode='html')

            elif call.data == 'subsThree':
                markup = types.InlineKeyboardMarkup(row_width=1)
                usdt = types.InlineKeyboardButton("USDT TRC20", callback_data='usdt3')
                card = types.InlineKeyboardButton("По номеру карты", callback_data='card3')
                qiwi = types.InlineKeyboardButton("Qiwi", callback_data='qiwi3')
                back = types.InlineKeyboardButton("🔙 Назад", callback_data='backRate')
                markup.add(usdt, card, qiwi, back)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"<b>3 Месяца\nЦена: {pricePer3Months} USD\nСрок подписки: 90 дней\n\nВы получите приглашение в Секретный Канал ForexDohod на 90 дней, в котором выкладываются абсолютно все сигналы без ограничений.</b>",
                reply_markup=markup, parse_mode='html')             
                
            elif call.data == "usdt":
                paymentWay('usdt', 1, call)

            elif call.data == "card":
                paymentWay('card', 1, call)

            elif call.data == "qiwi":
                paymentWay('qiwi', 1, call)

            elif call.data == "usdt3":
                paymentWay('usdt', 3, call)

            elif call.data == "card3":
                paymentWay('card', 3, call)

            elif call.data == "qiwi3":
                paymentWay('qiwi', 3, call)

            elif call.data == "payment":
                msg = bot.send_message(chat_id=call.message.chat.id, text='<b>💰 Оплатили?</b>\n\nОтправьте боту квитанцию об оплате: <b>скриншот или фото.</b>\nНа квитанции должны быть четко видны: <b>дата, время и сумма платежа.</b>', parse_mode='html')
                bot.register_next_step_handler(msg, checkPayment)

    except Exception as e:
        print(repr(e))


###  NEXT STEP HANDLERS  ###
def checkPayment(message):
    bot.send_message(message.chat.id, '✅ Спасибо! Квитанция отправлена на проверку, вы получите уведомление как только её проверят.')
    if message.text == None:
        bot.send_photo(creator_id, photo=message.photo[0].file_id, caption=message.caption)
        bot.send_message(creator_id, 'Пользователь с айди ' + str(message.chat.id) + ' приобрёл подписку')
    else:
        bot.send_message(creator_id, message.text)

def addPrivateUser(message):
    data = message.text.split(' ')
    if sql.execute('SELECT id from users WHERE user_id = ? and isSub = ?', (data[0], 0,)).fetchone() != None:
        sql.execute('UPDATE users SET isSub=?, untill=? WHERE user_id=?', (1, data[1] + " " + data[2], data[0]))
        db.commit()

        bot.send_message(data[0], 'Ваша подписка успешно активирована <b>до ' + data[1] + " " + data[2] + ".</b> Чтобы получить ссылку доступа, выберите в меню кнопку 'Подписка'.", parse_mode='html')
        bot.send_message(message.chat.id, 'Подписка для пользователя с id ' + data[0] + ' успешно оформлена до ' + data[1] + " " + data[2])

    elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (data[0], 1,)).fetchone() != None:
        bot.send_message(message.chat.id, 'у этого пользователя уже оформлена подписка')
        
    elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (data[0], 0,)).fetchone() == None:
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

        bot.kick_chat_member(-1001871050533, data)
        bot.unban_chat_member(-1001871050533, data)

        bot.send_message(data, 'Ваша подписка закончилась', parse_mode='html')
        bot.send_message(message.chat.id, 'Подписка для пользователя с id ' + data + ' теперь окончена')

    elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (data, 0,)).fetchone() != None:
        bot.send_message(message.chat.id, 'у этого пользователя уже закончилась подписка')

    elif sql.execute('SELECT * from users WHERE user_id = ? ', (data,)).fetchone() == None:
        bot.send_message(message.chat.id, 'такого пользователя не существует')

def writeToUser(message):
    data = message.text.split(' ')
    if sql.execute('SELECT id from users WHERE user_id = ?', (data[0],)).fetchone() != None:
        bot.send_message(data[0], f'<b>Сообщение от администратора:</b>\n\n{data[1]}', parse_mode='html')
        bot.send_message(message.chat.id, 'Ваше сообщение успешно отправлено пользователю')

    elif sql.execute('SELECT * from users WHERE user_id = ? ', (data[0],)).fetchone() == None:
        bot.send_message(message.chat.id, 'такого пользователя не существует')


###  OTHER FUNCTIONS  ###
def parseUsers(users):
    newArr = []
    for el in users:
        newArr.append(str(el).replace("'","").replace("(","").replace(")","").replace(",",""))
    return "\n".join(newArr)

def paymentWay(way, duration, call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    payment = types.InlineKeyboardButton("✅ Я оплатил", callback_data='payment')
    backPrice = types.InlineKeyboardButton("❌ Отменить", callback_data='subsThree')
    markup.add(payment, backPrice)
    if way == 'usdt':
        if duration == 1:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: USDT TRC20\nСумма к оплате: *{pricePerMonth} USDT*\nДля оплаты переведите указанную сумму Подписки на этот адрес кошелька:\n\n`{walletAddress}` (нажмите,адрес кошелька скопируется)\n\nЭто можно сделать, например, в популярной бирже Бинанс. Напротив валюты USDT нажмите кнопку "Вывод" и введите адрес, который указан выше.\n\nОбратите внимание на *сеть* криптовалюты: *TRC20*.', reply_markup=markup ,parse_mode='MARKDOWN')
        
        elif duration == 3:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: USDT TRC20\nСумма к оплате: *{pricePer3Months} USDT*\nДля оплаты переведите указанную сумму Подписки на этот адрес кошелька:\n\n`{walletAddress}` (нажмите,адрес кошелька скопируется)\n\nЭто можно сделать, например, в популярной бирже Бинанс. Напротив валюты USDT нажмите кнопку "Вывод" и введите адрес, который указан выше.\n\nОбратите внимание на *сеть* криптовалюты: *TRC20*.', reply_markup=markup ,parse_mode='MARKDOWN')

    elif way == 'card':
        if duration == 1:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: Оплата картой\nСумма к оплате: *{pricePerMonth} USD*\nДля оплаты переведите указанную сумму Подписки на этот номер карты:\n\n`{cardNumber}` (нажмите, номер карты скопируется)\n\n*Обратите внимание на то, что вы должны рассчитать количество рублей*, чтобы сумма совпадала с ценой подписки.', reply_markup=markup ,parse_mode='MARKDOWN')
        
        elif duration == 3:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: Оплата картой\nСумма к оплате: *{pricePer3Months} USD*\nДля оплаты переведите указанную сумму Подписки на этот номер карты:\n\n`{cardNumber}` (нажмите, номер карты скопируется)\n\n*Обратите внимание на то, что вы должны рассчитать количество рублей*, чтобы сумма совпадала с ценой подписки.', reply_markup=markup ,parse_mode='MARKDOWN')

    elif way == 'qiwi':
        if duration == 1:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: QIWI\nСумма к оплате: *{pricePerMonth} USD*\nДля оплаты переведите указанную сумму Подписки на этот номер телефона Qiwi:\n\n`{qiwiNumber}` (нажмите, номер телефона скопируется)\n\n*Обратите внимание на то, что вы должны рассчитать количество рублей*, чтобы сумма совпадала с ценой подписки.', reply_markup=markup ,parse_mode='MARKDOWN')
        
        elif duration == 3:
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: QIWI\nСумма к оплате: *{pricePer3Months} USD*\nДля оплаты переведите указанную сумму Подписки на этот номер телефона Qiwi:\n\n`{qiwiNumber}` (нажмите, номер телефона скопируется)\n\n*Обратите внимание на то, что вы должны рассчитать количество рублей*, чтобы сумма совпадала с ценой подписки.', reply_markup=markup ,parse_mode='MARKDOWN')


bot.polling(none_stop=True)