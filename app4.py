import mysql.connector

from flask import Flask, render_template, request

app = Flask(__name__)

connection = mysql.connector.connect(host='localhost',
                                         database='mokkiDB',
                                         user='root',
                                         password='root',port=8889)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        details = request.form
        firstName = details['firstname']
        lastName = details['lastname']
        email = details['email']
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Users(first_name, last_name, company_email) VALUES (%s, %s, %s)", (firstName, lastName, email))
        connection.commit()
        cursor.close()
        return 'success'
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)