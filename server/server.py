from flask import Flask, request, render_template, jsonify

from db.db_connection import yield_query_result, execute_query
from server.queries import check_user, insert_user, check_username, get_user_id_by_username, get_drive_data_by_drive_id
from server.sql_connection import SQLConnection


app = Flask(__name__)
connection = SQLConnection()


@app.route('/users/', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        request_as_dict = request.get_json(force=True)
        db, cursor = connection.get()
        return jsonify({"response": yield_query_result(db, cursor, check_user(**request_as_dict))})

    if request.method == 'POST':
        request_as_dict = request.get_json(force=True)
        db, cursor = connection.get()
        return jsonify({"response": execute_query(db, cursor, insert_user(**request_as_dict))})


@app.route('/drives/', methods=['GET', 'POST'])
def drives():
    if request.method == 'GET':
        request_as_dict = request.get_json(force=True)
        db, cursor = connection.get()
        return jsonify({"response": yield_query_result(db, cursor, get_last_driver_id(**request_as_dict))})
    if request.method == 'POST':
        request_as_dict = request.get_json(force=True)
        db, cursor = connection.get()
        return jsonify({"response": execute_query(db, cursor, update_drive(**request_as_dict))})


def start_server():
    connection.start()
    app.run(debug=True)


def stop_server():
    connection.stop()


# if __name__ == '__main__':
#     connection.start()
#     app.run(debug=True)
#     connection.stop()
