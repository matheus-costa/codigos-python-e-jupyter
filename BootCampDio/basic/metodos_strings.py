curso = "python"

print(curso.upper())#exibe tudo em maiúsculo
print()
print(curso.lower())#exibe tudo em minusculo
print()
print(curso.title())#primeiro caracter em maiúsculo
print()
print(curso.strip()) #remove espaços em branco
print()
print(curso.lstrip())#remove o espaço da esquerda
print()
print(curso.rstrip())#remove o espaço da direita
print()
print(curso.center(10, "#"))#aqui eu crio uma nova string centralizada, com o número de caracteres que vão ser ocupadas e o caracter que vão ficar nos espaços sobrando, se não for especificado vão ser caracters em branco
print()
print(".".join(curso))#aqui eu faço a junção do caracter

#INTERPOLAÇÃO DE VARIÁVEIS
print()
print("INTERPOLAÇÃO DE VARIÁVEIS")
print()

#OLD STYLE
print("OLD STYLE")
nome = "Matheus"
idade = 22
profissao = "Cientista de Dados"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

print()

#FORMAT 1° Forma
print("Format")
nome = "Matheus"
idade = 22
profissao = "Cientista de Dados"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}." .format(nome, idade, profissao, linguagem))

print()
print("F- String")
#F- STRING
nome = "Matheus"
idade = 22
profissao = "Cientista de Dados"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.")

print()

PI = 3.14159

print(f"Valor de PI {PI:.2f}")#passo primeiro um tamanho que adiciona um certo espaçamento e o .2 delimito em duas casas depois da virgula

#FATIAMENTO DE STRINGS triplas
print()
print("Linha tripla")
nome = "Theus"

mensagem = f""" Olá, meu nome é{nome}
                 eu estou estudando
                 Python por conta """
print(mensagem)

