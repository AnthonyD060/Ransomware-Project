from matplotlib import pyplot as plt 
import random
import re 
import os
import time
from collections import Counter as counta

def get_data():

    
    data = re.compile(r"\[(.*?)\]")

    term = re.compile(r'\w+.*')

    path = fr'C:/Users/{os.getlogin()}/Documents/Articles'

    os.chdir(path)

    companies_with_money_taken = {
        "company":[],
        "hq":[],
        "industry":[],
        "money taken":[]
    }


    for folder in os.listdir(os.getcwd()):
        os.chdir(f'{path}/{folder}')

        with open('zz results.txt', 'r') as f:
                      
            for line in f:
                if data.finditer(line):
                    comp = []

                    for f in data.finditer(line):

                        d = f.group()

                        if term.finditer(d):
                            for t in term.finditer(d):
                                a = t.group()
                                comp.append(a[:-2])
                    try:
                        if len(comp) == 4:
                            companies_with_money_taken['company'].append(comp[0])
                            companies_with_money_taken['hq'].append(comp[1])
                            companies_with_money_taken['industry'].append(comp[2])
                            companies_with_money_taken['money taken'].append(comp[3])

                    except:
                        pass                
    
    res = ['CNA']
    for i in companies_with_money_taken['company']:
        index = companies_with_money_taken['company'].index(i)
        if i not in res:
            res.append(i)
        else:
            companies_with_money_taken['company'].pop(index)
            companies_with_money_taken['hq'].pop(index)
            companies_with_money_taken['industry'].pop(index)
            companies_with_money_taken['money taken'].pop(index)
    comps, hqs, industries, money = companies_with_money_taken['company'],companies_with_money_taken['hq'],companies_with_money_taken['industry'],companies_with_money_taken['money taken']
    actual_money = []
    for m in money:
        index = money.index(m)
        ir = m[:3]
        actual_money.append(float(ir))
    Output = sorted(actual_money, key = lambda x:float(x))
    indexes = []
    for i in Output:
        g = actual_money.index(i)
        indexes.append(g)
        l=random.randint(0,100000)
        actual_money[g]=l
    comps_output = []
    industries_output = []
    hqs_output = []

    for i in indexes:
        comps_output.append(comps[i])
        hqs.append(hqs[i])
        industries_output.append(industries[i])
    def plot_money():
        plt.figure(figsize=(15.0,10.0))
        plt.bar(comps_output, Output)
        plt.title('money taken or demanded by ransomware groups from companies recently')
        plt.xlabel('companies')
        plt.ylabel('money taken (millions)')
        plt.xticks(fontsize = 10.0,rotation=45)
        fileName = (time.asctime(time.localtime(time.time()))).replace(':','')
        plt.savefig(fr"C:/Users/{os.getlogin()}/Documents/Ransomware Project/plots/money/{fileName}.png")
        
    def plot_industries():
        count = counta(industries_output)
        plt.figure(figsize=(15.0,10.0))
        plt.bar(count.keys(), count.values())
        plt.title('the industries affected')
        plt.ylabel('how many companies attacked were apart of this industry')
        plt.xlabel('the industry')
        plt.xticks(fontsize = 10,rotation=45)
        fileName = (time.asctime(time.localtime(time.time()))).replace(':','')
        plt.savefig(fr'C:/Users/{os.getlogin()}/Documents/Ransomware Project/plots/industry/{fileName}.png')
    plot_money()
    plot_industries()
