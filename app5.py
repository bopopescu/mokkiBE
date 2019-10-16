from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app5 = Flask(__name__)

app5.config['MYSQL_DATABASE_USER'] = 'root'
app5.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app5.config['MYSQL_DATABASE_DB'] = 'LibraryDB'
app5.config['MYSQL_DATABASE_HOST'] = 'localhost'
app5.config['MYSQL_DATABASE_PORT'] = 8889


mysql = MySQL()
mysql.init_app(app5)
conn = mysql.connect()
cursor = conn.cursor()

#endpoint for search
@app.route('/search2', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        book = request.form['name']
        # search by first or last name
        cursor.execute("SELECT first_name, last_name from Users WHERE first_name LIKE %s OR last_name LIKE %s", (book, book))
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(data) == 0 and book == 'all':
            cursor.execute("SELECT first_name, last_name from Book")
            conn.commit()
            data = cursor.fetchall()
        return render_template('search2.html', data=data)
    return render_template('search2.html')

if __name__ == '__main__':
    app.debug = True
    app.run()

