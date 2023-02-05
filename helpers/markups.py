from telebot import types

### MENU MARKUPS ###
rates = types.KeyboardButton("🤖 Купить Торгового Робота")
faq = types.KeyboardButton("Что за робот?")
revenue = types.KeyboardButton("Статистика доходности")
freeChannel = types.KeyboardButton("🗞️ Бесплатный канал")
feedback = types.KeyboardButton("☎️ Обратная связь")
adminCmd = types.KeyboardButton("🟰🟰🟰 АДМИН ПАНЕЛЬ 🟰🟰🟰")
menuMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).row(rates).add(faq, revenue, freeChannel, feedback)
menuAdminMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).row(rates).add(faq, revenue, freeChannel, feedback).row(adminCmd)

statistic = types.KeyboardButton("Статистика пользователей")
mailing = types.KeyboardButton("Рассылка по пользователям")
back = types.KeyboardButton("◀ Назад")
adminMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(statistic, mailing, back)

### INLINE MARKUPS ###
subsGold = types.InlineKeyboardButton("Робот GOLD (-20%)", callback_data='subsGold')
subsGoldMini = types.InlineKeyboardButton("Робот GOLD mini (-15%)", callback_data='subsGoldMini')
backMenu = types.InlineKeyboardButton("◀ Назад", callback_data='backMenu')
tariffsMarkup = types.InlineKeyboardMarkup(row_width=1).add(subsGold, subsGoldMini, backMenu)

docBtn = types.InlineKeyboardButton("✉️ Обсудить детали оплаты с админом", url='t.me/@faxweb_w', callback_data='docBtn')
backRate = types.InlineKeyboardButton("◀ Назад", callback_data='backRate')
paymentMarkup = types.InlineKeyboardMarkup(row_width=1).add(docBtn, backRate)