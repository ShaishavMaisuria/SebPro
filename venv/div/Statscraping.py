# scraped data from stats.nba page and got into a csv file
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://basketball.realgm.com/nba/awards/by-type/Player-Of-The-Week/30'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

columns = ['Seasons', 'Player Name', 'Conference', 'Date', 'Team', 'Pos', 'Height'
           ,'Weight', 'Age', 'PreDraftTeam', 'DraftYear', 'YOS']

# dataframe for columns
df = pd.DataFrame(columns=columns)

# particular atrribute for the classs that holds the data of the table
table = soup.find('table', attrs={'class':'tablesaw','data-tablesaw-mode':"swipe"}).tbody
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row, index=columns), ignore_index=True)


df.to_csv('nba player of the week.csv', index=False)