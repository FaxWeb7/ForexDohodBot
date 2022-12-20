import telebot
import config
import datetime
import sqlite3
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
db = sqlite3.connect('./privateUsers.db', check_same_thread=False)
sql = db.cursor()

@bot.message_handler(commands=['start'])
def welcome(message):
    sql.execute('SELECT * from users WHERE user_id = ?', (message.chat.id,))
    if sql.fetchone() == None:
        sql.execute('INSERT INTO users VALUES (NULL, ?, ?, ?)', (message.chat.id , 0, 0))
        db.commit()
    # else:
    #     if sql.execute('SELECT * from users WHERE user_id = ?', (message.chat.id,)).fetchone()[2] == 0:
    #         bot.send_message(message.chat.id, 'подписка недействительна')
    #     else:
    #         now = datetime.datetime.now()
    #         if now.strftime("%d-%m-%Y") > sql.execute('SELECT * from users WHERE user_id = ?', (message.chat.id,)).fetchone()[3] == 0:
    #             bot.send_message(message.chat.id, 'подписка закончилась')
    #         else:
    #             bot.send_message(message.chat.id, 'подписка действительна до ' + sql.execute('SELECT * from users WHERE user_id = ?', (message.chat.id,)).fetchone()[3])


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    rates = types.KeyboardButton("🛒 Тарифы")
    subscribe = types.KeyboardButton("📊 Подписка")
    education = types.KeyboardButton("Бесплатное обучение")
    revenue = types.KeyboardButton("Сколько можно заработать?")
    freeChannel = types.KeyboardButton("Бесплатный канал")
    feedback = types.KeyboardButton("Обратная связь")

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
            if sql.execute('SELECT id from users WHERE user_id = ? and isSub = ?', (message.chat.id, 0,)).fetchone() != None:
                data = sql.execute('SELECT id from users WHERE user_id = ? and isSub = ?', (message.chat.id, 0,)).fetchone()[0]
                sql.execute('UPDATE users SET isSub=? WHERE id=?', (1, data))
                db.commit()
                
            elif sql.execute('SELECT * from users WHERE user_id = ? and isSub = ?', (message.chat.id, 1,)).fetchone() != None:
                bot.send_message(message.chat.id, 'подписка действительна')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'subsOne':
                markup = types.InlineKeyboardMarkup(row_width=1)
                usdt = types.InlineKeyboardButton("USDT TRC20", callback_data='usdt')
                btc = types.InlineKeyboardButton("Bitcoin", callback_data='btc')
                card = types.InlineKeyboardButton("По номеру карты", callback_data='card')
                backRate = types.InlineKeyboardButton("🔙 Назад", callback_data='backRate')

                markup.add(usdt, btc, card, backRate)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>1 Месяц\nЦена: 50 USD\nСрок подписки: 30 дней\n\nВы получите приглашение в Секретный Канал ForexDohod на 30 дней, в котором выкладываются абсолютно все сигналы без ограничений.</b>",
                reply_markup=markup, parse_mode='html')

            elif call.data == 'subsThree':
                markup = types.InlineKeyboardMarkup(row_width=1)
                usdt = types.InlineKeyboardButton("USDT TRC20", callback_data='usdt')
                btc = types.InlineKeyboardButton("Bitcoin", callback_data='btc')
                card = types.InlineKeyboardButton("По номеру карты", callback_data='card')
                back = types.InlineKeyboardButton("🔙 Назад", callback_data='backRate')

                markup.add(usdt, btc, card, back)

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>3 Месяца\nЦена: 120 USD\nСрок подписки: 30 дней\n\nВы получите приглашение в Секретный Канал ForexDohod на 90 дней, в котором выкладываются абсолютно все сигналы без ограничений.</b>",
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

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
