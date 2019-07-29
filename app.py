from flask import Flask, render_template, g, redirect, url_for, request, jsonify
from flask_uploads import configure_uploads, UploadSet
import config
from os.path import abspath, dirname, join, isdir, isfile
import os.path as osp


app = Flask(__name__)
app.config.from_object(config)
app.config['homepage_dir'] = abspath(dirname(__file__))
app.config['upload'] = join(app.config['homepage_dir'], 'static/upload')
upload_dir = app.config['upload']


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template("index.html")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html")


@app.route('/generic')
def generic():
    return render_template("generic.html")


@app.route('/npr', methods=['POST', 'GET'])
def npr():
    return render_template("npr.html")


@app.route('/npr_api', methods=['POST'], strict_slashes=False)
def npr_api():
    f = request.files['file']
    rsz_fn = osp.join(upload_dir, f.filename)
    npr_imfn = osp.join(upload_dir, f.filename)
    f.save(osp.join(upload_dir, f.filename))
    npr_imfn = osp.relpath(npr_imfn, app.config['homepage_dir'])
    rsz_fn = osp.relpath(rsz_fn, app.config['homepage_dir'])
    return jsonify({
        'status': '0',
        'info': 'return cached data',
        'npr_img': npr_imfn,
        'input_img': rsz_fn
    })

@app.route('/cmp')
def cmp():
    return  render_template("cmp.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
