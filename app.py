# import libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# configure flask app
app = Flask(__name__)

# configure SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
# commands to create sqlite db
    # create sqlite db  and call sqlite shell -> sqlite3 <name>.db
    # save db -> .tables
    # exit sqlite shell -> .exit
    # check if db created -> ls

# define class for blogpost with a DB model
class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
# commands to create class with columns in the qlite db
# get python shell going -> python
# import db -> from app import db
# create class in db -> db.create_all()
# exit python shell -> exit()

# first route for home page and show user template index.html when goes to this url
@app.route('/')
def index():
    return render_template('index.html')

# 2nd route for about
@app.route('/about')
def about():
    return render_template('about.html')

# 3rd route
@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    date_posted = post.date_posted.strftime('%B %d, %Y')

    return render_template('post.html', post=post, date_posted=date_posted)

# 4th route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# 5th route
@app.route('/add')
def add():
    return render_template('add.html')

# 6th route
@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

# code to run app
if __name__ == '__main__':
    app.run(debug=True)