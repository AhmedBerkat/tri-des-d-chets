<h1>Waste Classification Project</h1>
Ce projet utilise un Raspberry Pi, un capteur PIR, une ESP CAM, et un modèle de classification basé sur TensorFlow pour détecter et classifier différents types de déchets.
<h3>Description</h3>
Le système fonctionne de la manière suivante :

<p>Détection de Mouvement : Un capteur PIR est utilisé pour détecter tout mouvement.</p>
<p>Capture d'Image : Lorsqu'un mouvement est détecté, une image est capturée par l'ESP CAM.</p
<p>Classification : L'image capturée est ensuite classifiée par un modèle de machine learning pour déterminer le type de déchet (par exemple : métal, papier, plastique).</p>
<p>Résultat : La classe prédite est affichée dans la console.</p>
<h3>Matériel Requis</h3>
Raspberry Pi (avec Python installé)
Capteur PIR
ESP CAM
<p>Modèle TensorFlow pré-entraîné pour la classification des déchets</p>
<p>Connexion Internet pour la communication avec l'ESP CAM</p>

<h3>Paramètres Clés</h3>

<p>PIR_SENSOR_PIN : Le numéro du GPIO utilisé pour le capteur PIR (par défaut : 17).</p>
<p>ESP_CAM_URL : L'URL de votre ESP CAM (par défaut : http://192.168.43.74/capture).</p>
<h4>Étape 1 :Charger l'Exemple de Serveur Web de Caméra

<p>Allez dans <b> Fichier -> Exemples -> esp32 -> Camera -> CameraWebServer.</b></p>
<p<decomenter  la ligne  <b> #define CAMERA_MODEL_AI_THINKER // Has PSRAM  </b></p>
</h4>
<h4>Étape 2 : Connectez l'ESP CAM à votre Réseau Wi-Fi
 1.Configurer le Code de l'ESP CAM : Assurez-vous que le code de votre ESP CAM contient les informations de votre réseau Wi-Fi (SSID et mot de passe). Ce code connecte l'ESP CAM à votre réseau Wi-Fi.
 2. Téléverser le Code sur l'ESP CAM : Utilisez l'IDE Arduino ou un autre environnement de développement pour téléverser le code sur l'ESP CAM. Une fois cela fait, l'ESP CAM se connectera à votre réseau Wi-Fi.
</h4>

<b>Une fois l'entraînement terminé, le modèle final est sauvegardé dans un fichier avec l'extension .h5, comme waste_classification_model.h5. Ce fichier contient l'architecture du réseau de neurones, les poids des couches, et les informations nécessaires pour prédire de nouvelles données. Cela permet de réutiliser le modèle sans avoir à le réentraîner, ce qui est particulièrement utile pour le déploiement sur un Raspberry Pi où la puissance de calcul est limitée.</b>
