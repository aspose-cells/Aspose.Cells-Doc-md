---  
title: Gérez les axes des graphiques Excel avec Node.js via C++  
description: Apprenez comment configurer les axes des graphiques dans Aspose.Cells for Node.js via C++. Notre guide vous montrera comment ajuster les axes primaires et secondaires, définir leurs plages et modifier leurs propriétés pour améliorer vos graphiques.  
keywords: Aspose.Cells for Node.js via C++, axes de graphique, configuration, axes primaires, axes secondaires, plage, propriétés.  
linktitle: Axes  
type: docs  
weight: 50  
url: /fr/nodejs-cpp/chart-axes/  
---  

{{% alert color="primary" %}}  

Dans les graphiques Excel, il existe 3 types d'axes :  
1. Axe horizontal (Catégorie) : Axe X  
1. Axe Vertical (Valeur) : Axe des Y  
1. Axe de Profondeur (Série) : Axe des Z  

{{% /alert %}}  

## **Options d'Axe**  
Aspose.Cells for Node.js via C++ permet également de gérer les axes du graphique lors de l'exécution. Avec l'objet [Axis](https://reference.aspose.com/cells/nodejs-cpp/axis/), vous pouvez modifier toutes les options de l'axe comme dans Excel.  

|![todo:image_alt_text](chart_axes.png)|  

## **Gérer les axes des X et Y**  
Dans un graphique Excel, les axes horizontal et vertical sont les deux axes les plus populaires à utiliser.  

Le fragment de code suivant montre comment définir les options des axes X et Y.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "chart_axes.xlsx");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue("Series1");
worksheet.getCells().get("A2").putValue(50);
worksheet.getCells().get("A3").putValue(100);
worksheet.getCells().get("A4").putValue(150);
worksheet.getCells().get("B1").putValue("Series2");
worksheet.getCells().get("B2").putValue(60);
worksheet.getCells().get("B3").putValue(32);
worksheet.getCells().get("B4").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);

// Hiding X axis
chart.getCategoryAxis().setIsVisible(false);

// Setting max value of Y axis
chart.getValueAxis().setMaxValue(200);
// Setting major unit
chart.getValueAxis().setMajorUnit(50);

// Save the file
workbook.save(filePath);
```  

## **Sujets avancés**  
- [Changer la direction des étiquettes des graduations](/cells/fr/nodejs-cpp/change-tick-label-direction/)  
- [Déterminer quels axes existent dans le graphique](/cells/fr/nodejs-cpp/determine-which-axis-exists-in-the-chart/)  
- [Gérer les unités automatiques de l'axe du graphique comme dans Microsoft Excel](/cells/fr/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)  
- [Lire les étiquettes des axes après le calcul du graphique](/cells/fr/nodejs-cpp/read-axis-labels-after-calculating-the-chart/)  
- [Comment définir l'axe des catégories dans un graphique Excel](/cells/fr/nodejs-cpp/how-to-set-category-axis/)  

