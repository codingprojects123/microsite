from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
import os
import random
import pymysql
import sys

r = lambda: random.randint(0,255)

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

host = "127.0.0.1"
port = "3306"
user = "root"
db = "data"

con = pymysql.connect(host=host, user=user, password="", db=db, cursorclass=pymysql.cursors.DictCursor)
cur = con.cursor()

@app.route('/data', methods=['GET'])
def all_data():
    response_object = {'status': 'success'}
    try:
        cur.execute("SELECT * FROM DATA")
        res = cur.fetchall()
        result_arr = []
        for row in res:
            result_arr.append(dict(row))
        response_object['models'] = result_arr
    except Exception as e:
        response_object['status'] = "error"
        response_object['msg'] = str(e)
    return jsonify(response_object)

@app.route('/entry', methods=['POST'])
def insert_data():
    response_object = {'status': 'success'}
    try:
        post_data = request.get_json()
        app.logger.info('{}'.format(request))
        app.logger.info('{}'.format(post_data))
        x = ('#%02X%02X%02X' % (r(),r(),r()))
        cur.execute("INSERT INTO DATA (name, count, color) VALUES ('{}', {}, '{}')".format(post_data['name'], post_data['count'], x))
        result = cur.fetchall()
        con.commit()
    except Exception as e:
        response_object['status'] = "error"
        response_object['msg'] = str(e)
    return jsonify(response_object)

@app.route('/delete', methods=['DELETE'])
def data_delete():
    response_object = {'status': 'success'}
    try:
        delete_data = request.get_json()
        app.logger.info('{}'.format(request))
        app.logger.info('{}'.format(delete_data))
        cur.execute("DELETE FROM DATA WHERE id='{}'".format(delete_data['id']))
        result = cur.fetchall()
        con.commit()
    except Exception as e:
        response_object['status'] = "error"
        response_object['msg'] = str(e)
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(debug=False)
