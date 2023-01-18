from telebot import types

### MENU MARKUPS ###
rates = types.KeyboardButton("🛒 Тарифы")
subscribe = types.KeyboardButton("📊 Подписка")
education = types.KeyboardButton("Бесплатное обучение")
revenue = types.KeyboardButton("Сколько можно заработать?")
freeChannel = types.KeyboardButton("🗞️ Бесплатный канал")
feedback = types.KeyboardButton("☎️ Обратная связь")
adminCmd = types.KeyboardButton("🟰🟰🟰 АДМИН ПАНЕЛЬ 🟰🟰🟰")
menuMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(rates, subscribe, education, revenue, freeChannel, feedback)
menuAdminMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(rates, subscribe, education, revenue, freeChannel, feedback, adminCmd)

privateSub = types.KeyboardButton("Добавить подписчика в секретный канал")
deleteSub = types.KeyboardButton("Удалить подписчика с секретного канала")
changeUserData = types.KeyboardButton("Изменить данные пользователя")
statistic = types.KeyboardButton("Статистика пользователей")
writeToSub = types.KeyboardButton("Написать сообщение пользователю")
mailing = types.KeyboardButton("Рассылка по пользователям")
back = types.KeyboardButton("◀ Назад")
adminMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(privateSub, deleteSub, changeUserData, statistic, writeToSub, mailing, back)

### INLINE MARKUPS ###
subsOne = types.InlineKeyboardButton("1 Месяц", callback_data='subsOne')
subsThree = types.InlineKeyboardButton("3 Месяца (-20%)", callback_data='subsThree')
backMenu = types.InlineKeyboardButton("◀ Назад", callback_data='backMenu')
tariffsMarkup = types.InlineKeyboardMarkup(row_width=1).add(subsOne, subsThree, backMenu)

usdt = types.InlineKeyboardButton("USDT TRC20", callback_data='usdt')
card = types.InlineKeyboardButton("По номеру карты", callback_data='card')
qiwi = types.InlineKeyboardButton("Qiwi", callback_data='qiwi')
backRate = types.InlineKeyboardButton("◀ Назад", callback_data='backRate')
paymentMarkup = types.InlineKeyboardMarkup(row_width=1).add(usdt, card, qiwi, backRate)

usdt3 = types.InlineKeyboardButton("USDT TRC20", callback_data='usdt3')
card3 = types.InlineKeyboardButton("По номеру карты", callback_data='card3')
qiwi3 = types.InlineKeyboardButton("Qiwi", callback_data='qiwi3')
backRate3 = types.InlineKeyboardButton("◀ Назад", callback_data='backRate')
paymentMarkup3 = types.InlineKeyboardMarkup(row_width=1).add(usdt3, card3, qiwi3, backRate3)

payment = types.InlineKeyboardButton("✅ Я оплатил", callback_data='payment')
backPrice = types.InlineKeyboardButton("❌ Отменить", callback_data='subsOne')
paymentDesc = types.InlineKeyboardMarkup(row_width=1).add(payment, backPrice)

payment3 = types.InlineKeyboardButton("✅ Я оплатил", callback_data='payment')
backPrice3 = types.InlineKeyboardButton("❌ Отменить", callback_data='subsThree')
paymentDesc3 = types.InlineKeyboardMarkup(row_width=1).add(payment3, backPrice3)