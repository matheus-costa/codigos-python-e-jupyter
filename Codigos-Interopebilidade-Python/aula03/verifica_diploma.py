from flask import Flask, request, json

programa = Flask (__name__, template_folder='.')

@programa.route('/verifica', methods=[ 'POST','GET' ] )
def valida():
    txt = request.get_data()#recebo um json da requisição
    obj = json.loads(txt)#ele carrega o obj JSON e DECODIFICANDO ele
    ensinomedio = obj['ensinomedio']#variável documento, contendo o obj documento que veio de requisição
    obj = {"status" : True }#atribuindo o status é a TRUE para o documento

    if(obj != null)
    return obj


    txt = json.dumps( obj )#codificando o obj python em json

    return txt #retornando o json
