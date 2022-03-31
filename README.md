# Banking System Web App 

<br>

## Website flow

- The landing page of our web app is the customer sign-up page through which the customer will be inserted in the `CUSTOMER` table of our `banking_system` database. He/She will need to enter his/her personal details such as first name, last name, street, and city. The `customer_id` will be assigned randomly and each customer will be assigned an employee.

- Once the user signs up, he will be added to the `CUSTOMER` table. Also, the sign-up will generate the 11 digit account number and 16 digit debit card number and the account will be generated corresponding to each customer. Hence, the account_number, balance, and card_number will be inserted as an entry in the `ACCOUNT` table.

- As we have many to many relationships (`DEPOSITOR`) between the `ACCOUNT` and `CUSTOMER`, on signing up, the `account_number` generated corresponding to the customer will be inserted in the `DEPOSITOR` table.

- Upon signing up, we land upon the profile page of the customer where we have an update button, delete button, borrow loan button, and account details button.

- If we click on the update button, a form will appear with the values we had already filled. We can edit the field & update the customer details. 

- The delete button will delete the customer from the DB such that his account will also be deleted. Then we get redirected to the signup page.

- On clicking the account details button, we get all the information regarding the customer.

- On clicking the borrow loan, a customer can borrow a loan. Once we took the loan, an entry will `loan_number` and the amount will be inserted into the `LOAN` table and we will get redirected to the profile page. 

<br>

<br>

## Operations

#### **INSERT**

#### WebApp asks the user to register/signup, as displayed in the below window

<img src="working-screenshots\insert-form.png">

<br>

#### `CUSTOMER` table in the DB is as follows before insertion

<img src="working-screenshots\before-insert.png">

<br>

#### `CUSTOMER` table in the DB is as follows after insertion

<img src="working-screenshots\after-insert.png">

<br>

#### Profile view for the user after signing up for the WebApp

<img src="working-screenshots\after-insert-view.png">

<br>

#### **UPDATE**

#### Update window before entering the updated values

<img src="working-screenshots\update-form.png">

<br>

#### Update window after entering the updated values

<img src="working-screenshots\update-form-entry.png">

<br>

#### `CUSTOMER` table in the DB with updated values

<img src="working-screenshots\updated-db.png">

<br>

#### Profile view for the user after updating the values

<img src="working-screenshots\updated.png">

<br>

#### **DELETE**

#### Profile view of the user before deletion

<img src="working-screenshots\before-delete.png">

<br>

#### `CUSTOMER` table in the DB with deleted values

<img src="working-screenshots\after-delete.png">

<br>

<br>

## How to run the code

- You will need the following packages -
    - `flask`
    - `flask-mysqldb`

- Dump the database provided into your system ( `*.sql file` )

- Enter the MySQL credentials into `app.py` file for database access

        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'your_user_name'
        app.config['MYSQL_PASSWORD'] = 'your_passwword'
        app.config['MYSQL_DB'] = 'database_name'

- Head to the `Banking_System` directory in the folder and run the `app.py` file

- Go to `localhost:5000` you will land at our signup page.
