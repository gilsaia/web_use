from flask import Flask,render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contactus.html")

@app.route('/intro')
def show_info():
    return render_template("introduction.html")

@app.route('/papers')
def show_pps():
    return render_template("papers.html")

@app.route('/A1')
def area1():
    return render_template("#")
@app.route('/A2')
def area2():
    return render_template("#")
@app.route('/A3')
def area3():
    return render_template("#")
@app.route('/A4')
def area4():
    return render_template("#")

if __name__ == '__main__':
    app.run()
