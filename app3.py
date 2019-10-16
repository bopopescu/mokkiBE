from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'mokkiDB'
app.config['MYSQL_PORT'] = 8889

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['firstname']
        lastName = details['lastname']
        email = details['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Users(first_name, last_name, company_email) VALUES (%s, %s, %s)", (firstName, lastName, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)