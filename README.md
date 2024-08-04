<h4><b></b> Voir le Système</b>    (https://github.com/user-attachments/assets/22c09e10-258a-4d4f-9bc8-48d9db42f646)</h4>  
<h4><b> Voir le déchet</b>  (https://github.com/user-attachments/assets/8e0ea2c2-6c29-40ef-bd1d-23afc786d5d6)</h4>  

<h1>Waste Classification Project</h1>
Ce projet utilise un Raspberry Pi, un capteur PIR, une ESP CAM, et un modèle de classification basé sur TensorFlow pour détecter et classifier différents types de déchets.
<h2>Description</h2>
Le système fonctionne de la manière suivante :

<p>Détection de Mouvement : Un capteur PIR est utilisé pour détecter tout mouvement.</p>
<p>Capture d'Image : Lorsqu'un mouvement est détecté, une image est capturée par l'ESP CAM.</p
<p>Classification : L'image capturée est ensuite classifiée par un modèle de machine learning pour déterminer le type de déchet (par exemple : métal, papier, plastique).</p>
<p>Résultat : La classe prédite est affichée dans la console.</p>
<h2>Matériel Requis</h2>
Raspberry Pi (avec Python installé)
Capteur PIR
ESP CAM
<p>Modèle TensorFlow pré-entraîné pour la classification des déchets</p>
<p>Connexion Internet pour la communication avec l'ESP CAM</p>

<h2>Paramètres Clés</h2>

<p>PIR_SENSOR_PIN : Le numéro du GPIO utilisé pour le capteur PIR (par défaut : 17).</p>
<p>ESP_CAM_URL : L'URL de votre ESP CAM (par défaut : http://192.168.43.74/capture).</p>
<h4>Étape 1 :Charger l'Exemple de Serveur Web de Caméra

<p>Allez dans <b> Fichier -> Exemples -> esp32 -> Camera -> CameraWebServer.</b></p>
<p<decomenter  la ligne  <b> #define CAMERA_MODEL_AI_THINKER // Has PSRAM  </b></p>
</h4>
<h4>Étape 2 : Connectez l'ESP CAM à votre Réseau Wi-Fi
<p>1.Configurer le Code de l'ESP CAM : Assurez-vous que le code de votre ESP CAM contient les informations de votre réseau Wi-Fi <b>(SSID et mot de passe)</b>. Ce code connecte l'ESP CAM à votre réseau Wi-Fi.</p> 
<p>2. Téléverser le Code sur l'ESP CAM : Utilisez l'IDE Arduino ou un autre environnement de développement pour téléverser le code sur l'ESP CAM. Une fois cela fait, l'ESP CAM se connectera à votre réseau Wi-Fi.</p>
</h4>
</br>
<h3>Une fois l'entraînement terminé, le modèle final est sauvegardé dans un fichier avec l'extension <b>.h5</b>, comme waste_classification_model.h5. Ce fichier contient l'architecture du réseau de neurones, les poids des couches, et les informations nécessaires pour prédire de nouvelles données. Cela permet de réutiliser le modèle sans avoir à le réentraîner, ce qui est particulièrement utile pour le déploiement sur un Raspberry Pi où la puissance de calcul est limitée.</h3>
