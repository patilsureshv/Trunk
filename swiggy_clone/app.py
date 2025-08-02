from flask import Flask, jsonify
from .data import RESTAURANTS

app = Flask(__name__)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    return jsonify(RESTAURANTS)

if __name__ == '__main__':
    app.run(debug=True)
