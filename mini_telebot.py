import telebot

# 1. Conexión con Telegram usando tu Token
TOKEN = "8806928055:AAF3itfm3-EPuRSz9TG7GTsCfWUfhkD_-f8"
bot = telebot.TeleBot(TOKEN)

# 2. "Escuchador": Si el usuario escribe /hola, ejecuta la función
@bot.message_handler(commands=['hola'])
def saludar(message):
    # 3. Respuesta del bot en el chat
    bot.reply_to(message, "¡Hola, bro! Todo bien por aquí.")

# 4. Mantiene el bot encendido escuchando mensajes
print("Bot encendido...")
bot.infinity_polling()
