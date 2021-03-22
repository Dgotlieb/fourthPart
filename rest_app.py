import os
from flask import Flask, request
import db_connector
# #
app = Flask(__name__)
#################################
# # supported methods
@app.route('/users/<user_id>', methods=['GET','POST','PUT','DELETE'])
def users(user_id):
    if request.method == 'POST':
        request_data = request.json
        user_name = request_data.get('user_name')
        if db_connector.user_create(user_id,user_name): # try to create new user
            return {'status': 'ok', 'user_added': user_name }, 200
        else: #  user exist
            return {'status': 'error', 'reason': user_id  + ' Already exist'}, 500

    if request.method == 'GET':
        user_name =  db_connector.get_user_name(user_id)
        if user_name != '':
            return {'status': 'ok', 'user_name': user_name}, 200
        else:
            return {'status': 'error', 'reason': 'no such id'}, 500

    if request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        if db_connector.user_update(user_id,user_name): # try to update a user
            return {'status': 'ok', 'user_Updated': user_name }, 200
        else: #  user exist
            return {'status': 'error', 'reason': user_id  + ' no such id'}, 500


    if request.method == 'DELETE':
        if db_connector.user_delete(user_id):
            return {'status': 'ok', 'user_deleted': user_id}, 200
        else:
            return {'status': 'error', 'reason': 'no such id'}, 500

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

#################################


app.run(host='0.0.0.0', debug=True, port=5002)
