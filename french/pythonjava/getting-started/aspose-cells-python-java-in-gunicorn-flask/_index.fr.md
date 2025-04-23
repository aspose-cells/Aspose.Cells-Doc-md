---
title: Comment utiliser Aspose.Cells pour Python via Java dans un environnement Gunicorn+Flask
type: docs
weight: 40
url: /fr/python-java/aspose-cells-python-java-in-gunicorn-flask/
description: Cette section compare les composants Aspose.Cells pour Python via Java et certaines autres bibliothèques d opérations Excel Python.
keywords: Excel Python, Python Excel, Python Excel via Java, Python via Java Excel, Pourquoi utiliser Aspose.Cells pour Python via Java, Pourquoi ne pas utiliser xlrd xlwt xlutils xlwings openpyxl xlswriter win32com DataNitro pandas.
---

{{% alert color="primary" %}}

Ce sujet pour débutants montre comment les développeurs peuvent créer une application simple (Hello World) en utilisant Aspose.Cells pour Python via Java. L'application crée un fichier Microsoft Excel avec le mot Hello World dans une cellule spécifiée d'une feuille de calcul.

{{% /alert %}}



## **Préparation complète de l'environnement**

L'environnement de running de l'exemple de ce guide est Ubuntu : 20.04, vous pouvez l'ajuster selon votre situation réelle. Afin de garantir que les exemples puissent fonctionner correctement, nous devons installer certains outils nécessaires dans l'environnement. Voici un guide étape par étape pour vous aider à compléter le processus. Veuillez noter qu'il ne s'agit que d'un guide approximatif, et que les détails spécifiques peuvent varier en fonction de votre système et de vos besoins.

### Python

S'il n'est pas installé, installez-le comme suit :
```
sudo apt install python3 python3-pip # Ubuntu/Debian
#sudo yum install python3 python3-pip # CentOS/RHEL
```
Vérifier la version
```
python3 --version
pip3 --version
```

### Java
S'il n'est pas installé, installez-le comme suit :
```
sudo apt install openjdk-11-jdk # Ubuntu/Debian
#sudo yum install java-17-openjdk # CentOS/RHEL
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
```
Vérifier la version
```
java -version
```

### environnement virtuel virtualenv
L'environnement virtuel est installé selon vos besoins réels. Il est recommandé d'utiliser des environnements virtuels pour gérer les dépendances du projet à la fois en développement et en production.
Veuillez suivre la commande suivante pour l'installation :
```
sudo apt install python3-venv # Ubuntu/Debian
#sudo yum install python3-venv # CentOS/RHEL
```
Créer un environnement virtuel
```
python3 -m venv myenv # Create a virtual environment named myenv in the current directory
```
Démarrer l'environnement virtuel
```
source myenv/bin/activate
```

***Remarque : Si un environnement virtuel est utilisé, les opérations suivantes nécessitent d'activer d'abord l'environnement virtuel correspondant***

### Flask
si non installé, veuillez suivre la commande suivante pour l'installer :
```
pip install Flask
```

### Gunicorn
si non installé, veuillez suivre la commande suivante pour l'installer :
```
pip install gunicorn
```

### Jpype
si non installé, veuillez suivre la commande suivante pour l'installer :
```
pip install jpype1
```

### aspose-cells
si non installé, veuillez suivre la commande suivante pour l'installer :
```
pip install aspose-cells
```

## **Création de l'application Hello World**

Pour créer l'application Hello World à l'aide de l'API Aspose.Cells :

1. Créez une instance de la classe [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook).
1. Appliquer la licence :
   1. Si vous avez acheté une licence, utilisez-la dans votre application pour accéder à toutes les fonctionnalités d'Aspose.Cells.
   1. Si vous utilisez la version d'évaluation du composant (si vous utilisez Aspose.Cells sans licence), ignorez cette étape.
1. Créez un nouveau fichier Microsoft Excel, ou ouvrez un fichier existant dans lequel vous souhaitez ajouter ou mettre à jour du texte.
1. Accédez à n'importe quelle cellule d'une feuille de calcul du fichier Microsoft Excel.
1. Insérez les mots **Bonjour le Monde !** dans une cellule accessible.
1. Générez le fichier Microsoft Excel modifié.

Les exemples ci-dessous démontrent les étapes ci-dessus.

### **Création d'un classeur**

L'exemple suivant crée un nouveau classeur à partir de zéro, écrit les mots "Bonjour le Monde !" dans la cellule A1 sur la première feuille de calcul, et sauvegarde le fichier.

Supposons que nous ayons un chemin de test "/app". Nous réaliserons le travail suivant sous ce chemin de test.

#### Fichiers de l'application Flask : hello.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask1.py" >}}


#### Fichier de la classe de démarrage personnalisée Gunicorn : custom_gunicorn.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask2.py" >}}

#### Démarrer le service

Vérifiez que tous les packages requis par le service sont installés, puis démarrez le service.

Si vous utilisez l'environnement virtuel python3-venv, vous devez créer un environnement virtuel dans le chemin de test, le démarrer, puis installer tous les packages nécessaires.

``` 
python custom_gunicorn.py Or python3 custom_gunicorn.py
``` 

#### Résultats de vérification

1 Ouvrez le navigateur et visitez http://127.0.0.1:5000/.

2 Entrez le nom de fichier que vous souhaitez sauvegarder dans la zone de saisie.

3 Cliquez sur le bouton 'Générer' pour sauvegarder le fichier.

Après cela, vous obtiendrez un fichier Excel nommé d'après le contenu que vous avez saisi dans le chemin de test actuel. La prévisualisation est la suivante :

![todo:image_alt_text](HelloWorldFileInFlask.png)


## Utilisation de Docker

Ou vous pouvez mettre les opérations ci-dessus dans un conteneur Docker. Il est très simple d'utiliser Docker pour construire l'environnement utilisé par l'exemple. Il suffit de mettre les opérations ci-dessus dans le fichier Dockerfile.

Voici un fichier Dockerfile pour référence. Il liste quelques outils nécessaires pour construire l'environnement.

### Dockerfile

``` 
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    openjdk-11-jdk \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "custom_gunicorn.py"]
```

### requirements.txt

Ce fichier est principalement utilisé pour fournir un environnement de dépendances pour les projets Python. Vous pouvez modifier la version dans ce fichier selon vos besoins.

```
aspose-cells==24.11.0
jpype1==1.5.1
Flask==3.0.3
gunicorn==23.0.0
```
### Fichiers principaux

La structure principale des fichiers est la suivante :
```
app/
|-requirements.txt
|-hello.py
|-custom_gunicorn.py
```

### Démarrer le conteneur

Vous pouvez démarrer le conteneur avec la commande suivante
```
docker run --rm -p 127.0.0.1:5000:5000 gunicorn_flask:v1.0 # gunicorn_flask:v1.0 - Image built by Dockerfile
```
