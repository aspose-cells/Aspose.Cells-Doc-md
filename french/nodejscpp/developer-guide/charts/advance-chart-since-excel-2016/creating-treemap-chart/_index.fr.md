---  
title: Comment créer un graphique TreeMap avec Node.js via C++  
linktitle: Comment créer un diagramme TreeMap  
description: Apprenez comment créer un graphique Treemap en Aspose.Cells for Node.js via C++. Notre guide vous aidera à comprendre les différentes propriétés et options de mise en forme disponibles pour les graphiques Treemap, y compris les couleurs, les étiquettes et la représentation des données.  
keywords: Aspose.Cells pour Node.js, graphique Treemap, créer, propriétés, mise en forme, couleurs, étiquettes, représentation des données, graphique circulaire, graphique hiérarchique.  
type: docs  
weight: 161  
url: /fr/nodejs-cpp/creating-treemap-chart/  
---  

## **Scénarios d'utilisation possibles**  
Un graphique à carte de chaleur fournit une vue hiérarchique de vos données et facilite la détection de schémas, tels que les articles les plus vendus d'un magasin. Les branches de l'arbre sont représentées par des rectangles et chaque sous-branche est présentée sous la forme d'un rectangle plus petit. Le graphique à carte de chaleur affiche les catégories par couleur et proximité et peut facilement montrer beaucoup de données qui seraient difficiles avec d'autres types de graphiques.  

![todo:image_alt_text](sample.png)  
## **Diagramme TreeMap**  
Après avoir exécuté le code ci-dessous, vous verrez le diagramme TreeMap comme indiqué ci-dessous.  

![todo:image_alt_text](result.png)  
## **Code d'exemple**  
Le code d'exemple suivant charge le [fichier Excel d'exemple](treemap.xlsx) et génère le [fichier Excel de sortie](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "treemap.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add a Treemap chart
const pieIdx = worksheet.getCharts().add(AsposeCells.ChartType.Treemap, 5, 6, 20, 12);
// Retrieve the Chart object
const chart = worksheet.getCharts().get(pieIdx);
// Set the legend can be showed
chart.setShowLegend(true);
// Set the chart title name 
chart.getTitle().setText("TreeMap Chart");
// Add series data range(D2:D13,actually)
chart.getNSeries().add("D2:F13", true);
// Set category data(A2:A13 is incorrect )
chart.getNSeries().setCategoryData("A2:C13");
// Show the DataLabels with category names
chart.getNSeries().get(0).getDataLabels().setShowCategoryName(true);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Save the Excel file
workbook.save("out.xlsx");
```  

