---
title: Créer un graphique de stock Open High Low Close (OHLC) avec Node.js via C++
description: Apprenez comment créer un graphique de stock open high low close en utilisant Aspose.Cells for Node.js via C++. Notre guide montrera comment tracer des données de marché boursier, y compris l ouverture, le haut, le bas et les prix de clôture, pour une meilleure analyse et visualisation.
keywords: Aspose.Cells for Node.js via C++, Graphique bourse Open High Low Close, Données boursières, Analyse, Visualisation.
type: docs
weight: 182
url: /fr/nodejs-cpp/create-open-high-low-close-stock-chart/
---

## **Scénarios d'utilisation possibles**
Le graphique Open-High-Low-Close (OHLC) utilise cinq colonnes de données, dans l'ordre : catégorie, ouverture, haut, bas et clôture. La plage de prix dans chaque catégorie est à nouveau indiquée par une ligne verticale, tandis que la plage entre l'ouverture et la clôture est donnée par une barre flottante plus large ; si le prix augmente dans la catégorie (la clôture est supérieure à l'ouverture), la barre est remplie d'une couleur, tandis que si le prix diminue, la barre est remplie d'une autre couleur. Ce type de graphique est souvent appelé un graphique en chandelier.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)
## **Améliorations de la visibilité dans le graphique**
Nous utilisons souvent des couleurs plutôt que du noir et blanc pour indiquer l'augmentation ou la diminution des prix. Dans le premier ensemble de chandeliers ci-dessous, le rouge montre une augmentation et le vert une diminution des prix.

![todo:image_alt_text](sample2.png)
## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](Open-High-Low-Close.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:E9", true);
// Set category data 
chart.getNSeries().getCategoryData("A2:A9");
// Set the DownBars and UpBars with different color
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Red);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
