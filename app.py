from flask import Flask,render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return render_template("base.html")

@app.route('/contact')
def contact():
    return render_template("Bcon.html")

@app.route('/intro')
def show_info():
    return render_template("Bintro.html")

@app.route('/researchA')
def show_pp():
    return render_template("Bpp.html")

@app.route('/researchA2')
def show_pp2():
    return render_template("Bpp2.html")

@app.route('/researchA3')
def show_pp3():
    return render_template("Bpp3.html")

@app.route('/researchA4')
def show_pp4():
    return render_template("Bpp4.html")

if __name__ == '__main__':
    app.run()
