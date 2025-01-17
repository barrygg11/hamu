from flask import Blueprint, request, jsonify

user_bp = Blueprint('user', __name__)

# 模拟数据库数据
users = []

@user_bp.route('/', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@user_bp.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    user = {
        'id': len(users) + 1,
        'username': data.get('username'),
        'email': data.get('email'),
    }
    users.append(user)
    return jsonify({'message': 'User added!', 'user': user})