import pandas as pd

url = 'https://www.amazon.com/Apple-iPhone-Fully-Unlocked-128/dp/B07P611Q4N'
all_tables = pd.read_html(url)
