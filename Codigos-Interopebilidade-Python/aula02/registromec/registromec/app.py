from flask import Flask, json, render_template, request, redirect, jsonify
import sqlite3
from random import getrandbits

app = Flask(__name__, template_folder='.')

@app.route('/gerar', methods=['GET', 'POST'])
def inserir():
	if request.method == 'POST':
		cpf    = request.values.get('cpf')
		nivel  = request.values.get('nivel')
		chave  = str(getrandbits(128))
		insert = "insert into registro values (null, '" + cpf + "', '" + nivel +  "', '" + chave + "', datetime('now')); "
		conexao = sqlite3.connect('banco.data')
		conexao.execute(insert)
		conexao.commit()
		conexao.close()
		return redirect('/gerar')
	elif request.method == 'GET':
		return render_template('cadastro.html')

@app.route('/buscar', methods=['GET', 'POST'])
def listar():
	if request.method == 'POST':
		cpf   = request.values.get('cpf')
		nivel = request.values.get('nivel')
		select = "select id, cpf, nivel, chave, datahora from registro where cpf = '" + cpf + "' and nivel = '" + nivel + "' order by id; "
		conexao = sqlite3.connect('banco.data')
		resultado = conexao.execute(select).fetchall()
		conexao.close()
		return render_template("buscar.html", resultado=resultado)
	elif request.method == 'GET':
		return render_template('buscar.html', resultado=None)

@app.route('/remover', methods=['GET'])
def remover() :
	id = request.values.get('id')
	delete = "delete from registro where id = '" + id + "'; "
	conexao = sqlite3.connect('banco.data')
	teste = minhafuncao(10, 20)
	conexao.execute(delete)
	conexao.commit()
	conexao.close()
	return redirect("/buscar")

@app.route('/', methods=['GET', 'POST'])
def inicio():
	return redirect('/buscar')
	
app.run(port=5002, use_reloader=True) 