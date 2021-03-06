from flask import Flask
from flask import render_template # the reason we import this is so we can get an output from our template file
from flask import url_for
from flask import flash
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 


app = Flask(__name__) # setting app variable to instance of Flask class
# __name__ just means the name of your module


@app.route('/') # decorators add additional functionality 
# ('/') --> root page
def hello():
    return "Hello World!"

# conditional
if __name__ == '__main__': # --> only true if we run this script directly 
    app.run(debug=True) # debug=True --> allows debug mode 


@app.route('/about') # another route with /about at the end of the website page link
def about():
    return "<h1> About Page </h1>"


# Want a route for our home page
@app.route('/home') # --> takes you to the same page/same thing as app.route('/')
def home():
    return "Home Page"
________________________________________________________________________________________________________________________________________________

# Best way to handle multiple routes is to have "templates" folder

# Example of using render_template
@app.route('/') 
def hello():
    return render_template('home.html') # --> this allows us to execute the template file called home.html

# Another example of using render_template
@app.route('/about') 
def about():
    return render_template('about.html')


# A database example
# Each dictionary will represent a single blog post 
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# So now whenever we use that varaible name (posts), it will give us access to that variable in the template
@app.route('/') 
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about') 
def about():
    return render_template('about.html', title='About') # Passing in a title of About. So for our home page
    # where we did not pass in a title, we will do something else in the about.html page following the jinja2 statement

________________________________________________________________________________________________________________________________________________

import secrets
# Secret key will help protect against cookies and modifying requests, etc.
app.config['SECRET_KEY'] = 'sdsad123213d82na1'
# using secrets module to get random letters and numbers generated 

# To import your modules from forms
from forms import RegistrationForm, LoginForm


@app.route('/register', methods = ['GET','POST']) # We created (methods = ['GET','POST']) because we want our browser to be 
# able to GET data as well as POST --> If we don't have this, when you try to register, it will give you an error
def register():
    form = RegistrationForm() # The () is so we can use RegistrationForm as an instance
    # Using the validate_on_submit method
    if form.validate_on_submit():
        # Using a flash message 
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) 
    return render_template('register.html', form=form) # form = form so we have access to that form


@app.route('/login', methods = ['GET','POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home')) 
        else:
            flash(f'Login Unsuccessful, please check Username and Password', 'danger')
    return render_template('login.html', form=form)

________________________________________________________________________________________________________________________________________________

# From import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # /// shows a relative path from the current file so the site.db file should get created

# Create a database instance:
db = SQLAlchemy(app) # Can be moved to a different file
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') 
    # default --> when an account is created, if the user did not specifiy an image --> default an image)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True) # This sets up a relationship with the class (Post)
    # backref is similar to adding another column to the post model, use the author attribute

    def __repr__(self): # the __repr__ method how the object ios printed when we print it out
        return f"User('{self.username}','{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # ForeginKey means this has a relationship with the other variable with relationship

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

________________________________________________________________________________________________________________________________________________


