#FOR    
print("        ")     
print("#FOR")

texto = input("informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
       print(letra, end="") 

print()

#RANGE interativo  
print("        ")   
print("#RANGE") 

for numero in range(1, 11): #exibe os valores de 0 á 10
    print(numero, end=" ")

#função build in range
print()
print("#função build in range")

for numero in range(0, 51, 5):#exibe a tabuada do 5=[start,stop,step]step=etapa
    print (numero, end=" ")

#função build in range
#WHILE   
print("        ")     
print("#WHILE")

opcao = -1

while opcao != 0:
    opcao = int(input("[1]Sacar \n [2]Extrato \n[0] Sair"))
    if opcao == 1:
       print("sacando...")
    elif opcao == 2:
        print("Extrato..")  
else:
    print("Obrigado por usar o sistema!!")        
    

#BREAK   
print()     
print("#BREAK")

while True: #vai executar em LOOP infinito, exceto quando o valor necessário for inserido

    numero = int(input("informe um número:"))

    if numero == 10:
       break

    print(numero)  

print()   
print("FOR IN RANGE COM BREAK")    

for numero in range(100):
    if numero == 10: #aqui ele corta a execução
        break
    print(f"Fim do Break{numero}")
    
print()   
print("FOR IN RANGE COM CONTINUE")   
for numero in range(30):
    if numero % 2 == 0:
        continue #usando o continue ele pula o valor...
    print(f"Fim do Break{numero}")
    


