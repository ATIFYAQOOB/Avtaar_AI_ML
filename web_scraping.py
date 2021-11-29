from bs4 import BeautifulSoup
import requests
import datetime 
import csv

def wiki(html_txt):
    list = []
    soup = BeautifulSoup(html_txt,'lxml')
    movie_name = soup.find('th',class_ = 'infobox-above summary').text
    #print(f"Movie Name : {movie_name}\n")
    list.append(movie_name)
    director_name = soup.find('td', class_ = 'infobox-data').text
    #print(f"Diector Name : {director_name}\n")
    list.append(director_name)
    a =[]
    for li in soup.find_all('div', class_ = 'plainlist'):
        release_date = li.find('li').text
        a.append(release_date)
    date = max(a,key =len).replace("\xa0"," ")
    #print(date)
    list.append(date)
    earning = soup.find_all('td', class_ = 'infobox-data')
    b =[]
    for i in earning:
        b.append(i.text)
    #print(f"The over all earning is:{b[-1][:-3]}\n")
    list.append(b[-1][:-3])
    cast = soup.find('div', class_ = 'div-col').text
    #print(F"Cast \n {cast}")
    cast =cast.replace("\n",'##')
    list.append(cast)
    s = ",".join(list)
    s = str(s)
    
    with open("assignment_2.csv","a") as f:
          f.write(s)
          f.write("\n")
    
header = ['Movie_name','Director_name','Release_date','Overall_gross_earning','The_cast']
with open('assignment_2.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
html_txt1 = requests.get('https://en.wikipedia.org/wiki/Real_Steel').text
wiki(html_txt1)

html_txt2 = requests.get('https://en.wikipedia.org/wiki/Twilight_(2008_film)').text
wiki(html_txt2)

html_txt3 = requests.get('https://en.wikipedia.org/wiki/Home_Alone').text
wiki(html_txt3)

html_txt4 = requests.get('https://en.wikipedia.org/wiki/Predator_(film)').text
wiki(html_txt4)

html_txt5 = requests.get('https://en.wikipedia.org/wiki/The_Girl_with_All_the_Gifts_(film)').text
wiki(html_txt5)
