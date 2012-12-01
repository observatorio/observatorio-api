from flask import Flask, request, url_for, redirect, render_template, flash
from flask.ext.sqlalchemy import SQLAlchemy

from json import dumps

app = Flask(__name__)

#Procesamiento


## Ruteo

@app.route('/', methods=['GET'])
def main():
    return redirect(url_for('get_datos_ciudad'))


@app.route("/santiago", methods=['GET'])
def get_datos_ciudad():
    list = (
        {'id': 478 , 'name': 'cerrillos'},
        {'id': 479, 'name': 'cerro navia'}
        )

    return dumps(list)

@app.route('/comuna/<comuna_id>', methods=['GET'])
def get_data_comuna(comuna_id):
    list = ({
        'transporte': 4,
        'salud': 5,
        'educacion': 3
        })
    return dumps(list)

@app.route('/comuna/<comuna_id>/<dimension>', methods=['GET'])
def get_dimension_comuna(comuna_id, dimension):
    pass



if __name__ == '__main__':
    app.run(debug=True)