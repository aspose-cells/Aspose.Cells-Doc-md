---
title: Utilisation de Sparklines et Formatage 3D avec Node.js via C++
linktitle: Utilisation de Sparklines et réglages du format 3D
type: docs
weight: 40
url: /fr/nodejs-cpp/using-sparklines-and-settings-3d-format/
description: Apprenez comment utiliser les miniatures et appliquer un formatage 3D dans les fichiers Excel avec Aspose.Cells for Node.js via C++. 
---

## **Utilisation des sparklines**
Microsoft Excel 2010 peut analyser les informations de plus de façons que jamais. Il permet aux utilisateurs de suivre et de mettre en évidence les tendances importantes des données avec de nouveaux outils d'analyse et de visualisation des données. Les sparklines sont des mini-graphiques que vous pouvez placer à l'intérieur des cellules afin de visualiser les données et le graphique sur la même table. Lorsque les sparklines sont utilisés correctement, l'analyse des données est plus rapide et plus directe. Ils offrent également une vue simple des informations, évitant les feuilles de calcul surchargées avec de nombreux graphiques complexes.

Aspose.Cells for Node.js via C++ fournit une API pour manipuler les miniatures dans les feuilles de calcul.
### **Sparklines dans Microsoft Excel**
Pour insérer des sparklines dans Microsoft Excel 2010 :

1. Sélectionnez les cellules où vous souhaitez voir apparaître les sparklines. Pour les rendre faciles à visualiser, sélectionnez les cellules à côté des données.
1. Cliquez sur **Insérer** dans le ruban, puis choisissez **colonne** dans le groupe **Sparklines**.
1. Sélectionnez ou saisissez la plage de cellules dans la feuille de calcul contenant les données source. Les graphiques apparaîtront.

Les Sparklines vous aident à visualiser les tendances, par exemple le bilan de victoires ou de défaites pour une ligue de softball. Les Sparklines peuvent même résumer l'ensemble de la saison de chaque équipe dans la ligue.
### **Miniatures utilisant Aspose.Cells for Node.js via C++**
Les développeurs peuvent créer, supprimer ou lire des miniatures (dans le fichier modèle) en utilisant l'API fournie par Aspose.Cells for Node.js via C++. Les classes qui gèrent les miniatures se trouvent dans le module [SparklineGroupCollection](https://reference.aspose.com/cells/nodejs-cpp/sparklinegroupcollection/), il est donc nécessaire de charger ce module avant d'utiliser ces fonctionnalités.

En ajoutant des graphiques personnalisés pour une plage de données donnée, les développeurs ont la liberté d'ajouter différents types de petits graphiques à des zones de cellules sélectionnées.

L'exemple ci-dessous illustre la fonctionnalité des Sparklines. L'exemple montre comment :

1. Ouvrir un fichier modèle simple.
1. Lire les informations des sparklines pour une feuille de calcul.
1. Ajouter de nouvelles sparklines pour une plage de données donnée à une zone de cellules.
1. Enregistrez le fichier Excel sur le disque.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Use the following lines if you need to read the Sparklines
// Read the Sparklines from the template file (if it has)
const sparklinesCount = sheet.getSparklineGroups().getCount();

for (let i = 0; i < sparklinesCount; i++)
{
const group = sheet.getSparklineGroups().get(i);
// Display the Sparklines group information e.g type, number of sparklines items
console.log(`sparkline group: type:${group.getType()}, sparkline items count:${group.getSparklines().getCount()}`);
const sparklineCount = sparklineGroup.getSparklines().getCount();
for (let j = 0; j < sparklineCount; j++) 
{
const sparkline = sparklineGroup.getSparklines().get(j);
// Display the individual Sparkines and the data ranges
console.log(`sparkline: row:${sparkline.getRow()}, col:${sparkline.getColumn()}, dataRange:${sparkline.getDataRange()}`);
}
}


// Add Sparklines
// Define the CellArea D2:D10
const ca = AsposeCells.CellArea.createCellArea(1, 4, 7, 4);
// Add new Sparklines for a data range to a cell area
const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "Sheet1!B2:D8", false, ca);
const group = sheet.getSparklineGroups().get(idx);
// Create CellsColor
const clr = workbook.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Save the excel file
workbook.save(path.join(dataDir, "Book1.out.xlsx"));
```
## **Réglage du format 3D**
Vous pourriez avoir besoin de styles de graphiques 3D pour obtenir uniquement les résultats pour votre scénario. Aspose.Cells for Node.js via C++ fournit l'API pertinente pour appliquer la mise en forme 3D de Microsoft Excel 2007.

Un exemple complet est donné ci-dessous pour démontrer comment créer un graphique et appliquer le format 3D de Microsoft Excel 2007. Après l'exécution du code d'exemple, un graphique en colonnes (avec effets 3D) sera ajouté à la feuille de calcul.


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "3d_format.out.xlsx");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Add a Data Worksheet
const dataSheet = book.getWorksheets().add("DataSheet");

// Add Chart Worksheet
const sheet = book.getWorksheets().add("MyChart");

// Put some values into the cells in the data worksheet
dataSheet.getCells().get("B1").putValue(1);
dataSheet.getCells().get("B2").putValue(2);
dataSheet.getCells().get("B3").putValue(3);
dataSheet.getCells().get("A1").putValue("A");
dataSheet.getCells().get("A2").putValue("B");
dataSheet.getCells().get("A3").putValue("C");

// Define the Chart Collection
const charts = sheet.getCharts();
// Add a Column chart to the Chart Worksheet
const chartSheetIdx = charts.add(AsposeCells.ChartType.Column, 5, 0, 25, 15);

// Get the newly added Chart
const chart = book.getWorksheets().get(2).getCharts().get(0);

// Set the background/foreground color for PlotArea/ChartArea
chart.getPlotArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Hide the Legend
chart.setShowLegend(false);

// Add Data Series for the Chart
chart.getNSeries().add("DataSheet!B1:B3", true);
// Specify the Category Data
chart.getNSeries().setCategoryData("DataSheet!A1:A3");

// Get the Data Series
const ser = chart.getNSeries().get(0);

// Apply the 3-D formatting
const spPr = ser.getShapeProperties();
const fmt3d = spPr.getFormat3D();

// Specify Bevel with its height/width
const bevel = fmt3d.getTopBevel();
bevel.setType(AsposeCells.BevelPresetType.Circle);
bevel.setHeight(2);
bevel.setWidth(5);

// Specify Surface material type
fmt3d.setSurfaceMaterialType(AsposeCells.PresetMaterialType.WarmMatte);

// Specify surface lighting type
fmt3d.setSurfaceLightingType(AsposeCells.LightRigType.ThreePoint);

// Specify lighting angle
fmt3d.setLightingAngle(20);

// Specify Series background/foreground and line color
ser.getArea().setBackgroundColor(AsposeCells.Color.Maroon);
ser.getArea().setForegroundColor(AsposeCells.Color.Maroon);
ser.getBorder().setColor(AsposeCells.Color.Maroon);

// Save the Excel file
book.save(filePath);
```
