from flask import Flask, render_template, g, redirect, url_for,request,jsonify
import random,string,stringprep
from flask_uploads import configure_uploads,UploadSet
import config
import os,base64

app = Flask(__name__)
app.config.from_object(config)

# 配置上传文件存放路径
base = os.path.dirname(os.path.abspath(__file__))
base = os.path.join(base, 'static')
app.config['UPLOADS_DEFAULT_DEST'] = base
photo = UploadSet()
configure_uploads(app, photo)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    return render_template("formversion/index.html")


@app.route('/gallery')
def gallery():
    return render_template("formversion/gallery.html")


@app.route('/generic')
def generic():
    return render_template("formversion/generic.html")


@app.route('/npr', methods=['POST', 'GET'])
def npr():
    if request.method == "GET":
        return render_template("formversion/npr.html")
    else:
        # 接收图片
        if(os.path.exists('static/files/img1/pic1.png')):
            os.remove('static/files/img1/pic1.png')
        random_num = str(random.randint(10, 10000000))
        random_num=random_num+".png"
        photo.save(request.files['file'], 'img1', random_num)  # 保存图片
        # print(request.data['hours']);
        return jsonify({
            'status':'0',
            'info':'new image',
            'npr_img':"static/files/img1/"+random_num,
            'input_img':"static/files/img1/"+random_num
        })
    # return render_template("formversion/npr.html")


@app.route('/npr_api',methods=['POST'])
def npr_api():
    request.files
    return render_template("formversion/gallery.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
