import sqlite3
import sys

def contains_word(string, word):
    return word in string

conn = sqlite3.connect('../data/gleiseproject.db')
cur = conn.cursor()

decision = 0

cur.execute("SELECT id FROM signee")
signees = cur.fetchall()

# CYCLE THROUGH SIGNEE DATA

for row in signees:
    # IDENTIFY ID OF SIGNEE
    signee_id = int(row[0])

    # EXECUTE QUERY TO FIND RELEVANCY OF THEIR ROLE INDUSTRY
    cur.execute("SELECT relevancy FROM industry WHERE industry_name IN (SELECT industry FROM signee_professional_information WHERE signee_id = ?)", (signee_id,))
    industry_relevancy_marker = cur.fetchone()
    industry_relevancy = int(industry_relevancy_marker[0])

    # GET GENERAL SIGNEE DATA FROM SIGNEE TABLE
    cur.execute("SELECT first_name, surname FROM signee WHERE id = ?",(signee_id,))
    signee_data = cur.fetchall()
    first_name = signee_data[0][0]
    surname = signee_data[0][1]

    # GET PROFESSIONAL INFO
    cur.execute("SELECT job_title FROM signee_professional_information WHERE signee_id = ?", (signee_id,))
    job_title_lower = str(cur.fetchone())
    job_title = job_title_lower.upper()

    # PERFORM CHECKS TO ENSURE DATA IS RETURNED
    if signee_data:
        signee_name = first_name + " " + surname
        print(f"Signee: {signee_name}")
    else:
        print("Error: ID not found in database.")
        sys.exit()

    # PERFORM CHECKS TO ENSURE INDUSTRY RELEVANCY IS RETURNED
    if industry_relevancy:
        print(f"Industry relevancy for {signee_name} is: {industry_relevancy}")
    else:
        print(f"No industry relevancy found for {signee_id}")

    # GET SALARY DATA AND PERFORM CHECKS TO ENSURE DATA IS RETURNED
    cur.execute("SELECT salary FROM signee_professional_information WHERE signee_id = ?", (signee_id,))
    salary_list = cur.fetchone()
    salary = float(salary_list[0])
    print(salary)

    if salary:
        print(f"Salary: {salary}")
    else:
        print(f"No salary found for {signee_id}")

    # CALCULATE SCORE
    prs = float(salary * industry_relevancy)
    print(f"Value of prs is {prs}")

    # GET ROLE MULTIPLIER DATA
    cur.execute("SELECT * FROM role_multipliers")
    role_multipliers = cur.fetchall()

    # SET PRS SCORE MULTIPLIER INITIALISE

    # MULTIPLY WHERE WORDS APPEAR IN THEIR ROLE
    for row in role_multipliers:
        if contains_word(job_title, row[1]) == 1:
            multiplier = float(row[2])
            prs = float(prs * multiplier)
            print(f"Match found for {row[1]}")
        else:
            print(f"No match found for {row[1]}")

    cur.execute("UPDATE signee SET prs = ? WHERE id = ?", (prs, signee_id))
    score = prs * 0.001
    cur.execute("UPDATE signee SET score = ? WHERE id = ?", (score, signee_id,))


conn.commit()
cur.close()
conn.close()