from flask import Flask
from datetime import date
from entities.package import Package
import json
app = Flask(__name__)

@app.route('/ping', methods = ['GET'])
def ping():
    return 'pong'

@app.route('/return/<int:id>', methods = ['GET'])
def showReturnById(id):
    x = Package(id, 3, 45, 'SENT', date.today())
    return str(id)

@app.route('/return/<int:id>', methods = ['PATCH'])
def updateReturnById(id):
    x = Package(id, 3, 45, 'SENT', date.today())
    return x

#@app.route('/return/create')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)

