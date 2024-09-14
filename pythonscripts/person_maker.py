import sqlite3
import csv
import random

# conn = sqlite3.connect('../data/gleiseproject.db')
# cur = conn.cursor()

x = random.randrange(1, 258001)

# GENERATE A NAME
with open ('../data/first-names.csv', mode='r') as first_names:
    csv_reader = csv.reader(first_names)
    rows = list(csv_reader)
    selected_row = rows[x][1]
    first_name = rows[x][1]

y = random.randrange(1, 100)

with open ('../data/last-names.csv', mode='r') as last_names:
    csv_reader = csv.reader(last_names)
    rows = list(csv_reader)
    selected_row = rows[y][0]
    surname = rows[y][0]
    
print (first_name + " " + surname)

month = random.randrange(1, 12)





# cur.close()
# conn.close()