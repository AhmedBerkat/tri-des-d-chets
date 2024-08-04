import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Chemin vers le dossier contenant les sous-dossiers 'metal', 'papier', 'plastique'
data_dir = '/home/pi/waste_classification_project/dataset'

# Gnrateur de donnes avec validation split
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)  # 20% des donnes seront utilises pour la validation

train_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(150, 150),  # Ajustez cette taille si ncessaire
    batch_size=32,
    class_mode='categorical',
    subset='training'  # Ensemble d'entranement
)

val_generator = datagen.flow_from_directory(
    data_dir,
    target_size=(150, 150),  # Ajustez cette taille si necssaire
    batch_size=32,
    class_mode='categorical',
    subset='validation'  # Ensemble de validation
)

# Dfinir le modle
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(3, activation='softmax')  # Ajustez ce nombre selon le nombre de classes
])

# Compiler le mode
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entraner le modle
history = model.fit(
    train_generator,
    epochs=25,  # Ajustez ce nombre si necessaire
    validation_data=val_generator
)

# Sauvegarder le modle
model.save('waste_classifier_model.h5')

