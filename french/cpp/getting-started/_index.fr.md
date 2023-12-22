---
title: Commencer
type: docs
weight: 10
url: /fr/cpp/getting-started/
description: Comment installer Aspose Cells for C++ et créer une application Hello World.
---
{{% alert color="primary" %}} 

Cette page vous montrera comment installer Aspose Cells for C++ et créer une application Hello World.

{{% /alert %}}

##  **Installation**

###  **Installez Aspose Cells à NuGet**

 NuGet est le moyen le plus simple de télécharger et d’installer Aspose.Cells for C++.
1. Créez un projet Visual Studio Microsoft for C++.
2. Incluez le fichier d'en-tête "Aspose.Cells.h".
3. Ouvrez Visual Studio Microsoft et le gestionnaire de packages NuGet.
 4. Recherchez « aspose.cells.cpp » pour trouver le Aspose.Cells for C++ souhaité.
5. Cliquez sur "Installer", le Aspose.Cells for C++ sera téléchargé et référencé dans votre projet.

**![Installer Aspose Cells à NuGet](InstallThroughNuget.png)**

 Vous pouvez également le télécharger depuis la page Web nuget pour aspose.cells :
[Aspose.Cells for C++ NuGet Paquet](https://www.nuget.org/packages/Aspose.Cells.Cpp/)

[Plus d'étape pour plus de détails](/cells/fr/cpp/installation/)

###  **Une démo pour utiliser le Aspose.Cells for C++ sur le Windows**

1. Téléchargez le Aspose.Cells for C++ à partir de la page suivante :
[Télécharger Aspose.Cells for C++(Windows)](https://downloads.aspose.com/cells/cpp/)
2. Décompressez le package et vous trouverez un exemple expliquant comment utiliser Aspose.Cells for C++.
3. Ouvrez le fichier example.sln avec Visual Studio 2017 ou une version supérieure
4. main.cpp : ce fichier montre comment coder pour tester Aspose.Cells for C++

###  **Une démo pour utiliser Aspose.Cells for C++ sous Linux**

1. Téléchargez le Aspose.Cells for C++ à partir de la page suivante :
[Télécharger Aspose.Cells for C++(Linux)](https://downloads.aspose.com/cells/cpp/)
2. Décompressez le package et vous trouverez un exemple expliquant comment utiliser Aspose.Cells for C++ pour Linux.
3. Assurez-vous que vous êtes dans le chemin où se trouve l'exemple.
4. Exécutez "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Exécutez "cmake --build example/build"

###  **Une démo pour utiliser Aspose.Cells for C++ sur Mac OS**

1. Téléchargez le Aspose.Cells for C++ à partir de la page suivante :
[Télécharger Aspose.Cells for C++ (MacOS)](https://downloads.aspose.com/cells/cpp/)
2. Décompressez le package et vous trouverez un exemple expliquant comment utiliser Aspose.Cells for C++ pour MacOS.
3. Assurez-vous que vous êtes dans le chemin où se trouve l'exemple.
4. Exécutez "cmake -S example -B example/build -DCMAKE_BUILD_TYPE=Release"
5. Exécutez "cmake --build example/build"

##  **Création de l'application Hello World**

Les étapes ci-dessous créent l'application Hello World à l'aide du Aspose.Cells API :

1.  Créez une instance du[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) classe.
1.  Si vous avez un permis, alors[applique-le](/cells/fr/cpp/licensing/).
 Si vous utilisez la version d'évaluation, ignorez les lignes de code liées à la licence.
1. Accédez à n’importe quelle cellule souhaitée d’une feuille de calcul dans le fichier Excel.
1. Insérez les mots "**Hello World!**" dans une cellule consultée.
1. Générez le fichier Excel Microsoft modifié.

La mise en œuvre des étapes ci-dessus est démontrée dans les exemples ci-dessous.

###  **Exemple de code : création d'un nouveau classeur**

L'exemple suivant crée un nouveau classeur à partir de zéro, insère « **Hello World !** » dans la cellule A1 de la première feuille de calcul et enregistre le fichier Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-FirstApplication-1-new.cpp" >}}

###  **Exemple de code : ouverture d'un fichier existant**

L'exemple suivant ouvre un fichier modèle Excel Microsoft existant, récupère une cellule et vérifie la valeur dans la cellule A1.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CPP-Introduction-OpenExistingFile-1-new.cpp" >}}
