from flask import Flask, render_template, request, jsonify

import Puzzle_Lineal as pl
import Vuelos as vl
import DFS as d
import Iterativo_DFS as dfsi
import Recursivo_DFS as dfsr
import Djikstra as dk

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['GET'])
def buscar():
    result = ""
    result = pl.imprimir()
    return jsonify(resultado=result)

@app.route('/Vuelos', methods=['GET'])
def Vuelos():
    result = ""
    result = vl.imprimir()
    return jsonify(resultado=result)

@app.route('/DFS', methods=['GET'])
def DFS():
    result = ""
    result = d.imprimir()
    return jsonify(resultado=result)

@app.route('/Iterativo_DFS', methods=['GET'])
def Iterativo_DFS():
    result = ""
    result = dfsi.imprimir()
    return jsonify(resultado=result)

@app.route('/Recursivo_DFS', methods=['GET'])
def Recursivo_DFS():
    result = ""
    result = dfsr.imprimir()
    return jsonify(resultado=result)

@app.route('/Djikstra', methods=['GET'])
def Djikstra():
    result = ""
    result = dk.etiquetas
    return jsonify(resultado=result)

if __name__ == "_main_":
    app.run(debug=True)