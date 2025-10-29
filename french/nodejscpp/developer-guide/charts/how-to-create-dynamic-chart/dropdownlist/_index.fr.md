---
title: Comment créer un graphique dynamique avec liste déroulante en utilisant Node.js via C++
linktitle: Comment créer un graphique dynamique avec liste déroulante
description: Apprenez comment créer un graphique dynamique qui se met à jour en fonction de la sélection d une liste déroulante en utilisant Aspose.Cells for Node.js via C++. Notre guide étape par étape vous montrera comment intégrer une liste déroulante dans votre graphique pour une visualisation flexible des données.
keywords: Aspose.Cells for Node.js via C++, Graphique dynamique, Liste déroulante, Visualisation des données, Intégration, Visualisation flexible.
type: docs
weight: 76
url: /fr/nodejs-cpp/create-dynamic-chart-with-dropdownlist/
---

## **Scénarios d'utilisation possibles**
Un graphique dynamique avec liste déroulante dans Excel est un outil puissant qui permet aux utilisateurs de créer des graphiques interactifs qui peuvent se mettre à jour dynamiquement en fonction des données sélectionnées. Cette fonctionnalité est particulièrement utile dans les situations où il est nécessaire d'analyser de multiples ensembles de données ou de comparer divers scénarios.

Une application courante d'un graphique dynamique avec liste déroulante est l'analyse financière. Par exemple, une entreprise peut avoir plusieurs ensembles de données financières pour différentes années ou départements. En utilisant une liste déroulante, les utilisateurs peuvent sélectionner l'ensemble de données spécifique qu'ils souhaitent analyser, et le graphique se mettra automatiquement à jour pour afficher les informations correspondantes. Cela permet de comparer facilement et d'identifier les tendances ou schémas.

Une autre application se trouve dans les ventes et le marketing. Une entreprise peut avoir des données de vente pour différents produits ou régions. Avec un graphique dynamique avec liste déroulante, les utilisateurs peuvent choisir un produit ou une région spécifique dans la liste déroulante, et le graphique se mettra à jour dynamiquement pour afficher les performances de vente pour l'option sélectionnée. Cela aide à identifier les zones ou produits les plus performants et à prendre des décisions basées sur les données.

En résumé, un graphique dynamique avec liste déroulante dans Excel offre un moyen flexible et interactif de visualiser et d'analyser les données. Il est précieux dans les situations où il est nécessaire de comparer plusieurs ensembles de données ou d'explorer différents scénarios, ce qui en fait un outil polyvalent pour l'analyse financière, les ventes et le marketing, et de nombreuses autres applications.

## **Utilisez Aspose Cells pour créer un graphique dynamique avec liste déroulante**
Dans les paragraphes suivants, nous vous montrerons comment créer un graphique dynamique avec liste déroulante en utilisant Aspose.Cells for Node.js via C++. Nous présenterons le code pour l'exemple, ainsi que le fichier Excel créé avec ce code.

## **Code d'exemple**
Le code d'exemple suivant générera le [fichier Dynamic Chart with Dropdownlist](DynamicChartWithDropdownlist.xlsx).

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
sheet.getCells().get("A3").putValue("Tea");
sheet.getCells().get("A4").putValue("Coffee");
sheet.getCells().get("A5").putValue("Sugar");

// In this example, we will add 12 months of data
sheet.getCells().get("B2").putValue("Jan");
sheet.getCells().get("C2").putValue("Feb");
sheet.getCells().get("D2").putValue("Mar");
sheet.getCells().get("E2").putValue("Apr");
sheet.getCells().get("F2").putValue("May");
sheet.getCells().get("G2").putValue("Jun");
sheet.getCells().get("H2").putValue("Jul");
sheet.getCells().get("I2").putValue("Aug");
sheet.getCells().get("J2").putValue("Sep");
sheet.getCells().get("K2").putValue("Oct");
sheet.getCells().get("L2").putValue("Nov");
sheet.getCells().get("M2").putValue("Dec");
const allMonths = 12;
const iCount = 3;
for (let i = 0; i < iCount; i++) {
for (let j = 0; j < allMonths; j++) {
const _row = i + 2;
const _column = j + 1; 
sheet.getCells().get(_row, _column).putValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
}
}

// This is the Dropdownlist for Dynamic Data
const ca = AsposeCells.CellArea.createCellArea(9, 0, 9, 0);
const _index = sheet.getValidations().add(ca);
const _va = sheet.getValidations().get(_index);
_va.setType(AsposeCells.ValidationType.List);
_va.setInCellDropDown(true);
_va.setFormula1("=$B$2:$M$2");
sheet.getCells().get("A9").putValue("Current Month");
sheet.getCells().get("A10").putValue("Jan");
const _style = sheet.getCells().get("A10").getStyle();
_style.getFont().setIsBold(true);
_style.setPattern(AsposeCells.BackgroundType.Solid);
_style.setForegroundColor(AsposeCells.Color.Yellow);
sheet.getCells().get("A10").setStyle(_style);

// Set the dynamic range for the chart's data source. 
let index = sheets.getNames().add("Sheet1!ChtMonthData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

// Set the dynamic range for the chart's data labels. 
index = sheets.getNames().add("Sheet1!ChtXLabels");
sheets.getNames().get(index).setRefersTo("=Sheet1!$A$3:$A$5");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Column, 8, 2, 20, 8);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("month", true);
chart.getNSeries().get(0).setName("=Sheet1!$A$10");
chart.getNSeries().get(0).setValues("Sheet1!ChtMonthData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtXLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicChartWithDropdownlist.xlsx"));
```

## **Remarques**
Dans le fichier généré, le graphique comptera dynamiquement les données pour le mois sélectionné. Cela est fait en utilisant la formule "OFFSET" dans le code d'exemple :

```
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Vous pouvez essayer de changer la valeur de la liste déroulante dans la cellule "Sheet1!$A$10", et vous verrez le changement dynamique du graphique. Nous avons maintenant créé avec succès un graphique dynamique avec liste déroulante en utilisant Aspose.Cells.
{{< app/cells/assistant language="nodejs-cpp" >}}
