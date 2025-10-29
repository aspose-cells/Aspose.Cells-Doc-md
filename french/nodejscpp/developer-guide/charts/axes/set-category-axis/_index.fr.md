---
title: Comment définir l axe des catégories avec Node.js via C++
linktitle: Comment définir l axe des catégories
description: Apprenez comment définir l axe des catégories dans Aspose.Cells for Node.js via C++. Notre guide vous aidera à comprendre comment définir la plage de l’axe des catégories, ajuster ses propriétés et formater ses étiquettes.
keywords: Aspose.Cells for Node.js via C++, axe des catégories, définition, plage, propriétés, formatage.
type: docs
weight: 205
url: /fr/nodejs-cpp/how-to-set-category-axis/
---

## **Scénarios d'utilisation possibles**
Après avoir créé un graphique dans une feuille de calcul, vous pouvez définir l'axe des catégories pour celui-ci. Dans cet article, nous vous montrerons comment définir l'axe des catégories pour un graphique Excel en utilisant Aspose.Cells avec un code d’exemple.

## **Les étapes dans le code d'exemple**

1. Créez un nouveau classeur.

2. Créez un nouveau graphique dans la première feuille de calcul.

3. Ajoutez quelques valeurs aux cellules de la première feuille de calcul.

4. Maintenant, vous pouvez définir l’axe des catégories ; il y a deux méthodes : en utilisant les données de cellules ou en utilisant directement des chaînes, comme indiqué dans le code d’exemple.

5. Définissez l'axe de valeur, puis enregistrez le classeur pour voir le résultat.

## **Code d'exemple**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const dataDir = ""; // Update with your path

// Create a new workbook
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CHART");

// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 8, 0, 20, 10);
const chart = worksheet.getCharts().get(chartIndex);

// Add some values to cells
worksheet.getCells().get("A1").putValue("Sales");
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("A4").putValue(130);
worksheet.getCells().get("A5").putValue(160);
worksheet.getCells().get("A6").putValue(150);
worksheet.getCells().get("B1").putValue("Days");
worksheet.getCells().get("B2").putValue(1);
worksheet.getCells().get("B3").putValue(2);
worksheet.getCells().get("B4").putValue(3);
worksheet.getCells().get("B5").putValue(4);
worksheet.getCells().get("B6").putValue(5);

// Some values in string
const Sales = "100,150,130,160,150";
const Days = "1,2,3,4,5";

// Set Category Axis Data with string
chart.getNSeries().setCategoryData(`{${Days}}`);
// Or you can set Category Axis Data with data in cells
// chart.getNSeries().setCategoryData("B2:B6");

// Add Series to the chart
chart.getNSeries().add("Demand1", true);
// Set value axis with string 
chart.getNSeries().get(0).setValues(`{${Sales}}`);
chart.getNSeries().add("Demand2", true);
// Set value axis with data in cells
chart.getNSeries().get(1).setValues("A2:A6");

// Set some Category Axis properties
chart.getCategoryAxis().getTickLabels().setRotationAngle(45);
chart.getCategoryAxis().getTickLabels().getFont().setSize(8);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

// Save the workbook to view the result file
workbook.save(path + "Output.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
