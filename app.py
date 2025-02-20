from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/aboutus')
def aboutus():
    return render_template('about_us.htm')

if __name__ == '__main__':
    app.run()