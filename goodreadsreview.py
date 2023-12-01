import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

r = requests.get('https://www.goodreads.com/book/show/24280/reviews?reviewFilters={%22workId%22:%22kca://work/amzn1.gr.work.v1.EK63uPAFrpWdWht9Sig4Tw%22,%22languageCode%22:%22en%22,%22after%22:%22MjA3NDEsMTU3NTE4MjEyMTAwNw%22}', headers= headers)

soup = BeautifulSoup(r.content, 'html.parser')

reviews =soup.find_all('article', class_='ReviewCard')
# print(reviews)
review_list=[]

for review in reviews:
    # Use find within each individual review element
    review_text = review.find('span', class_='Formatted').text
    review_list.append(review_text)

d = {'Reviews':review_list}
df = pd.DataFrame(data=d, index=range(1, len(review_list) + 1))
df.to_csv('scrape reviews of each book/Les_Miserables.csv', index= True)



