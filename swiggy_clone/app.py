from flask import Flask, jsonify
from .data import RESTAURANTS

app = Flask(__name__)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    return jsonify(RESTAURANTS)

@app.route('/restaurants/<int:restaurant_id>/menu', methods=['GET'])
def get_restaurant_menu(restaurant_id):
    restaurant = next((r for r in RESTAURANTS if r['id'] == restaurant_id), None)
    if restaurant:
        return jsonify(restaurant.get('menu', []))
    return jsonify({'message': 'Restaurant not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
