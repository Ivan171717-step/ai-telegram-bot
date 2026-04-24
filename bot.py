from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

from config import TELEGRAM_TOKEN
from llm import chat_with_ai
from search import web_search


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()

    if "найди" in user_text or "поиск" in user_text or "что такое" in user_text:
        results = web_search(user_text)
        prompt = f"""
Запрос: {user_text}

Результаты:
{results}

Ответ с сарказмом и комментариями.
"""
        reply = chat_with_ai(prompt)
    else:
        reply = chat_with_ai(user_text)

    await update.message.reply_text(reply)


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot started (polling)")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()