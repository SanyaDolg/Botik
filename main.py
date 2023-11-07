import telebot
token = '6713352456:AAGI7OCfdjU23NZMcw7huGh8SZ8oKcy8D5U'
bot = telebot.TeleBot(token)

@bot.message_handler()
def info(message):
    if message.text.lower()== '@all':
        bot.reply_to(message,'@Sashka_gg  @Ogboychik @Zzhhmiih @koko_jambooo @Evgeniq_07 @NoName549393 @tswowwji @bepebka1x1 @wweeerl @ijikk_iji')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Я работаю, ёпт")

bot.infinity_polling()
