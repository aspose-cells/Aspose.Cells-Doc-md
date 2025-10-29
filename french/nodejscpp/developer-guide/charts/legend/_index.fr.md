---
title: Gérer la légende des graphiques Excel avec Node.js via C++
description: Apprenez comment utiliser Aspose.Cells for Node.js via C++ pour exploiter efficacement et personnaliser les légendes des graphiques dans Microsoft Excel. Notre guide complet explique la fonctionnalité de la légende, comment y accéder et la modifier, ainsi que comment améliorer la visualisation et la compréhension des données avec des légendes.
keywords: Aspose.Cells for Node.js via C++, Légendes de graphique, Microsoft Excel, Visualisation, Compréhension des données.
linktitle: Légende
type: docs
weight: 50
url: /fr/nodejs-cpp/chart-legend/
---

## **Options de légende**
Aspose.Cells for Node.js via C++ permet également de gérer la légende d'un graphique à l'exécution. L'objet [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/) peut être déplacé, mis à jour et formaté.

|![todo:image_alt_text](chart_legend.png)|

## **Définir la légende du graphique**
Il est simple de gérer la légende du graphique avec Aspose.Cells [Legend](https://reference.aspose.com/cells/nodejs-cpp/legend/).

L'extrait de code suivant montre comment gérer la légende :


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

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

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Move the legend to left
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Left);

// Set font color of the legend
chart.getLegend().getFont().setColor(AsposeCells.Color.Blue);

// Save the file
workbook.save("chart_legend.xlsx");
```

## **Sujets avancés**
- [Définir le texte de l'entrée de la légende du graphique à aucun en utilisant Aspose.Cells](/cells/fr/nodejs-cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
{{< app/cells/assistant language="nodejs-cpp" >}}
