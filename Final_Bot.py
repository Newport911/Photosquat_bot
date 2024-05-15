import telebot
import gspread
from Inf import Token
import time
from telebot import types

gc = gspread.service_account(filename='credentials.json')

table_name = gc.open("Your table name")
first_list = table_name.worksheet("Лист1")
second_list = table_name.worksheet("Лист2")

lol = "test"
bot = telebot.TeleBot(Token.bot)


def search(wn, phone='None'):
    cell = first_list.find(wn, in_column=3)
    worksheet = first_list
    if cell is None:
        cell = second_list.find(wn, in_column=3)
        worksheet = second_list
    if cell is None:
        intermediate_result = """Упс! Заказ не найден ☹️ Возможно, ты 
указал(а) неверный номер заказа. Если ты 
уверен(а), что номер заказа введен верно, но 
выскакивает это сообщение — пожалуйста, 
обратись к нашему менеджеру @phsquat_chat, и 
мы попробуем найти твой заказ вручную 🙌🏼"""
    else:
        cell_number = cell.row  # ЭТО НОМЕР ЯЧЕЙКИ ВЕРТИКАЛЬНЫЙ СТОЛБЕЦ (ЦИФРЫ)
        values_list = worksheet.row_values(cell_number)  # Это для проверки статуса
        if phone == values_list[11]:
            for intermediate_result in values_list:
                if intermediate_result == "опл готов отпр":
                    intermediate_result = """Статус твоего заказа: оплачен, готов и отправлен на e-mail 📩 

Не забудь скачать фотографии по ссылке, они хранятся 60 дней с 
момента оформления заказа. Также мы ждем тебя в ФотоСквоте, 
чтобы забрать негативы! Заказ хранится в ФотоСквоте втечение 
60 дней с момента оформления заказа."""
                    return intermediate_result

                elif intermediate_result == "опл на проявку":
                    intermediate_result = "Статус твоего заказа: оплачен, в очереди на проявку! 🎞"
                    return intermediate_result
                elif intermediate_result == "опл на скан":
                    intermediate_result = "Статус твоего заказа: оплачен, в очереди на сканирование! 🎞"
                    return intermediate_result
                elif intermediate_result == "опл на отправку":
                    intermediate_result = """Статус твоего заказа: оплачен, скоро будет отправлен на почту! 
Осталось подождать совсем чуть-чуть 🤏🏼"""
                    return intermediate_result
                elif intermediate_result == "опл на печать":
                    intermediate_result = "Статус твоего заказа: оплачен, в очереди на печать! 🌠"
                    return intermediate_result
                elif intermediate_result == "опл готов":
                    intermediate_result = """Статус твоего заказа: оплачен и готов 💫 Можно забирать! 

Заказ хранится в ФотоСквоте втечение 60 дней с момента оформления заказа."""
                    return intermediate_result
                elif intermediate_result == "опл готов отпр отдан":
                    intermediate_result = """Статус твоего заказа: оплачен, готов, отправлен на e-mail и отдан тебе 🙂

Не забудь скачать фотографии по ссылке, они хранятся 60 дней с 
момента оформления заказа."""
                    return intermediate_result
                elif intermediate_result == "опл готов отдан":
                    intermediate_result = "Статус твоего заказа: оплачен, готов и отдан тебе 🙂"
                    return intermediate_result
                elif intermediate_result == "н/о готов":
                    intermediate_result = """Статус твоего заказа: не оплачен, готов. 

Если ты хочешь оплатить заказа онлайн по карте, пожалуйста, 
напиши нашим менеджерам @phsquat_chat, и они пришлют 
тебе инструкцию как оплатить заказ 💸
Заказ хранится в ФотоСквоте 60 дней с момента оформления заказа."""
                    return intermediate_result

                elif intermediate_result == "СРОЧНО опл на проявку":
                    intermediate_result = "Статус твоего заказа: ⚡️срочный заказ⚡️, оплачен, в очереди на проявку!"
                    return intermediate_result

                elif intermediate_result == "СРОЧНО опл на скан":
                    intermediate_result = "Статус твоего заказа:⚡️срочный заказ⚡️, оплачен, в очереди на сканирование!"
                    return intermediate_result

                elif intermediate_result == "н/о на проявку":
                    intermediate_result = """Статус твоего заказа: не оплачен, в очереди на проявку. 

Мы сможем приступить к выполнению твоего заказа только 
после 100% оплаты заказа 💸
Если ты хочешь оплатить заказа онлайн по карте, пожалуйста, 
напиши нашим менеджерам @phsquat_chat, и они пришлют 
тебе инструкцию как оплатить заказ :)"""
                    return intermediate_result

                elif intermediate_result == "н/о на скан":
                    intermediate_result = """Статус твоего заказа: не оплачен, в очереди на сканирование. 

Мы сможем приступить к выполнению твоего заказа только 
после 100% оплаты заказа 💸
Если ты хочешь оплатить заказа онлайн по карте, пожалуйста, 
напиши нашим менеджерам @phsquat_chat, и они пришлют 
тебе инструкцию как оплатить заказ 🙌🏼"""
                    return intermediate_result

                elif intermediate_result == "н/о на отправку":
                    intermediate_result = """Статус твоего заказа: не оплачен, в очереди на отправку на email 
н/о на отправку  💸

Мы сможем отправить твой заказ только после 100% оплаты 
заказа. 
Если ты хочешь оплатить заказа онлайн по карте, пожалуйста, 
напиши нашим менеджерам @phsquat_chat, и они пришлют 
тебе инструкцию как оплатить заказ 🙌🏼"""
                    return intermediate_result

                elif intermediate_result == "н/о на ремонт":
                    intermediate_result = """Статус твоего заказа: не оплачен, в очереди на ремонт 📷

Если тебе нужна дополнительная информация по срокам на 
ремонт, пожалуйста, напиши нашим менеджерам 
@phsquat_chat, и они подскажут сроки ожидания заказа  🙌🏼"""
                    return intermediate_result

            else:
                intermediate_result = "не заполнен. Для подробностей свяжитесь с нашим менеджером"
                return intermediate_result
        else:
            intermediate_result = """Упс! Мы не можем найти такой номер телефона ☹️ Укажи
телефон в формате +ХХХХХХХХХХХХ. Если ты уверен(а), что
телефон введен верно, но выскакивает это сообщение —
пожалуйста, обратись к нашему менеджеру @phsquat_chat, и
мы попробуем найти твой заказ вручную 🙌🏼"""
            return intermediate_result


def button_or_search(message):
    if message.text == '🍐Наши соц сети':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Instagram', url='https://www.instagram.com/phsquat/'))
        markup.add(types.InlineKeyboardButton('Telegram', url='https://t.me/phsquat/'))
        bot.reply_to(message, '🍐СОЦ СЕТИ🍐', reply_markup=markup)
    elif message.text == '❓Узнать статус заказа':
        bot.send_message(message.chat.id, text="""Чтобы узнать статус вашего заказа, введите в одном сообщении:
1) Номер вашего заказа в формате пяти первых цифр (без буквенного обозначения)
2) Ваш номер телефона в формате +ХХХХХХХХХХХХ

Например: 12345 +375257261476""")
    elif message.text == '🍋Цены на пленку (в разработке)':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Актуальный прайс', url='https://t.me/phsquat/658'))
        bot.reply_to(message, '🍋🍋🍋🍋', reply_markup=markup)
    else:
        try:
            wn = message.text.strip()
            wn_new = wn.replace('+', ' ')  # УБИРАЕТ ВСЕ + ИЗ ЗАПРОСА
            splitter = wn_new.split()  # TODO ПЕРЕПИШИ НАЗВАНИЕ splitter
            result_search = search(wn=splitter[0], phone=splitter[1])
            if result_search == """Упс! Мы не можем найти такой номер телефона ☹️ Укажи
телефон в формате +ХХХХХХХХХХХХ. Если ты уверен(а), что
телефон введен верно, но выскакивает это сообщение —
пожалуйста, обратись к нашему менеджеру @phsquat_chat, и
мы попробуем найти твой заказ вручную 🙌🏼""":
                result_search = search(wn=splitter[0] + "_1", phone=splitter[1])
        except:
            bot.reply_to(message, "Проверьте правильность введенных данных")  # ОШИБКА КОГДА ВВЕДЕНЫ БУКВЫ ИЛИ ОДНО
            # СЛОВО И Т.Д.
        else:
            bot.reply_to(message, result_search)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('❓Узнать статус заказа')
    markup.row(item1)
    item2 = types.KeyboardButton('🍐Наши соц сети')
    item3 = types.KeyboardButton('🍋Цены на пленку (в разработке)')
    markup.row(item2, item3)
    # item4 = types.KeyboardButton('🍇 (Просто заглушка на будущее)')
    bot.reply_to(message, """\
Привет! 👋🏼 Это бот фотолаборатории ФотоСквот в Минске 🎞 
Он создан для того, чтобы помочь тебе быстро узнать ответ на
часто задаваемые вопросы в любое время дня и ночи! Здесь ты 
можешь узнать статус своего заказа, а также получить ссылки 
на наши социальные сети и прайс-лист на услуги.\
""", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def number_work(message):
    start = time.time()
    button_or_search(message)
    end = time.time()
    print('The time of execution of above program is :',
          (end - start) * 10 ** 3, "ms")


def start():
    bot.infinity_polling()


start()
