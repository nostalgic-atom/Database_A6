# from crypt import methods
import re
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import random

app = Flask(__name__)

#db = yaml.load(open('db.yaml'))

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Rahul@1999'
app.config['MYSQL_DB'] = 'banking_system'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        customer_id = random.randint(100, 500)
        first_name = userDetails['firstname']
        last_name = userDetails['lastname']
        customer_street = userDetails['street']
        customer_city = userDetails['city']

        account_type = userDetails['flexRadioDefault']
        account_number = random.randint(10000000000, 99999999999)
        card_number = random.randint(1000000000000000, 9999999999999999)

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO CUSTOMER(customer_id, first_name, last_name, customer_street, customer_city) VALUES(%s, %s, %s, %s,%s)",
                    (customer_id, first_name, last_name, customer_street, customer_city))
        cur.execute("INSERT INTO ACCOUNT(account_number, card_number, account_type) VALUES (%s, %s, %s)", (account_number,card_number, account_type))
        mysql.connection.commit()
        cur.close()

        
        return redirect(url_for('home', customer_id = customer_id))

    return render_template('signup.html')

@app.route('/home/<customer_id>', methods=['GET','POST'])

def home(customer_id):

    if request.method == 'POST':
        updateDetails = request.form
        first_name = updateDetails['firstname']
        last_name = updateDetails['lastname']
        customer_street = updateDetails['street']
        customer_city = updateDetails['city']


        cur = mysql.connection.cursor()
        cur.execute("update customer set first_name=%s, last_name=%s, customer_street=%s, customer_city=%s where customer_id = '"+customer_id+"'",(first_name,last_name,customer_street,customer_city))
        mysql.connection.commit() 
        cur.close()

    cur = mysql.connection.cursor()
    cur.execute("select customer_id, first_name, last_name, customer_street, customer_city from customer where customer_id = '"+customer_id+"'")
    data = cur.fetchone()
    cur.close()

    
    return render_template('home.html', customers = data)

# @app.route('/update/<customer_id>', methods = ['GET', 'POST'])
# def update(customer_id):
#     return render_template('update.html')

@app.route('/delete/<customer_id>', methods=['GET','POST'])
def delete(customer_id):
    cur = mysql.connection.cursor()
    cur.execute("delete from customer where customer_id = %s",[customer_id])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
