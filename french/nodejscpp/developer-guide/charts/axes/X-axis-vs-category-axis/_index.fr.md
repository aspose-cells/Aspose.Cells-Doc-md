---
title: Axe X vs. Axe des catégories avec Node.js via C++
linktitle: Axe des X Vs. Axe des catégories
description: Apprenez à différencier l’axe X de l’axe des catégories dans Aspose.Cells for Node.js via C++. Notre guide vous aidera à comprendre les différences dans leur usage et leurs propriétés, et comment les configurer selon vos besoins.
keywords: Aspose.Cells for Node.js via C++, axe X, axe des catégories, différence, usage, propriétés, configuration.
type: docs
weight: 180
url: /fr/nodejs-cpp/X-axis-vs-category-axis/
---

## **Scénarios d'utilisation possibles**
Il existe différents types d'axes des X. Alors que l'axe des Y est un axe de type Valeur, l'axe des X peut être un axe de type Catégorie ou un axe de type Valeur. En utilisant un axe de Valeur, les données sont traitées comme des données numériques continuellement variables, et le marqueur est placé à un point le long de l'axe qui varie en fonction de sa valeur numérique. En utilisant un axe de Catégorie, les données sont traitées comme une séquence d'étiquettes de texte non numériques, et le marqueur est placé à un point le long de l'axe selon sa position dans la séquence. L'exemple ci-dessous illustre la différence entre les axes de Valeur et de Catégorie.
Nos données d'exemple sont présentées dans le [fichier de tableau d'exemple](sample.png) ci-dessous. La première colonne contient nos données d'axe des X, qui peuvent être traitées comme des catégories ou comme des valeurs. Notez que les nombres ne sont pas également espacés, et ils n'apparaissent même pas dans un ordre numérique.

![todo:image_alt_text](sample.png)
## **Manipulez l'axe des X et l'axe des catégories comme Microsoft Excel**
Nous afficherons ces données sur deux types de graphiques, le premier est un graphique XY (Dispersion) avec l'axe X en tant qu'axe de valeur, le second est un graphique en ligne avec l'axe X en tant qu'axe de catégorie.

![todo:image_alt_text](compare.png)
## **Code d'exemple**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Put the sample values used in charts
worksheet.getCells().get("A2").putValue(1);
worksheet.getCells().get("A3").putValue(3);
worksheet.getCells().get("A4").putValue(2.5);
worksheet.getCells().get("A5").putValue(3.5);
worksheet.getCells().get("B1").putValue("Cats");
worksheet.getCells().get("C1").putValue("Dogs");
worksheet.getCells().get("D1").putValue("Fishes");
worksheet.getCells().get("B2").putValue(7);
worksheet.getCells().get("B3").putValue(6);
worksheet.getCells().get("B4").putValue(5);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("C2").putValue(7);
worksheet.getCells().get("C3").putValue(5);
worksheet.getCells().get("C4").putValue(4);
worksheet.getCells().get("C5").putValue(3);
worksheet.getCells().get("D2").putValue(8);
worksheet.getCells().get("D3").putValue(7);
worksheet.getCells().get("D4").putValue(3);
worksheet.getCells().get("D5").putValue(2);

// Create Line Chart: X as Category Axis
let pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 6, 15, 20, 21);
// Retrieve the Chart object
let chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$5");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);

// Create XY (Scatter) Chart: X as Value Axis
pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);
// Retrieve the Chart object
chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:D5", true);
// Set X values for series 
chart.getNSeries().get(0).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(1).setXValues("{1,3,2.5,3.5}");
chart.getNSeries().get(2).setXValues("{1,3,2.5,3.5}");
// Set the first series name
chart.getNSeries().get(0).setName("Cats");
// Set the second series name
chart.getNSeries().get(1).setName("Dogs");
// Set the third series name
chart.getNSeries().get(2).setName("Fishes");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("XAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
