import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8888202399:AAFwdWrj114id-ARauxYl4v8ScdCiV7rNLA")
ORDER_URL = os.environ.get("ORDER_URL", "https://b2b.moysklad.ru/public/Bya8IC3N6odI")

MATN = """
🎬 Mahsulot haqida batafsil ma'lumot!

✅ Sifatli mahsulot
✅ Tez yetkazib berish  
✅ Qulay narx

Qo'shimcha savollar bo'lsa, bog'laning!
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 Buyurtmani boshlang", url=ORDER_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Faylni topish
    base_dir = os.path.dirname(os.path.abspath(__file__))
    video_path = os.path.join(base_dir, "IMG_0224.mp4")
    
    print(f"Video path: {video_path}")
    print(f"File exists: {os.path.exists(video_path)}")
    print(f"Files in dir: {os.listdir(base_dir)}")

    with open(video_path, "rb") as video_file:
        await update.message.reply_video(
            video=video_file,
            caption=MATN,
            reply_markup=reply_markup,
        )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot ishga tushdi ✅")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
