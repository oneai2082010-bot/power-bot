from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN", "9047328284:AAGwbhOK_plflLsJ6_MRa_zG00I2-c4jor4")

def get_start_text(name):
    return f"أهلا، {name} 👋\n~ ابدأ البحث واحصل على معلومات مستخدمي NFT\n~ استخدم المساعدة لرؤية الأوامر"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("بروفايل NFT 👤", callback_data="nft"), InlineKeyboardButton("كشف محفظة 📄", callback_data="wallet")],
        [InlineKeyboardButton("تحويل عملات 🔄", callback_data="convert"), InlineKeyboardButton("أسعار العملات ₿", callback_data="prices")],
        [InlineKeyboardButton("أكواد الكاش 💵", callback_data="cash"), InlineKeyboardButton("تعزيز ⚡", callback_data="boost")],
        [InlineKeyboardButton("النجوم ⭐", callback_data="stars"), InlineKeyboardButton("بريميوم ☐", callback_data="premium")],
        [InlineKeyboardButton("تتبع محفظة 📄", callback_data="track"), InlineKeyboardButton("شبكات ☐", callback_data="networks")],
        [InlineKeyboardButton("مساعدة 📖", callback_data="help"), InlineKeyboardButton("رجوع ↩️", callback_data="back")],
    ]
    markup = InlineKeyboardMarkup(keyboard)
    name = update.effective_user.first_name
    await update.message.reply_text(get_start_text(name), reply_markup=markup)

async def btn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    await q.message.reply_text(f"دوسـت على: {q.data}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(btn))
    app.run_polling()

if __name__ == "__main__":
    main()
