from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST - used to receive data
# GET - used to send data and back only 

# POST /store data: {name:}
@app.route('/store', methods=['POST', 'GET'])
def create_store():
    request_data = request.get_json(force=True)
    print("zysfhvb")
    new_store = {
        'name': request_data['name']
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/some_name
def get_store(name):
    for store in stores:
        if stores['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/stores')
def get_stores(): 
    return jsonify({'stores':stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if stores['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

if __name__ == '__main__':
    app.run(port = 4999 ,debug=True)    