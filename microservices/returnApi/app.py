from flask import Flask
app = Flask(__name__)

@app.route('/ping', methods = ['GET'])
def ping():
    return 'pong'

@app.route('/return/<int:id>', methods = ['GET'])
def showReturnById(id):
    return str(id)

@app.route('/return/<int:id>', methods = ['PATCH'])
def updateReturnById(id):
    return 'patch'

#@app.route('/return/create')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)

