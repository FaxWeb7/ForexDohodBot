import telebot
import config
import datetime
import requests
import sqlite3
import time
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
db = sqlite3.connect('./privateUsers.db', check_same_thread=False)
sql = db.cursor()
creator_id = 1056056149

@bot.message_handler(commands=['start'])
def welcome(message):
    global creator_id

    sql.execute('SELECT * from users WHERE user_id = ?', (message.chat.id,))
    if sql.fetchone() == None:
        sql.execute('INSERT INTO users VALUES (NULL, ?, ?, ?, ?)', (message.chat.id , 0, 0, 0))
        db.commit()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    rates = types.KeyboardButton("🛒 Тарифы")
    subscribe = types.KeyboardButton("📊 Подписка")
    education = types.KeyboardButton("Бесплатное обучение")
    revenue = types.KeyboardButton("Сколько можно заработать?")
    freeChannel = types.KeyboardButton("Бесплатный канал")
    feedback = types.KeyboardButton("Обратная связь")
    privateSub = types.KeyboardButton("Добавить подписчика в секретный канал")

    if message.chat.id == creator_id:
        markup.add(rates, subscribe, education, revenue, freeChannel, feedback, privateSub)
    else:
        markup.add(rates, subscribe, education, revenue, freeChannel, feedback)

    bot.send_message(message.chat.id, 
    """
        👋 <b>Добро пожаловать в ForexDohodBot, {0.first_name}!</b>\n\nМеня зовут Артём! <b>В этом боте вы можете пройти бесплатное обучение 📘</b>, узнать все о моем <b>🤖Роботе</b> , а также приобрести подписку на <b>🔒Секреный канал</b>.\n\nПосле покупки доступа в 🔒Секретный канал, вам будут доступны <b>абсолютно все сигналы от моего робота по Золоту, а также в ближайшем будущем и по валютным парам 💹</b>. 
    """
    .format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
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
                    sql.execute('UPDATE users SET isSub=?, untill=?, subLink=? WHERE user_id=?', (0,0,0,message.chat.id))
                    db.commit()
                    markup = types.InlineKeyboardMarkup()
                    subscribeBtn = types.InlineKeyboardButton("🛒 Перейти к покупке", callback_data='backRate')
                    markup.add(subscribeBtn)

                    bot.send_message(message.chat.id, 'Ваша подписка на <b>Секретный Канал ForexDohod</b> закончилась\nПерейти к покупке?', parse_mode='html' ,reply_markup=markup)
                
                elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (message.chat.id, 1,)).fetchone() != None:
                    untill = sql.execute('SELECT untill from users WHERE user_id = ?', (message.chat.id,)).fetchone()[0]
                    subLink = sql.execute('SELECT subLink from users WHERE user_id = ?', (message.chat.id,)).fetchone()[0]
                    markup = types.InlineKeyboardMarkup()
                    subscribeBtn = types.InlineKeyboardButton("Перейти в Секретный Канал ForexDohod", url=subLink ,callback_data='privateLink')
                    markup.add(subscribeBtn)

                    bot.send_message(message.chat.id, 'Ваша подписка на <b>Секретный Канал ForexDohod</b> действует до ' + untill + '\n\n<b>Ваши приватные ссылки для доступа  👇</b>\n⚠ Если у вас появляется ошибка ссылка не действительна или чат не существует или вы не можете войти в сообщество, просто попробуйте ещё раз через пару минут (особенность Telegram)', parse_mode='html' ,reply_markup=markup)

            elif sql.execute('SELECT id from users WHERE user_id = ? and isSub = ?', (message.chat.id, 0,)).fetchone() != None:
                markup = types.InlineKeyboardMarkup()
                subscribeBtn = types.InlineKeyboardButton("🛒 Перейти к покупке", callback_data='backRate')
                markup.add(subscribeBtn)

                bot.send_message(message.chat.id, 'У вас нет активных подписок. Перейти к покупке?', reply_markup=markup)
        elif message.text == 'Добавить подписчика в секретный канал':
            if message.chat.id == creator_id:
                msg = bot.send_message(message.chat.id, 'Введите данные для private-user через пробел (12345678 22-22-2022 22:22)')
                bot.register_next_step_handler(msg, parsePrivateUser)
            else:
                bot.send_message(message.chat.id, 'Эта функция недоступна для вас')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'subsOne':
                markup = types.InlineKeyboardMarkup(row_width=1)
                usdt = types.InlineKeyboardButton("USDT TRC20", callback_data='usdt')
                card = types.InlineKeyboardButton("По номеру карты", callback_data='card')
                qiwi = types.InlineKeyboardButton("Qiwi", callback_data='qiwi')
                backRate = types.InlineKeyboardButton("🔙 Назад", callback_data='backRate')

                markup.add(usdt, card, qiwi, backRate)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>1 Месяц\nЦена: 60 USD\nСрок подписки: 30 дней\n\nВы получите приглашение в Секретный Канал ForexDohod на 30 дней, в котором выкладываются абсолютно все сигналы без ограничений.</b>",
                reply_markup=markup, parse_mode='html')

            elif call.data == 'subsThree':
                markup = types.InlineKeyboardMarkup(row_width=1)
                usdt = types.InlineKeyboardButton("USDT TRC20", callback_data='usdt3')
                card = types.InlineKeyboardButton("По номеру карты", callback_data='card3')
                qiwi = types.InlineKeyboardButton("Qiwi", callback_data='qiwi3')
                back = types.InlineKeyboardButton("🔙 Назад", callback_data='backRate')

                markup.add(usdt, card, qiwi, back)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>3 Месяца\nЦена: 140 USD\nСрок подписки: 90 дней\n\nВы получите приглашение в Секретный Канал ForexDohod на 90 дней, в котором выкладываются абсолютно все сигналы без ограничений.</b>",
                reply_markup=markup, parse_mode='html')

            elif call.data == "backRate":
                markup = types.InlineKeyboardMarkup(row_width=1)
                subsOne = types.InlineKeyboardButton("1 Месяц", callback_data='subsOne')
                subsThree = types.InlineKeyboardButton("3 Месяца (-20%)", callback_data='subsThree')
                backMenu = types.InlineKeyboardButton("🔙 Назад", callback_data='backMenu')

                markup.add(subsOne, subsThree, backMenu)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='<b>Выберите длительность доступа в 🔒Секретный Канал</b>', parse_mode='html', reply_markup=markup)
                
            elif call.data == "backMenu":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вы в главном меню', reply_markup=None)                
                
            elif call.data == "usdt":
                markup = types.InlineKeyboardMarkup(row_width=1)
                payment = types.InlineKeyboardButton("✅ Я оплатил", callback_data='payment')
                backPrice = types.InlineKeyboardButton("❌ Отменить", callback_data='subsOne')

                markup.add(payment, backPrice)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Способ оплаты: USDT TRC20\nСумма к оплате: *60 USDT*\nДля оплаты переведите указанную сумму Подписки на этот адрес кошелька:\n\n`TRoha2nsRGVDeDQomuFhtCXBo1uRBqs2W5` (нажмите,адрес кошелька скопируется)\n\nЭто можно сделать, например, в популярной бирже Бинанс. Напротив валюты USDT нажмите кнопку "Вывод" и введите адрес, который указан выше.\n\nОбратите внимание на *сеть* криптовалюты: *TRC20*.', reply_markup=markup ,parse_mode='MARKDOWN')

            elif call.data == "card":
                markup = types.InlineKeyboardMarkup(row_width=1)
                payment = types.InlineKeyboardButton("✅ Я оплатил", callback_data='payment')
                backPrice = types.InlineKeyboardButton("❌ Отменить", callback_data='subsOne')

                markup.add(payment, backPrice)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Способ оплаты: Оплата картой\nСумма к оплате: *60 USD*\nДля оплаты переведите указанную сумму Подписки на этот номер карты:\n\n`2200700408479524` (нажмите, номер карты скопируется)\n\n*Обратите внимание на то, что вы должны рассчитать количество рублей*, чтобы сумма совпадала с ценой подписки.', reply_markup=markup ,parse_mode='MARKDOWN')

            elif call.data == "qiwi":
                markup = types.InlineKeyboardMarkup(row_width=1)
                payment = types.InlineKeyboardButton("✅ Я оплатил", callback_data='payment')
                backPrice = types.InlineKeyboardButton("❌ Отменить", callback_data='subsOne')

                markup.add(payment, backPrice)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Способ оплаты: QIWI\nСумма к оплате: *60 USD*\nДля оплаты переведите указанную сумму Подписки на этот номер телефона Qiwi:\n\n`89260534553` (нажмите, номер телефона скопируется)\n\n*Обратите внимание на то, что вы должны рассчитать количество рублей*, чтобы сумма совпадала с ценой подписки.', reply_markup=markup ,parse_mode='MARKDOWN')

            elif call.data == "usdt3":
                markup = types.InlineKeyboardMarkup(row_width=1)
                payment = types.InlineKeyboardButton("✅ Я оплатил", callback_data='payment')
                backPrice = types.InlineKeyboardButton("❌ Отменить", callback_data='subsThree')

                markup.add(payment, backPrice)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Способ оплаты: USDT TRC20\nСумма к оплате: *140 USDT*\nДля оплаты переведите указанную сумму Подписки на этот адрес кошелька:\n\n`TRoha2nsRGVDeDQomuFhtCXBo1uRBqs2W5` (нажмите,адрес кошелька скопируется)\n\nЭто можно сделать, например, в популярной бирже Бинанс. Напротив валюты USDT нажмите кнопку "Вывод" и введите адрес, который указан выше.\n\nОбратите внимание на *сеть* криптовалюты: *TRC20*.', reply_markup=markup ,parse_mode='MARKDOWN')

            elif call.data == "card3":
                markup = types.InlineKeyboardMarkup(row_width=1)
                payment = types.InlineKeyboardButton("✅ Я оплатил", callback_data='payment')
                backPrice = types.InlineKeyboardButton("❌ Отменить", callback_data='subsThree')

                markup.add(payment, backPrice)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Способ оплаты: Оплата картой\nСумма к оплате: *140 USD*\nДля оплаты переведите указанную сумму Подписки на этот номер карты:\n\n`2200700408479524` (нажмите, номер карты скопируется)\n\n*Обратите внимание на то, что вы должны рассчитать количество рублей*, чтобы сумма совпадала с ценой подписки.', reply_markup=markup ,parse_mode='MARKDOWN')

            elif call.data == "qiwi3":
                markup = types.InlineKeyboardMarkup(row_width=1)
                payment = types.InlineKeyboardButton("✅ Я оплатил", callback_data='payment')
                backPrice = types.InlineKeyboardButton("❌ Отменить", callback_data='subsThree')

                markup.add(payment, backPrice)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Способ оплаты: QIWI\nСумма к оплате: *140 USD*\nДля оплаты переведите указанную сумму Подписки на этот номер телефона Qiwi:\n\n`89260534553` (нажмите, номер телефона скопируется)\n\n*Обратите внимание на то, что вы должны рассчитать количество рублей*, чтобы сумма совпадала с ценой подписки.', reply_markup=markup ,parse_mode='MARKDOWN')

            elif call.data == "payment":
                markup = types.InlineKeyboardMarkup(row_width=1)
                backPrice = types.InlineKeyboardButton("❌ Отменить", callback_data='subsThree')
                markup.add(backPrice)

                msg = bot.send_message(chat_id=call.message.chat.id, text='<b>💰 Оплатили?</b>\n\nОтправьте боту квитанцию об оплате: <b>скриншот или фото.</b>\nНа квитанции должны быть четко видны: <b>дата, время и сумма платежа.</b>', parse_mode='html', reply_markup=markup)
                bot.register_next_step_handler(msg, checkPayment)

    except Exception as e:
        print(repr(e))

def parsePrivateUser(message):
    data = message.text.split(' ')
    if sql.execute('SELECT id from users WHERE user_id = ? and isSub = ?', (data[0], 0,)).fetchone() != None:
        sql.execute('UPDATE users SET isSub=?, untill=? WHERE user_id=?', (1, data[1] + " " + data[2], data[0]))
        db.commit()
        untill = str(sql.execute('SELECT untill from users WHERE user_id = ?', (message.chat.id,)).fetchone()).replace("'","").replace("(","").replace(")","").replace(",","")
        untillTs = time.mktime(datetime.datetime.strptime(untill, "%d-%m-%Y %H:%M").timetuple())
        chatLink = bot.create_chat_invite_link(-1001871050533, member_limit=1, expire_date=untillTs)
        sql.execute('UPDATE users SET subLink=? WHERE user_id=?', (str(chatLink.invite_link), data[0]))
        db.commit()
        bot.send_message(message.chat.id, 'Подписка для пользователя с id ' + data[0] + ' успешно оформлена до ' + data[1] + " " + data[2])
        bot.send_message(data[0], 'Ваша подписка успешно активирована <b>до ' + data[1] + " " + data[2] + "</b>", parse_mode='html')
    elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (data[0], 1,)).fetchone() != None:
        bot.send_message(message.chat.id, 'у этого пользователя уже оформлена подписка')
    elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (data[0], 0,)).fetchone() == None:
        bot.send_message(message.chat.id, 'такого пользователя не существует')

def checkPayment(message):
    bot.send_message(message.chat.id, '✅ Спасибо! Квитанция отправлена на проверку, вы получите уведомление как только её проверят.')
    if message.text == None:
        bot.send_photo(creator_id, photo=message.photo[0].file_id, caption=message.caption)
        bot.send_message(creator_id, 'Пользователь с айди ' + str(message.chat.id) + ' приобрёл подписку')
    else:
        bot.send_message(creator_id, message.text)
    

bot.polling(none_stop=True)
