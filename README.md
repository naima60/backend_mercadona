# backend_mercadona

# Description de l’application
Ceci est une application Django développée pour fournir deux APIREST : produits et catégories représentant le backend qui sera exploité
dans une autre application React pour la partie frontend dont vous trouverez le lien ci-dessous.

# Installation
1. Assurez-vous que Python est installé sur votre machine. Recommandation : Python 3.10.10 

2. Clonez ce dépôt sur votre machine locale en exécutant la commande :
    git clone https://github.com/naima60/backend_mercadona.git
3. Accéder au projet via l’invite de commande
    cd backend_mercadona 
4. Créer un environnement virtuel en exécutant la commande :
    python -m venv my_env
5. Activer l’environnement virtuel en exécutant la commande :
    my_env\Scripts\activate (sous Windows)
6 . Pour installer les dépendances, exécutez la commande :
    pip install -r requirements.txt
7. Ouvrez le projet avec un éditeur de code comme Pycharm ou VSCode
8. Ajouter l’environnement virtuel dans le fichier gitignore ainsi:
#Ignore les fichiers de l'environnement virtuel
my_env/

# Configuration
  ## base de données et variable d'environnement
  A. Les personnes qui ont un accès total à mon application doivent juste copier les variables d'environnement que je leur ai déjà communiqué dans un 
  fichier .env qu'ils doivent créer au préalable.

  B. Pour les autres personnes intéressées, veuillez appliquer ce qui suit :  
  1. Créer une base de données PostgreSQL 
  2. Créez un fichier `.env` à la racine du projet
  3. Dans ce fichier, spécifiez les variables d'environnement nécessaires (la clé secrète et les paramètres de base de données) en complétant ce qui suit:
      - SECRET_KEY=votre clé Django (sans ajouter d'espace)
      - DB_NAME=le nom de votre base de données (sans ajouter d'espace)
      - DB_USER=l’utilisateur de la base de données (sans ajouter d'espace)
      - DB_PASSWORD=le mot de passe de votre base de données (sans ajouter d'espace)
      - DB_HOST=le host de votre base de données (sans ajouter d'espace)
      - DB_PORT=le port de votre base de données (généralement c'est 5432) 
   * l'utilisation de ces varibales vous évite d'ajuster le fichier settings.py qui est déjà paramétré avec ces mêmes variables

  ## Migration de la base de données
  1. Pour appliquer les migrations à la base de données, exécutez la commande :
   python manage.py migrate 

# Connexion à l'administration Django
  ## Créer un superuser
  Afin d’accéder à l’administration Django, il convient d’ajouter un super utilisateur (admin) avec la commande :
      python manage.py createsuperuser
  ## lancer le serveur
  1. exécuter la commande : python manage.py runserver
  2. ajouter l'URI /admin/ à l'URL de base pour avoir :  http://127.0.0.1:8000/admin/ 
  3. saisissez le login et mot de passe du superuser
  4. c'est à vous de jouer maintenant : ajouter des catégories, produits, promotions
  5. Vérifier votre base de données si elle contient les éléments saisis

# Utilisation de l’application
1. Pour démarrer le serveur de développement, exécutez la commande :
    python manage.py runserver
2. Accédez à `http://localhost:8000` dans votre navigateur pour vérifier que l'application est en cours d'exécution.

# les ApiRest
  ## API Rest produits (lecture seule)
  - http://127.0.0.1:8000/api/product/ : [GET] => affiche les produits (id, libellé, description, prix normal, remise (si prix remisé),
  image, id catégorie, l’état active).

  ## API Rest catégories (lecture seule)
  - http://127.0.0.1:8000/api/category/ : [GET] => affiche les catégories (id, libellé et l’état active).

## Structure du projet
- `backend/`: Contient le fichier settings.py qui comporte le paramétrage général de l'application Django.
-`urls.py/`: se trouve dans le dossier backend, il contient les différents endpoints de l’application. 
	  - http://127.0.0.1:8000/ => accès au site (page d’accueil)
    - http://127.0.0.1:8000/admin/  => accéder à l’administration Django
	  - http://127.0.0.1:8000/api/product => Api rest produits
	  - http://127.0.0.1:8000/api/category/ => Api Rest catégories
- `models.py`: se trouve dans le dossier product contient les modèles de base de données.
- `serializers.py`: Sérialiseurs pour convertir les objets en JSON (dossier apiRest)
- `views.py`: Vues pour les endpoints de l'API(dossier apiRest)
- `media/`: contient le répertoire products ou les images des produits sont ajoutés et stockés automatiquement.
- `static/`: contient les fichier statiques CSS, JS
- `templates/`: contient les fichiers.html
- `requirements.txt`: Fichier de dépendances Python.

# lien application React (Frontend)
  ## application déployée : 
  ## application à installer : 

# Auteur
Naima Boutrah



