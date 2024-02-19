//copy token from telegram
import telegram.ext

Token= "    "
updater = telegram.ext.updater(" token copy", use_context-True)
dispatcher = updater.dispatcher
def start(update,context):
    update.message.reply_text("hello welcom to telegram_bot")
def help(update,context):
    update.message.reply_text(
        """ 
        /start -> welcome to the channel
        /help  -> This particular message 
        /contetx -> About various playList 
        python -> The first video from sql playList
        """
    )

def context(update,context):
    update.message.reply_text(" we have various playlist and articles available")
def python(update,context):
    update.message.reply("tutorial link : http://youtube")
dispatcher.add_handler(telegram.ext.commandHandler('start', start))
dispatcher.add_handler(telegram.ext.commandHandler('help', help))
dispatcher.add_handler(telegram.ext.commandHandler('context', context))
dispatcher.add_handler(telegram.ext.commandHandler('python', python))
update-start_polling()
update.idle()