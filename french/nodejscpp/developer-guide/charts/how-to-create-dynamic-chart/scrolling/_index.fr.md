---
title: Comment créer un graphique défilant dynamique avec Node.js via C++
linktitle: Comment créer un graphique dynamique déroulant
description: Apprenez comment créer un graphique défilant dynamique en utilisant Aspose.Cells for Node.js via C++. Notre guide étape par étape vous montrera comment implémenter des transitions de données fluides et un défilement automatique dans votre graphique pour un affichage continu et mis à jour.
keywords: Aspose.Cells pour Node.js, graphique défilant dynamique, transitions de données, défilement fluide, affichage continu, mise à jour de la visualisation.
type: docs
weight: 75
url: /fr/nodejs-cpp/create-dynamic-scrolling-chart/
---

## **Scénarios d'utilisation possibles**
Un graphique dynamique déroulant est un type de représentation graphique utilisé pour afficher des données qui changent avec le temps. Il est conçu pour fournir une vue en temps réel des données, permettant aux utilisateurs de suivre les mises à jour et les tendances continues. Le graphique se met à jour en continu lorsque de nouvelles données sont ajoutées, et il défile automatiquement pour afficher les informations les plus récentes.

Les graphiques dynamiques déroulants sont couramment utilisés dans diverses industries, telles que la finance, l'analyse du marché boursier, le suivi météorologique et l'analyse des médias sociaux. Ils permettent aux utilisateurs de visualiser et d'analyser les motifs de données et de prendre des décisions éclairées en fonction des informations en temps réel.

Ces graphiques sont généralement interactifs, permettant à l'utilisateur de zoomer, de faire défiler les données historiques et d'ajuster les intervalles de temps. Ils prennent souvent en charge plusieurs séries de données, offrant une vue complète des différentes mesures et de leurs corrélations.

 Globalement, les graphiques dynamiques déroulants sont des outils précieux pour surveiller et analyser les données en séries chronologiques, faciliter la prise de décisions en temps réel et améliorer les capacités de visualisation des données.

## **Utilisez Aspose.Cells pour créer un graphique défilant dynamique**
Dans les paragraphes suivants, nous vous montrerons comment créer un graphique défilant dynamique en utilisant Aspose.Cells for Node.js via C++. Nous présenterons le code pour l'exemple, ainsi que le fichier Excel créé avec ce code.

## **Code d'exemple**
Le code d'exemple suivant générera le [Fichier de graphique dynamique déroulant](DynamicScrollingChart.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Your local test path
const localPath = "";

// Create a new workbook and access the first worksheet.
const workbook = new AsposeCells.Workbook();
const sheets = workbook.getWorksheets();
const sheet = sheets.get(0);

// Populate the data for the chart. Add values to cells and set series names.
sheet.getCells().get("A1").putValue("Day");
sheet.getCells().get("B1").putValue("Sales");
// In this example, we will add 30 days of data
const allDays = 30;
const showDays = 10;
let currentDay = 1;

for (let i = 0; i < allDays; i++) {
const cellA = `A${i + 2}`;
const cellB = `B${i + 2}`;
sheet.getCells().get(cellA).putValue(i + 1);
sheet.getCells().get(cellB).putValue(50 * (i % 2) + 20 * (i % 3) + 10 * Math.floor(i / 3));
}

// This is the Dynamic Scrolling Control Data
sheet.getCells().get("G19").putValue("Start Day");
sheet.getCells().get("G20").putValue(currentDay);
sheet.getCells().get("H19").putValue("Show Days");
sheet.getCells().get("H20").putValue(showDays);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtScrollData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtScrollLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

// Add a ScrollBar for the Dynamic Scrolling Chart
const bar = sheet.getShapes().addScrollBar(2, 0, 3, 0, 200, 30);
bar.setMin(0);
bar.setMax(allDays - showDays);
bar.setCurrentValue(currentDay);
bar.setLinkedCell("$G$20");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 2, 4, 15, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtScrollData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtScrollLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicScrollingChart.xlsx"));
```

## **Remarques**
Dans le fichier généré, vous pouvez agir sur la barre de défilement, tandis que le graphique compte dynamiquement les 10 derniers ensembles de données. Cela est fait en utilisant la formule "OFFSET" dans le code d'exemple:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Vous pouvez essayer de changer le nombre "10" en "15" dans la cellule "Sheet1!$H$20", et le graphique dynamique comptera les 15 dernières données. Nous avons maintenant créé un graphique défilant dynamique avec succès en utilisant Aspose.Cells for Node.js via C++.
