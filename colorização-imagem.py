import cv2
import numpy as np

def colorizar_imagem(imagem_path):
    # Carrega a imagem em preto e branco
    imagem_pb = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)

    # Cria uma imagem colorida a partir da imagem em preto e branco
    imagem_colorida = cv2.cvtColor(imagem_pb, cv2.COLOR_GRAY2BGR)

    # Define as cores que você deseja aplicar (exemplo: vermelho e verde)
    vermelho = np.array([0, 0, 255], dtype=np.uint8)
    verde = np.array([0, 255, 0], dtype=np.uint8)

    # Aplica a cor em áreas específicas (exemplo: região superior)
    imagem_colorida[0:imagem_colorida.shape[0]//2, 0:imagem_colorida.shape[1]] = vermelho
    # Aplica a cor em outra região (exemplo: região inferior)
    imagem_colorida[imagem_colorida.shape[0]//2:imagem_colorida.shape[0], 0:imagem_colorida.shape[1]] = verde

    # Exibe as imagens
    cv2.imshow('Imagem em Preto e Branco', imagem_pb)
    cv2.imshow('Imagem Colorida', imagem_colorida)

    # Espera até que uma tecla seja pressionada
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    caminho_imagem = 'caminho/para/sua/imagem_pb.jpg'  # Substitua pelo caminho da sua imagem em preto e branco
    colorizar_imagem(caminho_imagem)
