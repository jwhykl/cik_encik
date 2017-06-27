#scrape KLSE
import requests
from bs4 import BeautifulSoup
import pandas as pd
import string
import re

main_link = 'http://www.malaysiastock.biz/Listed-Companies.aspx'
page = requests.get(main_link)

soup = BeautifulSoup(page.content, 'html.parser')
body = soup.find('table',id='MainContent_tStock')

zero_to_nine ='http://www.malaysiastock.biz/Listed-Companies.aspx?type=A&value=0'
#companies_a = 'http://www.malaysiastock.biz/Listed-Companies.aspx?type=A&value=A'
companies_alphbet = 'http://www.malaysiastock.biz/Listed-Companies.aspx?type=A&value='
all_links = [zero_to_nine]
for i in string.ascii_uppercase:
    new_list = companies_alphbet+i
    all_links.append(new_list)
    

all_companies =[]
regex = re.compile(".*?\((.*?)\)")

for alink in all_links:
    main_link = alink#'http://www.malaysiastock.biz/Listed-Companies.aspx'
    page = requests.get(main_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find('table',id='MainContent_tStock')
    for tr in body.find_all('tr')[2:]:
        tds = tr.find_all('td')
        #print "Company: %s, Category: %s, Market Cap: %s, Last Price: %s, PE: %s, DY: %s, ROE: %s" % \
        #      (tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text)
        #print (tds[0].a['href'])
        all_companies.append([re.sub('\(.*?\)','',tds[0].a.text),tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text,tds[0].a['href'],re.findall('\d+',tds[0].a.text)[0]])

    
#print(all_companies)
df = pd.DataFrame(all_companies, columns=('EQUITY','COMPANY','CATEGORY','MARKET CAP','LAST PRICE','PE', 'DY', 'ROE', 'LINK', 'NUMBER'))

df.to_csv("C:\\Users\\J-Why\\Desktop\\Projects\\Python\\KLSE_Trade\\Results\\All_Bursa.csv", index=False)

    

    
    
    
    #for bd in body:
#    full_bd = bd.find('tr')
#    print (full_bd)

#print body

#full_bd = body.find('tr')
#print(full_bd)

#full_bd = body.find('tr') 
#print(full_bd)

#for bd in full_bd: 
#    print(bd)
#    print("     ")
    #td_chose = full_bd.select('td')
    #pie = [pp.get_text() for pp in td_chose]
    #print(pie)
    
    
    #for fbd in full_bd:
    #    pie = fbd.find('td').text
    #    print (pie)
    #    print "     "

