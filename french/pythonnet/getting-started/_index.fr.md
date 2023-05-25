---
title: Commencer
linktitle: Commencer
type: docs
weight: 4
url: /fr/python-net/getting-started/ 
keywords: python, excel, instal
description: Configuration Aspose.Cells for Python via .NET et directives d'installation.
---
##  **Configuration requise**
 Aspose.Cells for Python via .NET est indépendant de la plate-forme API et peut être utilisé sur n'importe quelle plate-forme (Windows et Linux) où[Python](https://www.python.org/downloads/) est installé.

##  **Version Python**
- Python 3.6 ou supérieur

##  **Installation**
###  **Windows:**
 Vous pouvez facilement utiliser Aspose.Cells for Python via .NET à partir de[pypi](https://pypi.org/project/aspose-cells-python/) avec la commande suivante.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux :**
 Vous pouvez facilement utiliser Aspose.Cells for Python via .NET à partir de[pypi](https://pypi.org/project/aspose-cells-python/) avec la commande suivante.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Remarque : vous devez exécuter la commande suivante avant l'installation
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **Mac OS :**
 Vous pouvez facilement utiliser Aspose.Cells for Python via .NET à partir de[pypi](https://pypi.org/project/aspose-cells-python/) avec la commande suivante.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Remarque : Si votre python est Python3.7 (prenez python3.7, par exemple, ici), après avoir installé aspose-cells-python, il peut y avoir les erreurs suivantes
 '/usr/local/lib/libpython3.7m.dylib' (aucun fichier de ce type), '/usr/lib/libpython3.7m.dylib' (aucun fichier de ce type).
 Dans une telle situation, veuillez ajouter la commande suivante à votre bash_profile (Recherchez d'abord où se trouve libpython3.7m.dylib, prenez /Library/Frameworks/Python.framework/Versions/3.7/lib
 par exemple ici)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}
##  **Création de l'application Hello World**

-  Créer un fichier nommé**CréationHelloWorldFile.py** et utilisez l'exemple de code suivant :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Maintenant, enregistrez le code ci-dessus dans "CreatingHelloWorldFile.py" et exécutez "python CreatingHelloWorldFile.py" @invite de commande.

