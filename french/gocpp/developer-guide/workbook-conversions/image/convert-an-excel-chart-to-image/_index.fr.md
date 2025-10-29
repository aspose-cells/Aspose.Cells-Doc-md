---
title: Convertir un graphique Excel en image avec Golang via C++
linktitle: Convertir un graphique Excel en image
type: docs
weight: 20
url: /fr/go-cpp/convert-an-excel-chart-to-image/
description: Apprenez à convertir les graphiques Excel en images en utilisant Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

 Les graphiques sont attrayants visuellement et permettent aux utilisateurs de voir facilement les comparaisons, les modèles et les tendances dans les données. Par exemple, plutôt que d'analyser des colonnes de numéros de feuille de calcul, un graphique montre en un coup d'œil si les ventes diminuent ou augmentent, ou comment les ventes réelles se comparent aux prévisions. Les gens doivent souvent présenter des informations statistiques et graphiques d'une manière facile à comprendre et à maintenir. Une image aide.

 Parfois, des graphiques sont nécessaires dans une application ou sur des pages Web. Ou ils peuvent être nécessaires pour un document Word, un fichier PDF, une présentation PowerPoint ou une autre application. Dans chaque cas, vous souhaitez rendre le graphique sous forme d’image afin de l’utiliser ailleurs.

{{% /alert %}}

## **Conversion des graphiques en images**

 Dans les exemples ici, un graphique en secteur et un graphique en colonnes sont convertis en images.

### **Conversion d'un graphique circulaire en fichier image**

Tout d'abord, créez un graphique circulaire dans Microsoft Excel et convertissez-le ensuite en un fichier image avec Aspose.Cells. Le code de cet exemple crée une image EMF basée sur le graphique circulaire dans le fichier de modèle Microsoft Excel.

|**Sortie : image du graphique circulaire**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Créer un graphique en secteur dans Microsoft Excel:
   1. Ouvrir un nouveau classeur dans Microsoft Excel.
   1. Entrer des données dans une feuille de calcul.
   1. Créez un graphique circulaire basé sur les données.
   1. Enregistrez le fichier.

|**Le fichier d'entrée.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/).
   1. Installez-le sur votre ordinateur de développement.

Tous les composants [Aspose](http://www.aspose.com/) fonctionnent en mode d'évaluation lorsqu'ils sont installés pour la première fois. Le mode d'évaluation n'a pas de limite de temps et il ne fait qu'insérer des filigranes dans les documents de sortie.

1. Créer un projet :
   1. Démarrez votre environnement de développement C++ (par exemple, Visual Studio).
   1. Créez une nouvelle application console.
   1. Ajoutez une référence à Aspose.Cells. Ce projet utilise Aspose.Cells, donc ajoutez une référence à la bibliothèque Aspose.Cells.
   1. Écrire le code qui trouve et convertit le graphique. Ci-dessous se trouve le code utilisé par le composant pour accomplir la tâche. Très peu de lignes de code sont utilisées.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertAnExcelChartToImage.go" >}}
### **Conversion d'un graphique à colonnes en un fichier image**

Tout d'abord, créez un graphique en colonnes dans Microsoft Excel et convertissez-le en fichier image, comme ci-dessus. Après l'exécution du code d'exemple, un fichier JPEG est créé à partir du graphique en colonnes dans le fichier Excel modèle.

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertAnExcelChartToImage-1.go" >}}
