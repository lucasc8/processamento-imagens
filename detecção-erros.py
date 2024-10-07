import cv2
import numpy as np

def detectar_anomalias(imagem_referencia_path, imagem_test_path):
    # Carrega as imagens
    imagem_referencia = cv2.imread(imagem_referencia_path)
    imagem_test = cv2.imread(imagem_test_path)

    # Verifica se as imagens foram carregadas
    if imagem_referencia is None or imagem_test is None:
        print("Erro ao carregar as imagens.")
        return

    # Conversão para escala de cinza
    imagem_referencia_gray = cv2.cvtColor(imagem_referencia, cv2.COLOR_BGR2GRAY)
    imagem_test_gray = cv2.cvtColor(imagem_test, cv2.COLOR_BGR2GRAY)

    # Redimensionamento para garantir que ambas as imagens tenham o mesmo tamanho
    imagem_referencia_gray = cv2.resize(imagem_referencia_gray, (800, 600))
    imagem_test_gray = cv2.resize(imagem_test_gray, (800, 600))

    # Aplicação de um filtro de desfoque
    imagem_referencia_blur = cv2.GaussianBlur(imagem_referencia_gray, (5, 5), 0)
    imagem_test_blur = cv2.GaussianBlur(imagem_test_gray, (5, 5), 0)

    # Detecção de bordas
    bordas_referencia = cv2.Canny(imagem_referencia_blur, 100, 200)
    bordas_test = cv2.Canny(imagem_test_blur, 100, 200)

    # Encontrar contornos
    contornos_referencia, _ = cv2.findContours(bordas_referencia, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contornos_test, _ = cv2.findContours(bordas_test, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Desenhar contornos nas imagens
    imagem_referencia_contornos = cv2.drawContours(np.zeros_like(imagem_referencia), contornos_referencia, -1, (255, 0, 0), 1)
    imagem_test_contornos = cv2.drawContours(np.zeros_like(imagem_test), contornos_test, -1, (255, 0, 0), 1)

    # Exibir imagens
    cv2.imshow('Contornos Referência', imagem_referencia_contornos)
    cv2.imshow('Contornos Teste', imagem_test_contornos)

    # Verifica se há diferença significativa nos contornos
    if len(contornos_test) > len(contornos_referencia):
        print("Anomalia detectada: há mais contornos na imagem de teste.")
    else:
        print("Nenhuma anomalia detectada.")

    # Espera até que uma tecla seja pressionada
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    imagem_referencia_path = 'caminho/para/imagem_referencia.jpg'  # Imagem normal
    imagem_test_path = 'caminho/para/imagem_test.jpg'              # Imagem a ser analisada

    detectar_anomalias(imagem_referencia_path, imagem_test_path)
