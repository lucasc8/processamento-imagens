import cv2

def carregar_imagem(caminho):
    """Carrega uma imagem a partir de um caminho especificado."""
    imagem = cv2.imread(caminho)
    if imagem is None:
        print(f"Erro ao carregar a imagem: {caminho}")
        return None
    return imagem

def converter_para_preto_e_branco(imagem):
    """Converte a imagem colorida para preto e branco."""
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

def redimensionar(imagem, largura, altura):
    """Redimensiona a imagem para as dimensões especificadas."""
    return cv2.resize(imagem, (largura, altura))

def equalizar_histograma(imagem):
    """Equaliza o histograma da imagem em escala de cinza."""
    return cv2.equalizeHist(imagem)

def exibir_imagem(titulo, imagem):
    """Exibe uma imagem em uma janela."""
    cv2.imshow(titulo, imagem)
    cv2.waitKey(0)  # Espera até que uma tecla seja pressionada
    cv2.destroyAllWindows()  # Fecha todas as janelas abertas

def main():
    # Caminho da imagem colorida
    caminho = 'img/cachorroolhudo.jpg'  # Substitua pelo caminho da sua imagem colorida

    # Carregar imagem colorida
    imagem_colorida = carregar_imagem(caminho)

    if imagem_colorida is not None:
        # Converter para preto e branco
        imagem_pb = converter_para_preto_e_branco(imagem_colorida)
        exibir_imagem('Imagem Preto e Branco', imagem_pb)

        # Redimensionar a imagem colorida (aumentar e diminuir)
        imagem_aumentada = redimensionar(imagem_colorida, 800, 600)  # Aumenta o tamanho
        exibir_imagem('Imagem Colorida Aumentada', imagem_aumentada)

        imagem_diminuida = redimensionar(imagem_colorida, 400, 300)  # Diminui o tamanho
        exibir_imagem('Imagem Colorida Diminuida', imagem_diminuida)

        # Equalização de histograma da imagem original (aplicada na versão em P&B)
        imagem_equalizada = equalizar_histograma(imagem_pb)
        exibir_imagem('Imagem Equalizada', imagem_equalizada)

        # Salvar imagens processadas
        cv2.imwrite('imagem_preto_e_branco.jpg', imagem_pb)
        cv2.imwrite('imagem_colorida_aumentada.jpg', imagem_aumentada)
        cv2.imwrite('imagem_colorida_diminuida.jpg', imagem_diminuida)
        cv2.imwrite('imagem_equalizada.jpg', imagem_equalizada)

if __name__ == '__main__':
    main()
