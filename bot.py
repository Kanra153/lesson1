from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def main():
	updater = Updater('315529609:AAGmijYhvnDt_O56S3Y_5PrpXH5RahsTbU8')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))# когда пользователь пишет старт активируется фунция
	dp.add_error_handler(show_error)
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	updater.start_polling() # подключились к обновлениям
	updater.idle() # ждём обновлений
def talk_to_me(bot, update):
	print(update.message.text)	
	bot.sendMessage(update.message.chat_id, update.message.text)
def show_error(bot, update, error): #обработка ошибки
	print(error)
def greet_user(bot, update):
	print ('Вызван /start')
	bot.sendMessage(update.message.chat_id, text="Привет, поговорим?")#Функция посылает сообщение в чат
main ()