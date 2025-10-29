---
title: Gérer les titres des graphiques Excel avec Node.js via C++
description: Apprenez à utiliser Aspose.Cells for Node.js via C++ pour ajouter et formater les titres de graphique et d’axes dans Microsoft Excel. Notre guide montrera comment définir différents types de titres, ajuster leur apparence et modifier les titres d’axes pour une meilleure représentation et clarté des données.
keywords: Aspose.Cells for Node.js via C++, Titres de graphique, Titres d’axes, Microsoft Excel, Représentation des données, Apparence.
linktitle: Titres
type: docs
weight: 50
url: /fr/nodejs-cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

Dans les graphiques Excel, il existe 2 types de titres :
1. Titre du graphique 
1. Titres des axes

{{% /alert %}}

## **Options de titre**
Aspose.Cells for Node.js via C++ permet également de gérer les titres du graphique en temps réel. Avec l’objet [Title](https://reference.aspose.com/cells/nodejs-cpp/title/), vous pouvez changer le texte, la police et le format de remplissage pour les titres.

|![todo:image_alt_text](chart_title.png)|

## **Configuration des titres des graphiques ou des axes**
Vous pouvez utiliser Microsoft Excel pour définir les titres d’un graphique et de ses axes dans un environnement WYSIWYG. Aspose.Cells for Node.js via C++ permet également aux développeurs de définir les titres d’un graphique et de ses axes à l’exécution. Tous les graphiques et leurs axes contiennent une propriété [Title](https://reference.aspose.com/cells/nodejs-cpp/title/) qui peut être utilisée pour définir leurs titres comme indiqué dans un exemple ci-dessous.

Le code suivant montre comment définir des titres pour des graphiques et des axes.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

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

// Setting the foreground color of the plot area
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.Blue);

// Setting the foreground color of the chart area
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.Yellow);

// Setting the foreground color of the 1st SeriesCollection area
chart.getNSeries().get(0).getArea().setForegroundColor(AsposeCells.Color.Red);

// Setting the foreground color of the area of the 1st SeriesCollection point
chart.getNSeries().get(0).getPoints().get(0).getArea().setForegroundColor(AsposeCells.Color.Cyan);

// Filling the area of the 2nd SeriesCollection with a gradient
chart.getNSeries().get(1).getArea().getFillFormat().setOneColorGradient(AsposeCells.Color.Lime, 1, AsposeCells.GradientStyleType.Horizontal, 1);

// Setting the title of a chart
chart.getTitle().setText("Title");

// Setting the font color of the chart title to blue
chart.getTitle().getFont().setColor(AsposeCells.Color.Blue);

// Setting the title of category axis of the chart
chart.getCategoryAxis().getTitle().setText("Category");

// Setting the title of value axis of the chart
chart.getValueAxis().getTitle().setText("Value");

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"));
```

## **Sujets avancés**
- [Lire le sous-titre du graphique à partir du fichier ODS](/cells/fr/nodejs-cpp/read-chart-subtitle-from-ods-file/)
{{< app/cells/assistant language="nodejs-cpp" >}}
