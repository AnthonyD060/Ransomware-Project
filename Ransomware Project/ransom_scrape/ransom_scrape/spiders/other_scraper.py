from bs4 import BeautifulSoup as b 
import requests
import re 
import os

def scrape_ABC():

    source = requests.get("https://www.nbcnews.com/tech/cyber-security").text 

    soup = b(source, 'lxml')

    headlines = soup.find_all('h2')

    for h in headlines:
        print(h.text)

    print(soup.find('h2', class_="tease-card__headline tease-card__title tease-card__title--news relative").find('a', attrs={'href': re.compile("^https://")}).get('href'))

    links = []

    for headline in headlines:

        try:
            link = headline.find('a', attrs={'href': re.compile("^https://")}).get('href')

            links.append(link)
        except:
            pass

    print(links)

    os.chdir(fr"C:/Users/{os.getlogin()}/Documents/Articles/NBC")

    for link in links:

        paragraphs = []

        try:
            source = requests.get(link).text

            soup = b(source, 'lxml')

            headline = soup.find("h1", class_='article-hero-headline__htag').text

            ps = soup.find('div', class_='article-body__content').find_all('p')   

            for paragraph in ps:
                paragraphs.append(paragraph.text)

            with open(f'{headline}.txt', 'w+') as f:
                for p in paragraphs:
                    f.write(p)

            paragraphs.clear()
        

        except:
            pass

    
def scrape_top10():

    source = requests.get("https://searchsecurity.techtarget.com/feature/The-biggest-ransomware-attacks-this-year").text 

    soup = b(source, 'lxml')

    attacks = soup.find_all("section", class_="section main-article-chapter")

    os.chdir(fr'C:/Users/{os.getlogin()}/Documents/Articles/search_sec_top10')

    for attack in attacks:
        headline = attack.find("h3").text

        paragraphs = attack.find_all('p')

        headline = headline [3:].strip()

        with open(f'{headline}.txt','w+') as f:
            for ps in paragraphs:
                f.write(ps.text)

scrape_top10()
