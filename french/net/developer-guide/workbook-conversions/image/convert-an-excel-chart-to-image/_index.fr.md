---
title: Convertir un graphique Excel en image
type: docs
weight: 20
url: /fr/net/convert-an-excel-chart-to-image/
---
{{% alert color="primary" %}}

Les graphiques sont visuellement attrayants et permettent aux utilisateurs de voir facilement des comparaisons, des modèles et des tendances dans les données. Par exemple, plutôt que d'analyser des colonnes de numéros de feuille de calcul, un graphique indique en un coup d'œil si les ventes sont en baisse ou en hausse, ou comment les ventes réelles se comparent aux ventes prévues. On demande souvent aux gens de présenter des informations statistiques et graphiques d'une manière facile à comprendre et à maintenir. Une image aide.

Parfois, des graphiques sont nécessaires dans une application ou des pages Web. Ou il peut être nécessaire pour un document Word, un fichier PDF, une présentation PowerPoint ou une autre application. Dans chaque cas, vous souhaitez afficher le graphique sous forme d'image afin de pouvoir l'utiliser ailleurs.

{{% /alert %}}

## **Conversion de graphiques en images**

Dans les exemples ici, un graphique à secteurs et un caractère de colonne sont convertis en images.

### **Conversion d'un graphique à secteurs en fichier image**

Tout d'abord, créez un graphique à secteurs dans Microsoft Excel, puis convertissez-le en un fichier image avec Aspose.Cells. Le code de cet exemple crée une image EMF basée sur le graphique à secteurs dans le modèle de fichier Excel Microsoft.

|**Sortie : image de graphique à secteurs**|
|:- |
|![tâche : image_autre_texte](convert-an-excel-chart-to-image_1.png)|

1. Créer un camembert dans Microsoft Excel :
 1. A ouvert un nouveau classeur dans Microsoft Excel.
 1. Entrez des données dans une feuille de calcul.
 1. Création d'un graphique à secteurs basé sur les données.
 1. Enregistrez le fichier.

|**Le fichier d'entrée.**|
|:- |
|![tâche : image_autre_texte](convert-an-excel-chart-to-image_2.png)|

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. Installez-le sur votre ordinateur de développement.

 Tout[Aspose](http://www.aspose.com/) les composants fonctionnent en mode d'évaluation lors de la première installation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents de sortie.

1. Créer un projet :
 1. Démarrez Visual Studio.Net.
 1. Créez une nouvelle application console. Cet exemple utilise une application console C#, mais vous pouvez également utiliser VB.NET.
 1. Ajoutez une référence. Ce projet utilise Aspose.Cells donc ajoutez une référence à Aspose.Cells, par exemple ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. Écrivez le code qui trouve et convertit le graphique. Vous trouverez ci-dessous le code utilisé par le composant pour accomplir la tâche. Très peu de lignes de code sont utilisées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Conversion d'un histogramme en fichier image**

Créez d'abord un histogramme dans Microsoft Excel et convertissez-le en fichier image, comme ci-dessus. Après avoir exécuté l'exemple de code, un fichier JPEG est créé sur la base de l'histogramme du modèle de fichier Excel.

|**Fichier de sortie : une image d'histogramme.**|
|:- |
|![tâche : image_autre_texte](convert-an-excel-chart-to-image_3.png)|

1. Créez un histogramme dans Microsoft Excel :
 1. Ouvrez un nouveau classeur dans Microsoft Excel.
 1. Entrez des données dans une feuille de calcul.
 1. Créez un histogramme basé sur les données.
 1. Enregistrez le fichier.

|**Fichier d'entrée.**|
|:- |
|![tâche : image_autre_texte](convert-an-excel-chart-to-image_4.png)|

1. Mettre en place un projet, avec des références, comme décrit ci-dessus.
1. Convertissez le graphique en image dynamiquement. Voici le code utilisé par le composant pour accomplir la tâche. Le code est similaire au précédent :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
