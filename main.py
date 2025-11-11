from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import aiogram
# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Привет 👋", "Помощь ❓"], ["Весёлое сообщение 😄", "Прощай 👋"], ["что я такое?", "фото"], ["перезапуск"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Здравствуй путник!. Выбирай действие:", reply_markup=reply_markup
    )

# Ответ на текстовые сообщения
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "привет" in text:
        await update.message.reply_text("Привет! Рад тебя видеть 😎")
    elif "помощь" in text:
        await update.message.reply_text("Вот что я умею:\n- Привет 👋\n- Весёлое сообщение 😄\n- Прощай 👋")
    elif "весёлое" in text:
        await update.message.reply_text("😆 Вот тебе шутка: Почему программисты любят кофе? Потому что без него код не компилируется!")
    elif "прощай" in text:
        await update.message.reply_text("Пока! 👋 До скорой встречи!")
    elif "что я такое?" in text:
        await update.message.reply_text("Я телеграм бот созданный на коленке за 10 минут на паре по специальности"
                                        "я не принимаю сообщений или сложных комманд, потому что автор ещё лох")
    elif "фото" in text:
        await update.message.reply_text("Фото здесь нет, я ещё не научился)) так что ожидай")
    elif "перезапуск" in text:
        await update.message.reply_text("/start")
    else:
        await update.message.reply_text("Такой команды не существует :( 🤔")

# Основная функция запуска бота
def main():
    TOKEN = "8081410799:AAFprn7ai0QvmKWOJ-hCR7qn1p4AvH4khpE"

    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()