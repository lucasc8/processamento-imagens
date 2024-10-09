# processamento-imagens
trabalho sobre processamento de imagens com opencv em python 
bibliotecas utilizadas: cv2, numpy e matplot

-> Carregamento de imagem
O que o Script faz:
Carrega uma imagem do disco usando cv2.imread().
Verifica se a imagem foi carregada corretamente.
Exibe a imagem em uma janela usando cv2.imshow().
Aguarda que você pressione uma tecla antes de fechar a janela.

-> Detecção de Anomalias
O que o Script faz:
Carrega a imagem de referência e a imagem a ser analisada.
Converte ambas as imagens para escala de cinza e aplica um filtro de desfoque.
Detecta as bordas nas imagens e encontra os contornos.
Compara o número de contornos encontrados e indica se uma anomalia foi detectada.

-> Colorização de imagens
O que o Script faz:
Carrega uma imagem em preto e branco.
Cria uma imagem colorida a partir da imagem em preto e branco.
Aplica cores em regiões específicas da imagem, criando um efeito de colorização básica.
Exibe a imagem original em preto e branco e a imagem colorida.

-> Detecção de contornos, cantos e pontos de atenção
O que o código faz:
Shi-Tomasi: Detecta cantos usando o método Shi-Tomasi.
Harris: Detecta cantos usando o método Harris.
Contornos: Detecta contornos na imagem.
SIFT: Detecta pontos de interesse usando o algoritmo SIFT.



