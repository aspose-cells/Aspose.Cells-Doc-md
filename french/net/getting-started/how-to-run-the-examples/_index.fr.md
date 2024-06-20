---
title: Comment exécuter les exemples
type: docs
weight: 140
url: /fr/net/how-to-run-the-examples/
---

## **Exigences logicielles**
Assurez-vous de remplir les exigences suivantes avant de télécharger et d'exécuter les exemples.

1. Visual Studio 2015 ou version supérieure
1. Gestionnaire de package NuGet installé dans Visual Studio. Il est principalement déjà installé dans Visual Studio 2015. Pour plus de détails sur la façon d'installer le gestionnaire de package NuGet, veuillez consulter : [Installation des outils clients NuGet](https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools)
1. Allez dans Outils->Options->Gestionnaire de package NuGet->Sources de packages et assurez-vous que l'option **nuget.org** est cochée
1. L'exemple de projet utilise la fonction de restauration automatique de package NuGet, vous devez donc avoir une connexion internet active. Si vous n'avez pas de connexion internet active sur la machine où les exemples doivent être exécutés, veuillez consulter [Installation](/cells/fr/net/installation-and-deployment/) et ajouter manuellement la référence à Aspose.Cells.dll dans le projet d'exemple.
## **Télécharger depuis GitHub**
Tous les exemples de Aspose.Cells for .NET sont hébergés sur [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET).
## **Exemples Aspose.Cells**
- Vous pouvez soit cloner le dépôt à l'aide de votre client GitHub préféré, soit télécharger le fichier ZIP à partir de [ici](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Extraire le contenu du fichier ZIP dans un dossier de votre ordinateur. Tous les exemples sont situés dans le dossier **Examples**.
- Il y a un fichier de solution Visual Studio pour les exemples de C# c'est-à-dire **Aspose.Cells.Examples.CSharp.sln**.
- Le projet est créé et maintenu dans Visual Studio 2015.
- Ouvrez le fichier de solution dans Visual Studio et construisez le projet.
- Lors de la première exécution, les dépendances seront automatiquement téléchargées via NuGet. Vous pouvez également télécharger séparément les DLL depuis [ici](https://downloads.aspose.com/cells/net).
- Le dossier **Data** à la racine du dossier **Examples** contient les fichiers d'entrée utilisés par les exemples CSharp. Il est obligatoire de télécharger le dossier **Data** avec le projet d'exemples.
- Ouvrez **RunExamples.cs**, tous les exemples sont appelés à partir d'ici.
- Décommentez les exemples que vous souhaitez exécuter à partir du projet.
## **Exemples Aspose.Cells.GridDesktop**
- Les exemples Aspose.Cells.GridDesktop sont également inclus dans le dépôt [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) et seront disponibles dans le fichier ZIP téléchargeable à partir de [ici](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Tous les exemples sont situés dans le dossier **Examples_GridDesktop**.
- De manière similaire aux exemples Aspose.Cells, le nom du fichier de solution des exemples GridWeb est **Aspose.Cells.GridDesktop.Examples.CSharp.sln**.
- Ouvrez le fichier de solution dans Visual Studio et construisez le projet.
- Toutes les dépendances sont incluses dans le projet d'exemples. Vous pouvez également télécharger les DLL séparément à partir de [ici](https://downloads.aspose.com/cells/net).
- Le dossier **Data** à la racine du dossier **Examples_GridDesktop** contient des fichiers d'entrée utilisés par les exemples. Il est obligatoire de télécharger le dossier **Data** avec le projet d'exemples.
- Ouvrez et exécutez le projet.
- Cliquez sur l'exemple dans le menu que vous souhaitez exécuter à partir du formulaire.
## **Exemples Aspose.Cells.GridWeb**
- Les exemples Aspose.Cells.GridWeb sont également inclus dans le dépôt [Aspose.Cells GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET) et seront disponibles dans le fichier ZIP téléchargeable depuis [ici](https://github.com/aspose-cells/Aspose.Cells-for-.NET/archive/master.zip).
- Tous les exemples se trouvent dans le dossier **Examples_GridWeb**.
- Tout comme les exemples Aspose.Cells, le nom du fichier de solution des exemples GridWeb est **Aspose.Cells.GridWeb.Examples.CSharp.sln**.
- Ouvrez le fichier de solution dans Visual Studio et construisez le projet.
- Toutes les dépendances sont incluses dans les projets d'exemples. Vous pouvez également télécharger les DLL séparément à partir de [ici](https://downloads.aspose.com/cells/net).
- Le dossier **Data** à la racine du dossier **Examples_GridWeb** contient des fichiers d'entrée utilisés par les exemples. Il est obligatoire de télécharger le dossier **Data** avec le projet d'exemples.
- Ouvrez et exécutez **Examples.aspx** dans le projet d'exemples.
- Cliquez sur l'exemple dans le navigateur que vous souhaitez exécuter à partir du projet.
