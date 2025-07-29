import requests
import pandas as pd
from datetime import datetime, timedelta
from config_private import API_KEY
from config_public import KEYWORDS, SELECTED_SOURCES

# API Setup
URL = 'https://newsapi.org/v2/everything'

from_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')

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

# Export to Excel 

output_file = 'filtered_news.xlsx'

df = pd.DataFrame(articles)
df.to_excel(output_file, index=False)
print(f"Saved {len(articles)} articles to '{output_file}'")
print(data)