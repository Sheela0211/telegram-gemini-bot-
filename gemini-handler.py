import google.generativeai as genai

genai.configure(api_key="your_gemini_api_key")
model = genai.GenerativeModel('gemini-pro')

async def chat(update: Update, context):
    user_input = update.message.text
    response = model.generate_content(user_input)
    await update.message.reply_text(response.text)
    # Save chat history to MongoDB
    chat_history = {
        "user_input": user_input,
        "bot_response": response.text,
        "timestamp": datetime.now()
    }
    db["chat_history"].insert_one(chat_history)
