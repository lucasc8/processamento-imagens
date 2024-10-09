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

# Aplicar Desfoque (Blur)
imagem_blur = cv2.GaussianBlur(imagem_original, (15, 15), 0)

# Detecção de Bordas (Canny)
imagem_canny = cv2.Canny(imagem_original, 100, 200)

# Detecção de Bordas (Sobel)
sobel_x = cv2.Sobel(imagem_original, cv2.CV_64F, 1, 0, ksize=5)  # Sobel na direção X
sobel_y = cv2.Sobel(imagem_original, cv2.CV_64F, 0, 1, ksize=5)  # Sobel na direção Y
imagem_sobel = cv2.magnitude(sobel_x, sobel_y)

# Aplicar Filtro Laplaciano
imagem_laplaciano = cv2.Laplacian(imagem_original, cv2.CV_64F)

# Mostrar as imagens resultantes
mostrar_imagens(
    [imagem_original, imagem_blur, imagem_canny, imagem_sobel.astype(np.uint8), imagem_laplaciano.astype(np.uint8)],
    ['Imagem Original', 'Desfoque (Blur)', 'Detecção de Bordas (Canny)', 'Detecção de Bordas (Sobel)', 'Filtro Laplaciano']
)
