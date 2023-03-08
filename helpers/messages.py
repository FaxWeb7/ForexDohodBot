import helpers.markups as markups

### STRING MESSAGES ###

startMessage = """
    👋 <b>Добро пожаловать в ForexDohodBot, {0.first_name}!</b>\n\nМеня зовут Артём! Тут вы можете узнать все про <b>торгового робота, его статистику, каким образом он торгует прибыльно, и сколько он стоит.</b>\n\n<b>После покупки торгового робота вам будет доступно:</b>\n\n🤖 Полная инструкция по открытию счета и установке на него бота.\n🔒 Доступ к закрытому каналу, в котором состоят <b>только пользователи с приобретенным торговым роботом</b>\n📘 Краткое руководство <b>по Форексу</b> (книга pdf)
"""

profitabilityMsg = """
    ✅ Средняя доходность торгового робота составляет <b>от 8 до 30% в месяц</b>. Во многом, она <b>зависит от волатильности рынка, а также от настроек агрессивности робота</b>.\n\n📈 Ниже приведены <b>ссылки на открытую статистику роботов (используется демо-счёт)</b>, вы можете ознакомиться с ними, и если вас все устроит, <b>можете приобрести робота</b>.
"""

freeChannelMsg = """
    <b>Еще не подписаны на мой Телеграм канал "ForexDohod"? 🙈</b>\n\n<b><u>В нём вы сможете найти:</u></b>\n\n▪️Бесплатные сигналы\n▪️Обзор рынка\n▪️Важные новости и другое!\n\n<a href="https://t.me/ForexDohod"><b>✅Ссылка на канал✅</b></a>
"""

feedbackMsg = """
    Если у вас возникли вопросы, то свяжитесь с <a href="t.me/@faxweb_w">админом</a>, он ответит вам в ближайшее время.
"""

faqMsg = """<b>Сейчас мы разберем, что за торговый робот, и как он работает.</b>\n\nТорговый робот - это <b>компьютерное программное обеспечение для автоматичиской торговли на рынке Forex</b> у брокера <b><a href="https://my.roboforex.com/en/?a=ymht">RoboForex</a></b>, которое анализирует массивы данных и совершает сделки <b>на определённых парах</b> по написанному алгоритму на языке <b>MQL</b>.\n\nВсе сделки робота открываются после <b>сигнала индикатора, который считывает поведение рынка и строит средние скользящие на опережение рынка</b>, тем самым гарантируя <b>удачную точку входа в рынок</b> как на покупку, так и на продажу <b>золота</b>. Последующие усреднения производятся с <b>определенным нами диапазонном и выверенным коэффициентом умножения предыдущей сделки</b>.\n\nУ робота стоят разнообразные <b>"защиты" для сохранения депозита</b>. Простыми словами, если вдруг после открытой сделки рынок <b>резко меняет своё поведение</b>, робот зафиксирует небольшой убыток, либо постарается вывести сделки в ноль. После этого робот продолжит работать с новыми сделками.\n\nТак же робот <b>не берет усреднения на сквизах и в период излишней волатильности рынка.</b>
"""

### FUNCTION MESSAGES ###

def paymentMsg(price, tariff):
    ifBuy = f'<u><b>Завершив этот заказ, вы получите:</b></u>\n🤖 Полную <b>инструкцию по открытию счета</b> и помощь по установке на него бота.\n📢 Доступ к закрытому каналу, в котором состоят <b>только пользователи с приобретенным торговым роботом</b>\n📘 Краткое руководство <b>по Форексу</b> (книга pdf)\n🌆 <b>Возможна реальная встреча</b> для настройки робота (если вы находитесь в Москве)'
    if price != 0: asd = int(price.replace(".",""))+(int(price.replace(".",""))*0.2)
    if tariff == 'gold':
        return f"<b>Я рад, что вы решили совершить покупку!</b>\n\n🤖Торговый робот: <b>Золотой</b>\n💰Стоимость: <s>{round(int(price.replace('.',''))+(int(price.replace('.',''))*0.25))}</s> <b>{price}₽</b>\n💲Разрешенный размер депозита:\n<b>от 1.000$ до 50.000$</b>\n\n{ifBuy}"
    elif tariff == 'currency':
        return f"<b>Я рад, что вы решили совершить покупку!</b>\n\n🤖Торговый робот: <b>Валютный</b>\n💰Стоимость: <s>{round(int(price.replace('.',''))+(int(price.replace('.',''))*0.25))}</s> <b>{price}₽</b>\n💲Разрешенный размер депозита:\n<b>5.000$ | 10.000$ | 20.000$</b>\n\n{ifBuy}"
    elif tariff == 'goldMini':
        return f"<b>Я рад, что вы решили совершить покупку!</b>\n\n🤖Торговый робот: <b>Мини-Золотой</b>\n💰Стоимость: <s>{round(int(price.replace('.',''))+(int(price.replace('.',''))*0.175))}</s> <b>{price}₽</b>\n💲Разрешенный размер депозита:\n<b>от 100$ до 2.000$</b>\n\n{ifBuy}"
    elif tariff == 'difference':
        return f"<b>💸 Итак, давайте разберёмся чем торует каждый из роботов и на каком размере депозита он это делает:</b>\n\n<u><b>1) Золотой Робот</b></u> - делает сделки на паре <b>XAU/USD (золото)</b>. Разрешенный размер депозита, тоесть <b>диапазон количества денежных средств</b>, которые вы можете положить на депозит робота составляет <b>от 1.000$ до 50.000$</b>.\n\n<u><b>2) Мини-Золотой Робот</b></u> - делает сделки на паре <b>XAU/USD (золото)</b>. Точно такой же робот, что и Золотой, <b>кроме разрешенного размера депозита</b>, тут он составляет <b>от 100$ до 2.000$</b>.\n\n<u><b>3) Валютный Робот</b></u>- делает сделки на парах <b>EUR/NZD и AUD/USD</b>. Если на золотых роботов вы можете положить определенный диапазон денег, то на валютного робота вы можете положить <b>конкретную сумму - 5.000$, 10.000$, или 20.000$.</b>"

def statisticMsg(users):
    return f'<b>Статистика пользователей ForexDohodBot</b>\n\nКоличество пользователей(без первых 263): {str(len(users)+263)}'


# <b><u>Чем GOLD отличается от GOLD mini?</u></b>\nДанные роботы <b>отличаются только разрешенным размером депозита</b>, который вы на него ложите. Если на депозит робота <b>GOLD</b> вы можете положить <b>от 1.000$ до 50.000$</b>, то на депозит робота <b>GOLD mini</b> вы можете положить <b>от 100$ до 2.000$</b>.\n\n




# educationMsg = """‍Отлично, я рад, что <b>вы выбрали путь обучения, это совершенно бесплатно и поможет сохранить ваши деньги!</b>\n\nПоэтому <b>изучить все короткие обучающие статьи ниже очень важно!</b>\n\nЯ постараюсь ответить на максимальное количество ваших вопросов с помощью статей ниже:\n\n<b>1.</b> Проверенные Форекс-Брокеры: <a href="https://roboforex.com">RoboForex</a>, <a href="https://www.exness.com/">Exness</a>, <a href="https://www.icmarkets.com/intl/ru/">ICMarkets</a>.\n<b>2.</b> <a href="https://telegra.ph/Registraciya-i-Verifikaciya-na-RoboForex-12-18">Как зарегистрироваться и верифицировать аккаунт у Форекс-Брокера?</a>\n<b>3.</b> <a href="https://telegra.ph/Kak-otkryt-i-popolnit-schet-u-brokera-RoboForex-12-18">Как открыть и пополнить счет у брокера RoboForex?</a>\n<b>4.</b> <a href="https://telegra.ph/Kak-skachat-terminal-MetaTrader4-i-zajti-na-torgovyj-schet-vashego-brokera-12-18">Как скачать терминал MetaTrader4 и зайти на счет вашего брокера?</a>\n<b>5.</b> <a href="https://telegra.ph/Osnovy-tehnicheskogo-analiza-12-18">Основы технического анализа</a>.\n<b>6.</b> <a href="https://telegra.ph/Manimenedzhment-i-usrednenie-pozicii-12-18">Манименеджмент и усреднение позиции</a>.\n<b>7.</b> <a href="https://telegra.ph/Vsyo-o-moem-robote-Kak-on-rabotaet-torguet-i-daet-signaly-12-18">Как мой робот дает сигналы, и как их повторить без потерь.</a>\n<b>8.</b> <a href="https://telegra.ph/Poleznye-servisy-12-18">Полезные сервисы</a>.\n\nНапоминаю, что <b>изучение этих моментов очень важно для того, чтобы вы сохранили свои деньги и начали их преумножать!</b>
# """
