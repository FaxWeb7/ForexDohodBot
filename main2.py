import telebot
import config
import sqlite3
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
db = sqlite3.connect('./forexUsers.db', check_same_thread=False)
sql = db.cursor()

@bot.message_handler(commands=['start'])
def welcome(message):
    if sql.execute('SELECT * from users WHERE user_id = ?', (message.chat.id,)).fetchone() == None:
        sql.execute('INSERT INTO users VALUES (NULL, ?, ?, ?)', (message.chat.id , 0, 0))
        db.commit()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    education = types.KeyboardButton("Бесплатное обучение")
    revenue = types.KeyboardButton("Сколько можно заработать?")
    freeChannel = types.KeyboardButton("🗞️ Бесплатный канал")
    feedback = types.KeyboardButton("☎️ Обратная связь")

    markup.add(education, revenue, freeChannel, feedback)

    bot.send_message(message.chat.id, 
    """
        👋 <b>Добро пожаловать в ForexDohodBot, {0.first_name}!</b>\n\nМеня зовут Артём! <b>В этом боте вы можете пройти бесплатное 📘обучение</b>, а также узнать все о моем <b>🤖Роботе</b>  
    """
    .format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def Buttons(message):
    if message.chat.type == 'private':
        if message.text == 'Сколько можно заработать?':
            bot.send_photo(message.chat.id, caption="""
            <b>Сколько можно заработать? 🧐</b>\n\nПеред тем, как узнать ответ на этот вопрос - <b>обязательно пройдите обучение в нашем боте</b>, либо сделайте это после прочтения этого сообщения.\n\nКонечно все зависит от вашего депозита, опыта, терпения и так далее, но <b>в среднем данная цифра варьируется от 15% до 30% в месяц к депозиту.</b>\n\n<b>В среднем можно зарабатывать по 0.5-1% в день к депозиту</b>. Если вы знакомы с понятием <b>сложного процента</b>, то знаете, что с депозитом всего в 1000$ и ежедневным приростом в размере хотябы 0.7% можно в по истечение двух лет иметь на счету порядка 80 000$, что является огромной прибылью.\n\nНо трейдинг так и работает, <b>тут важно зарабатывать постоянно</b>, хоть и небольшие проценты. В противном случае жадность может привести вас к потере денег.\n\n✅ <b><u>На данном этапе я бы вам посоветовал:</u></b>\n\n<b>1.</b> Начать бесплатное обучение в этом боте\n<b>2.</b> Подписаться на <a href="https://t.me/ForexDohod">мой Телеграм канал</a>, чтобы не пропускать бесплатные сигналы, новости и мои мысли
            """, parse_mode='html', photo=open('./assets/rate.jpeg', 'rb'))
        elif message.text == '🗞️ Бесплатный канал':
            bot.send_message(message.chat.id, """
            <b>Еще не подписаны на мой Телеграм канал "ForexDohod"? 🙈</b>\n\n<b><u>В нём вы сможете найти:</u></b>\n\n▪️Бесплатные сигналы\n▪️Обзор рынка\n▪️Важные новости и другое!\n\n<a href="https://t.me/ForexDohod"><b>✅Ссылка на канал✅</b></a>
            """, parse_mode='html')
        elif message.text == '☎️ Обратная связь':
            bot.send_message(message.chat.id, """
            Если у вас возникли вопросы, то свяжитесь с <a href="t.me/@faxweb_w">админом</a>, он ответит вам в ближайшее время.
            """, parse_mode='html')
        elif message.text == 'Бесплатное обучение':
            bot.send_photo(message.chat.id, photo=open('./assets/education.jpg', 'rb'), caption="""‍Отлично, я рад, что <b>вы выбрали путь обучения, это совершенно бесплатно и поможет сохранить ваши деньги!</b>\n\nПоэтому <b>изучить все короткие обучающие статьи ниже очень важно!</b>\n\nЯ постараюсь ответить на максимальное количество ваших вопросов с помощью статей ниже:\n\n<b>1.</b> Проверенные Форекс-Брокеры: <a href="https://roboforex.com">RoboForex</a>, <a href="https://www.exness.com/">Exness</a>, <a href="https://www.icmarkets.com/intl/ru/">ICMarkets</a>.\n<b>2.</b> <a href="https://telegra.ph/Registraciya-i-Verifikaciya-na-RoboForex-12-18">Как зарегистрироваться и верифицировать аккаунт у Форекс-Брокера?</a>\n<b>3.</b> <a href="https://telegra.ph/Kak-otkryt-i-popolnit-schet-u-brokera-RoboForex-12-18">Как открыть и пополнить счет у брокера RoboForex?</a>\n<b>4.</b> <a href="https://telegra.ph/Kak-skachat-terminal-MetaTrader4-i-zajti-na-torgovyj-schet-vashego-brokera-12-18">Как скачать терминал MetaTrader4 и зайти на счет вашего брокера?</a>\n<b>5.</b> <a href="https://telegra.ph/Osnovy-tehnicheskogo-analiza-12-18">Основы технического анализа</a>.\n<b>6.</b> <a href="https://telegra.ph/Manimenedzhment-i-usrednenie-pozicii-12-18">Манименеджмент и усреднение позиции</a>.\n<b>7.</b> <a href="https://telegra.ph/Vsyo-o-moem-robote-Kak-on-rabotaet-torguet-i-daet-signaly-12-18">Как мой робот дает сигналы, и как их повторить без потерь.</a>\n<b>8.</b> <a href="https://telegra.ph/Poleznye-servisy-12-18">Полезные сервисы</a>.\n\nНапоминаю, что <b>изучение этих моментов очень важно для того, чтобы вы сохранили свои деньги и начали их преумножать!</b>""", parse_mode='html')


bot.polling(none_stop=True)
