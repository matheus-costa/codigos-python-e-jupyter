MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

#IF simples
idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print ("pode tirar a CNH.")

if idade <  MAIOR_IDADE:
     print("Não pode tirar a CNH.")     

#if/else
print("        ")     
print("#Usando if/else")

if idade >= MAIOR_IDADE:
    print ("pode tirar a CNH.")
else:
     print("Não pode tirar a CNH.")  


#ELIF é o ElseIf do Python
print("        ")     
print("#Usando elif")
if idade >= MAIOR_IDADE:
     print ("pode tirar a CNH.")
elif idade >= IDADE_ESPECIAL:
     print("Pode fazer aulas teórias, más não pode fazer aulas práticas.")  
else:   
     print("Não pode tirar a CNH")  


#IF ANINHADO
print("        ")     
print("#IF ANINHADO ")
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 5000 
cheque_especial = 450    


if conta_normal:
   if saldo >= saque:
        print("Valor sacado")
   elif  saque <= (saldo+cheque_especial):  
        print("Valor sacado")   
   else:        
         print("Não foi Possível realizar o saque")    
            
elif conta_universitaria:        
    if saldo >= saque:
        print("Valor sacado") 
    else:        
         print("saldo insuficiente")


#IF TERNÁRIO      
print("        ")        
print("#IF TERNÁRIO")

saldo = 2000
saque = 300 

status = "Sucesso" if saldo > saque  else "Falha"

print(f"{status} ao realizar saque")

#IF TERNÁRIO    
print("        ")     
print("#Estruturas de Repetição")