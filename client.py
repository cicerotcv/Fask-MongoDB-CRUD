# -*- coding utf-8 -*-
from flask import Flask, request, jsonify, abort, make_response
from mongoengine import connect, Document
from models import Super

app = Flask(__name__)
DB = connect("PythonCRUD")


@app.route('/supers', methods=["GET"])
def list_super():
    super_list = Super.objects.to_json()
    return super_list


@app.route('/supers', methods=["POST"])
def create():
    if not request.json:
        abort(400)

    new_super = Super()
    new_super.real_name = request.json.get("real_name")
    new_super.alias = request.json.get("alias")
    new_super.abilities = request.json.get("abilities")
    new_super.save()

    return new_super.to_json()


@app.route('/supers/<string:super_id>', methods=["GET"])
def read(super_id):
    if not super_id:
        make_response("No id provided", 400)

    super = Super.objects.get(id=super_id).to_json()
    return super


@app.route("/supers/<string:super_id>", methods=["PUT"])
def update(super_id):
    if not request.json:
        make_response("Update data not provided", 400)
    if not request.json:
        make_response("Update id not provided", 400)

    super = Super.objects.get(id=super_id)
    super.update(**request.json)
    super.save()
    super.reload()
    return super.to_json()


@app.route('/supers/<string:super_id>', methods=["DELETE"])
def delete(super_id):
    if not super_id:
        make_response("No id provided", 400)

    result = Super.objects(id=super_id).delete()
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
