from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#Coneccion a la bases de datos
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'noteapp'
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)

#Setting
app.secret_key = 'secrectkey'

#Rutas
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM notas')
    data = cur.fetchall()

    return render_template('index.html', pubs = data)

@app.route('/add', methods = ['POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO notas (title, description) VALUES (%s, %s)', (title, description))
        mysql.connection.commit()
        return redirect(url_for('index'))

@app.route('/edit/<id>')
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM notas WHERE id = %s', (id))
    data = cur.fetchall()

    return render_template('edit.html', pub = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update(id):
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        cur = mysql.connection.cursor()
        print(title)
        cur.execute('UPDATE notas SET title = %s, description = %s WHERE id = %s', (title, description, id))
        cur.connection.commit()
        return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM notas WHERE id = %s', (id))
    mysql.connection.commit()
    return redirect(url_for('index'))
    
@app.route('/prueba')
def prueba():
    return "Funciona"

#Servidor
if __name__ == '__main__':
    app.run()