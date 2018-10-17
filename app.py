#!/usr/bin/env python3
#-*-coding:UTF-8-*-

from flask import Flask
from flask import send_from_directory
from flask import render_template
from flask import jsonify
from flask_bootstrap import Bootstrap
from flask_bootstrap import WebCDN
from SWProxy import SWProxyStart
from os import listdir
import multiprocessing
import socket


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.extensions['bootstrap']['cdns']['bootstrap'] = WebCDN('//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.1/')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Welcome SWProxy Web App')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About')

@app.route('/start', methods=['GET'])
def start():
    port = 8080
    ip = [[(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]][0]
    log = 'INFO'
    SWProxy = multiprocessing.Process(target=SWProxyStart, args=(ip, port, log))
    SWProxy.start()
    if (SWProxy.is_alive()):
        return render_template('start.html', title='SWProxy on progress', status= 'sucess', ip=ip, port=port)
    else:
        return render_template('start.html', title='Failed to launch', status= 'failed')


@app.route('/files', methods=['GET'])
def files():
    dloads_dir = 'data'
    dloads = listdir(dloads_dir)
    dloads_src = ['/download/{}'.format(i) for i in dloads]
    return jsonify(dloads_src)

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    download = 'data'
    return send_from_directory(directory=download, filename=filename, as_attachment=True)


@app.errorhandler(404)
@app.errorhandler(500)
def page_not_found(e):
    return render_template('404.html', title='404 Not found'), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)

