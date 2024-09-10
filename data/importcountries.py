import csv
import sqlite3

conn = sqlite3.connect('gleiseproject.db')
cursor = conn.cursor()

f = open('countries.txt', 'r')
y = 0

for x in f.readlines():
    cursor.execute('INSERT INTO countries (id, country) VALUES (?, ?)', (y, x))
    y = y + 1

conn.commit()
conn.close()
