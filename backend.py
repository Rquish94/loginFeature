import sqlite3
from flask import Flask
import time
from passlib.hash import pbkdf2_sha256

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('frontendLoginPage.html')


@app.route('/next', methods=['GET', 'POST'])
def addNew():
    user = request.form['username']
    password = request.form['password']
    myHash = pbkdf2_sha256.encrypt("",rounds=2000, salt_size=16)
    print(user,password,myHash)
    print('Processing')
    time.sleep(2)
    checkinput =input('What is your Password?')
    if pbkdf2_sha256.verify(checkinput, myHash) ==True:
        print("YASSS")
    else:
        print("BOO")



if __name__ == '__main__':
    app.run()
# conn = sqlite3.connect('defnotpasswords.db')
# c = conn.cursor()
# c.execute('''CREATE TABLE usernames
#              (date text, trans text, symbol text, qty real, price real)''')

