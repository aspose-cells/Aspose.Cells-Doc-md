---  
title: Convertir un graphique Excel en image avec Node.js via C++  
linktitle: Convertir un graphique Excel en image  
type: docs  
weight: 20  
url: /fr/nodejs-cpp/convert-an-excel-chart-to-image/  
description: Apprenez comment convertir des graphiques Excel en images en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Les graphiques sont attrayants visuellement et facilitent la comparaison, l'identification de modèles et de tendances dans les données. Par exemple, au lieu d'analyser des colonnes de chiffres de feuille de calcul, un graphique montre d'un coup d'œil si les ventes chutent ou augmentent, ou comment les ventes réelles se comparent aux ventes projetées. On demande souvent aux personnes de présenter des informations statistiques et graphiques de manière facile à comprendre et à maintenir. Une image aide.  

Parfois, des graphiques sont nécessaires dans une application ou des pages web. Ou il peut être nécessaire pour un document Word, un fichier PDF, une présentation PowerPoint ou une autre application. Dans chaque cas, vous souhaitez rendre le graphique en tant qu'image pour pouvoir l'utiliser ailleurs.  

{{% /alert %}}  

## **Conversion des graphiques en images**  

 Dans les exemples ici, un graphique en secteur et un graphique en colonnes sont convertis en images.  

### **Conversion d'un graphique circulaire en fichier image**  

Tout d'abord, créez un graphique circulaire dans Microsoft Excel, puis convertissez-le en fichier image avec Aspose.Cells for Node.js via C++. Le code dans cet exemple crée une image EMF basée sur le graphique circulaire dans le fichier Excel modèle.  

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
   1. [Téléchargez Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp).  
   1. Installez-le sur votre ordinateur de développement.  

Tous les composants [Aspose](http://www.aspose.com/) fonctionnent en mode d'évaluation lorsqu'ils sont installés pour la première fois. Le mode d'évaluation n'a pas de limite de temps et il ne fait qu'insérer des filigranes dans les documents de sortie.  

1. Créer un projet :  
   1. Lancez votre IDE préféré.  
   1. Créez une nouvelle application console. Cet exemple utilise une application Node.js, mais vous pouvez la créer avec n'importe quel environnement d'exécution JavaScript.  
   1. Ajoutez une référence. Ce projet utilise Aspose.Cells, donc ajoutez une référence à Aspose.Cells for Node.js via C++.  
   1. Écrire le code qui trouve et convertit le graphique. Ci-dessous se trouve le code utilisé par le composant pour accomplir la tâche. Très peu de lignes de code sont utilisées.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open the existing excel file which contains the pie chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "PieChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "PieChart.out.emf"), AsposeCells.ImageType.Emf);
```  

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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open the existing excel file which contains the column chart.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "ColumnChart.xlsx"));

// Get the designer chart (first chart) in the first worksheet of the workbook.
const chart = workbook.getWorksheets().get(0).getCharts().get(0);

// Convert the chart to an image file.
chart.toImage(path.join(dataDir, "ColumnChart.out.jpeg"), AsposeCells.ImageType.Jpeg);
```  

