import telebot

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7675941600:AAEhk-kpHLpUj_i9WWNcMLK9HRgN3CrjSmE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот-энциклопедия про 'Глобальное потепление'. Напиши команду /help чтобы узнать какие вопросы можно задать.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Список вопросов: /question1 (Что такое глобальное потепление?), /question2 (Насколько эта проблема серьезна, и касается ли она нас?), /question3 (Что провоцирует глобальное потепление?), /question4 (Как мы можем сдерживать глобальное потепление?), /question5 (Можно ли остановить глобальное потепление?)")

@bot.message_handler(commands=['question1'])
def send_question1(message):
    bot.reply_to(message, "Что такое глобальное потепление?: Это повышение средней температуры Земли, которое наблюдается с конца XIX века. ")
    bot.send_photo(message.chat.id, "https://neftegaz.ru/upload/iblock/267/3ng59kl5amjmqbrh1hw3fgjb8yqo2qcg/5-Arktika.jpg")

@bot.message_handler(commands=['question2'])
def send_password(message):
    bot.reply_to(message, "Насколько эта проблема серьезна, и касается ли она нас?: глобальное потепление является самой большой отдельно взятой угрозой в сфере здравоохранения. Его последствия, в том числе волны жары, засухи и наводнения, оборачиваются гибелью и болезнями людей, вспышками инфекций и голодом.")
    bot.send_photo(message.chat.id, "https://global.unitednations.entermediadb.net/assets/mediadb/services/module/asset/downloads/preset/Libraries/Production+Library/06-08-2021_Unsplash_Iceland.jpg/image1170x530cropped.jpg")

@bot.message_handler(commands=['question3'])
def send_emodji(message):
    bot.reply_to(message, "Что провоцирует глобальное потепление?: Ископаемые виды топлива — уголь, нефть и газ — вносят наибольший вклад в глобальное изменение климата: на их долю приходится свыше 75 процентов глобальных выбросов парниковых газов и почти 90 процентов всех выбросов углекислого газа. ")
    bot.send_photo(message.chat.id, "https://cdn.unenvironment.org/s3fs-public/inline-images/20230703_Noor%20Solare%20Inger%20Andersen%20Visit_Morocco_UNEP_Duncan%20Moore_1760%20%281%29.jpg")

@bot.message_handler(commands=['question4'])
def send_coin(message):
    bot.reply_to(message, "Как мы можем сдерживать глобальное потепление?: Деятельность человека способствует изменению климата, вызывая изменения концентрации в атмосфере парниковых газов, аэрозолей (мелких частиц) и облачности. Наибольший известный вклад вносит сжигание ископаемых видов топлива, при котором в атмосферу выбрасывается углекислый газ.")
    bot.send_photo(message.chat.id, "https://rg.ru/uploads/images/2023/11/01/1istock-1327251915_8f6.jpeg")

@bot.message_handler(commands=['question5'])
def send_coin(message):
    bot.reply_to(message, "Можно ли остановить глобальное потепление?: Каждый может помочь ограничить последствия изменения климата. Мы можем добиться перемен к лучшему в самых разных областях: от того, на чем мы ездим, до электричества, которое мы потребляем, и продуктов, которые мы едим.")
    bot.send_photo(message.chat.id, "https://cdnn1.img.crimea.ria.ru/img/111839/84/1118398445_0:6:3000:1694_1920x0_80_0_0_e18cd04d18423b999b8e4c7b0e8dc4bd.jpg")
# Запускаем бота
bot.polling()