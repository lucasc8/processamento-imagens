import cv2


def main():
    # Caminho da imagem
    image_path = 'C:\Users\lgabr\Imagens\img-processamento\praia1.jpg'  # Substitua pelo caminho da sua imagem

    # Leitura da imagem
    image = cv2.imread(image_path)

    # Verifica se a imagem foi carregada corretamente
    if image is None:
        print("Erro ao carregar a imagem. Verifique o caminho e o formato do arquivo.")
        return

    # Exibição da imagem
    cv2.imshow('Imagem', image)

    # Espera até que uma tecla seja pressionada
    cv2.waitKey(0)

    # Fecha todas as janelas abertas
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
