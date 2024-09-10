import csv
import datetime
import sqlite3

print("Enter your industry from the following: ")

with open ('data/industries.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(csvreader)
    x = 1
    for row in csvreader:
        print(f"{x}. {(row[0])}")
        x = x + 1

user_choice = int(input("Enter corresponding number here: "))
user_score = 0

with open ('data/industries.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    rows = list(csvreader)
    specific_cell = rows[user_choice][0]
    print(f"You selected {specific_cell} which has a value relevancy of {rows[user_choice][1]}.")
    user_score = rows[user_choice][1]

print(f"Your current score is {user_score}.")