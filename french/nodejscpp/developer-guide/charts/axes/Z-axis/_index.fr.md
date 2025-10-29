---
title: Axe Z avec Node.js via C++
description: Apprenez à travailler avec l’axe Z dans Aspose.Cells for Node.js via C++. Notre guide vous aidera à comprendre comment configurer et personnaliser l’axe Z, y compris son échelle et ses étiquettes, pour améliorer vos graphiques.
keywords: Aspose.Cells for Node.js via C++, axe Z, graphique, configuration, personnalisation, échelle, étiquettes.
type: docs
weight: 210
url: /fr/nodejs-cpp/z-axis/
---

## **Scénarios d'utilisation possibles**
Pour certains graphiques 3D comme la colonne 3D, le cône 3D ou la pyramide 3D, qui ont un axe de série (profondeur), également appelé axe Z, que vous pouvez modifier. Vous pouvez spécifier l’intervalle entre les marques de graduation, les étiquettes d’axe et d’autres opérations.

## ** Gérer l’axe principal et l’axe secondaire comme Microsoft Excel**
Veuillez voir le code d’exemple ci-dessous qui crée un nouveau fichier Excel et place les valeurs du graphique dans la première feuille. Ensuite, nous ajoutons un graphique et définissons le type de graphique à Column3D, puis vous pouvez voir l’axe Z également appelé axe profondeur. 

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
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Put values to cells for creating chart
worksheet.getCells().get("A1").putValue("A");
worksheet.getCells().get("B1").putValue("B");
worksheet.getCells().get("C1").putValue("C");
worksheet.getCells().get("A2").putValue(2);
worksheet.getCells().get("A3").putValue(1);
worksheet.getCells().get("B2").putValue(2);
worksheet.getCells().get("B3").putValue(3);
worksheet.getCells().get("C2").putValue(2);
worksheet.getCells().get("C3").putValue(3);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column3D, 9, 6, 25, 16);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Calculate the chart
chart.calculate();
// Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
chart.setChartDataRange("A2:C3", true);
// Hide the CategoryAxis axis
chart.getCategoryAxis().setIsVisible(false);
// Hide the ValueAxis axis
chart.getValueAxis().setIsVisible(false);
// Save the file
workbook.save("ZAxis.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
