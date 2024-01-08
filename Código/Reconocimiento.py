"""
Este script de Python utiliza una red neuronal convolucional para realizar el reconocimiento de imágenes. Comienza importando las bibliotecas necesarias, como numpy, os, re, matplotlib, sklearn, y keras.

El script luego define una ruta a un directorio que contiene las imágenes a procesar. Recorre este directorio y todos sus subdirectorios, leyendo cada imagen que encuentra y agregándola a una lista de imágenes. También lleva un registro de cada directorio que visita y cuántas imágenes contiene.

Una vez que ha leído todas las imágenes, el script crea etiquetas para cada imagen basándose en el directorio en el que se encontró. Estas etiquetas se utilizan luego para entrenar la red neuronal.

El script divide las imágenes y las etiquetas en conjuntos de entrenamiento y prueba utilizando la función train_test_split de sklearn. Luego muestra la primera imagen de cada conjunto.

Las imágenes se normalizan dividiéndolas por 255 (el valor máximo de un pixel), y las etiquetas se convierten a un formato de codificación one-hot.

El script luego define y compila un modelo de red neuronal convolucional utilizando keras. Este modelo se entrena con los datos de entrenamiento y se valida con un conjunto de datos de validación.

Una vez que el modelo ha sido entrenado, se guarda para su uso futuro. El script luego evalúa el rendimiento del modelo en los datos de prueba y muestra la pérdida y la precisión.

Finalmente, el script utiliza el modelo para hacer predicciones en un conjunto de nuevas imágenes. Estas imágenes se leen desde el disco, se redimensionan para que coincidan con el tamaño de entrada del modelo, y luego se pasan al modelo para la predicción.
"""

# Resto del código...
# from google.colab import drive
# drive.mount('/c/')
import numpy as np
import os
import re
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow import keras
from keras.utils import to_categorical
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization, LeakyReLU

dirname = os.path.join('E:\\IAparaEco\\ecosistema')
imgpath = dirname + os.sep

images = []
directories = []
dircount = []
prevRoot = ''
cant = 0

print("leyendo imagenes de ", imgpath)

for root, dirnames, filenames in os.walk(imgpath):
    for filename in filenames:
        if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            cant=cant+1
            filepath = os.path.join(root, filename)
            image = plt.imread(filepath)
            images.append(image)
            cant = cant + 1
            filepath = os.path.join(root, filename)
            image = plt.imread(filepath)
            images.append(image)
            b = "Leyendo..." + str(cant)
            print(b, end="\r")
            if prevRoot != root:
                print(root, cant)
                prevRoot = root
                directories.append(root)
                dircount.append(cant)
                cant = 0
dircount.append(cant)

#dircount = dircount[1:]
dircount[0] += 1
print('Directorios leidos:', len(directories))
print("Imagenes en cada directorio", dircount)
print('suma Total de imagenes en subdirs:', sum(dircount))

labels = []
indice = 0
for cantidad in dircount:
    for i in range(cantidad):
        labels.append(indice)
    indice = indice + 1
print("Cantidad etiquetas creadas: ", len(labels))

deportes = []
indice = 0
for directorio in directories:
    name = directorio.split(os.sep)
    print(indice, name[len(name) - 1])
    deportes.append(name[len(name) - 1])
    indice = indice + 1

y = np.array(labels)
X = np.array(images, dtype=np.uint8)  # convierto de lista a numpy

# Encontrando los valores de las etiquetas de entrenamiento
classes = np.unique(y)
nClasses = len(classes)
print('Total de salidas : ', nClasses)
print('Clases de salida : ', classes)

# Mezclar todo y crear los grupos de entrenamiento y testing
train_X, test_X, train_Y, test_Y = train_test_split(X, y, test_size=0.2)
print('Training data shape : ', train_X.shape, train_Y.shape)
print('Testing data shape : ', test_X.shape, test_Y.shape)

plt.figure(figsize=[5, 5])

# Muestra la primera imagen del conjunto de entrenamiento
plt.subplot(121)
plt.imshow(train_X[0, :, :], cmap='gray')
plt.title("Ground Truth : {}".format(train_Y[0]))

# Muestra la primera imagen de los datos de prueba
plt.subplot(122)
plt.imshow(test_X[0, :, :], cmap='gray')
plt.title("Ground Truth : {}".format(test_Y[0]))

train_X = train_X.astype('float32')
test_X = test_X.astype('float32')
train_X = train_X / 255.
test_X = test_X / 255.

# Cambio de etiquetas categoricas a estilo One-hot Encoding
train_Y_one_hot = to_categorical(train_Y)
test_Y_one_hot = to_categorical(test_Y)

# Muestra el cambio
print('Etiqueta original:', train_Y[0])
print('Después de la conversión one-hot:', train_Y_one_hot[0])

train_X, valid_X, train_label, valid_label = train_test_split(train_X, train_Y_one_hot, test_size=0.2, random_state=13)

print(train_X.shape, valid_X.shape, train_label.shape, valid_label.shape)

INIT_LR = 1e-3
epochs = 6
batch_size = 64

sport_model = Sequential()
sport_model.add(Conv2D(32, kernel_size=(3, 3), activation='linear', padding='same', input_shape=(360, 640, 3)))
sport_model.add(LeakyReLU(alpha=0.1))
sport_model.add(MaxPooling2D((2, 2), padding='same'))
sport_model.add(LeakyReLU(alpha=0.1))
sport_model.add(Dropout(0.5))
sport_model.add(Dense(nClasses, activation='softmax'))

sport_model.summary()

sport_model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.Adagrad(lr=INIT_LR, decay=INIT_LR / 100),metrics=['accuracy'])

sport_train = sport_model.fit(train_X, train_label, batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(valid_X, valid_label))

# guardamos la red, para reutilizarla en el futuro, sin tener que volver a entrenar
sport_model.save("ecos_mnist.h5py")

test_eval = sport_model.evaluate(test_X, test_Y_one_hot, verbose=1)

print('Pérdida:', test_eval[0])
print('Presición:', test_eval[1])

accuracy = sport_train.history['accuracy']
val_accuracy = sport_train.history['val_accuracy']
loss = sport_train.history['loss']
val_loss = sport_train.history['val_loss']
epochs = range(len(accuracy))
plt.plot(epochs, accuracy, 'bo', label='Precisión del entrenamiento')
plt.plot(epochs, val_accuracy, 'b', label='Precisión de validación')
plt.title('Precisión de entrenamiento y validación')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Pérdida en entrenamiento')
plt.plot(epochs, val_loss, 'b', label='Pérdida en validación')
plt.title('Pérdida en entrenamiento y validación')
plt.legend()
plt.show()

predicted_classes2 = sport_model.predict(test_X)
predicted_classes=[]
for predicted_sport in predicted_classes2:
    predicted_classes.append(predicted_sport.tolist().index(max(predicted_sport)))
predicted_classes=np.array(predicted_classes)
predicted_classes.shape, test_Y.shape

correct = np.where(predicted_classes==test_Y)[0]
print("Hay %d etiquetas correctas" % len(correct))
for i, correct in enumerate(correct[0:9]):
    plt.subplot(3,3,i+1)
    plt.imshow(test_X[correct].reshape(360,640,3), cmap='gray', interpolation='none')
    plt.title("{}, {}".format(deportes[predicted_classes[correct]],
                                                    deportes[test_Y[correct]]))

    plt.tight_layout()

incorrect = np.where(predicted_classes!=test_Y)[0]
print("Hay %d etiquetas icorrectas" % len(incorrect))
for i, incorrect in enumerate(incorrect[0:9]):
    plt.subplot(3,3,i+1)
    plt.imshow(test_X[incorrect].reshape(360,640,3), cmap='gray', interpolation='none')
    plt.title("{}, {}".format(deportes[predicted_classes[incorrect]],
                                                    deportes[test_Y[incorrect]]))
    plt.tight_layout()

target_names = ["Class {}".format(i) for i in range(nClasses)]
print(classification_report(test_Y, predicted_classes, target_names=target_names))

test_eval = sport_model.evaluate(test_X, test_Y_one_hot, verbose=1)

print('Pérdida de la prueba:', test_eval[0])
print('Presición de la prueba:', test_eval[1])

from keras import models
from skimage.transform import resize

model = models.load_model('ecos_mnist.h5py')

images=[]
filenames=['laofice.png','gum.png']

for filepath in filenames:
    image = plt.imread(filepath)
    image_resized = resize(image,(360,640,3),preserve_range=True)
    images.append(image_resized)

X = np.array(images, dtype=np.uint8)#convertir de lista a numpy
test_X=X.astype('float32')
test_X=test_X/255.

predicted_classes=model.predict(test_X)
prediccion=predicted_classes[1] #para ver la predicción de la primera foto

print(prediccion)