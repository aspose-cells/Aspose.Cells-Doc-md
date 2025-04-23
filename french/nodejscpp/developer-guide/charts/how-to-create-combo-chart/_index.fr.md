---
title: Comment créer un graphique combiné avec Node.js via C++
linktitle: Comment créer un graphique mixte
description: Apprenez à créer un graphique combiné en utilisant Aspose.Cells for Node.js via C++. Notre guide complet démontrera comment combiner différents types de graphiques en un graphique combiné pour une présentation plus efficace des données.
keywords: Aspose.Cells for Node.js via C++, Graphique combiné, Combinaison de types de graphiques, Présentation des données, Visualisation efficace.
type: docs
weight: 73
url: /fr/nodejs-cpp/create-combo-chart/
---

## **Scénarios d'utilisation possibles**
Les graphiques mixtes dans Excel vous permettent de profiter de cette option car vous pouvez facilement combiner deux types de graphiques ou plus pour rendre vos données compréhensibles. Les graphiques mixtes sont utiles lorsque vos données contiennent plusieurs types de valeurs, y compris le prix et le volume. De plus, les graphiques mixtes sont faisables lorsque vos nombres de données changent largement de série en série.
En prenant l'ensemble de données suivant comme exemple, nous pouvons observer que ces données sont assez similaires aux données mentionnées dans [**VHCL**](https://docs.aspose.com/cells/nodejs-cpp/create-volume-high-low-close-stock-chart/). Si nous voulons visualiser la série0, qui correspond à "Revenu Total", sous forme de graphique en courbes, comment devrions-nous procéder?

![todo:image_alt_text](sample.png)
## **Graphique mixte**
Après avoir exécuté le code ci-dessous, vous verrez le graphique mixte tel qu'indiqué ci-dessous.

![todo:image_alt_text](result.png)
## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](combo.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "combo.xlsx");

// Create the workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a stock volume (VHLC)
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeHighLowClose, 15, 0, 34, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Combo Chart");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E12", true);
// Set category data 
chart.getNSeries().get(0).setXValues("A2:A12");  // Corrected method

// Set the Series[1] Series[2] and Series[3] to different Marker Style
for (let j = 0; j < chart.getNSeries().getCount(); j++) {
switch (j) {
case 1:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Circle);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Pink);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 2:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.Orange);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
case 3:
chart.getNSeries().get(j).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Square);
chart.getNSeries().get(j).getMarker().setMarkerSize(15);
chart.getNSeries().get(j).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(j).getMarker().getArea().setForegroundColor(AsposeCells.Color.LightBlue);
chart.getNSeries().get(j).getBorder().setIsVisible(false);
break;
}
}
// Set the chart type for Series[0] 
chart.getNSeries().get(0).setType(AsposeCells.ChartType.Line);
// Set style for the border of first series
chart.getNSeries().get(0).getBorder().setStyle(AsposeCells.LineType.Solid);
// Set Color for the first series
chart.getNSeries().get(0).getBorder().setColor(AsposeCells.Color.DarkBlue);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
