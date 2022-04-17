from audioop import cross
from flask import Flask, jsonify, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# Configure and get an instance of the db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cars'
app.config['CORS_HEADERS'] = 'Content-Type'
db = MySQL(app)

# App configurations
app.secret_key = 'secret_key'

#Routes
@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        cur = db.connection.cursor()
        cur.execute('SELECT * FROM car')
        data = cur.fetchall() #Get the query in variable data

    return jsonify([{'id':car[0],'brand': car[1], 'model': car[2], 'year': car[3]} for car in data])

@app.route('/add_car', methods=['POST'])
def add_car():
    if request.method == 'POST':
        data = request.get_json()
        brand = data["brand"]
        model = data["model"]
        year = data["year"]

        # Get the cursor
        cur = db.connection.cursor()
        cur.execute('INSERT INTO car (brand, model, year) VALUES(%s, %s, %s)', (brand, model, year))

        db.connection.commit()

    return jsonify(data = 'post was posted successfully')

@app.route('/update_car', methods=["PUT"])
def update_car():
    if request.method == 'PUT':
        data = request.get_json()
        id = data["id"]
        brand = data["brand"]
        model = data["model"]
        year = data["year"]

        # Get the cursor
        cur = db.connection.cursor()
        cur.execute('UPDATE car SET brand=%s, model=%s, year=%s WHERE id=%s', (brand, model, year, id))

        db.connection.commit()

    return jsonify(data = 'post was updated successfully')

@app.route('/delete_car/<string:id>', methods=["DELETE"])
def delete_car(id):
    if request.method == 'DELETE':
        # Get the cursor
        cur = db.connection.cursor()
        cur.execute('DELETE FROM car WHERE id=%s', (id,))
        
        db.connection.commit()
    
    return jsonify(data = 'post was deleted successfully')

# Run the server if the executed file is the main file
if __name__ == '__main__':
    app.run(port = 3000, debug = True)