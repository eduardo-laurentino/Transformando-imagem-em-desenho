import cv2
import os

#função que recebe o nome da arquivo por parâmetro e faz o tratamento da imagem
def tratar_imagem(arquivo, qtd_filtro):
    #carrega a imagem
    img = cv2.imread(f"imagem/{arquivo}")
    #transforma a imagem em preto e branco
    imagem_pb = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invertida = cv2.bitwise_not(imagem_pb)
    imagem_blur = cv2.GaussianBlur(img_invertida, (qtd_filtro, qtd_filtro), 0)
    imagem_blur_invertida = cv2.bitwise_not(imagem_blur)
    imagem_tratada = cv2.divide(imagem_pb, imagem_blur_invertida, scale=256.0)
    #cv2.imshow("Foto Eduardo", imagem_tratada)
    #salva a imagem na pasta desejada
    cv2.imwrite(f"img_tratada/{arquivo}", imagem_tratada)
lista_imagens = os.listdir("imagem")
#trata todas as imagens de uma pasta
for arquivo in lista_imagens:
    tratar_imagem(arquivo, 95)
