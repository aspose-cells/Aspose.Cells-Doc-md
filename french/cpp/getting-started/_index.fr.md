---
title: Pour commencer
type: docs
weight: 10
url: /fr/cpp/getting-started/
description: Comment installer Aspose Cells pour C++ et créer une application Hello World.
---

{{% alert color="primary" %}} 

Cette page vous montrera comment installer Aspose Cells pour C++ et créer une application Hello World.

{{% /alert %}}

## **Installation**

### **Installer Aspose Cells via NuGet**

NuGet est le moyen le plus simple de télécharger et d'installer Aspose.Cells for C++. 
1. Créer un projet Microsoft Visual Studio pour C++.
2. Inclure le fichier d'en-tête "Aspose.Cells.h".
3. Ouvrir Microsoft Visual Studio et le gestionnaire de paquets NuGet.
4. Rechercher "aspose.cells.cpp" pour trouver le Aspose.Cells for C++ souhaité. 
5. Cliquez sur "Installer", Aspose.Cells for C++ sera téléchargé et référencé dans votre projet.

**![Installer Aspose Cells via NuGet](InstallThroughNuget.png)**

Vous pouvez aussi le télécharger à partir de la page web de nuget pour aspose.cells : 
[Paquet NuGet Aspose.Cells for C++](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Plus d'étapes pour les détails](/cells/fr/cpp/installation/)

### **Une démo pour utiliser Aspose.Cells for C++ sur Windows**

1. Téléchargez Aspose.Cells for C++ à partir de la page suivante :
[Télécharger Aspose.Cells for C++ (Windows)](https://downloads.aspose.com/cells/cpp/)
2. Décompressez le package et vous trouverez un exemple qui montre comment utiliser Aspose.Cells for C++.
3. Ouvrez le fichier example.sln avec Visual Studio 2017 ou une version ultérieure
4. main.cpp : ce fichier montre comment coder pour tester Aspose.Cells for C++

### **Une démo pour utiliser Aspose.Cells for C++ sur Linux**

1. Téléchargez Aspose.Cells for C++ à partir de la page suivante :
[Télécharger Aspose.Cells for C++ (Linux)](https://downloads.aspose.com/cells/cpp/)
2. Décompressez le package et vous trouverez un exemple qui montre comment utiliser Aspose.Cells for C++ pour Linux.
3. Assurez-vous d'être dans le chemin où se trouve l'exemple.
4. Exécutez "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Exécutez "cmake --build example/build"

### **Une démo pour utiliser Aspose.Cells for C++ sur Mac OS**

1. Téléchargez Aspose.Cells for C++ à partir de la page suivante :
[Télécharger Aspose.Cells for C++ (MacOS)](https://downloads.aspose.com/cells/cpp/)
2. Décompressez le package et vous trouverez un exemple qui montre comment utiliser Aspose.Cells for C++ pour MacOS.
3. Assurez-vous d'être dans le chemin où se trouve l'exemple.
4. Exécutez "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Exécutez "cmake --build example/build"

## **Création de l'application Hello World**

Les étapes ci-dessous créent l'application Bonjour le monde en utilisant l'API Aspose.Cells :

1. Créez une instance de la classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
1. Si vous avez une licence, alors [appliquez-la](/cells/fr/cpp/licensing/).
   Si vous utilisez la version d'évaluation, ignorez les lignes de code relatives à la licence.
1. Accédez à n'importe quelle cellule souhaitée d'une feuille de calcul dans le fichier Excel.
1. Insérez les mots "**Bonjour le monde !**" dans une cellule accessible.
1. Générez le fichier Microsoft Excel modifié.

La mise en œuvre des étapes ci-dessus est démontrée dans les exemples ci-dessous.

### **Exemple de Code: Création d'un Nouveau Classeur**

L'exemple suivant crée un nouveau classeur à partir de zéro, insère "**Bonjour le monde !**" dans la cellule A1 de la première feuille de calcul et enregistre le fichier Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

### **Exemple de Code: Ouverture d'un Fichier Existant**

L'exemple suivant ouvre un fichier de modèle Microsoft Excel existant, récupère une cellule et vérifie la valeur dans la cellule A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
