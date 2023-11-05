import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")

# Function to add a family member
def add_family_member(data):
    member_id = jackson_family._generateId()
    data["id"] = member_id
    jackson_family.add_member(data)

# Define data for the first 3 family members
member1_data = {
    "first_name": "John",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
}

member2_data = {
    "first_name": "Jane",
    "age": 35,
    "lucky_numbers": [10, 14, 3]
}

member3_data = {
    "first_name": "Jimmy",
    "age": 5,
    "lucky_numbers": [1]
}

# Add the first 3 family members
add_family_member(member1_data)
add_family_member(member2_data)
add_family_member(member3_data)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_family_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_one_family_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is not None:
        return jsonify(member), 200
    else:
        return jsonify({'error': 'Member not found'}), 400

@app.route('/member', methods=['POST'])
def add_new_family_member():
    request_data = request.get_json()
    if request_data is not None:
        member_id = request_data.get("id", None)
        if member_id is None:
            member_id = jackson_family._generateId()
            request_data["id"] = member_id
        jackson_family.add_member(request_data)
        return jsonify({}), 200
    else:
        return jsonify({'error': 'Invalid request data'}), 400

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_family_member(member_id):
    if jackson_family.delete_member(member_id):
        return jsonify({'done': True}), 200
    else:
        return jsonify({'error': 'Member not found'}), 400

if __name__ == '__main__':
    app.run()
