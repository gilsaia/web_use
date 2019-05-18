from flask import Flask, render_template, g, redirect, url_for
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template("formversion/index.html")


@app.route('/gallery')
def gallery():
    return render_template("formversion/gallery.html")


@app.route('/generic')
def generic():
    return render_template("formversion/generic.html")


@app.route('/npr')
def npr():
    return render_template("formversion/npr.html")


@app.route('/contact')
def contact():
    return render_template("eVersion/Bcon.html")


@app.route('/intro')
def show_info():
    return render_template("eVersion/Bintro.html")


@app.route('/researchA')
def show_pp():
    return render_template("eVersion/Bpp.html")


@app.route('/researchA2')
def show_pp2():
    return render_template("eVersion/Bpp2.html")


@app.route('/researchA3')
def show_pp3():
    return render_template("eVersion/Bpp3.html")


@app.route('/researchA4')
def show_pp4():
    return render_template("eVersion/Bpp4.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
