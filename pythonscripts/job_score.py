import sqlite3
import sys

conn = sqlite3.connect('../data/gleiseproject.db')
cur = conn.cursor()

with open("../sqlscripts/get_all_customer_info.sql", "r") as sql_file:
    sql_script = sql_file.read()

cur.execute(sql_script)

signee_data = cur.fetchall()

for row in signee_data:
    # (salary * job_score * job_title(seniority)) / 1000
    score = (row[5] * row[6]) / 1000
    print(f"Score for {row[1]} {row[2]}: {score}")

cur.close()
conn.close()



