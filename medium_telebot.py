import telebot
import threading

# 1. Conexión con tu Token
TOKEN = "8806928055:AAF3itfm3-EPuRSz9TG7GTsCfWUfhkD_-f8"
bot = telebot.TeleBot(TOKEN)

# 2. Función que se ejecutará cuando termine el tiempo de espera
def enviar_recordatorio(chat_id, mensaje):
    bot.send_message(chat_id, f"⏰ ¡RECORDATORIO!: {mensaje}")

# 2. "Escuchador": Si el usuario escribe /hola, ejecuta la función
@bot.message_handler(commands=['hola'])
def saludar(message):
    # 3. Respuesta del bot en el chat
    bot.reply_to(message, "¡Hola, bro! Todo bien por aquí.")
    
# 4. Escuchador del comando /recordar
@bot.message_handler(commands=['recordar'])
def programa_recordatorio(message):
    try:
        # Pica el mensaje enviado: "/recordar 5 Hola bro" -> ["/recordar", "5", "Hola bro"]
        partes = message.text.split(" ", 2)
        tiempo = partes[1]  # Convierte el "5" en un número
        texto = partes[2]          # Guarda "Hola bro"
        
        if tiempo.endswith("m"):
        	segundos = int(tiempo[:-1]) * 60
        else:
        	segundos = int(tiempo)

        # Crea un temporizador en segundo plano para esperar los segundos pedidos
        temporizador = threading.Timer(segundos, enviar_recordatorio, args=[message.chat.id, texto])
        temporizador.start()

        # Le confirma al usuario que el recordatorio fue agendado
        bot.reply_to(message, f"✅ Vale, te recordaré '{texto}' en {segundos} segundos.")

    except Exception:
        bot.reply_to(message, "❌ Usa el formato:\n`/recordar [segundos] [mensaje]`\nEjemplo: `/recordar 5 Sacar la basura`", parse_mode="Markdown")

print("🤖 Bot encendido y listo...")
bot.infinity_polling()
