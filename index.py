from flask import Flask
from flask import render_template

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/La_escuela')
def escuela():
    return render_template('La_escuela.html')

@app.route('/Director')
def director():
    return render_template('Director.html')    

@app.route('/MisionyVision')
def mision_vision():
    return render_template('Mision_vision.html') 

@app.route('/Objetivos')
def objetivos():
    return render_template('Objetivo.html') 

@app.route('/Plan_Estudios')
def plan_estudios():
    return render_template('Plan_estudios.html')

@app.route('/Grados_academicos')
def grados_academicos():
    return render_template('Grados_academicos.html')

if __name__ == '__main__':
    app.run(debug=True)    