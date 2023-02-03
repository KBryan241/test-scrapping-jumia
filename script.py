import requests
from bs4 import BeautifulSoup
import pyodbc

# conn = pyodbc.connect(
#     'Driver = {ODBC Driver 17 for SQL Server};'
#     'Server = localhost;'
#     'Database = scrappingJumia;'
#     'Trusted_Connection = yes;'
    
# )
# cursor = conn.cursor()
url ="https://www.jumia.ci/"

reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, 'html.parser')
links = soup.find_all("a", class_ = "itm")
lien = []
for link in links:
    b = link.get("href")
    if b is not None : 
        lien.append(b)
        
flink = []
for a in lien:
    url = "https://www.jumia.ci/" + a
    rep2 = requests.get(url)
    if rep2.status_code != 404:
        flink.append(url)

print(flink)
for b in flink :
    url = b
    rep3 = requests.get(url)
    soup1 = BeautifulSoup(rep3.text,'html.parser')
    articles = soup1.find_all("a",class_ = "core")

    for article in articles:
        t = article.get("href")
        

    

    




