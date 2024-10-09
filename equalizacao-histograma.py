# Importando as bibliotecas necessárias
import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt

# Configurando os parâmetros de exibição de imagens e gráficos
matplotlib.rcParams['image.cmap'] = 'gray'
matplotlib.rcParams['image.interpolation'] = 'bicubic'
#%matplotlib inline

# Carrega uma foto em grayscale
image_path = "img/neel1.jpg"
image = cv2.imread(image_path, 0)

# Calcule o histograma
hist, bins = np.histogram(image.flatten(), 256, [0, 256])

# Compute a função de distribuição acumulada
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

# Plotar histograma e C.D.F.
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Mostrar a imagem em grayscale
axs[0].imshow(image, cmap="gray", vmin=100, vmax=1000) 
axs[0].axis("off")

# Plotar o histograma e a CDF
axs[1].plot(cdf_normalized, color="black", linestyle="--", linewidth=1)
axs[1].hist(image.flatten(), 256, [0, 256], color="r", alpha=0.5)
axs[1].set_xlim([0, 256])
axs[1].legend(("CDF", "Histograma"), loc="upper left")

plt.show()