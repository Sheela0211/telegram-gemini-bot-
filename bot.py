from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from pymongo import MongoClient

# MongoDB setup
client = MongoClient("mongodb_url")
db = client["telegram_bot"]
users_collection = db["users"]

async def start(update: Update, context):
    user = update.message.from_user
    user_data = {
        "first_name": user.first_name,
        "username": user.username,
        "chat_id": update.message.chat_id
    }
    users_collection.insert_one(user_data)
    await update.message.reply_text("Welcome! Please share your phone number using the contact button.")
