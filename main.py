from flask import Flask, request, render_template, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure and get an instance of the db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cars'
db = MySQL(app)

# App configurations
app.secret_key = 'secret_key'

#Routes
@app.route('/cars')
def Index():
    if request.method == 'GET':
        cur = db.connection.cursor()
        cur.execute('SELECT * FROM car')
        data = cur.fetchall() #Get the query in variable data
        print(data) 

    return render_template('index.html')

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
