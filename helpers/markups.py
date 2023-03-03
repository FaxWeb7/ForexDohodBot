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
findUser = types.KeyboardButton("Поиск по user_id")
back = types.KeyboardButton("◀ Назад")
adminMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(statistic, mailing, findUser).row(back)

### INLINE MARKUPS ###
subsCurrency = types.InlineKeyboardButton("Золотой Робот (-20%)", callback_data='subsGold')
subsGold = types.InlineKeyboardButton("Валютный Робот (-20%)", callback_data='subsCurrency')
subsGoldMini = types.InlineKeyboardButton("Мини-Золотой Робот (-15%)", callback_data='subsGoldMini')
subsDifference = types.InlineKeyboardButton("В чём их отличия?", callback_data='subsDifference')
backMenu = types.InlineKeyboardButton("◀ Назад", callback_data='backMenu')
tariffsMarkup = types.InlineKeyboardMarkup(row_width=1).add(subsCurrency, subsGold, subsGoldMini, subsDifference, backMenu)

goldStat = types.InlineKeyboardButton("⚜️ Статистика Золотого Робота", url='https://www.myfxbook.com/members/Maximilian777/clever-gold/9534287')
currStat = types.InlineKeyboardButton("💶 Статистика Валютного Робота", url='https://www.myfxbook.com/members/Maximilian777/clever-10000/9488108')
statMarkup = types.InlineKeyboardMarkup(row_width=1).add(goldStat, currStat)

linkBtn = types.InlineKeyboardButton("✉️ Обсудить детали оплаты с админом", url='t.me/@faxweb_w')
backRate = types.InlineKeyboardButton("◀ Назад", callback_data='backRate')
paymentMarkup = types.InlineKeyboardMarkup(row_width=1).add(linkBtn, backRate)
differenceMarkup = types.InlineKeyboardMarkup(row_width=1).add(backRate)