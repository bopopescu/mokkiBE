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


    def checkemail(email, allemails):
        if email in allemails:
            return True
        return False

    if request.method == "POST":
        details = request.form
        firstName = details['firstname']
        lastName = details['lastname']
        email = details['email']
        getemails = "SELECT company_email from Users"
        mycursor = connection.cursor()
        mycursor.execute(getemails)
        allemails = mycursor.fetchall()
        mycursor.close()
        if checkemail((email,),allemails) == False:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Users(first_name, last_name, company_email) VALUES (%s, %s, %s)", (firstName, lastName, email))
            connection.commit()
            cursor.close()
            msg = 'user added to DB :)'
            return render_template('add_user.html', msg=msg)
        else :
            yocursor = connection.cursor()
            select_stmt = "SELECT * from Users WHERE company_email = %(company_email)s"
            yocursor.execute(select_stmt, { 'company_email': email })
            data = yocursor.fetchall()
            connection.commit()
            yocursor.close()
            msg = 'email already in DB :('
            return render_template('add_user.html', msg=msg, datav=data)
    return render_template('add_user.html')


@app.route("/search_user_by_fn", methods=['GET','POST'])
def search():
    if request.method == "POST":
        details = request.form
        name = details['name']
        mycursor = connection.cursor()
        select_stmt= "SELECT * from Users WHERE first_name LIKE %s or last_name LIKE %s"
        mycursor.execute(select_stmt, (name, name))
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

