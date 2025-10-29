---
title: Axe principal et axe second avec Node.js via C++
description: Apprenez à comprendre et à travailler avec les axes principal et secondaire dans Aspose.Cells for Node.js via C++. Notre guide vous aidera à comprendre les différences entre axes principal et secondaire, et comment les configurer et les utiliser efficacement dans vos graphiques.
keywords: Aspose.Cells for Node.js via C++, axes principaux, axes secondaires, compréhension, différences, configuration, utilisation.
type: docs
weight: 190
url: /fr/nodejs-cpp/primary-and-second-axis/
---

## **Scénarios d'utilisation possibles**
Lorsque les nombres dans un graphique varient largement d'une série de données à une autre, ou lorsque vous avez des types de données mélangés (prix et volume), tracez une ou plusieurs séries de données sur un axe vertical (valeur) secondaire. L'échelle de l'axe vertical secondaire affiche les valeurs des séries de données associées. Un axe secondaire fonctionne bien dans un graphique qui montre une combinaison de graphiques en colonnes et en lignes.

## **Gérer les axes primaire et secondaire comme Microsoft Excel**
Veuillez voir le code d’exemple ci-dessous qui crée un nouveau fichier Excel et place les valeurs du graphique dans la première feuille. 
Ensuite, nous ajoutons un graphique et montrons le deuxième axe.

![todo:image_alt_text](excel.png)

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

// Put the sample values used in a chart
worksheet.getCells().get("A1").putValue("Region");
worksheet.getCells().get("A2").putValue("Peking");
worksheet.getCells().get("A3").putValue("New York");
worksheet.getCells().get("A4").putValue("Paris");
worksheet.getCells().get("B1").putValue("Sales Volume");
worksheet.getCells().get("C1").putValue("Growth Rate");
worksheet.getCells().get("B2").putValue(100);
worksheet.getCells().get("B3").putValue(80);
worksheet.getCells().get("B4").putValue(140);
worksheet.getCells().get("C2").putValue(0.7);
worksheet.getCells().get("C3").putValue(0.8);
worksheet.getCells().get("C4").putValue(1.0);

// Create a Scatter chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Scatter, 6, 6, 15, 11);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Add Series
chart.getNSeries().add("B2:C4", true);
// Set the category data
chart.getNSeries().setCategoryData("=Sheet1!$A$2:$A$4");
// Set the Second-Axis
chart.getNSeries().get(1).setPlotOnSecondAxis(true);
// Show the Second-Axis
chart.getSecondValueAxis().setIsVisible(true);
// Set the second series ChartType to line
chart.getNSeries().get(1).setType(AsposeCells.ChartType.Line);
// Set the series name
chart.getNSeries().get(0).setName("Sales Volume");
chart.getNSeries().get(1).setName("Growth Rate");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Fill the PlotArea area with nothing
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the file
workbook.save("PrimaryandSecondaryAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
