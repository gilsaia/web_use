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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
