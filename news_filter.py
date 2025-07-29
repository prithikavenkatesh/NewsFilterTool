import requests
import pandas as pd
from datetime import datetime, timedelta

#API Setup
URL = 'https://newsapi.org/v2/everything'

from_date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')