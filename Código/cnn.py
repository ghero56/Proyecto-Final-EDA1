import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow import keras
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, LeakyReLU
from skimage.transform import resize
from keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

try:
    model = keras.models.load_model("series_cnn.h5py")
    print('Modelo encontrado, cargando "series_cnn.h5py"')
except Exception as e:
    print('ocurrió un error al cargar el modelo: ' + str(e))
    # Directorio principal que contiene subdirectorios para cada clase
    data_dir = 'E:\\IAparaS\\series'

    # Configuración del generador de imágenes
    batch_size = 8
    image_size = (128, 128)

    # Utiliza ImageDataGenerator con flow_from_directory para cargar imágenes por lotes
    datagen = ImageDataGenerator(rescale=1./255)
    data_generator = datagen.flow_from_directory(
        data_dir,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='categorical'
    )

    # Obtener las clases del generador de imágenes
    classes = list(data_generator.class_indices.keys())

    # Imprimir las clases
    print("Clases disponibles:", classes)

    # Obtener el número total de muestras
    total_samples = data_generator.samples

    # Crear el modelo de CNN
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='linear', padding='same', input_shape=(128, 128, 3)))
    model.add(LeakyReLU(alpha=0.1))
    model.add(MaxPooling2D((2, 2), padding='same'))
    model.add(LeakyReLU(alpha=0.1))
    model.add(Dropout(0.5))
    model.add(Flatten())
    model.add(Dense(data_generator.num_classes, activation='softmax' ))

    INIT_LR = 1e-3
    epochs = 10

    # Compilar el modelo
    model.compile(loss=keras.losses.categorical_crossentropy,
                optimizer=keras.optimizers.Adagrad(learning_rate=INIT_LR, decay=INIT_LR / 100),
                metrics=['accuracy'])

    # Entrenar el modelo usando el generador de imágenes
    history = model.fit(data_generator, epochs=epochs, steps_per_epoch=total_samples // batch_size)
    
    # Guardar el modelo entrenado
    model.save("series_cnn.h5py")

# Rutas de las imágenes de prueba
test_filenames = [
    'E:\\IAparaS\\test\\gumball.png',
    'E:\\IAparaS\\test\\loki.jpeg',
    'E:\\IAparaS\\test\\theoffice.png',
    'E:\\IAparaS\\test\\simpson.jpg'
]
model.summary()

# Preprocesar las imágenes de prueba
test_datagen = ImageDataGenerator(rescale=1./255)
test_images = [resize(plt.imread(filepath), (128, 128, 3), preserve_range=True) for filepath in test_filenames]
test_X = np.array(test_images, dtype=np.float32)
# test_X = test_datagen.standardize(test_X)

# Realizar predicciones
predicted_classes = model.predict(test_X)

# Obtener las clases predichas
predicted_labels = np.argmax(predicted_classes, axis=1)

# Imprimir las predicciones
for i, prediction in enumerate(predicted_labels):
    probabilidad = predicted_classes[i][np.argmax(predicted_classes[i])]
    if probabilidad < .75:
        print(f"Predicción para {test_filenames[i]}: Clase más parecida: {prediction}, Con probabilidades de: {predicted_classes[i]}")
    else:
        print(f"Predicción para {test_filenames[i]}: Clase predicha: {prediction}, Con una probabilidad de: {predicted_classes[i][np.argmax(predicted_classes[i])]}")
    image = plt.imread(test_filenames[i])
    plt.imshow(image)
    plt.show()