---
title: Créer un graphique boursier Volume Open High Low Close (VOHLC) avec Node.js via C++
description: Apprenez comment créer un graphique boursier volume open high low close en utilisant Aspose.Cells for Node.js via C++. Notre guide vous montrera comment tracer des données boursières, y compris le volume, l ouverture, le haut, le bas, et les prix de clôture, sur un graphique pour une meilleure analyse et visualisation.
keywords: Aspose.Cells for Node.js via C++, Graphique boursier Volume Open High Low Close, Données boursières, Analyse, Visualisation.
type: docs
weight: 184
url: /fr/nodejs-cpp/create-volume-open-high-low-close-stock-chart/
---

## **Scénarios d'utilisation possibles**
Le quatrième graphique que nous examinerons est le graphique Volume Open High Low Close. Encore une fois, il est important de répéter que vous devez disposer des données dans le bon ordre. Si vous avez besoin de réarranger votre tableau de données, faites-le avant de configurer votre graphique. Ce graphique inclut une colonne pour le volume immédiatement après la première colonne (catégorie), et les graphiques incluent un graphique en colonnes sur l'axe principal affichant ce volume, tandis que les prix sont déplacés vers l'axe secondaire.

![todo:image_alt_text](data.png)
## **Graphique boursier Volume-Ouverture-Haut-Bas-Fermeture (VHLC)**

![todo:image_alt_text](sample.png)
## **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](Volume-Open-High-Low-Close.xlsx) et génère le [fichier Excel de sortie](out.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Volume-Open-High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockVolumeOpenHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("Volume-Open-High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:F9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set Color for the first series (Volume) data 
chart.getNSeries().get(0).getArea().setForegroundColor(new AsposeCells.Color(79, 129, 189));
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
