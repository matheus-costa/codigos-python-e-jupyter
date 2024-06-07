from flask import Flask, request, json

programa = Flask (__name__, template_folder='.')

@programa.route('/valida', methods=[ 'POST','GET' ] )
def valida():
    txt = request.get_data()#recebo um json da requisição
    obj = json.loads(txt)#ele carrega o obj JSON e decodifica ele
    documento = obj['documento']#variável documento, contendo o obj documento que veio de requisição
    obj = {"status" : True }#atribuindo o status é a TRUE para o documento

    if len(documento) != 11:#verifica se o valor recebido é diferente de 11
       obj = { "status" : False } 

    if not documento.isdigit():#verifica se toda a string é composta por números
        obj = { "status" : False }

    soma = 0 #declaração da variável soma
    #usando um for com a função range e ir iterando de 0 á 9
      #CALCULAR O PRIMEIRO DIGITO IDENTIFICADOR
    for i in range(0, 9):
        n = int(documento[i])#variável 'N' que recebe os valores dos PRIMEIROS 9 número dentro de documento
        m = 10-i #variável 'M' é o multiplicador desta forma ele itera de forma decrescente
        soma = soma + (n*m) #soma é a multiplicação das variáveis N e M 
    resto = soma%11 #calculo do RESTO da divisão do valor de SOMA, dividido por 11

    dv = 11-resto #dv recebe o valor de 11 menos o RESTO
    if dv > 9:#se dv for maior que 9, dv receberá o valor 0
        dv = 0

    if dv != int(documento[9]):#se dv for um valor diferente do valor presente em documento no índice 9
        obj = { "status" : False }#obj será falso
    soma = 0

      #CALCULAR O SEGUNDO IDENTIFICADOR
    for i in range(0, 10):
        n = int(documento[i])
        m = 11-i
        soma = soma + (n*m)
    resto = soma%11
    dv = 11-resto

    if dv > 9:
        dv = 0

    if dv != int(documento[10]):
        obj = { "status" : False }

    txt = json.dumps( obj )#codificando o obj python em json

    return txt #retornando o json

programa.run( port=5001, use_reloader=True )