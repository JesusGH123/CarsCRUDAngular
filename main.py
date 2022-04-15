from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__)

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
@app.route('/')
@cross_origin()
def index():
    if request.method == 'GET':
        cur = db.connection.cursor()
        cur.execute('SELECT * FROM car')
        data = cur.fetchall() #Get the query in variable data
        print(data)
    return jsonify([{'id':car[0],'brand': car[1], 'model': car[2], 'year': car[3]} for car in data])

@app.route('/add_car', methods=['POST'])
def add_car():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        year = request.form['year']

        # Get the cursor
        cur = db.connection.cursor()
        cur.execute('INSERT INTO car (brand, model, year) VALUES(%s, %s, %s)', (brand, model, year))

        db.connection.commit()

        flash('Car added successfully!')
    return redirect(url_for('Index'))

@app.route('/delete_car/:id')
def delete_car():
    return 'Deleting car'

# Run the server if the executed file is the main file
if __name__ == '__main__':
    app.run(port = 3000, debug = True)
