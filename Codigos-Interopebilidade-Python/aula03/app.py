#serviço web que recebe um cpf e verifica se ela tem diploma do ensino médio,
#se não tiver, não entra no ensino superior.

from flask import Flask, json, render_template, request, redirect
import sqlite3
import requests

app = Flask(__name__, template_folder='.')


@app.route('/test', methods=['GET', 'POST'])
def test():
    cpf  = request.values.get('cpf')
    ensinomedio = request.values.get('ensinomedio')

    obj = {"documento" : cpf}
    obje = {'diploma' : ensinomedio}

    txt = json.dumps( obj )
    txtt = json.dumps( obje)

    resposta = requests.post(url="http://localhost:5001/valida")

    txt = resposta.content
    txtt = resposta.content

    obj = json.loads( txt )
    obje = json.loads( txtt) 
    
                    
app.run(port=5003, use_reloader=True)        