from flask import Flask, jsonify
import json

obj = Flask(__name__)

@obj.route('/v1/users')
def Users():
    with open('database.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)
    
if __name__ == "__main__":
    obj.run(debug=True)