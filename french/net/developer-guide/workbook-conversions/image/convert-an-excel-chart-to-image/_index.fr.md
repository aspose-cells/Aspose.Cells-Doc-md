---
title: Convertir un graphique Excel en image
type: docs
weight: 20
url: /fr/net/convert-an-excel-chart-to-image/
---

{{% alert color="primary" %}}

Les graphiques sont attrayants visuellement et facilitent la comparaison, l'identification de modèles et de tendances dans les données. Par exemple, au lieu d'analyser des colonnes de chiffres de feuille de calcul, un graphique montre d'un coup d'œil si les ventes chutent ou augmentent, ou comment les ventes réelles se comparent aux ventes projetées. On demande souvent aux personnes de présenter des informations statistiques et graphiques de manière facile à comprendre et à maintenir. Une image aide.

Parfois, les graphiques sont nécessaires dans une application ou sur des pages web. Ou ils pourraient être nécessaires pour un document Word, un fichier PDF, une présentation PowerPoint ou une autre application. Dans tous les cas, vous souhaitez rendre le graphique sous forme d'image afin de pouvoir l'utiliser ailleurs.

{{% /alert %}}

## **Conversion des graphiques en images**

Dans les exemples ci-dessous, un graphique circulaire et un graphique à colonnes sont convertis en images.

### **Conversion d'un graphique circulaire en fichier image**

Tout d'abord, créez un graphique circulaire dans Microsoft Excel et convertissez-le ensuite en un fichier image avec Aspose.Cells. Le code de cet exemple crée une image EMF basée sur le graphique circulaire dans le fichier de modèle Microsoft Excel.

|**Sortie : image du graphique circulaire**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Créer un graphique circulaire dans Microsoft Excel :
   1. Ouvrir un nouveau classeur dans Microsoft Excel.
   1. Entrer des données dans une feuille de calcul.
   1. Créer un graphique circulaire basé sur les données.
   1. Enregistrez le fichier.

|**Le fichier d'entrée.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Téléchargez et installez Aspose.Cells :
   1. [Téléchargez Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
   1. Installez-le sur votre ordinateur de développement.

Tous les composants [Aspose](http://www.aspose.com/) fonctionnent en mode d'évaluation lorsqu'ils sont installés pour la première fois. Le mode d'évaluation n'a pas de limite de temps et il ne fait qu'insérer des filigranes dans les documents de sortie.

1. Créer un projet :
   1. Démarrer Visual Studio.Net.
   1. Créer une nouvelle application console. Cet exemple utilise une application console C#, mais vous pouvez aussi utiliser VB.NET.
   1. Ajouter une référence. Ce projet utilise Aspose.Cells, donc ajoutez une référence à Aspose.Cells, par exemple ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
   1. Écrire le code qui trouve et convertit le graphique. Ci-dessous se trouve le code utilisé par le composant pour accomplir la tâche. Très peu de lignes de code sont utilisées.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingPieChartToImageFile-1.cs" >}}

### **Conversion d'un graphique à colonnes en un fichier image**

Créez d'abord un graphique à colonnes dans Microsoft Excel et convertissez-le en un fichier image, comme indiqué ci-dessus. Après avoir exécuté le code d'exemple, un fichier JPEG est créé à partir du graphique à colonnes dans le fichier Excel modèle.

|**Fichier de sortie : une image de graphique à colonnes.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Créer un graphique à colonnes dans Microsoft Excel :
   1. Ouvrir un nouveau classeur dans Microsoft Excel.
   1. Entrer des données dans une feuille de calcul.
   1. Créer un graphique à colonnes basé sur les données.
   1. Enregistrez le fichier.

|**Fichier d'entrée.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Configurer un projet, avec des références, comme décrit ci-dessus.
1. Convertir le graphique en une image dynamiquement. Voici le code utilisé par le composant pour accomplir la tâche. Le code est similaire à celui précédent :

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertExcelChartToImage-ConvertingColumnChartToImage-1.cs" >}}
