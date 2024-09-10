import csv
import sqlite3

conn = sqlite3.connect('gleiseproject.db')
cursor = conn.cursor()

with open ('data/industries.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(csvreader)
    for row in csvreader:
        industry_name = row[0]
        relevancy = row[1]
        cursor.execute('INSERT INTO industry (industry_name, relevancy) VALUES (?, ?);', (industry_name, relevancy))
        
conn.commit()
conn.close()