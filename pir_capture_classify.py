import RPi.GPIO as GPIO
import time
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import requests

# Configurer le capteur PIR
PIR_SENSOR_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_SENSOR_PIN, GPIO.IN)

# Charger le modele
model = load_model('/home/pi/waste_classification_project/waste_classification_model.h5')

def download_image_from_esp_cam(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f'Image enregistree a {save_path}')
    else:
        print("echec de la capture de l'image depuis l'ESP CAM")

def classify_image(image_path):
    img = image.load_img(image_path, target_size=(150, 150))  # Ajustez la taille si necessaire
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normaliser l'image entre [0, 1]

    predictions = model.predict(img_array)
    class_names = ['metal', 'paper', 'plastic']  
    predicted_class = class_names[np.argmax(predictions)]
    print(f'Classe predite : {predicted_class}')
    return predicted_class

print("Test du capteur PIR (CTRL+C pour quitter)")
time.sleep(2)
print("Pret")

esp_cam_url = 'http://192.168.43.74/capture'  # Remplacez par l'URL de votre ESP CAM

try:
    while True:
        if GPIO.input(PIR_SENSOR_PIN):
            print("Mouvement detecte!")
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            save_path = f'/home/pi/waste_classification_project/captured_image_{timestamp}.jpg'
            
            # Charger l'image depuis l'ESP CAM
            download_image_from_esp_cam(esp_cam_url, save_path)

            # Classifier l'image
            classification = classify_image(save_path)
            
        time.sleep(1)  # Delai pour eviter une surcharge de la boucle

except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()