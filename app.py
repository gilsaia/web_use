from flask import Flask, render_template,
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return render_template("eVersion/hello_world.html")


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


@app.route('/ch')
def Chello_world():
    return render_template("cVersion/base.html")


@app.route('/ch/contact')
def Ccontact():
    return render_template("cVersion/Bcon.html")


@app.route('/ch/intro')
def Cshow_info():
    return render_template("cVersion/Bintro.html")


@app.route('/ch/researchA')
def Cshow_pp():
    return render_template("cVersion/Bpp.html")


@app.route('/ch/researchA2')
def Cshow_pp2():
    return render_template("cVersion/Bpp2.html")


@app.route('/ch/researchA3')
def Cshow_pp3():
    return render_template("cVersion/Bpp3.html")


@app.route('/ch/researchA4')
def Cshow_pp4():
    return render_template("cVersion/Bpp4.html")


@app,context
if __name__ == '__main__':
    app.run()
