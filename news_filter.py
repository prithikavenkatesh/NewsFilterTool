import requests
import pandas as pd
from datetime import datetime, timedelta
import os
import platform
from config_private import API_KEY
from config_public import KEYWORDS, SELECTED_SOURCES


# Platform-specific imports
if platform.system() == 'Windows':
    import msvcrt
else:
    import fcntl

def is_file_locked(filepath):
    try:
        with open(filepath, 'a') as f:
            if platform.system() == 'Windows':
                msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
                msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
                fcntl.flock(f, fcntl.LOCK_UN)
        return False
    except (OSError, BlockingIOError):
        return True
    except Exception as e:
        print(f"Error checking file lock: {e}")
        return True


# API Setup
URL = 'https://newsapi.org/v2/everything'
from_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

# Error-handling for config files
try:
    from config_private import API_KEY
except ImportError:
    print("Error: config_private.py is missing or API_KEY is not defined.")
    exit(1)
try:
    from config_public import KEYWORDS, SELECTED_SOURCES
    if not KEYWORDS:
        raise ValueError ("KEYWORDS list is empty.")
except ImportError:
    print("Error: config_public.py is missing or variables are not defined.")
    exit(1)
except ValueError as ve:
    print(f"Error: {ve}")
    exit(1)

# Collect articles
articles = []
for keyword in KEYWORDS:
    params = {
        'q' : keyword,
        'from' : from_date,
        'sortBy' : 'relevancy',
        'language' : 'en',
        'apiKey' : API_KEY
    }

    if SELECTED_SOURCES:
        params['sources'] = SELECTED_SOURCES
    
    response = requests.get(URL, params=params)
    data = response.json()

    if data.get('status') != 'ok':
        print(f"Error fetching articles for {keyword}': {data.get('message')} ")
        continue
    
    print(f"Keyword: {keyword} - Found: {len(data.get('articles', []))} articles")
    for article in data.get('articles', []):
        articles.append({
            'Date': article['publishedAt'][:10],
            'Headline' : article['title'],
            'Source' : article['source']['name'],
            'Summary' : article['description'],
            'Link' : article['url']
        })

# Export to Excel with file lock check
output_file = 'filtered_news.xlsx'


try:
    if os.path.exists(output_file) and is_file_locked(output_file):
        print(f"The file '{output_file}' appears to be open or locked. Please close it and try again.")
        exit()

    # Save to Excel
    df = pd.DataFrame(articles)
    df.to_excel(output_file, index=False)
    print(f"Saved {len(articles)} articles to '{output_file}'")
    print(data)
except PermissionError:
    print(f"Permission denied: Unable to write to '{output_file}'. Please close the file if it's opena nd try again.")


