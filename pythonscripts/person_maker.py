import sqlite3
import csv
import random

conn = sqlite3.connect('../data/gleiseproject.db')
cur = conn.cursor()

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

# MAKE RANDOM DOB
year = random.randrange(1960, 2024)
month = random.randrange(1, 12)
if month == (1, 3, 5, 7, 8, 10, 12):
    day = random.randrange(1 , 31)
elif month == (4, 6, 9, 11):
    day = random.randrange(1, 30)
else:
    day = random.randrange(1, 28)

day_formatted = str(day).zfill(2) # make it always appear as double digits
month_formatted = str(month).zfill(2) # ditto

print(f"DOB: {day_formatted}-{month_formatted}-{year}")

year_string = str(year)
dob = day_formatted + '-' + month_formatted + '-' + year_string

# GRAB A COUNTRY
selector = random.randrange(0, 195)    
cur.execute("SELECT country FROM countries WHERE id = ?", (selector,))
countries = cur.fetchone() # Produces a singular row
country = countries[0] # Grab the cell we want
print(f"Country: {country}")

# MAKE AN EMAIL
year_str = str(year)
year_slice = (year_str[2:])
email = first_name + surname + year_slice +"@glieseproject.org"
print(f"Email: {email}")

# SELECT AN INDUSTRY
selector = random.randrange(1, 20)
cur.execute("SELECT industry_name FROM industry WHERE id = ?", (selector,))
industry_exc = cur.fetchone()
industry = industry_exc[0]
print(f"Industry: {industry}")

# JOB TITLE
# Prefix: No prefix, senior, head, VP, CEO
selector = random.randrange(1, 5)
prefix = ''
if selector == 1:
    prefix = ' '
elif selector == 2:
    prefix = 'Senior'
elif selector == "3":
    prefix = 'Head'
elif selector == "4":
    prefix = 'VP'
elif selector == "5":
    prefix = 'CEO'
# Secondary Title
if selector < 5 and selector > 1:
    selector = random.randrange(1, 100)
    cur.execute("SELECT role_name FROM roles WHERE id = ?", (selector,))
    role_row = cur.fetchone()
    role = str(role_row[0])
    job_title = prefix + ' ' + role
elif selector == 1:
    selector = random.randrange(1, 100)
    cur.execute("SELECT role_name FROM roles WHERE id = ?", (selector,))
    role_row = cur.fetchone()
    role = str(role_row[0])
    job_title = role
elif selector == 5:
    job_title = prefix

print(f"Job title: {job_title}")

# SALARY MAKER
if 'CEO' in job_title:
    salary_int = random.randrange(100000, 9999999999)
    salary = float(salary_int)
elif 'VP' in job_title:
    salary_int = random.randrange(75000, 5000000)
    salary = float(salary_int)
elif 'Head' in job_title:
    salary_int = random.randrange(40000, 250000)
    salary = float(salary_int)
elif 'Senior' in job_title:
    salary_int = random.randrange(30000, 96000)
    salary = float(salary_int)
else:
    salary_int = random.randrange(25000, 75000)
    salary = float(salary_int)

# INDUSTRY MULTIPLIERS
if 'Scientific' in industry:
    salary = salary * 1.25
elif 'Technology' in industry:
    salary = salary * 1.2
elif 'Finance' in industry:
    salary = salary * 1.5

print(f"Salary: {salary}")

# add the information to database
cur.execute('INSERT INTO signee (first_name, surname, email, dob) VALUES (?, ?, ?, ?)', (first_name, surname, email, dob))
# grab the generated signee id
cur.execute('SELECT id FROM signee WHERE email = ? ', (email,))
signee_id = cur.fetchone()[0]
# include signee id to link table
cur.execute('INSERT INTO signee_country (signee_id, country) VALUES (?, ?)', (signee_id, country))
# signee professional information
cur.execute('INSERT INTO signee_professional_information (signee_id, industry, job_title, salary) VALUES (?, ?, ?, ?)', (signee_id, industry, job_title, salary))
# close the connection

conn.commit()
cur.close()
conn.close()