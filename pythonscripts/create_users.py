import sqlite3
import bcrypt
import getpass

def hash_password(plain_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed_password

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

# CONFIRM USERNAME
username = ' '
username_confirm = '_'
plain_password = ' '
plain_password_confirm = '_'

while username != username_confirm:
    username = input('Please enter username: ')
    username_confirm = input('Confirm username: ')
    if (username != username_confirm):
        print('Did not match.')

# CONFIRM PASSWORD
while plain_password != plain_password_confirm:#
    plain_password = getpass.getpass('Please enter a password: ')
    plain_password_confirm = getpass.getpass('Please confirm the password: ')
    if (plain_password != plain_password_confirm):
        print('Incorrect confirmation, retry.')

#HASH PASSWORD
secure_password = hash_password(plain_password)
print(f"Hashed password: {secure_password}")

conn = sqlite3.connect('../data/gleiseproject.db')
cur = conn.cursor()

cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, secure_password))


cur.close()
conn.commit()
conn.close()

