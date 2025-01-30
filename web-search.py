import requests

async def web_search(update: Update, context):
    query = " ".join(context.args)
    search_url = f"https://api.serpapi.com/search?q={query}&api_key=your_serpapi_key"
    response = requests.get(search_url).json()
    summary = model.generate_content(f"Summarize this: {response['snippet']}")
    await update.message.reply_text(f"Summary: {summary.text}\nTop Link: {response['link']}")
