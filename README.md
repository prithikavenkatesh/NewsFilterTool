# 📰 NewsFilterTool

**NewsFilterTool** is a Python-based utility that filters news articles from NewsAPI based on user-defined keywords and sources. It's designed to be simple, customizable, and beginner-friendly.

---

## 🚀 Features

- Filter news articles by keywords
- Optionally restrict results to specific sources
- Easy configuration via Python files
- Secure API key management
- Error handling for missing or malformed config files
- Future support for `.env` files and GUI interface

---

## 🛠️ Setup Instructions

1. **Clone the repository**:
   git clone https://github.com/your-username/NewsFilterTool.git
   cd NewsFilterTool

2. **Install dependencies**:
   pip install -r requirements.txt

3. **Edit the public configuration file**:
Open config_public.py and customize the following:

KEYWORDS: List of topics to filter news by
SELECTED_SOURCES: (Optional) Comma-separated source IDs from NewsAPI (e.g., "bbc-news,cnn")
Example:

KEYWORDS = ["sustainable packaging", "green economy", "climate change"]
SELECTED_SOURCES = "bbc-news"

4. **Edit the private configuration file**
Step 1: Open the file named config_private.py in the root directory.
Step 2: Replace "your_api_key_here" with your actual API key that you can obtain from https://newsapi.org/ .

Optional: To keep your API key private, especially before publishing your project online, you can add config_private.py to your .gitignore file.

5. **Run the tool**:
py news_filter.py

The script will:

- Fetch news articles using the built-in API key
- Filter them based on your keywords and sources
- Export the results to an Excel file


🧯 Error Handling
The script includes basic error handling for:

Missing or empty KEYWORDS list
Malformed values in config files
Clear messages will guide users to fix issues.

📜 License & Credits
This project is developed by Prithika Venkatesh.
News data is sourced via NewsAPI.org.