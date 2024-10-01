from flask import Flask

obj = Flask(__name__)

@obj.route('/v1/users')
def hello_world():
    return 'Hello World!'
    
if __name__ == "__main__":
    obj.run(debug=True)