from flask import Blueprint, request, jsonify

inventory_bp = Blueprint('inventory', __name__)

# 模拟库存数据
inventory = []

@inventory_bp.route('/', methods=['GET'])
def get_inventory():
    return jsonify({'inventory': inventory})

@inventory_bp.route('/add', methods=['POST'])
def add_inventory_item():
    data = request.get_json()
    item = {
        'id': len(inventory) + 1,
        'name': data.get('name'),
        'quantity': data.get('quantity'),
    }
    inventory.append(item)
    return jsonify({'message': 'Item added!', 'item': item})