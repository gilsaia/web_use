from flask import Flask, render_template, g, redirect, url_for, request, jsonify
from flask_uploads import configure_uploads, UploadSet
import config
from os.path import abspath, dirname, join, isdir, isfile
import os.path as osp
import json

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
    nprupload_dir = join(upload_dir, 'images')
    rsz_fn = osp.join(nprupload_dir, f.filename)
    npr_imfn = osp.join(nprupload_dir, f.filename)
    f.save(osp.join(nprupload_dir, f.filename))
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
    return render_template("cmp.html")


@app.route('/cmp_api_sample')
def cmp_api_sample():
    return jsonify({
        "code": 0,
        "msg": "",
        "count": 1000,
        "data": [
            {
                "id": 10000,
                "par1": 1.0,
                "par1cmp": 0.0,
                "par2": 1.0,
                "par2cmp": 0.0
            },
            {
                "id": 10029,
                "par1": 1.0,
                "par1cmp": 0.0,
                "par2": 1.0,
                "par2cmp": 0.0
            }
        ]
    })


@app.route('/cmp_api', methods=['POST', 'GET'])
def cmp_api():
    if request.method == 'GET':
        cmpdownload_dir = join(upload_dir, 'json')
        jsonfile = osp.join(cmpdownload_dir, 'try.json')
        f = open(jsonfile, 'r', encoding='UTF8')
        return jsonify(json.load(f))
    else:
        f = request.files['file']
        # do something
        return jsonify({
            'data': 'ttt'
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
