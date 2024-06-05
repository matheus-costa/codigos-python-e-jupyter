from flask import Flask, request, json

programa = Flask (__name__, template_folder='.')

@programa.route('/valida', methods=[ 'POST','GET' ] )
def valida():
    txt = request.get_data()#recebo um json da requisição
    obj = json.loads(txt)#ele carrega o obj JSON e decodifica ele
    documento = obj['documento']
    obj = {"status" : True }

    if len(documento) != 11:
       obj = { "status" : False }    
    if not documento.isdigit():#verifica se toda a string é composta por números
        obj = { "status" : False }    

    txt = json.dumps( obj )    

    return txt

programa.run( port=5002, use_reloader=True )