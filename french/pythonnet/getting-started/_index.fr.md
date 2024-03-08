---
title: Commencer
linktitle: Commencer
type: docs
weight: 4
url: /fr/python-net/getting-started/
description: Découvrez comment installer Aspose.Cells for Python via .NET et créer l'application Hello World.
keywords: How to install Aspose.Cells for Python via .NET in Windows Linux and MacOS, installation guidelines for Aspose.Cells for Python via .NET, Python Via .NET Hello World program. 
---
##  **Configuration requise**
 Aspose.Cells for Python via .NET est indépendant de la plate-forme API et peut être utilisé sur n'importe quelle plate-forme (Windows et Linux) où[Python](https://www.python.org/downloads/) est installé.

##  **Version Python**
- Python 3.6 ou supérieur

##  **Installation**
###  **Windows:**
 Vous pouvez facilement utiliser le Aspose.Cells for Python via .NET depuis[Pypi](https://pypi.org/project/aspose-cells-python/) avec la commande suivante.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

###  **Linux :**
 Vous pouvez facilement utiliser le Aspose.Cells for Python via .NET depuis[Pypi](https://pypi.org/project/aspose-cells-python/) avec la commande suivante.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Remarque : vous devez exécuter la commande suivante avant l'installation
{{< highlight "NET" >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

###  **Mac OS :**
 Vous pouvez facilement utiliser le Aspose.Cells for Python via .NET depuis[Pypi](https://pypi.org/project/aspose-cells-python/) avec la commande suivante.
{{< highlight "NET" >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Remarque : si votre python est Python3.7 (prenez python3.7, par exemple, ici), après avoir installé aspose-cells-python, les erreurs suivantes peuvent survenir
 '/usr/local/lib/libpython3.7m.dylib' (aucun fichier de ce type), invite '/usr/lib/libpython3.7m.dylib' (aucun fichier de ce type).
 Dans une telle situation, veuillez ajouter la commande suivante à votre bash_profile (Trouvez d'abord où se trouve libpython3.7m.dylib, prenez /Library/Frameworks/Python.framework/Versions/3.7/lib
 par exemple ici)
{{< highlight "NET" >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Remarque : En raison de notre dépendance à l'égard de la bibliothèque graphique SkiaSharp, si vous rencontrez l'erreur suivante :
**System.DllNotFoundException : impossible de charger la bibliothèque partagée « libSkiaSharp » ou l'une de ses dépendances.** veuillez installer SkiaSharp.
{{< highlight "NET" >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.3
{{< /highlight >}}
 Après l'installation, veuillez exécuter la commande suivante
{{< highlight "NET" >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.3/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

 Bien sûr, si vous souhaitez que ce soit plus simple, vous pouvez également télécharger[libSkiaSharp.dylib](libSkiaSharp.dylib) et puis**copie** il au**/usr/local/lib** annuaire.

##  **Comment créer l'application Hello World à l'aide de Aspose.Cells for Python via .NET**

-  Créez un fichier nommé**Création de HelloWorldFile.py** et utilisez l'exemple de code suivant :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Enregistrez maintenant le code ci-dessus dans "CreatingHelloWorldFile.py" et exécutez l'invite de commande @python CréationHelloWorldFile.py.

##  **Python via .NET Exemple github**
-  Veuillez visiter le[Aspose.Cells for Python via .NET Exemple](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github pour voir plus d'exemples de codes.


