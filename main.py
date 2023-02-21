from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os
# get token from env
TOKEN = os.environ['TOKEN']
path= os.getcwd()
print(path)
def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['👨Otam','👩‍🦱Ayam','👩Opam N.1'],
        ['🧑Akam','👩Opam N.1','🧑🏻‍💻Men']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )
def shop(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    keyboar1 = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Rasmlar",callback_data="Apple")],
        [InlineKeyboardButton(text="Malumot",callback_data="samsung")],
        

        ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text="Assalom alaykum OTAM haqida",
    reply_markup=keyboar1)
def cart(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    keyboar1 = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Rasmlar",callback_data="Shop")],
        [InlineKeyboardButton(text="Malumot",callback_data="Older")]
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text="Assalom alaykum AYAM haqida",
    reply_markup=keyboar1)
def about(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    keyboar1 = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Rasmlar",callback_data="📝About as")],
        [InlineKeyboardButton(text="Malumot",callback_data="📝About the bot")]
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text="Assalom alaykum OPAM haqida",
    reply_markup=keyboar1)
def akam(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    keyboar1 = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Rasmlar",callback_data="aka")],
        [InlineKeyboardButton(text="Malumot",callback_data="aha")]
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text="Assalom alaykum AKAM haqida",
    reply_markup=keyboar1)
def opam(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    keyboar1 = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Rasmlar",callback_data="opa")],
        [InlineKeyboardButton(text="Malumot",callback_data="salom")]
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text="Assalom alaykum OPAM haqida",
    reply_markup=keyboar1)
def query(update: Update, context: CallbackContext):
    print('salom')
    
    quer=update.callback_query
    quer.answer("hi")
    chat_id=quer.message.chat_id
    bot = context.bot
    if quer.data=='number':
        bot.sendMessage(chat_id,"admin https://t.me/Muhammadyusuf_5538")
    elif quer.data=="https://chrontime.com/city-uz-zarafshan/102293":
        bot.sendMessage(chat_id,"Navoi viloyat Zarafshon shahar")
    elif quer.data=="location":
        bot.sendLocation(chat_id, latitude=39.661211, longitude =67.010697 )
    elif quer.data=="email":
        bot.sendMessage(chat_id,"mamaniyozovmuhammadyusuf5@gmail.com")
    elif quer.data=="Apple":
        bot.sendPhoto(chat_id,"https://images.uzum.uz/cdq99lgv1htd23ai39og/original.jpg")
        bot.sendMessage(chat_id,"Экран 6.1/2556x1179 ПиксТехнология экрана OLEDВстроенная память (ROM) 128 ГБсновная камера МПикс 48/12/12")
    elif quer.data=="samsung":
        bot.sendPhoto(chat_id,"https://images.uzum.uz/ceko3hol08kcldtp8rd0/original.jpg")