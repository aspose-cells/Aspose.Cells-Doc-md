---
title: Pour commencer
linktitle: Pour commencer
type: docs
weight: 4
url: /fr/python-net/getting-started/
description: Apprenez comment installer Aspose.Cells pour Python via .NET et créer une application Hello World.
keywords: Comment installer Aspose.Cells pour Python via .NET dans Windows, Linux et MacOS, directives d installation pour Aspose.Cells pour Python via .NET, programme Hello World en Python Via .NET. 
---

## **Configuration requise**
Aspose.Cells pour Python via .NET est une API indépendante de la plateforme et peut être utilisée sur n'importe quelle plateforme (Windows et Linux) où [Python](https://www.python.org/downloads/) est installé. 

## **Version de Python**
- Python 3.6 ou ultérieure

## **Installation**
### **Windows:**
Vous pouvez facilement utiliser Aspose.Cells pour Python via .NET depuis [pypi](https://pypi.org/project/aspose-cells-python/) avec la commande suivante.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}

### **Linux:**
Vous pouvez facilement utiliser Aspose.Cells pour Python via .NET depuis [pypi](https://pypi.org/project/aspose-cells-python/) avec la commande suivante.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Remarque : Vous devez exécuter la commande suivante avant l'installation
{{< highlight NET >}}
For Ubuntu/Debian: apt-get install libgdiplus 
For CentOS/RHEL/Fedora: yum install libgdiplus 
{{< /highlight >}}

### **MacOS:**
Vous pouvez facilement utiliser Aspose.Cells pour Python via .NET depuis [pypi](https://pypi.org/project/aspose-cells-python/) avec la commande suivante.
{{< highlight NET >}}

 $ pip install aspose-cells-python

{{< /highlight >}}
- Remarque : Si votre Python est Python3.7 (prenez par exemple python3.7 ici), après l'installation de aspose-cells-python, il peut y avoir les erreurs suivantes
  '/usr/local/lib/libpython3.7m.dylib' (aucun fichier de ce type), '/usr/lib/libpython3.7m.dylib' (aucun fichier de ce type) invite.
  Dans une telle situation, veuillez ajouter la commande suivante à votre bash_profile (Trouvez d'abord où se trouve libpython3.7m.dylib, prenez par exemple /Library/Frameworks/Python.framework/Versions/3.7/lib)
  par exemple ici).
{{< highlight NET >}}
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
{{< /highlight >}}

- Remarque : En raison de notre dépendance à la bibliothèque graphique SkiaSharp, si vous rencontrez l'erreur suivante :
**System.DllNotFoundException: Impossible de charger la bibliothèque partagée 'libSkiaSharp' ou l'une de ses dépendances.** veuillez installer SkiaSharp.
{{< highlight NET >}}
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.6
{{< /highlight >}}
Après l'installation, veuillez exécuter la commande suivante 
{{< highlight NET >}}
cp ./SkiaSharp.NativeAssets.macOS.2.88.6/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
{{< /highlight >}}

Bien sûr, si vous voulez simplifier, vous pouvez également télécharger [libSkiaSharp.dylib](libSkiaSharp.dylib) et ensuite **copiez** dans le répertoire **/usr/local/lib**.

## **Comment créer l'application Hello World en utilisant Aspose.Cells pour Python via .NET**

- Créez un fichier nommé **CreatingHelloWorldFile.py** et utilisez le code source suivant :

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CreatingHelloWorldFile.py" >}}

- Enregistrez maintenant le code ci-dessus dans "CreatingHelloWorldFile.py" et exécutez "python CreatingHelloWorldFile.py" @invite de commande.

## **Exemple Python via .NET github**
- Veuillez visiter l'exemple [Python via .NET d'Aspose.Cells](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github pour consulter plus d'exemples de code.


