import cv2
import numpy as np

def carregar_e_exibir_imagem(caminho):
    imagem = cv2.imread(caminho)
    cv2.imshow('Imagem Original', imagem)
    cv2.waitKey(0)
    return imagem

def pre_processamento(imagem):
    # Conversão para escala de cinza
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Redimensionamento
    resized = cv2.resize(gray, (400, 400))

    # Equalização de histograma
    equalized = cv2.equalizeHist(resized)

    return equalized

def aplicar_filtros(imagem):
    # Desfoque
    blur = cv2.GaussianBlur(imagem, (5, 5), 0)

    # Detecção de bordas - Canny
    edges = cv2.Canny(blur, 100, 200)

    # Filtro Laplaciano
    laplacian = cv2.Laplacian(blur, cv2.CV_64F)

    return edges, laplacian

def detectar_caracteristicas(imagem):
    # Detecção de cantos de Harris
    harris_corners = cv2.cornerHarris(imagem, 2, 3, 0.04)

    # Detecção de contornos
    contours, _ = cv2.findContours(imagem, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return harris_corners, contours

def transformacoes_geometricas(imagem):
    # Rotação
    (h, w) = imagem.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(imagem, M, (w, h))

    # Translação
    M_trans = np.float32([[1, 0, 50], [0, 1, 100]])
    translated = cv2.warpAffine(imagem, M_trans, (w, h))

    return rotated, translated

def operacoes_morfológicas(imagem):
    kernel = np.ones((5, 5), np.uint8)
    eroded = cv2.erode(imagem, kernel, iterations=1)
    dilated = cv2.dilate(imagem, kernel, iterations=1)
    return eroded, dilated

def segmentacao(imagem):
    # Limiarização
    _, thresh = cv2.threshold(imagem, 127, 255, cv2.THRESH_BINARY)

    # Watershed
    dist_transform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * np.max(dist_transform), 255, 0)
    return thresh, sure_fg

def operacoes_aritmeticas(imagem1, imagem2):
    blended = cv2.addWeighted(imagem1, 0.5, imagem2, 0.5, 0)
    return blended

def salvar_imagem(imagem, caminho):
    cv2.imwrite(caminho, imagem)

def main():
    imagem = carregar_e_exibir_imagem('img/cachorroolhudo.jpg')
    
    pre_processada = pre_processamento(imagem)
    edges, laplacian = aplicar_filtros(pre_processada)
    
    harris_corners, contours = detectar_caracteristicas(pre_processada)

    rotated, translated = transformacoes_geometricas(pre_processada)

    eroded, dilated = operacoes_morfológicas(pre_processada)

    thresh, sure_fg = segmentacao(pre_processada)

    # Salvar exemplos
    salvar_imagem(pre_processada, 'imagem_processada.jpg')
    salvar_imagem(edges, 'edges.jpg')
    salvar_imagem(rotated, 'rotated.jpg')
    salvar_imagem(thresh, 'thresh.jpg')

    cv2.imshow('Edges', edges)
    cv2.imshow('Laplacian', laplacian)
    cv2.imshow('Rotated', rotated)
    cv2.imshow('Eroded', eroded)
    cv2.imshow('Dilated', dilated)
    cv2.imshow('Threshold', thresh)
    cv2.imshow('Sure Foreground', sure_fg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
