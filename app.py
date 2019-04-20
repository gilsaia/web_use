from flask import Flask,render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/interact')
def interact():
    return render_template("interactions.html")

@app.route('/intro')
def show_info():
    return render_template("introduction.html")

@app.route('/papers')
def show_pps():
    return render_template("papers.html")

if __name__ == '__main__':
    app.run()
