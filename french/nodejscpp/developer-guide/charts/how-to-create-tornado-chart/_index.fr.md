---
title: Comment créer un graphique en tornade avec Node.js via C++
linktitle: Comment créer un graphique en entonnoir
type: docs
weight: 73
url: /fr/nodejs-cpp/create-tornado-chart/
description: Apprenez à créer un graphique en tornade avec l API Aspose.Cells for Node.js via C++.
keywords: Node.js créer un graphique en tornado, ajouter un graphique en tornado, insérer un graphique en tornado
---

## **Introduction**
Un diagramme en forme de tornade, également connu sous le nom de diagramme en forme de tornade ou graphique en forme de tornade, est un type de visualisation de données souvent utilisé pour l'analyse de sensibilité dans Excel. Il vous aide à comprendre l'impact des variables changeantes sur un résultat particulier.

## **Comment créer un diagramme en forme de tornade dans Excel**
Vous pouvez créer un diagramme en forme de tornade dans Excel en suivant ces étapes :
1. Sélectionnez les données et allez dans Insertion --> Graphiques --> Insérer un histogramme ou un graphique à barres --> Graphique à barres empilées. Cliquez dessus.
<br>
<img src="1.png" width=70% />
2. Modifiez l'axe des Y : Cliquez avec le bouton droit sur l'axe des y. Cliquez sur formater l'axe. Dans les étiquettes, cliquez sur le menu déroulant de la position des étiquettes et sélectionnez l'élément inférieur.
<br>
<img src="2.png" width=70% />
3. Sélectionnez une barre quelconque et allez dans le formatage. Définissez une largeur d'écart appropriée.
<br>
<img src="3.png" width=70% />
4. Supprimons le signe moins (-) du diagramme en forme de tornade. Sélectionnez l'axe des x. Allez dans le formatage. Dans les options d'axe, cliquez sur le nombre. Dans la catégorie, sélectionnez personnalisé. Dans le code de format, écrivez ###0,###0. Cliquez sur ajouter.
<br>
<img src="4.png" width=70% />
5. cliquez sur l'axe des y et allez dans les options d'axe. Dans les options d'axe, cochez Catégories dans l'ordre inverse.
<br>
<img src="5.png" width=70% />

## **Comment ajouter un graphique en tornado dans Aspose.Cells for Node.js via C++**
Veuillez consulter le code d'exemple suivant. Il charge le [fichier Excel d'exemple](sample.xlsx) qui contient des données d'exemple. Ensuite, il crée le graphique à barres empilées basé sur les données initiales et définit les propriétés pertinentes. Enfin, il enregistre le classeur au format [XLSX de sortie](out.xlsx). La capture d'écran suivante montre le diagramme en forme de tornade créé par Aspose.Cells dans le fichier Excel de sortie.
<br>
<img src="6.png" width=70% />

### **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);
const charts = sheet.getCharts();
// Add bar chart
const index = charts.add(AsposeCells.ChartType.BarStacked, 8, 1, 24, 8);
const chart = charts.get(index);

// Set data for bar chart
chart.setChartDataRange("A1:C7", true);

// Set properties for bar chart
chart.getTitle().setText("Tornado chart");
chart.setStyle(2);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getPlotArea().getBorder().setColor(AsposeCells.Color.White);
chart.getLegend().setPosition(AsposeCells.LegendPositionType.Bottom);

chart.getCategoryAxis().setTickLabelPosition(AsposeCells.TickLabelPositionType.Low);
chart.getCategoryAxis().setIsPlotOrderReversed(true);

chart.setGapWidth(10);

const valueAxis = chart.getValueAxis();
valueAxis.getTickLabels().setNumberFormat("#,##0;#,##0");

workbook.save("out.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
