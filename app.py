#!/usr/bin/env python3
#-*-coding:UTF-8-*-

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_bootstrap import Bootstrap
from flask_bootstrap import WebCDN
from wtforms import Form, TextField, validators
from random import randint
import csv
import re



app = Flask(__name__)
bootstrap = Bootstrap(app)
app.extensions['bootstrap']['cdns']['bootstrap'] = WebCDN('//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.1/')



class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])



@app.errorhandler(404)
@app.errorhandler(500)
def page_not_found(e):
    form = ReusableForm(request.form)
    return render_template('404.html', title='404 Not found',form=form), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)

