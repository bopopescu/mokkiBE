from connectDB import connection
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY']='13542764GTH'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/add_user', methods=['GET', 'POST'])
def signup():

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
    return render_template('signup.html')


@app.route("/search_user_by_fn", methods=['GET','POST'])
def search():
    if request.method == "POST":
        details = request.form
        firstName = details['firstname']
        mycursor = connection.cursor()
        select_stmt = "SELECT * FROM Users WHERE first_name = %(first_name)s"
        mycursor.execute(select_stmt, {'first_name': firstName})
        data = mycursor.fetchall()
        connection.commit()
        mycursor.close()
        return render_template('search.html', dataz=data)
    return render_template('search.html')


#@app.route('/search', methods=['GET', 'POST'])
#def search():
#    if request.method == "POST":
#        book = request.form['book']
#        # search by author or book
#        cursor.execute("SELECT name, author from Book WHERE name
#                        LIKE %s OR author LIKE %s", (book, book))
#        conn.commit()
#        data = cursor.fetchall()
#        # all in the search box will return all the tuples
#        if len(data) == 0 and book == 'all':
#            cursor.execute("SELECT name, author from Book")
#            conn.commit()
#            data = cursor.fetchall()
#        return render_template('search.html', data=data)
#    return render_template('search.html')


@app.route("/register", methods=['GET','POST']) # last bit tells what methods are allowed
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.firstname.data} {form.lastname.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)











@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)


