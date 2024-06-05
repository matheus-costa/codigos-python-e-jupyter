from flask import Flask , render_template
import sqlite3 

#instância do obj flask
#name remete ao nome do sistema
#template é usado paa ajudar o python a encontrar os arquivos
app = Flask(__name__, template_folder='.')

#rota que o usuario vai acessar + método que vai ser usado nesta função
#metódo GET envia dados pela URL
@app.route('/inicio', methods=[ 'GET' ] )
def inicio():
    return render_template('inicio.html')

#segunda fora
@app.route('/dinamico', methods=[ 'GET' ]) 
def dinamico():
    frase='Matheus é o cara'
    return render_template('dinamico.html', parametro=frase)

#terceira rota
@app.route('/dinamico2', methods=['GET'])
def dinamico2():
    conexao = sqlite3.connect('banco')#sqlite3 conetando com banco de dados
    consulta = "select * from pessoa order by nome;"#consulta em sql
#execução da consulta selecionando tudo
    resultado = conexao.execute(consulta).fetchall()
#uso o render_template, para que seja procurado o arquivo dinamico
#esse arquivo dinamico dois espera receber uma variável DADOS 
#a variável DADOS desta aplicação recebe a consulta em SQL
    return render_template('dinamico2.html', dados=resultado)

#aqui mandamos a aplicação rodar.
#reloader faz com o que a plicação seja atualizada automaticamente MÁS SOMENTE
#este bloco de código será atualizado
app.run( port=5001, use_reloader=True )
