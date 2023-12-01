from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# IMP NOTE: The page at the given URL is maintained by "wikipedia", which might be updated in future, hence the current data might be different.
# Perform data scraping from scratch with HTML Tags/Class Names!


# Task oneURLto Scrape Data
url = ''

# Get url  using requests
page = 

# Parse Page
soup = 

# Get <table> with class = 'wikitable sortable'
star_table = soup.find_all('table', {"class":"wikitable sortable"})

total_table = len(star_table)


temp_list= []


table_rows = star_table[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

#  creste empty list with the name of Stars_names=[],Distance=[],Mass=[],Radius=[]

print(temp_list)

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

# Convert to CSV
headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

# save it as dwarf_stars.csv

