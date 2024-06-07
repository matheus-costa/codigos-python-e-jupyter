from flask import Flask, json, render_template, request, redirect
import sqlite3
import requests

app = Flask(__name__, template_folder='.')


@app.route('/inserir', methods=['GET', 'POST'])
def inserir():
	if request.method == 'POST':		
		cpf   = request.values.get('cpf') #atribuindo o cpf vindo de uma requisição 

		obj = { "documento" : cpf } #atribuindo o valor "documento"	que é a variável cpf
		txt = json.dumps( obj )# codificando o objeto 
#enviando a requisição contendo o cpf, codificado!
		resposta = requests.post(url="http://localhost:5002/valida", data=txt)
		txt = resposta.content
		obj = json.loads( txt )#decodificando o cpf 
#verificando se o CPF é válido! Se for Válido o código segue executando! Caso não seja é exibida a mensagem CPF inválido		
		if obj['status'] == False:
			return 'CPF inválido.'

		nome  = request.values.get('nome')
		curso = request.values.get('curso')
		chave = ''
		insert = "insert into aluno values (null, '" + cpf + "', '" + nome + "', '" + curso + "', '" + chave + "', datetime('now')); "
		conexao = sqlite3.connect('banco.data')#conexão com o Banco de dados
		conexao.execute(insert)#executando a consulta
		conexao.commit()#"confirmação da consulta"
		conexao.close()#fechamento da conexão
		return redirect('/listar')#redirecionando para o LISTAR
	elif request.method == 'GET':
		return render_template('cadastro.html')

@app.route('/listar', methods=['GET'])
def listar():
	select = "select id, cpf, nome, curso, ensinomedio, datahora from aluno order by nome; "
	conexao = sqlite3.connect('banco.data')
	resultado = conexao.execute(select).fetchall()
	conexao.close()
	return render_template("listar.html", resultado=resultado)

@app.route('/remover', methods=['GET'])
def remover() :
	id = request.values.get('id')
	delete = "delete from aluno where id = '" + id + "'; "
	conexao = sqlite3.connect('banco.data')
	conexao.execute(delete)
	conexao.commit()
	conexao.close()
	return redirect("/listar")
#Edita
@app.route('/editar', methods=['GET'])
def editar():
	id = request.values.get('id')
	cpf  = request.values.get('cpf')
	nome = request.values.get('nome')
	curso = request.values.get('curso')
	ensinomedio = request.values.get('ensinomedio')
	datahora = request.values.get('datahora')

	editar = "update aluno set cpf = "+cpf+ "nome ="+nome+"curso ="+curso+"ensinomedio ="+ensinomedio+"datahora ="+datahora+"where  id = '" + id + "'; "
	conexao = sqlite3.connect('banco.data')
	conexao.execute(editar)
	conexao.commit()
	conexao.close()
	return redirect("/listar")


@app.route('/', methods=['GET', 'POST'])
def inicio():
	return redirect('/listar')
	
app.run(port=5001, use_reloader=True)
