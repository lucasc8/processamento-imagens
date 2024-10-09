import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para exibir imagens
def mostrar_imagens(imagens, titulos):
    n = len(imagens)
    plt.figure(figsize=(20, 10))
    for i in range(n):
        plt.subplot(1, n, i + 1)
        plt.imshow(cv2.cvtColor(imagens[i], cv2.COLOR_BGR2RGB))
        plt.title(titulos[i])
        plt.axis('off')
    plt.show()

# Carregar a imagem
imagem_original = cv2.imread('img/cachorroolhudo.jpg')  # Substitua pelo caminho da sua imagem
imagem_gray = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)

# Detecção de Cantos - Shi-Tomasi
corners_shi_tomasi = cv2.goodFeaturesToTrack(imagem_gray, maxCorners=100, qualityLevel=0.01, minDistance=10)
cantos_shi_tomasi = cv2.drawChessboardCorners(imagem_original.copy(), (1, 1), corners_shi_tomasi, True)

# Detecção de Cantos - Harris
harris_corners = cv2.cornerHarris(imagem_gray, blockSize=2, ksize=3, k=0.04)
imagem_harris = imagem_original.copy()
imagem_harris[harris_corners > 0.01 * harris_corners.max()] = [255, 0, 0]  # Marcar os cantos em vermelho

# Detecção de Contornos
imagem_binaria = cv2.threshold(imagem_gray, 127, 255, cv2.THRESH_BINARY)[1]
contornos, _ = cv2.findContours(imagem_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
imagem_contornos = cv2.drawContours(imagem_original.copy(), contornos, -1, (0, 255, 0), 2)  # Contornos em verde

# Detecção de Pontos de Interesse - SIFT
sift = cv2.SIFT_create()
keypoints_sift, _ = sift.detectAndCompute(imagem_gray, None)
imagem_sift = cv2.drawKeypoints(imagem_original.copy(), keypoints_sift, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)



# Mostrar as imagens resultantes
mostrar_imagens(
    [imagem_original, cantos_shi_tomasi, imagem_harris, imagem_contornos, imagem_sift],
    ['Imagem Original', 'Cantos Shi-Tomasi', 'Cantos Harris', 'Contornos', 'Pontos de Interesse (SIFT)']
)
