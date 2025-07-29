import requests
import pandas as pd
from datetime import datetime, timedelta

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