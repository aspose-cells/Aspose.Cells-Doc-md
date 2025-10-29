---
title: Comment créer un graphique de Gantt avec Node.js via C++
linktitle: Comment créer un graphique de Gantt
type: docs
weight: 72
url: /fr/nodejs-cpp/how-to-create-gantt-chart/
description: Apprenez à créer un graphique de Gantt avec l API Aspose.Cells for Node.js via C++.
keywords: Node.js crée un graphique de Gantt, ajouter un graphique de Gantt, insérer un graphique de Gantt
---

## **Qu’est-ce qu’un graphique de Gantt**

Un graphique de Gantt est un type de diagramme à barres qui illustre un calendrier de projet. Il montre les dates de début et de fin des différents éléments d’un projet. Chaque tâche ou activité est représentée par une barre, dont la longueur correspond à sa durée. Les graphiques de Gantt indiquent également les dépendances entre les tâches, permettant aux gestionnaires de visualiser la séquence dans laquelle les tâches doivent être accomplies. Ils sont largement utilisés en gestion de projet pour planifier, programmer et suivre efficacement les projets.

## **Comment créer un graphique de Gantt dans Excel**

Vous pouvez créer un graphique de Gantt dans Excel en suivant ces étapes :
1. Ajoutez des données pour le graphique de Gantt. 
<br>
<img src="00.png" width=50% />
1. Sélectionnez les données et allez dans Insertion --> Graphiques --> Insérer un graphique à colonnes ou à barres --> Graphique à barres empilées. Dans notre exemple, c’est B1:B7, puis insérez le **Graphique à barres empilées**.
<br>
<img src="1.png" width=50% />

1. Sélectionnez le graphique, **Sélectionner les données** -> **Ajouter**, configurez le **Nom de la série** et **Valeurs de la série** comme suit.
<br>
<img src="2.png" width=50% />

1. Sélectionnez le graphique, modifiez les **Labels de l’axe horizontal (catégorie)**.
<br>
<img src="3.png" width=50% />

1. **Mettre en forme l’axe** Y, sélectionnez **Catégories en ordre inverse**.
1. Sélectionnez la **série bleue** et définissez la **Remplissage -> Sans remplissage**.
1. **Mettre en forme l’axe** X, définissez le **Minimum** et **Maximum** (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Ajouter des étiquettes de données** pour le graphique, vous obtiendrez ainsi un graphique de Gantt.
<br>
<img src="0.png" width=50% />


## **Comment ajouter un graphique de Gantt dans Aspose.Cells**
Veuillez voir le code exemple ci-dessous. Il charge le [fichier Excel exemple](sample.xlsx) contenant des données exemples. Il crée ensuite le graphique à barres empilées basé sur ces données initiales et définit les propriétés pertinentes. Enfin, il enregistre le classeur au format [XLSX de sortie](result.xlsx). La capture d’écran suivante montre le graphique de Gantt créé par Aspose.Cells dans le fichier Excel de sortie.
<br>
<img src="5.png" width=60% />

### **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Create BarStacked Chart
const i = worksheet.getCharts().add(AsposeCells.ChartType.BarStacked, 5, 6, 20, 15);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(i);
// Set the chart title name 
chart.getTitle().setText("Gantt Chart");
// Set the chart title is Visible
chart.getTitle().setIsVisible(true);
// Set data range
chart.setChartDataRange("B1:B6", true);
// Add series data range
chart.getNSeries().add("C2:C6", true);
// No fill for one serie
chart.getNSeries().get(0).getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set the Horizontal(Category) Axis
chart.getNSeries().setCategoryData("A2:A6");
// Reverse the Horizontal(Category) Axis
chart.getCategoryAxis().setIsPlotOrderReversed(true);
// Set the value axis's MinValue and MaxValue
const minValue = parseFloat(worksheet.getCells().get("B2").getValue());
const maxValue = parseFloat(worksheet.getCells().get("D6").getValue());
chart.getValueAxis().setMinValue(isNaN(minValue) ? 0 : minValue);
chart.getValueAxis().setMaxValue(isNaN(maxValue) ? 0 : maxValue);
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Show the DataLabels
chart.getNSeries().get(1).getDataLabels().setShowValue(true);
// Disable the Legend
chart.setShowLegend(false);
// Save the result
workbook.save("result.xlsx");
```

{{< app/cells/assistant language="nodejs-cpp" >}}
