from flask import Flask , render_template
import sqlite3

#
app = Flask(__name__, template_folder='.')

#rota que o usuario vai acessar + método que vai ser usado nesta função
@app.route('/inicio', methods=[ 'GET' ] )
def inicio():
    return render_template('inicio.html')

@app.route('/dinamico', methods=[ 'GET' ]) 
def dinamico():
    frase='Matheus é o cara'
    return render_template('dinamico.html', parametro=frase)


@app.route('/dinamico2', methods=['GET'])
def dinamico2():
    conexao = sqlite3.connect('banco')
    consulta = "select * from pessoa order by nome;"
    resultado = conexao.execute(consulta).fetchall()
    return render_template('dinamico2.html', dados=resultado)
    
app.run( port=5001, use_reloader=True )
