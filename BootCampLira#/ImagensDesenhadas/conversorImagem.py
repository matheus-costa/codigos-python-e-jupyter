#IMPORTAÇÃO DA BIBLIOTECA
import cv2
import os

#CARREGANDO A IMAGEM QUE SERÁ DESENHADA
imagem = cv2.imread("ImagensDesenhadas/imagens/michael.jpeg")

#Tranformando a imagem em preto e brano
imagem_PB = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

#para tornar a imagem em desenho, será invertida as cores
imagem_invertida = cv2.bitwise_not(imagem_PB)

#imagem com blur para parecer um desenho
#ele recebe 3 parâmetros:1°Imagem que será usado o Gaussian, 2° Uma tupla
#quantidade de filtro, 3° desvio padrão
qntd_filtro = 95
#comando abaixo deixa um aspecto mais desenhado na imagem
imagem_blur = cv2.GaussianBlur(imagem_invertida, (qntd_filtro, qntd_filtro ), 0 )
#inverte ás cores da imagem novamente
imagem_blur_invertida = cv2.bitwise_not(imagem_blur)

#aqui eu sobreponho as imagens 

imagem_desenho = cv2.divide(imagem_PB, imagem_blur_invertida, scale = 256.0)
#para que o valor dos pixels não fiquem entre 0 e 1 deixando a imagem estranha, se usa o scale

#printando a imagem na tela
cv2.imshow("Foto Michel",imagem_desenho) 

#os dois comandos abaixo fazem com que a imagem não fique aparecendo várias vezes na tela
cv2.waitKey(0)
cv2.destroyAllWindows()