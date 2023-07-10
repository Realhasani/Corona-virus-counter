import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
from sklearn import tree
myask1 = input('Enter 1 for all information, otherwise press enter')
erfan = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database=''
)
my_countery = ['us', 'spain', 'italy', 'India', 'france', 'germany', 'turkey', 'russia', 'iran', 'brazil','peru','chile','israel','japan'
                   ,'morocco','kuwait','finland','malaysia','egypt','australia','panama','belgium','ecuador','sweden','pakistan'
                   ,'chile','singapore','belarus','qatar','romania','ukraine','indonesia','denmark']
x2 = []
y2 = []
x = []
y = []
uq = 1
tedadnoghte = 1
for i in my_countery:
    my_list = []
    my_list3 = []
    my_list2 = []

    m = 0
    get = requests.get('https://www.worldometers.info/coronavirus/country/' + i + "/")
    one = BeautifulSoup(get.text, "html.parser")
    two = one.find_all('h1')
    three = one.find_all('div', attrs={'class': 'maincounter-number'})
    for ii in two:
        m = re.sub('\s+', '', ii.text).strip()
        my_list.append(m)
    for b in three:
        l = re.sub('\s+', '', b.text).strip()
        my_list2.append(l)
    g = len(my_list2)
    Cursor = erfan.cursor()

    a = str(my_list[0])
    b = str(my_list2[0])
    x.append(int(b.replace(',','')))
    c = str(my_list2[1])

    d = str(my_list2[2])
    x.append(int(d.replace(',','')))
        
    x.append(int(c.replace(',', '')))
    x2.append(x[0:2])
    y2.append(x[2])
    print(i, 'cheak')
    print('.' * tedadnoghte)
    Cursor.execute('INSERT INTO database name VALUE(\'%s\',\'%s\',\'%s\',\'%s\')' % (a, b, c, d))  
    erfan.commit()
    my_list.clear()
    my_list2.clear()
    uq = uq + 1
    x.clear()
    tedadnoghte += 1
erfan = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database=''
    )
Cursor = erfan.cursor()
query = 'SELECT * FROM database name'  
Cursor.execute(query)
for (name, coronaviruscases, deaths, recovered) in Cursor:
    a = str(name)
    b = str(coronaviruscases)
    c = str(deaths)
    d = str(recovered)
    if myask1 == '1':
        print('name = ', a, '/', 'corona virus cases = ', b, '/', 'deaths = ', c, '/', 'recovered = ', d)
cif = tree.DecisionTreeClassifier()
cif = cif.fit(x2,y2)
tedad_case_fayal = input('Enter the number of corona patients : ')
tedad_khob_shodegan = input('Enter the number of people who have fully recovered : ')
    
new_data = [[tedad_case_fayal,tedad_khob_shodegan]]
answer = cif.predict(new_data)
print(answer,'will probably die')
erfan.close()