---
title: Comment créer un graphique roulant dynamique avec Node.js via C++
linktitle: Comment créer un graphique dynamique roulant
description: Apprenez comment créer un graphique roulant dynamique en utilisant Aspose.Cells for Node.js via C++. Notre guide démontrera comment implémenter des transitions de données fluides et des moyennes mobiles dans votre graphique pour une affichage continu et mis à jour.
keywords: Aspose.Cells pour Node.js, graphique roulant dynamique, transitions de données, moyennes mobiles, affichage continu, mise à jour de la visualisation.
type: docs
weight: 74
url: /fr/nodejs-cpp/create-dynamic-rolling-chart/
---

## **Scénarios d'utilisation possibles**
Un graphique dynamique roulant se réfère à une représentation graphique qui affiche des points de données constamment en mouvement et se met à jour au fil du temps. Il s'agit d'un type de graphique qui se met continuellement à jour, présentant une fenêtre roulante des points de données les plus récents tout en éliminant les anciens points de données au fur et à mesure que de nouveaux arrivent.

Les graphiques dynamiques roulants sont couramment utilisés pour visualiser les tendances et les motifs dans les données en temps réel ou en continu. Ils sont particulièrement utiles dans des scénarios où les aspects temporels et les changements au fil du temps sont critiques, comme l'analyse du marché boursier, la surveillance météorologique ou le suivi des performances en direct.

Ces graphiques utilisent généralement des mécanismes d'animation ou de défilement automatique pour garantir que les informations les plus récentes sont toujours présentées. La longueur de la fenêtre roulante peut être personnalisée pour afficher une période de temps spécifique, comme la dernière heure, le jour ou la semaine.

En résumé, un graphique dynamique roulant est une représentation graphique continuellement mise à jour qui affiche les derniers points de données tout en éliminant les anciens, permettant aux utilisateurs d'observer les tendances et les motifs en temps réel.

## **Utilisez Aspose Cells pour créer un graphique dynamique roulant**
Dans les prochains paragraphes, nous vous montrerons comment créer un graphique dynamique roulant en utilisant Aspose.Cells. Nous vous montrerons le code de l'exemple, ainsi que le fichier Excel créé avec ce code.

## **Code d'exemple**
Le code d'exemple suivant générera le [fichier Dynamic Rolling Chart](DynamicRollingChart.xlsx).

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
sheet.getCells().get("A1").putValue("Month");
sheet.getCells().get("A2").putValue(1);
sheet.getCells().get("A3").putValue(2);
sheet.getCells().get("A4").putValue(3);
sheet.getCells().get("A5").putValue(4);
sheet.getCells().get("A6").putValue(5);
sheet.getCells().get("A7").putValue(6);
sheet.getCells().get("A8").putValue(7);

sheet.getCells().get("B1").putValue("Sales");
sheet.getCells().get("B2").putValue(50);
sheet.getCells().get("B3").putValue(45);
sheet.getCells().get("B4").putValue(55);
sheet.getCells().get("B5").putValue(60);
sheet.getCells().get("B6").putValue(55);
sheet.getCells().get("B7").putValue(65);
sheet.getCells().get("B8").putValue(70);

// Set the dynamic range for the chart's data source.
let index = sheets.getNames().add("Sheet1!ChtData");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

// Set the dynamic range for the chart's data labels.
index = sheets.getNames().add("Sheet1!ChtLabels");
sheets.getNames().get(index).setRefersTo("=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

// Create a chart object and set its data source.
const chartIndex = sheet.getCharts().add(AsposeCells.ChartType.Line, 10, 3, 25, 10);
const chart = sheet.getCharts().get(chartIndex);
chart.getNSeries().add("Sales", true);
chart.getNSeries().get(0).setValues("Sheet1!ChtData");
chart.getNSeries().get(0).setXValues("Sheet1!ChtLabels");

// Save the workbook as an Excel file.
workbook.save(path.join(localPath, "DynamicRollingChart.xlsx"));
```

## **Remarques**
Dans le fichier généré, vous pouvez continuer à ajouter des données dans les colonnes A et B, tandis que le graphique comptera dynamiquement les 5 ensembles de données les plus récents. Cela est fait en utilisant la formule "OFFSET" dans le code d'exemple :

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Vous pouvez essayer de modifier le nombre "-5" en "-10" dans la formule, et le graphique dynamique comptera les 10 derniers ensembles de données. Nous avons maintenant créé avec succès un graphique roulant dynamique en utilisant Aspose.Cells.
{{< app/cells/assistant language="nodejs-cpp" >}}
