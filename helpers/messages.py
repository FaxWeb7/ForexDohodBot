import helpers.markups as markups

### STRING MESSAGES ###

startMessage = """
    👋 <b>Добро пожаловать в ForexDohodBot, {0.first_name}!</b>\n\nМеня зовут Артём! <b>В этом боте вы можете пройти бесплатное 📘обучение</b>, узнать все о моем <b>🤖Роботе</b> , а также приобрести подписку на <b>🔒VIP-канал</b>.\n\nПосле покупки доступа в VIP-канал, вам будут доступны <b>абсолютно все сигналы от моего робота по Золоту, а также в ближайшем будущем и по валютным парам 💹</b>. 
"""

revenueMsg = """
    <b>Сколько можно заработать? 🧐</b>\n\nПеред тем, как узнать ответ на этот вопрос - <b>обязательно пройдите обучение в нашем боте</b>, либо сделайте это после прочтения этого сообщения.\n\nКонечно все зависит от вашего депозита, опыта, терпения и так далее, но <b>в среднем данная цифра варьируется от 15% до 30% в месяц к депозиту.</b>\n\n<b>В среднем можно зарабатывать по 0.5-1% в день к депозиту</b>. Если вы знакомы с понятием <b>сложного процента</b>, то знаете, что с депозитом всего в 1000$ и ежедневным приростом в размере хотябы 0.7% можно в по истечение двух лет иметь на счету порядка 80 000$, что является огромной прибылью.\n\nНо трейдинг так и работает, <b>тут важно зарабатывать постоянно</b>, хоть и небольшие проценты. В противном случае жадность может привести вас к потере денег.\n\n✅ <b><u>На данном этапе я бы вам посоветовал:</u></b>\n\n<b>1.</b> Начать бесплатное обучение в этом боте\n<b>2.</b> Подписаться на <a href="https://t.me/ForexDohod">мой Телеграм канал</a>, чтобы не пропускать бесплатные сигналы, новости и мои мысли\n<b>3.</b> Приобрести доступ в мой закрытый канал и зарабатывать намного больше вместе с нами
"""

freeChannelMsg = """
    <b>Еще не подписаны на мой Телеграм канал "ForexDohod"? 🙈</b>\n\n<b><u>В нём вы сможете найти:</u></b>\n\n▪️Бесплатные сигналы\n▪️Обзор рынка\n▪️Важные новости и другое!\n\n<a href="https://t.me/ForexDohod"><b>✅Ссылка на канал✅</b></a>
"""

feedbackMsg = """
    Если у вас возникли вопросы, то свяжитесь с <a href="t.me/@faxweb_w">админом</a>, он ответит вам в ближайшее время.
"""

educationMsg = """‍
    Отлично, я рад, что <b>вы выбрали путь обучения, это совершенно бесплатно и поможет сохранить ваши деньги!</b>\n\nПоэтому <b>изучить все короткие обучающие статьи ниже очень важно!</b>\n\nЯ постараюсь ответить на максимальное количество ваших вопросов с помощью статей ниже:\n\n<b>1.</b> Проверенные Форекс-Брокеры: <a href="https://roboforex.com">RoboForex</a>, <a href="https://www.exness.com/">Exness</a>, <a href="https://www.icmarkets.com/intl/ru/">ICMarkets</a>.\n<b>2.</b> <a href="https://telegra.ph/Registraciya-i-Verifikaciya-na-RoboForex-12-18">Как зарегистрироваться и верифицировать аккаунт у Форекс-Брокера?</a>\n<b>3.</b> <a href="https://telegra.ph/Kak-otkryt-i-popolnit-schet-u-brokera-RoboForex-12-18">Как открыть и пополнить счет у брокера RoboForex?</a>\n<b>4.</b> <a href="https://telegra.ph/Kak-skachat-terminal-MetaTrader4-i-zajti-na-torgovyj-schet-vashego-brokera-12-18">Как скачать терминал MetaTrader4 и зайти на счет вашего брокера?</a>\n<b>5.</b> <a href="https://telegra.ph/Osnovy-tehnicheskogo-analiza-12-18">Основы технического анализа</a>.\n<b>6.</b> <a href="https://telegra.ph/Manimenedzhment-i-usrednenie-pozicii-12-18">Манименеджмент и усреднение позиции</a>.\n<b>7.</b> <a href="https://telegra.ph/Vsyo-o-moem-robote-Kak-on-rabotaet-torguet-i-daet-signaly-12-18">Как мой робот дает сигналы, и как их повторить без потерь.</a>\n<b>8.</b> <a href="https://telegra.ph/Poleznye-servisy-12-18">Полезные сервисы</a>.\n\nНапоминаю, что <b>изучение этих моментов очень важно для того, чтобы вы сохранили свои деньги и начали их преумножать!</b>
"""

### FUNCTION MESSAGES ###

def paymentMsg(price, duration):
    if duration == 1:
        return f"Я рад, что вы решили присоединиться!\nНиже вы можете найти подробную информацию о выбранном вами плане. Выберите пожалуйста способ оплаты.\n\nПлан: <b>VIP SIGNALS</b>\nПродолжительность: <b>1 Месяц</b>\nСтоимость: <b>{price} USD</b>\nАвто-продляемая подписка: <b>Нет</b>\n\nЗавершив этот заказ, вы получите доступ к следующим чатам:\n📢 Канал <b>ForexDohod VIP SIGNALS ®</b>"
    else:
        return f"Я рад, что вы решили присоединиться!\nНиже вы можете найти подробную информацию о выбранном вами плане. Выберите пожалуйста способ оплаты.\n\nПлан: <b>VIP SIGNALS</b>\nПродолжительность: <b>3 Месяца</b>\nСтоимость: <b>{price} USD</b>\nАвто-продляемая подписка: <b>Нет</b>\n\nЗавершив этот заказ, вы получите доступ к следующим чатам:\n📢 Канал <b>ForexDohod VIP SIGNALS ®</b>"

def statisticMsg(users, privateUsers, parseUsers, usersId, privateUsersId):
    return f'<b>Статистика пользователей ForexDohodBot</b>\n\nКоличество пользователей: {str(len(users))}\nКоличество пользоватей с подпиской: {str(len(privateUsers))}\nПроцент пользователей с подпиской: {round((len(privateUsers)/len(users))*100, 2)}%\n\nИнформация о пользователях без подписки:\n{parseUsers(usersId)}\n\nИнформация о пользователях с подпиской (id, user_id, isSub, untill):\n{parseUsers(privateUsersId)}\n\nИнформация о всех пользователях (id, user_id, isSub, untill):\n{parseUsers(users)}'

def paymentWayMsg(bot, price, walletAddress, duration, call, pay_url, bill_id):
    if duration == 1:
        if call.data == 'usdt':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: USDT TRC20\nСумма к оплате: *{price} USDT*\nДля оплаты переведите указанную сумму Подписки на этот адрес кошелька:\n\n`{walletAddress}` (нажмите,адрес кошелька скопируется)\n\nЭто можно сделать, например, в популярной бирже Бинанс. Напротив валюты USDT нажмите кнопку "Вывод" и введите адрес, который указан выше.\n\nОбратите внимание на *сеть* криптовалюты: *TRC20*.', reply_markup=markups.paymentDesc ,parse_mode='MARKDOWN')
        
        if call.data == 'yooMoney':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: YooMoney\nСумма к оплате: *{price} USD*\n\nДля оплаты перейдите по ссылке ниже.', reply_markup=markups.paymentYooDesc(pay_url, bill_id) ,parse_mode='MARKDOWN')

        if call.data == 'qiwi':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: QIWI\nСумма к оплате: *{price} USD*\n\nДля оплаты перейдите по ссылке ниже.', reply_markup=markups.paymentQiwiDesc(pay_url, bill_id) ,parse_mode='MARKDOWN')
        
    elif duration == 3:
        if call.data == 'usdt3':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: USDT TRC20\nСумма к оплате: *{price} USDT*\nДля оплаты переведите указанную сумму Подписки на этот адрес кошелька:\n\n`{walletAddress}` (нажмите,адрес кошелька скопируется)\n\nЭто можно сделать, например, в популярной бирже Бинанс. Напротив валюты USDT нажмите кнопку "Вывод" и введите адрес, который указан выше.\n\nОбратите внимание на *сеть* криптовалюты: *TRC20*.', reply_markup=markups.paymentDesc3 ,parse_mode='MARKDOWN')

        elif call.data == 'yooMoney3':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: YooMoney\nСумма к оплате: *{price} USD*\n\nДля оплаты перейдите по ссылке ниже.', reply_markup=markups.paymentYooDesc3(pay_url, bill_id) ,parse_mode='MARKDOWN')

        elif call.data == 'qiwi3':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Способ оплаты: QIWI\nСумма к оплате: *{price} USD*\n\nДля оплаты перейдите по ссылке ниже.', reply_markup=markups.paymentQiwiDesc3(pay_url, bill_id) ,parse_mode='MARKDOWN')