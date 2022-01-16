from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from funct import *
from cons import *
upd = Updater(token=TOKEN, workers=4)
dis = upd.dispatcher
dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(CommandHandler(command='wwwwww', callback=wwwwww))
dis.add_handler(CommandHandler(command='get_date', callback=get_date))
dis.add_handler(CallbackQueryHandler(pattern='ru_change', callback=ru_change))
dis.add_handler(CallbackQueryHandler(pattern='uz_change', callback=uz_change))
dis.add_handler(CallbackQueryHandler(pattern='ru', callback=ru))
dis.add_handler(CallbackQueryHandler(pattern='uz', callback=uz))
dis.add_handler(MessageHandler(Filters.text, next_func))
dis.add_handler(MessageHandler(Filters.contact, get_contac))
dis.add_handler(MessageHandler(Filters.location, get_location))
dis.add_handler(MessageHandler(Filters.photo, adm))

upd.start_polling(drop_pending_updates=True)
