---
title: Axe de date avec Node.js via C++
description: Apprenez comment gérer l axe de date dans Aspose.Cells for Node.js via C++. Notre guide vous aidera à comprendre comment travailler avec différents formats de date, échelles de temps et fréquences d étiquettes.
keywords: Aspose.Cells pour Node.js, axe de date, gestion, formats de date, échelles de temps, fréquences d étiquettes.
type: docs
weight: 200
url: /fr/nodejs-cpp/date-axis/
---

## **Scénarios d'utilisation possibles**
Lorsque vous créez un graphique à partir des données de la feuille de calcul utilisant des dates, et que ces dates sont tracées le long de l'axe horizontal (catégories) du graphique, Aspose.Cells for Node.js via C++ change automatiquement l'axe de catégorie en un axe date (échelle temporelle).
Un axe de date affiche les dates dans l'ordre chronologique à des intervalles ou unités de base spécifiques, tels que le nombre de jours, de mois ou d'années, même si les dates sur la feuille de calcul ne sont pas dans l'ordre séquentiel ou dans les mêmes unités de base.
Par défaut, Aspose.Cells détermine les unités de base pour l'axe de date en fonction de la plus petite différence entre deux dates dans les données de la feuille. Par exemple, si vous avez des données sur les prix d'actions où la différence la plus petite entre les dates est de sept jours, Excel définit l'unité de base en jours, mais vous pouvez la changer en mois ou en années si vous souhaitez voir la performance de l'action sur une période plus longue.

## **Gérez l'axe de date comme Microsoft Excel**
Veuillez voir le code d’exemple ci-dessous qui crée un nouveau fichier Excel et place les valeurs du graphique dans la première feuille. 
Ensuite, nous ajoutons un graphique et définissons le type du [**Axis**](https://reference.aspose.com/cells/nodejs-cpp/axis/) 
à [**Axis.getCategoryType()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getCategoryType--) puis nous définissons les unités de base en jours.

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
// Add the sample values to cells
worksheet.getCells().get("A1").putValue("Date");
// 14 means datetime format
const style = worksheet.getCells().getStyle();
style.setNumber(14);
// Put values to cells for creating chart
worksheet.getCells().get("A2").setStyle(style);
worksheet.getCells().get("A2").putValue(new Date(Date.UTC(2022, 5, 26)));
worksheet.getCells().get("A3").setStyle(style);
worksheet.getCells().get("A3").putValue(new Date(Date.UTC(2022, 4, 22)));
worksheet.getCells().get("A4").setStyle(style);
worksheet.getCells().get("A4").putValue(new Date(Date.UTC(2022, 7, 3)));
worksheet.getCells().get("B1").putValue("Price");
worksheet.getCells().get("B2").putValue(40);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(60);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 9, 6, 21, 13);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);         
// Set the Axis type to Date time
chart.getCategoryAxis().setCategoryType(AsposeCells.CategoryType.TimeScale);
// Set the base unit for CategoryAxis to days
chart.getCategoryAxis().setBaseUnitScale(AsposeCells.TimeUnit.Days);
// Set the direction for the axis text to be vertical
chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Vertical);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set max value of Y axis.
chart.getValueAxis().setMaxValue(70);
// Set major unit.
chart.getValueAxis().setMajorUnit(10);
// Save the file
workbook.save("DateAxis.xlsx");
```
