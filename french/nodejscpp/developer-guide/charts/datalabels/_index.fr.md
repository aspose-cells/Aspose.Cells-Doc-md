---  
title: Gérer DataLabels des graphiques Excel avec Node.js via C++  
description: Apprenez à gérer efficacement les étiquettes de données dans les graphiques Excel en utilisant Aspose.Cells for Node.js via C++. Ce guide complet couvre diverses tâches de gestion, notamment l’ajout, la suppression et la modification des étiquettes pour améliorer la lisibilité et la convivialité du graphique.  
keywords: Aspose.Cells pour Node.js, graphiques Excel, étiquettes de données, gestion, lisibilité, convivialité, ajout, suppression, modification.  
linktitle: Étiquettes de données  
type: docs  
weight: 50  
url: /fr/nodejs-cpp/insert-datalabels-to-chart/  
---  

{{% alert color="primary" %}}  

Les étiquettes de données sont une partie importante d'un graphique.  
Nous pouvons facilement connaître la valeur, le pourcentage, etc. de chaque série.  

{{% /alert %}}  

## **Options d'étiquettes de données**  
Aspose.Cells for Node.js via C++ permet également de gérer les étiquettes de données du graphique à l’exécution, avec l’objet [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/), il est simple de déplacer, mettre à jour et formater les étiquettes de données du graphique.  

|![todo:image_alt_text](chart_datalabels.png)|  

## **Gérer les étiquettes de données du graphique**  
Il est simple de gérer les étiquettes de données du graphique avec Aspose.Cells [DataLabels](https://reference.aspose.com/cells/nodejs-cpp/datalabels/).  

L'extrait de code suivant montre comment gérer DataLabels :  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(60);
worksheet.getCells().get("B2").putValue(32);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Show value labels
chart.getNSeries().get(0).getDataLabels().setShowValue(true);
// Show series name labels
chart.getNSeries().get(1).getDataLabels().setShowSeriesName(true);
// Move labels to center
chart.getNSeries().get(1).getDataLabels().setPosition(AsposeCells.LabelPositionType.Center);

// Save the file
workbook.save("chart_datalabels.xlsx");
```  

## **Sujets avancés**  
- [Ajouter des étiquettes personnalisées aux points de données de la série du graphique](/cells/fr/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)  
- [Désactiver le retour à la ligne pour les étiquettes de données du graphique](/cells/fr/nodejs-cpp/disable-text-wrapping-for-data-labels-of-the-chart/)  
- [Redimensionner la forme de l'étiquette de données du graphique pour s'adapter au texte](/cells/fr/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/)  
- [Étiquette de données personnalisée Rich Text du point de graphique](/cells/fr/nodejs-cpp/rich-text-custom-data-label-of-chart-point/)  
- [Définir le type de forme des étiquettes de données du graphique](/cells/fr/nodejs-cpp/set-the-shape-type-of-data-labels-of-chart/)  
- [Affichage de la plage de cellules sous forme d'étiquettes de données](/cells/fr/nodejs-cpp/showing-cell-range-as-the-data-labels/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
