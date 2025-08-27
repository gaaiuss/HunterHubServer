# Tutorial https://www.youtube.com/watch?v=Qd8JT0bnJGs
import re

import requests
from bs4 import BeautifulSoup

url = 'http://localhost:8000/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# if parsed_html.title is not None:
# print(parsed_html.title.text)

the_apex_title = parsed_html.select_one('#apex > div > h2')
if the_apex_title is not None:
    # print(the_apex_title.text)
    article = the_apex_title.parent
    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1}', ' ', p.text).strip())
