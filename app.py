from flask import Flask, render_template, g, redirect, url_for,request
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
    if request.method == "POST":
        # 接收图片
        if(os.path.exists('static/files/img1/pic.png')):
            os.remove('static/files/img1/pic.png')
        photo.save(request.files['file'], 'img1', 'pic.png')  # 保存图片

        # 发送图片
        img = open("static/files/img1/pic.png", 'rb')  # 读取图片文件
        data = base64.b64encode(img.read()).decode()  # 进行base64编码
        html = '''<img src="data:image/png;base64,{}" style="width:100%;height:100%;"/>'''  # html代码
        htmlstr = html.format(data)  # 添加数据
        return htmlstr
    return render_template("formversion/npr.html")


@app.route('/npr_api',methods=['POST'])
def npr_api():
    request.files
    return render_template("formversion/gallery.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
