# import libraries
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# configure flask app
app = Flask(__name__)

# configure SQLite DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mnt/C:/Users/sampe/OneDrive/Code Projects/blog-flask/blogdb.db"
db = SQLAlchemy(app)

# first route for home page and show user template index.html when goes to this url
@app.route('/')
def index():
    return render_template('index.html')

# 2nd route for about
@app.route('/about')
def about():
    return render_template('about.html')

# 3rd route
@app.route('/post')
def post():
    return render_template('post.html')

# 4th route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# code to run app
if __name__ == '__main__':
    app.run(debug=True)