---  
title: Créer un graphique haute basse close (HLC) avec Node.js via C++  
linktitle: Créer un graphique de stocks High Low Close (HLC)  
description: Apprenez comment créer un graphique de stock haut bas close en utilisant Aspose.Cells for Node.js via C++. Notre guide étape par étape montrera comment tracer des données de marché boursier, y compris les prix haut, bas et de clôture, pour une meilleure analyse et visualisation.  
keywords: Aspose.Cells pour Node.js, graphique de stock haut bas close, données de marché boursier, analyse, visualisation.  
type: docs  
weight: 181  
url: /fr/nodejs-cpp/create-high-low-close-stock-chart/  
---  

## **Scénarios d'utilisation possibles**  
Le graphique de stock haut-bas-close (HLC) utilise quatre colonnes de données. La première colonne est une catégorie, généralement une date mais les noms d'actions peuvent aussi être utilisés. Les trois colonnes suivantes correspondent respectivement aux prix haut, bas et de clôture. La plage de prix pour chaque catégorie est indiquée par une ligne verticale allant du bas au haut, et le prix de clôture est représenté par une marque à droite de cette ligne.  

![todo:image_alt_text](sample.png)  
## **Améliorations de la visibilité dans le graphique**  
Parfois, pour rendre le graphique plus intuitif, nous pouvons modifier l'apparence du marqueur (clôture), ou le faire s'afficher sur l'axe secondaire.  

![todo:image_alt_text](sample2.png)  
## **Code d'exemple**  
Le code d'exemple suivant charge le [fichier Excel d'exemple](High-Low-Close.xlsx) et génère le [fichier Excel de sortie](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "High-Low-Close.xlsx");

// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Create High-Low-Close-Stock Chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.StockHighLowClose, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("High-Low-Close Stock");
// Set the Legend at the bottom of the chart area
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);
// Set data range
chart.setChartDataRange("A1:D9", true);
// Set category data 
chart.getNSeries().setCategoryData("A2:A9");
// Set the marker with the built-in data 
chart.getNSeries().get(2).getMarker().setMarkerStyle(AsposeCells.ChartMarkerType.Dash);
chart.getNSeries().get(2).getMarker().setMarkerSize(20);
chart.getNSeries().get(2).getMarker().getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(2).getMarker().getArea().setForegroundColor(AsposeCells.Color.Maroon);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

