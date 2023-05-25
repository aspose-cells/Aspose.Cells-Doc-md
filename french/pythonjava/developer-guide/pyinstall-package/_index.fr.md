---
title: Utilisation de PyInstaller pour distribuer facilement les applications Python
linktitle: Paquet utilisant Pyinstaller
type: docs
weight: 10
url: /fr/python-java/pyinstaller-python/
description: Empaquetez le code python dans exe via pyinstaller.
---
##  **A quoi sert PyInstaller ?**
PyInstaller lit un script Python écrit par vous. Il analyse votre code pour découvrir tous les autres modules et bibliothèques dont votre script a besoin pour s'exécuter. Ensuite, il collecte des copies de tous ces fichiers, y compris l'interpréteur actif Python !

##  **Pourquoi utiliser Pyinstaller pour empaqueter Python ?**
PyInstaller est utilisé pour empaqueter le code Python dans des applications exécutables autonomes pour divers systèmes d'exploitation. Il prend un script Python et génère un seul fichier exécutable qui contient toutes les dépendances nécessaires et peut être exécuté sur des ordinateurs sur lesquels Python n'est pas installé. Cela permet une distribution et un déploiement faciles des applications Python, car l'utilisateur n'a pas besoin d'avoir Python et tous les modules requis installés sur son système pour exécuter l'application. De plus, PyInstaller peut également être utilisé pour créer des exécutables à un seul fichier, qui sont des fichiers exécutables uniques contenant toutes les dépendances requises pour l'application. Cela peut rendre encore plus facile la distribution de l'application, car l'utilisateur n'a besoin de télécharger qu'un seul fichier.

##  **Comment installer PyInstaller**
 PyInstaller est disponible sous forme de package standard Python. Les archives sources des versions publiées sont disponibles sur[PyPi](https://pypi.org/project/pyinstaller/) , mais il est plus facile d'installer la dernière version en utilisant[pépin](https://pip.pypa.io/en/stable/):
{{< highlight "java" >}}

C:\> pip install pyinstaller

{{< /highlight >}}

Pour mettre à niveau l'installation existante de PyInstaller vers la dernière version, utilisez :
{{< highlight "java" >}}

C:\> pip install --upgrade pyinstaller

{{< /highlight >}}
Pour installer la version de développement actuelle, utilisez :
{{< highlight "java" >}}

C:\> pip install https://github.com/pyinstaller/pyinstaller/tarball/

{{< /highlight >}}

##  **Comment créer un EXE en utilisant PyInstaller**
 Nous prendrons un seul fichier python comme exemple pour expliquer en détail les étapes d'empaquetage. Prenez Python 3.11.0 comme exemple après l'installation[aspose.cells](https://pypi.org/project/aspose-cells/).

1.  Créez un exemple de fichier Python nommé[exemple.py](example.py).
{{< highlight "java" >}}

import os
from jpype import *

__cells_jar_dir__ = os.path.dirname(__file__)
addClassPath(os.path.join(__cells_jar_dir__, "aspose-cells-23.1.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcprov-jdk15on-160.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "bcpkix-jdk15on-1.60.jar"))
addClassPath(os.path.join(__cells_jar_dir__, "JavaClassBridge.jar"))

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType, CellsHelper

print(CellsHelper.getVersion())
workbook = Workbook(FileFormatType.XLSX)
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World")
workbook.save("output.xlsx")

jpype.shutdownJVM()

{{< /highlight >}}
1. Créez un dossier en tant que c:\app et copiez example.py (joint) vers c:\app.
1. Ouvrez votre invite de commande et exécutez la commande pyinstaller example.py.
{{< highlight "java" >}}

C:\app> pyinstaller example.py

{{< /highlight >}}
1. Copiez les jars (aspose-cells-xxx.jar, bcprov-jdk15on-160.jar, bcpkix-jdk15on-1.60.jar, JavaClassBridge.jar. Ils existent dans le dossier C:\Python311\Lib\site-packages\asposecells\lib ) à c:\app.
1.  Modifiez le fichier avec le suffixe spec pour ajouter une section de données comme[exemple.spec](example.spec).
![todo:image_alt_text](example.png)
1. Exécutez pyinstaller example.spec dans la fenêtre d'invite de commande.
{{< highlight "java" >}}

C:\app> pyinstaller example.spec

{{< /highlight >}}
1. Basculez le répertoire vers C:\app\dist\example et vous trouverez le fichier example.exe.
