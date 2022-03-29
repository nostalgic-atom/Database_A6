from flask import Flask, render_template, request
from flask_mysqldb import MySQL
#import yaml

app = Flask(__name__)

#db = yaml.load(open('db.yaml'))

#app.config['MYSQL_HOST'] = db['mysql_host']
#app.config['MYSQL_USER'] = db['mysql_user']
#app.config['MYSQL_PASSWORD'] = db['mysql_password']
#app.config['MYSQL_'] = db['mysql_db']

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        first_name = userDetails['firstname']
        last_name = userDetails['lastname']
        customer_street = userDetails['street']
        customer_city = userDetails['city']

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
