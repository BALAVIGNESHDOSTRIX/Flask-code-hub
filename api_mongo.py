import flask
from flask import request, jsonify
from pymongo import MongoClient

app = flask.Flask(__name__)
app.config["DEBUG"] = True

try:
    connection = MongoClient('localhost', 27017)
    user_db = connection["partner_db"]
    userdb_col = user_db["partner"]
except Exception as e:
    print(e)

# CREATE USER
@app.route('/api/v1/create', methods=["POST"])
def create_mongo_user():
    id = request.form.get('id')
    username = request.form.get('username')
    age = request.form.get('age')
    salary = request.form.get('salary')
    userdb_col.insert_one({'_id': id, 'username': username,
                           'age': age, 'salary': salary})
    return jsonify({"result": "successfully created."})

@app.route('/api/v1/get_all_emp', methods=["GET"])
def get_all_emps():
    all_dict = []
    for x in userdb_col.find():
        all_dict.append(x)
    return jsonify(all_dict)

@app.route('/api/v1/emp', methods=["GET"])
def get_single_emp():
    search_id = request.args.get('id')
    print(search_id)
    for x in userdb_col.find({}, {'_id': int(search_id)}):
        return jsonify(x)

@app.route('/api/v1/update/<int:id>', methods=["PUT"])
def update_user_salary(id):
    update_salary = request.form.get('salary')
    ser_q = {"_id": int(id)}
    print(ser_q, update_salary)
    up_q = {"$set": {"salary": int(update_salary)}}
    print(up_q)
    userdb_col.update_one(ser_q, up_q)
    # return jsonify({"result": "successfully created."})


app.run()