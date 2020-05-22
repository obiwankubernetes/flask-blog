from flask import Flask, render_template

app = Flask(__name__)

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
def add():
    return render_template('contact.html')

# code to run app
if __name__ == '__main__':
    app.run(debug=True)