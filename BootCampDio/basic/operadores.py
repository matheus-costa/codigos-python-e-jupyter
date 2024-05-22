produto_1 = 20
produto_2 = 10

#OPERADORES ARITMÉTICOS

#adição
print(produto_1 + produto_2)

#subtração
print(produto_1 - produto_2)

#divisão
print(produto_1 / produto_2)

#divisão INTEIRA sem valores após o .
print(produto_1 // produto_2)

#multiplicacao
print(produto_1 * produto_2)

#módulo
print(produto_1 % produto_2)

#exponenciação
print(produto_1 ** produto_2)

#OPERADORES DE COMPARAÇÃO

saldo = 200
saque = 200 

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print(saldo < saque)
print(saldo <= saque)

#ATRIBUIÇÃO DE VALOR

saldo = 500
saldo += 200 #atribuição com adição
saldo -= 200 #atribuição com subtração
saldo /= 2   #atribuição com divisão
saldo //= 2  #atribuição com divisão inteira

print(saldo)


#OPERADORES LÓGICOS


saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
#operador E, as duas expressões tem que ser verdadeiras, para que se retorne TRUE

saldo >= saque or saque <= limite
#operador OU, uma das expressões tem que ser verdadeiras, para que se retorne TRUE


not 1000 > 1500
#OPERADOR DE NEGAÇÃO a negação de falso é TRUE



saldo = 1000
saque = 200
limite = 100
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque 
print(exp)
#PARENTESES delimitam a precedência de comparação
exp_Two = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) 
print(exp_Two)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_three = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(exp_three)





#OPERADORES DE IDENTIDADE
#É usado para saber se os objetos ocupam a mesma região na memória

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso 
#True

curso is not nome_curso
#False

saldo is limite
#True

#OPERADORES DE ASSOCIAÇÃO

curso = "Curso de Python"
frutas = ["Laranja", "Uva", "Limão"]
saques = [1500, 100]


"python" in curso
#True

"maçã" not in frutas
#True

200 in saques
#False


