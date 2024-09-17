from flask import Flask, render_template, request
import sqlite3
import bcrypt

def hash_password(plain_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed_password

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':

        # create a reader of the industry table from sqlite3
        
        # connect to the database + create object 'conn'
        conn = sqlite3.connect('data/gleiseproject.db')

        # create a cursor object for navigating db
        cur = conn.cursor()

        # select our table that we want
        cur.execute("SELECT industry_name FROM industry")

        # return all rows and fetch into variable industry_rows
        industry_rows = cur.fetchall()

        # select new table
        cur.execute("SELECT country FROM countries")

        # fetch countries into variable
        countries = cur.fetchall()

        # close connection
        conn.close()

        return render_template('signup.html', industries=industry_rows, countries=countries)
    
    elif request.method == 'POST':
        # create objects for all user inputs
        first_name = request.form['firstName']
        surname = request.form['lastName']
        email = request.form['email']
        dob = request.form['dateOfBirth']
        country = request.form['country']
        industry = request.form['industry']
        job_title = request.form['job_title']
        salary = request.form['salary']

        # connect to database
        conn = sqlite3.connect('data/gleiseproject.db')
        cur = conn.cursor()

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
        conn.close()
        return render_template('index.html')


@app.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')

@app.route("/planet")
def planet():
    return render_template("planet.html")

@app.route("/project")
def project():
    return render_template("project.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        #
        username = request.form['username']
        password = hash_password(request.form['password'])
        #
        conn = sqlite3.connect('data/gleiseproject.db')
        cur  = conn.cursor()
        #
        cur.execute('SELECT username FROM users WHERE username = ?', (username,))
        username_validation = str(cur.fetchone()[0])
        cur.execute('SELECT password FROM users WHERE username = ?', (username,))
        password_validation = str(cur.fetchone()[0])
        #
        if password == password_validation:
            render_template('user_index.html')

@app.route("/user_index")
def user_index():
    return render_template('user_index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
