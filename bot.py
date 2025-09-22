from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# અહીં તમારો બોટ ટોકન મૂકો
TOKEN = "8227956896:AAGIhSNsreiYfED216x92Wlkvgb-GpaMxa4"

# /start કમાન્ડ
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "નમસ્તે! 🙏 હું તમારો <b>ગુજરાતી Telegram Bot</b> છું.\n"
        "મારે /help લખો મદદ માટે.",
        parse_mode="HTML"
    )

# /help કમાન્ડ
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "<b>સહાય મેનૂ</b>\n"
        "<i>તમે નીચેના કમાન્ડ વાપરી શકો છો:</i>\n"
        "/start – શરૂ કરવા\n"
        "/help – મદદ જોવા\n"
        "/html – HTML ફોર્મેટિંગ ઉદાહરણ",
        parse_mode="HTML"
    )

# /html કમાન્ડ (HTML ટેગ્સ ડેમો)
async def html_demo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "<b>Bold</b>\n"
        "<i>Italic</i>\n"
        "<u>Underline</u>\n"
        "<s>Strikethrough</s>\n"
        "<span class='tg-spoiler'>Spoiler text</span>\n"
        "<a href='https://google.com'>Google Link</a>\n"
        "<code>print('Hello')</code>\n"
        "<pre>for i in range(5):\n    print(i)</pre>",
        parse_mode="HTML"
    )

# મુખ્ય ફંકશન
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("html", html_demo))

    print("Bot ચાલી રહ્યો છે... ✅")
    app.run_polling()

if __name__ == "__main__":
    main()
