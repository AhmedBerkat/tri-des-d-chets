<h1>Waste Classification Project</h1>
Ce projet utilise un Raspberry Pi, un capteur PIR, une ESP CAM, et un modèle de classification basé sur TensorFlow pour détecter et classifier différents types de déchets.
<h3>Description</h3>
Le système fonctionne de la manière suivante :

Détection de Mouvement : Un capteur PIR est utilisé pour détecter tout mouvement.
Capture d'Image : Lorsqu'un mouvement est détecté, une image est capturée par l'ESP CAM.
Classification : L'image capturée est ensuite classifiée par un modèle de machine learning pour déterminer le type de déchet (par exemple : métal, papier, plastique).
Résultat : La classe prédite est affichée dans la console.
<h3>Matériel Requis</h3>
Raspberry Pi (avec Python installé)
Capteur PIR
ESP CAM
Modèle TensorFlow pré-entraîné pour la classification des déchets
Connexion Internet pour la communication avec l'ESP CAM

<h3>Paramètres Clés</h3>

PIR_SENSOR_PIN : Le numéro du GPIO utilisé pour le capteur PIR (par défaut : 17).
ESP_CAM_URL : L'URL de votre ESP CAM (par défaut : http://192.168.43.74/capture).

Une fois l'entraînement terminé, le modèle final est sauvegardé dans un fichier avec l'extension .h5, comme waste_classification_model.h5. Ce fichier contient l'architecture du réseau de neurones, les poids des couches, et les informations nécessaires pour prédire de nouvelles données. Cela permet de réutiliser le modèle sans avoir à le réentraîner, ce qui est particulièrement utile pour le déploiement sur un Raspberry Pi où la puissance de calcul est limitée.
