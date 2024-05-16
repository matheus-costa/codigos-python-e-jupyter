#importação das bibliotecas
import PyPDF2 
import os

#aqui eu faço a instnaicação do meu obj
merger = PyPDF2.PdfMerger()

#esse comando faz com que o Python percorra a pasta e  liste os documentos PDF
lista_arquivos = os.listdir("MesclarDocumentosPDF")

#percorrendo a lista de pdf's
for arquivo in lista_arquivos:
 #verificição se os arquivos são .pdf para que não sejam mesclados arquivos ocultos     
     if ".pdf" in arquivo: 
#aqui eu mesclo todos os arquivos presentes na pasta MesclarDocumentosPDF  
          merger.append(f"MesclarDocumentosPDF/{arquivo}")    

merger.write("PDF_FINAL.PDF")
#aqui é "criado" o documento PDF_FINAL.PDF que contém a mescla do arquivos
