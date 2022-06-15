from bs4 import BeautifulSoup as b 
import os 
from string import punctuation
import pandas as pd
import re
import time

def scrape_files():

    groups = [
    'REvil',
    'Conti',
    'Darkside',
    'CLOP',
    'Egregor',
    'DoppelPaymer',
    'Babuk',
    'Ragnar',
    'Astro',
    'Hotarus',
    ]

    money = re.compile(r"\$[0-9]+(\.[0-9]+)?\s?(million|billion|thousand)", flags=re.I)


    companies_table = pd.read_csv(fr"C:/Users/{os.getlogin()}/Documents/Ransomware Project/table-1.csv")

    companies = list(companies_table["Name"])
    industries = list(companies_table["Industry"])
    states = list(companies_table["Headquarters"])


    path = fr"C:/Users/{os.getlogin()}/Documents/Articles"


    os.chdir(path)

    for folder in os.listdir(path):
        print('\n')
        print(f"files from {folder} folder\n")

        os.chdir(f'{path}/{folder}')

        try:
            with open('zz results.txt', 'a') as f:
                f.write(f"\nlogged on {time.asctime(time.localtime(time.time()))}\n")
                f.write("\n")

        except:
            pass

        for files in os.listdir(f"{path}/{folder}/"):

            if files == "zz results.txt":
                pass

            else:
                
                if ".txt" in files:

                    fn, ext = files.split(".txt")

                    try:

                        with open(files, 'r', encoding="utf8", errors="ignore") as f:

                            content = f.read()

                            words = content.strip(punctuation).split(" ")

                            group_responsible = ''

                            companies_affected = {
                                "Company":[],
                                "States":[],
                                "Industry":[],
                                "Money Taken":[]
                            }

                            match = money.finditer(content)

                            

                            for word in words:
                                
                                if fn in companies and fn not in companies_affected['Company']:
                                    index = companies.index(fn)
                                    companies_affected["Company"].append(fn)
                                    companies_affected["States"].append(states[index])
                                    companies_affected["Industry"].append(industries[index])


                                    print(f'companies affected:{companies_affected}')
                                    print(f'the group responsible: {group_responsible}')
                                    
                                    try:
                                        moneys = ''
                                        for m in match:
                                            if m.group() in moneys:
                                                pass
                                            else:
                                                moneys+=m.group()
                                                moneys+=','
                                        moneys.strip()
                                        if "," in moneys:
                                            moneys = moneys.split(",")
                                            moneys = moneys[0]
                                        
                                        companies_affected['Money Taken'].append(moneys)


                                    except:
                                        pass
                                    print('')

                                elif word in companies and word not in companies_affected['Company']:
                                    index = companies.index(word)
                                    companies_affected["Company"].append(word)
                                    companies_affected["States"].append(states[index])
                                    companies_affected["Industry"].append(industries[index])


                                    print(f'companies affected:{companies_affected}')
                                    print(f'the group responsible: {group_responsible}')

                                    try:
                                        moneys = ''
                                        for m in match:
                                            if m.group() in moneys:
                                                pass
                                            else:
                                                moneys+=m.group()
                                                moneys+=','
                                        moneys.strip()
                                        
                                        if "," in moneys:
                                            moneys = moneys.split(",")
                                            moneys = moneys[0]
                                        companies_affected['Money Taken'].append(moneys)

                                            
                                    except:
                                        pass
                                    print('')



                                if word in groups:
                                    group_responsible = word

                            print(f'{os.getcwd()}/{files}\n')


                            with open('zz results.txt', 'a') as results:
                                results.write(f'{os.getcwd()}/{files}\ncompanies affected:{companies_affected}\nthe group responsible: {group_responsible}\n')

                    except FileNotFoundError as r:
                        print(r)
