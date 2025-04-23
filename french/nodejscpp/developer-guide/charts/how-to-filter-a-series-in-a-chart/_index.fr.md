---
title: Trois méthodes pour filtrer les données du graphique avec Node.js via C++
linktitle: Trois méthodes pour filtrer les données du graphique
description: Apprenez à filtrer les graphiques dans Excel en utilisant Aspose.Cells for Node.js via C++. Notre guide complet vous montrera comment appliquer des filtres aux graphiques, personnaliser les éléments du graphique et utiliser les outils d’analyse de données pour de meilleures insights et des décisions éclairées.
keywords: Aspose.Cells for Node.js via C++, Filtrage des graphiques dans Excel, Analyse de données, Prise de décision, Visualisation.
type: docs
weight: 2210
url: /fr/nodejs-cpp/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Filtrer les séries pour afficher un graphique**

### **Étapes pour filtrer les séries d'un graphique dans Excel**
Dans Excel, nous pouvons filtrer des séries spécifiques dans un graphique, ce qui empêche ces séries filtrées d'être affichées dans le graphique. Le graphique original est montré dans **Figure 1**. Cependant, lorsque nous filtrons **Testseries2** et **Testseries4**, le graphique apparaîtra comme dans **Figure 2**.

Dans Aspose.Cells for Node.js via C++, nous pouvons effectuer une opération similaire. Pour un fichier [exemple](seriesFiltered.xlsx) comme celui-ci, si nous voulons filtrer **Testseries2** et **Testseries4**, nous pouvons exécuter le code suivant. De plus, nous maintiendrons deux listes : une ([Chart.getNSeries()](https://reference.aspose.com/cells/nodejs-cpp/chart/#getNSeries--)) pour stocker toutes les séries sélectionnées.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d'exemple](seriesFiltered.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "seriesFiltered.xlsx");
// Create an instance of existing Workbook
let workbook = new AsposeCells.Workbook(filePath);
// Get filtered series list
let nSeriesFiltered = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getFilteredNSeries();
// Get selected series list
let nSeries = workbook.getWorksheets().get(0).getCharts().get("Chart 1").getNSeries();
// Should be 0
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 6
console.log("Visible Series count: " + nSeries.getCount());
// Process from the end to the beginning
nSeries.get(1).setIsFiltered(true);
nSeries.get(0).setIsFiltered(true);
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
workbook.save("seriesFiltered-out.xlsx");
workbook = new AsposeCells.Workbook("seriesFiltered-out.xlsx");
// Should be 2
console.log("Filtered Series count: " + nSeriesFiltered.getCount());
// Should be 4
console.log("Visible Series count: " + nSeries.getCount());
```

## **2. Filtrer les données et laisser le changement de graphique**

Filtrer vos données est une excellente façon de gérer les filtres de graphiques avec beaucoup de données. Lorsque vous filtrez les données, le graphique changera. Un problème que nous devrons résoudre est de faire en sorte que le graphique reste à l'écran. Lors du filtrage, des lignes masquées apparaissent, et parfois, le graphique sera dans ces lignes masquées.

![todo:image_alt_text](Figure3.png)

### **Étapes pour utiliser les filtres de données pour changer le graphique dans Excel**

1. Cliquez à l'intérieur de la plage de vos données.
2. Cliquez sur l'onglet **Données**, et activez les filtres en cliquant sur Filtres. Votre ligne d'en-tête aura des flèches déroulantes.
3. Créez un graphique en allant sur l'onglet **Insertion** et en sélectionnant un graphique à colonnes.
4. Filtrer maintenant vos données en utilisant les flèches déroulantes dans les données. N'utilisez pas les filtres de graphique.

### **Code d'exemple**
Le code d'exemple suivant montre la même fonctionnalité en utilisant Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of Worksheet
const sheet = workbook.getWorksheets().get("Sheet1");
// Add data into details cells.
sheet.getCells().get(0, 0).putValue("Fruits Name");
sheet.getCells().get(0, 1).putValue("Fruits Price");
sheet.getCells().get(1, 0).putValue("Apples");
sheet.getCells().get(2, 0).putValue("Bananas");
sheet.getCells().get(3, 0).putValue("Grapes");
sheet.getCells().get(4, 0).putValue("Oranges");
sheet.getCells().get(1, 1).putValue(5);
sheet.getCells().get(2, 1).putValue(2);
sheet.getCells().get(3, 1).putValue(1);
sheet.getCells().get(4, 1).putValue(4);

// Add a chart to the worksheet
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
// Access the instance of the newly added chart
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B5", true);
// Set AutoFilter range
sheet.getAutoFilter().setRange("A1:B5");
// Add filters for a filter column.
sheet.getAutoFilter().addFilter(0, "Bananas");
sheet.getAutoFilter().addFilter(0, "Oranges");
// Apply the filters
sheet.getAutoFilter().refresh();
chart.toImage("Autofilter.png");
workbook.save("Autofilter.xlsx");
```

## **3. Filtrer les données en utilisant un tableau et laisser le changement du graphique**

Utiliser un tableau est similaire à la Méthode 2, en utilisant une plage, mais vous avez des avantages avec les tableaux par rapport aux plages. Lorsque vous modifiez votre plage en un tableau et ajoutez des données, le graphique se met à jour automatiquement. Avec une plage, vous devrez modifier la source de données.

### **Format en tableau dans Excel**

Cliquez à l'intérieur de vos données et utilisez **CTRL + T** ou utilisez l'onglet Accueil, **Format en Tableau**

![todo:image_alt_text](Figure4.png)

### **Code d'exemple**
Le code d'exemple suivant charge le [fichier Excel d’exemple](TableFilters.xlsx) et montre la même fonctionnalité en utilisant Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "TableFilters.xlsx");
// Create a workbook.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const sheet = workbook.getWorksheets().get(0);
// Access the instance of the newly added chart
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 7, 7, 15, 15);
const chart = sheet.getCharts().get(chartIndex);
// Set data range
chart.setChartDataRange("A1:B7", true);
// Convert the chart to image
chart.toImage("TableFilters.before.png");
// Add a new List Object to the worksheet
const listObject = sheet.getListObjects().get(sheet.getListObjects().add("A1", "B7", true));
// Add default style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);
// Show Total
listObject.setShowTotals(false);
// Add filters for a filter column.
listObject.getAutoFilter().addFilter(0, "James");
// Apply the filters
listObject.getAutoFilter().refresh();
// After adding new value the chart will change
listObject.putCellValue(7, 0, "Me");
listObject.putCellValue(7, 1, 1000);
// Check the changed images
chart.toImage("TableFilters.after.png");
// Saving the Excel file
workbook.save("TableFilter.out.xlsx");
```
