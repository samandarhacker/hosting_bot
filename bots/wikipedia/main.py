w=0
  
import telebot
import wikipedia


token_file = open(f"{chat_id}/bots/wikipedia/token.txt","r+")
token_a = token_file.read()
print(token_a)
bot = telebot.TeleBot(token=token_a)
wikipedia.set_lang("uz")
def obuna(id):
	try:
		obuna = bot.get_chat_member("@python3600", id).status
		if obuna == "member":
			return True
		elif obuna == "creator":
			return True
		elif obuna == "administrator":
			return True
	except:
		return True
buttons = telebot.types.InlineKeyboardMarkup([[
telebot.types.InlineKeyboardButton(" Kanalga kirish ", url="https://t.me/python3600")],
[telebot.types.InlineKeyboardButton(' Kanalga kirish ',url="https://t.me/python36001")]])
button = telebot.types.ReplyKeyboardMarkup(True)
butto = telebot.types.ReplyKeyboardRemove(True)
button.add("Foydali kanallar","Bot Zakaz berish","Bot Haqida Malumot Olish")
@bot.message_handler(commands=["NotButton"])
def notbutton(message):
	bot.send_message(message.chat.id,"Tugmalar Olibtashlandi Tugmalarni qo'shinuchun /Buttons", reply_markup=butto)
@bot.message_handler(commands=["Buttons"])
def buttonnns(message):
	bot.send_message(message.chat.id,"Tugmalar qo'shildi!!!\nTugmalarni o'chirish /NotButton",reply_markup=button)
@bot.message_handler(commands=["start"])
def salom(message):
	ism = message.from_user.first_name
	if obuna(message.chat.id):
		bot.send_message(message.chat.id," Assalomu alaykum {} wikipedi botimizga hush kelibsiz".format(ism))
		bot.send_message(message.from_user.id," Bot haqida malumot olish /help\nBotni qayta ishga tushurish /start\nFoydali botlar /Bots\nTugmalardan foydalanish /Buttons")
	else:
		bot.send_message(message.chat.id,"Botdan foydalanish uchun kanallarga obuna bo'lish va / start buyrug'ini yuboring",reply_markup=buttons)

@bot.message_handler(commands=["Bots"])
def bots(message):
	bot.send_message(message.chat.id,"Foydali botlar ro'yhati\n@translator_python3600_bot\n@VideoToAudioPythonBot\n@Wikipediandlinebot")
@bot.message_handler(commands=["help"])
def help(message):
	bot.send_message(message.chat.id," Men wikipediadan maqolalarni sizga topib beraman buning uchun menga matin yuboring men matinga aloqador maqolani yuboaraman")
@bot.message_handler()
def malumot(message):
	if message.text == "Bot Zakaz berish":
		bot.send_message(message.chat.id,"Bot zakaz berish uchun @Azamov_Samandar ga murojat qiling!!!!")
	elif message.text == "Foydali kanallar":
		bot.send_message(message.chat.id,"Foydali Kanallar\nhttps://t.me/python3600\nhttps://t.me/python36001")
	elif message.text == "Bot Haqida Malumot Olish":
		bot.send_message(message.chat.id,"bot python dasturlash tilida yaratilgan va wikipedia api dan foydalanilgan bot kodi xabar tagida!!!!")
	else:
		try:
			malumot = wikipedia.summary(message.text)
			bot.send_message(message.chat.id,malumot)
		except:
			bot.send_message(message.chat.id," Bu mavzudagi maqola topilmadi")
bot.polling(none_stop=True)