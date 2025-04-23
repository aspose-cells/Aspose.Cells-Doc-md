---  
title: Ajout d’étiquettes personnalisées aux points de données dans la série du graphique avec Node.js via C++  
linktitle: Ajouter des étiquettes personnalisées aux points de données de la série du graphique  
description: Apprenez comment ajouter des étiquettes personnalisées aux points de données dans la série d’un graphique en utilisant Aspose.Cells for Node.js via C++. Ce guide montrera comment modifier l’apparence, la position et la mise en forme des étiquettes, tout en les liant à votre source de données pour une représentation précise.  
keywords: Aspose.Cells pour Node.js, création de graphiques, étiquettes personnalisées, points de données, série, apparence, position, mise en forme, source de données, représentation.  
type: docs  
weight: 100  
url: /fr/nodejs-cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/  
---  

{{% alert color="primary" %}}  

Vous pouvez ajouter des étiquettes personnalisées aux points de données de la série du graphique à l'aide de la propriété [**DataLabels.getText()**](https://reference.aspose.com/cells/nodejs-cpp/datalabels/#getText--). Cet article expliquera comment utiliser cette propriété pour ajouter des étiquettes personnalisées aux points de données de la série du graphique.

{{% /alert %}}  

Le code suivant crée un **Grafique en dispersion reliés par des lignes avec des marqueurs de données** et ajoute **des étiquettes personnalisées** aux **points de données** dans la **série** du **graphique**. Chaque étiquette personnalisée affiche le **nom de la série** et le **nom du point**. Vous pouvez utiliser tout autre texte à la place.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Put data
sheet.getCells().get(0, 0).putValue(1);
sheet.getCells().get(0, 1).putValue(2);
sheet.getCells().get(0, 2).putValue(3);

sheet.getCells().get(1, 0).putValue(4);
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(1, 2).putValue(6);

sheet.getCells().get(2, 0).putValue(7);
sheet.getCells().get(2, 1).putValue(8);
sheet.getCells().get(2, 2).putValue(9);

// Generate the chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
const chart = sheet.getCharts().get(chartIndex);

chart.getTitle().setText("Test");
chart.getCategoryAxis().getTitle().setText("X-Axis");
chart.getValueAxis().getTitle().setText("Y-Axis");

chart.getNSeries().setCategoryData("A1:C1");

// Insert series
chart.getNSeries().add("A2:C2", false);

let series = chart.getNSeries().get(0);

let pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 1" + "\n" + "Point " + i);
}

// Insert series
chart.getNSeries().add("A3:C3", false);

series = chart.getNSeries().get(1);

pointCount = series.getPoints().getCount();
for (let i = 0; i < pointCount; i++) {
const pointIndex = series.getPoints().get(i);
pointIndex.getDataLabels().setText("Series 2" + "\n" + "Point " + i);
}

workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

