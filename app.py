from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import check_password_hash
import sqlite3
import bcrypt
from flask_session import Session 

def hash_password(plain_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed_password

def verify_password(plain_password, hashed_password):
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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
        session.clear()
        return render_template("login.html")
    elif request.method == 'POST':
        #
        username = request.form['username']
        password = request.form['password']
        #
        conn = sqlite3.connect('data/gleiseproject.db')
        cur  = conn.cursor()
        #
        cur.execute('SELECT username FROM users WHERE username = ?', (username,))
        username_validation = (cur.fetchone()[0])
        cur.execute('SELECT password FROM users WHERE username = ?', (username,))
        hashed_password = (cur.fetchone()[0])
        #
        if verify_password(password, hashed_password):
            cur.execute('SELECT id FROM users WHERE username = ?', (username,))
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('admin'))

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        if not session.get('logged_in'):
            session.clear()
            return render_template('login.html')
        return render_template('admin.html', username=session.get('username'))
    
@app.route("/config", methods=['GET', 'POST'])
def config():
    if request.method == 'GET':
        conn = sqlite3.connect('data/gleiseproject.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        return render_template('config.html', users=users)
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)
        conn = sqlite3.connect('data/gleiseproject.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password,))
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        conn.commit()
        conn.close()
        return render_template('config.html', users=users)
    
@app.route('/delete_user', methods=['POST'])
def deleteuser():
    conn = sqlite3.connect('data/gleiseproject.db')
    cur = conn.cursor()
    user_id = request.form.get('user_id')
    cur.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('config'))


@app.route('/signee', methods=['GET', 'POST'])
def signee():
    conn = sqlite3.connect('data/gleiseproject.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM successful_signee_view')
    successful_signees = cur.fetchall()
    return render_template('signee.html', successful_signees=successful_signees)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
