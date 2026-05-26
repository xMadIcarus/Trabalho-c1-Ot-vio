import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# 1. DIVISÃO 80/20 (PARETO)
print("Separando imagens 80% para treino e 20% para teste...")
caminho_das_imagens = "dataset_imagens"

# Pega 80% para ensinar a IA
dados_treino = tf.keras.utils.image_dataset_from_directory(
    caminho_das_imagens, validation_split=0.2, subset="training", seed=123, image_size=(224, 224)
)

# Pega os 20% restantes para a prova
dados_teste = tf.keras.utils.image_dataset_from_directory(
    caminho_das_imagens, validation_split=0.2, subset="validation", seed=123, image_size=(224, 224)
)

# Nomes das categorias (Ex: Metal, Green_glass)
nomes_classes = dados_treino.class_names

# 2. O NOVO TREINAMENTO
print("Criando e treinando a IA do zero...")
# Usando a mesma base do Teachable Machine para ser rápido
modelo_base = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False)
modelo_base.trainable = False 

modelo = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./127.5, offset=-1), # Prepara as cores
    modelo_base,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(len(nomes_classes), activation='softmax')
])

modelo.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# TIRA O PRINT DESSA PARTE RODANDO!
modelo.fit(dados_treino, epochs=5) 

# 3. AVALIAÇÃO COM OS 20%
print("A IA fará a prova agora com os 20%...")
respostas_certas = []
chutes_da_ia = []

for imagens, labels_verdadeiras in dados_teste:
    previsoes = modelo.predict(imagens, verbose=0)
    chutes = np.argmax(previsoes, axis=1)
    
    respostas_certas.extend(labels_verdadeiras.numpy())
    chutes_da_ia.extend(chutes)

# 4. GERANDO AS MÉTRICAS AUTOMATICAMENTE
print("\n--- RESULTADOS PARA O SEU PDF ---")
# Aqui sai a Precisão, Recall, F1-Score e Acurácia de uma vez só!
print(classification_report(respostas_certas, chutes_da_ia, target_names=nomes_classes))

print("\n--- MATRIZ DE CONFUSÃO ---")
print(confusion_matrix(respostas_certas, chutes_da_ia))