from bs4 import BeautifulSoup
import requests
import urllib.request

url = 'https://basketball.realgm.com/nba/awards/by-type/Player-Of-The-Week/30'


headers = {"User-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
page = requests.get(url, headers =headers)


soup = BeautifulSoup(page.content, 'html.parser')

tableContent = soup.find_all("td")
#, {"nowrap class":"tablesaw-cell-persist"})


text=""
for td in tableContent:
    #print(str(td))
    '''if(td['class']== 'tablesaw-cell-persist'):
        print (td)'''
   # soup.find("table", {"class": "GroupBox3"}

    if((str(td.text)=="Eddie Johnson, Jr.") and (count==0)):
        text=str(td) +"\n"
        count=1;
        print("Eddie Johnson")
identify='href="'
finish='">'
s = text

def find_between(s, first, last):
        if not (s.__contains__(first)):
            return ""
        else:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            str = s[start:end]

        return  str

link = find_between(s, identify, finish)
print("https://basketball.realgm.com" + link)


