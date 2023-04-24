from flask import Flask
from flask import render_template
from flask import request
import sys
from waitress import serve

app = Flask(__name__)


@app.route('/')
def main_view():
    name = 'Rekruto'
    message = 'Давай дружить'
    params = request.args
    if params:
        name, message = params.get('name'), params.get('message')
    return render_template('main_view_temp.html', name=name, message=message)



if __name__ == '__main__':
    serve(app, host='0.0.0.0')

