---
title: Créer et gérer des graphiques avec Node.js via C++
linktitle: Graphiques
description: Apprenez comment utiliser Aspose.Cells pour Node.js afin de créer des graphiques dans Microsoft Excel. Notre guide démontrera divers types de graphiques et comment personnaliser leur apparence et leur formatage.
keywords: Aspose.Cells pour Node.js, Création de graphiques, Microsoft Excel, Types de graphiques, Personnalisation, Apparence, Formatage.
type: docs
weight: 130
url: /fr/nodejs-cpp/creating-charts/
---

{{% alert color="primary" %}}

Il est possible d'ajouter divers graphiques aux feuilles de calcul avec Aspose.Cells. Aspose.Cells propose de nombreux objets de création de graphiques flexibles. Ce sujet traite des objets de création de graphiques d'Aspose.Cells.

{{% /alert %}}

## **Création de graphiques**

### **Création simple d'un graphique**
Il est simple de créer un graphique avec Aspose.Cells avec les codes d'exemple suivants:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Obtaining the reference of the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Adding sample values to cells
worksheet.getCells().get("A2").putValue("Category1");
worksheet.getCells().get("A3").putValue("Category2");
worksheet.getCells().get("A4").putValue("Category3");

worksheet.getCells().get("B1").putValue("Column1");
worksheet.getCells().get("B2").putValue(4);
worksheet.getCells().get("B3").putValue(20);
worksheet.getCells().get("B4").putValue(50);
worksheet.getCells().get("C1").putValue("Column2");
worksheet.getCells().get("C2").putValue(50);
worksheet.getCells().get("C3").putValue(100);
worksheet.getCells().get("C4").putValue(150);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Setting chart data source as the range "A1:C4"
chart.setChartDataRange("A1:C4", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Choses à savoir pour créer un graphique**

Avant de créer des graphiques, il est important de comprendre certains concepts de base qui sont utiles lors de la création de graphiques avec Aspose.Cells.

#### **Objets de graphiques**

Les objets de création de graphiques sont listés ci-dessous :

- Série, une seule série de données dans un graphique.
- Axe, un axe de graphique.
- Graphique, un seul graphique Excel.
- Zone de graphique, la zone de graphique dans la feuille de calcul.
- Table de données du graphique, une table de données de graphique.
- Cadre de graphique, l'objet de cadre dans un graphique.
- Point de graphique, un point unique dans une série dans un graphique.
- Collection de points de graphique, une collection qui contient tous les points dans une série.
- Graphiques, une collection d'objets de graphique.
- Étiquettes de données, une collection de tous les objets d'étiquette de données pour la série spécifiée.
- Format de remplissage, format de remplissage pour une forme.
- Sol, le sol d'un graphique 3D.
- Légende, la légende du graphique.
- Ligne, la ligne de graphique.
- Collection de séries, une collection d'objets de série.
- TickLabels, les étiquettes de repère associées aux repères sur un axe de graphique.
- Title, le titre d'un graphique ou d'un axe.
- Trendline, une tendance dans un graphique.
- TrendlineCollection, une collection de tous les objets Trendline pour la série de données spécifiée.
- Walls, les murs d'un graphique 3D.

#### **Utilisation des objets de graphique**

Comme mentionné ci-dessus, tous les objets de graphique sont des instances de leurs classes respectives et fournissent des propriétés et des méthodes spécifiques pour effectuer des tâches spécifiques. Utilisez les objets de graphique pour créer des graphiques.

Ajoutez tout type de graphique à une feuille de calcul en utilisant la collection [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--). Chaque élément de la collection [**getCharts()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCharts--) représente un objet [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/). Un objet [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) encapsule tous les autres objets de création de graphiques nécessaires pour personnaliser l'apparence du graphique. La section suivante montre comment utiliser quelques objets de création de graphiques pour créer un graphique simple.

### **Créer un graphique en utilisant Aspose.Cells**

**Étapes:**

1. Ajoutez des données aux cellules de la feuille en utilisant la méthode [**putValue(string)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-string-) de l'objet [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell/).
   Cela sera utilisé comme la source de données pour le graphique.
1. Ajoutez un graphique à la feuille en appelant la méthode [**add**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection/#add-charttype-number-number-number-number-) de la collection [**ChartCollection**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection), encapsulée dans l'objet [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/).
1. Spécifiez le type de graphique avec l'énumération [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).
   Par exemple, l'exemple ci-dessous utilise la valeur [**ChartType.Pyramid**](https://reference.aspose.com/cells/nodejs-cpp/charttype) comme type de graphique.
1. Accédez au nouvel objet [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) dans la collection [**Charts**](https://reference.aspose.com/cells/nodejs-cpp/chartcollection) en passant son index.
1. Utilisez l'un des objets de création de graphiques encapsulés dans l'objet [**Chart**](https://reference.aspose.com/cells/nodejs-cpp/chart/) pour gérer le graphique.
   L'exemple ci-dessous utilise l'objet [**SeriesCollection**](https://reference.aspose.com/cells/nodejs-cpp/seriescollection/) de création de graphique pour spécifier la source de données du graphique.

Lors de l'ajout de données source au graphique, la source de données peut être une plage de cellules (par exemple, "A1:C3"), ou une séquence de cellules non contiguës (par exemple, "A1, A3, A5"), ou une séquence de valeurs (par exemple, "1,2,3").

Ces étapes générales vous permettent de créer n'importe quel type de graphique. Utilisez différents objets de graphique pour créer différents graphiques.

Il est possible de créer de nombreux types de graphiques avec Aspose.Cells. Tous les graphiques standard pris en charge par Aspose.Cells sont prédéfinis dans une énumération nommée [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/).

Les types de graphiques prédéfinis sont :

|**Types de graphiques**|**Description**|
| :- | :- |
|Column|Représente un graphique à colonnes groupées|
|ColumnStacked|Représente un graphique à colonnes empilées|
|Column100PercentStacked|Représente un graphique à colonnes empilées à 100 %|
|Column3DClustered|Représente un graphique à colonnes groupées en 3D|
|Column3DStacked|Représente un graphique à colonnes empilées en 3D|
|Column3D100PercentStacked|Représente un graphique à colonnes empilées à 100 % en 3D|
|Column3D|Représente un graphique à colonnes en 3D|
|Bar|Représente un graphique à barres groupées|
|BarStacked|Représente un graphique à barres empilées|
|Bar100PercentStacked|Représente un graphique à barres empilées à 100 %|
|Bar3DClustered|Représente un graphique à barres groupées en 3D|
|Bar3DStacked|Représente un graphique à barres empilées en 3D|
|Bar3D100PercentStacked|Représente un graphique à barres empilées à 100 % en 3D|
|Line|Représente un graphique linéaire|
|LineStacked|Représente un graphique linéaire empilé|
|Line100PercentStacked|Représente un graphique linéaire empilé à 100 %|
|LineWithDataMarkers|Représente un graphique linéaire avec des repères de données|
|LineStackedWithDataMarkers|Représente un graphique en courbes empilées avec des marqueurs de données|
|Line100PercentStackedWithDataMarkers|Représente un graphique en courbes empilées à 100 % avec des marqueurs de données|
|Line3D|Représente un graphique en courbes 3D|
|Pie|Représente un graphique circulaire|
|Pie3D|Représente un graphique circulaire 3D|
|PiePie|Représente un graphique secteur dans un graphique circulaire|
|PieExploded|Représente un graphique circulaire éclaté|
|Pie3DExploded|Représente un graphique circulaire 3D éclaté|
|PieBar|Représente un graphique en barres dans un graphique circulaire|
|Scatter|Représente un graphique de dispersion|
|ScatterConnectedByCurvesWithDataMarker|Représente un graphique de dispersion connecté par des courbes, avec des marqueurs de données|
|ScatterConnectedByCurvesWithoutDataMarker|Représente un graphique de dispersion connecté par des courbes, sans marqueurs de données|
|ScatterConnectedByLinesWithDataMarker|Représente un graphique de dispersion connecté par des lignes, avec des marqueurs de données|
|ScatterConnectedByLinesWithoutDataMarker|Représente un graphique de dispersion connecté par des lignes, sans marqueurs de données|
|Area|Représente un graphique en aires|
|AreaStacked|Représente un graphique en aires empilées|
|Area100PercentStacked|Représente un graphique en aires empilées à 100 %|
|Area3D|Représente un graphique en aires 3D|
|Area3DStacked|Représente un graphique en aires 3D empilées|
|Area3D100PercentStacked|Représente un graphique en aires 3D empilées à 100 %
|Doughnut|Représente le graphique en anneau |
|DoughnutExploded|Représente le graphique en anneau explosé |
|Radar|Représente le graphique radar |
|RadarWithDataMarkers|Représente le graphique radar avec des marqueurs de données |
|RadarFilled|Représente le graphique radar rempli |
|Surface3D|Représente le graphique de surface 3D |
|SurfaceWireframe3D|Représente le graphique de surface 3D à structure filaire |
|SurfaceContour|Représente le graphique de contour |
|SurfaceContourWireframe|Représente le graphique de contour à structure filaire |
|Bubble|Représente le graphique de bulles |
|Bubble3D|Représente le graphique de bulles 3D |
|Cylinder|Représente le graphique cylindrique |
|CylinderStacked|Représente le graphique cylindrique empilé |
|Cylinder100PercentStacked|Représente le graphique cylindrique 100% empilé |
|CylindericalBar|Représente le graphique de barres cylindriques |
|CylindericalBarStacked|Représente le graphique de barres cylindriques empilées |
|CylindericalBar100PercentStacked|Représente le graphique de barres cylindriques 100% empilées |
|CylindericalColumn3D|Représente le graphique de colonnes cylindriques 3D |
|Cone|Représente le graphique en cône |
|ConeStacked|Représente le graphique en cône empilé |
|Cone100PercentStacked|Représente un diagramme en cônes empilés à 100 %|
|ConicalBar|Représente un diagramme en barres coniques|
|ConicalBarStacked|Représente un diagramme en barres coniques empilées|
|ConicalBar100PercentStacked|Représente un diagramme en barres coniques empilées à 100 %|
|ConicalColumn3D|Représente un diagramme en colonnes coniques 3D|
|Pyramid|Représente un diagramme en pyramide|
|PyramidStacked|Représente un diagramme en pyramide empilée|
|Pyramid100PercentStacked|Représente un diagramme en pyramide empilée à 100 %|
|PyramidBar|Représente un diagramme en barres pyramidal|
|PyramidBarStacked|Représente un diagramme en barres pyramidal empilées|
|PyramidBar100PercentStacked|Représente un diagramme en barres pyramidal empilées à 100 %|
|PyramidColumn3D|Représente un diagramme en colonnes pyramidal 3D|
{{% alert color="primary" %}}

Lorsque vous attribuez une plage de cellules comme source de données, vous ne pouvez définir la plage que de haut en bas à gauche. Par exemple, "A1:C3" est valide tandis que "C3:A1" est invalide.

{{% /alert %}}

#### **Diagramme en pyramide**

Lorsque le code exemple est exécuté, un diagramme en pyramide est ajouté à la feuille de calcul.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Pyramid, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Diagramme linéaire**

Dans l'exemple ci-dessus, il suffit de changer [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) en *Ligne* pour créer un graphique en ligne. La source complète est fournie ci-dessous. Lors de l'exécution du code, un graphique en ligne est ajouté à la feuille.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Adding a new worksheet to the Excel object
const sheetIndex = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(sheetIndex);

// Adding sample values to cells
worksheet.getCells().get("A1").putValue(50);
worksheet.getCells().get("A2").putValue(100);
worksheet.getCells().get("A3").putValue(150);
worksheet.getCells().get("B1").putValue(4);
worksheet.getCells().get("B2").putValue(20);
worksheet.getCells().get("B3").putValue(50);

// Adding a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Line, 5, 0, 15, 5);

// Accessing the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);

// Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
chart.getNSeries().add("A1:B3", true);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Diagramme en bulles**

Pour créer un graphique à bulles, le [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) doit être défini sur [**ChartType.Bubble**](https://reference.aspose.com/cells/nodejs-cpp/charttype) et quelques propriétés supplémentaires telles que BubbleSizes, Values et XValues doivent être configurées en conséquence. Lors de l'exécution du code suivant, un graphique à bulles est ajouté à la feuille de calcul.

#### **Diagramme linéaire avec marqueur de données**

Pour créer un graphique avec des marqueurs de données en ligne, [**ChartType**](https://reference.aspose.com/cells/nodejs-cpp/charttype/) doit être défini sur *ChartType.LineWithDataMarkers* et quelques propriétés supplémentaires telles que la zone d'arrière-plan, les marqueurs de série, les valeurs et XValues doivent être configurées en conséquence. Lors de l'exécution du code suivant, un graphique en ligne avec des marqueurs de données est ajouté à la feuille de calcul.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Instantiate a workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set columns title 
worksheet.getCells().get(0, 0).putValue("X");
worksheet.getCells().get(0, 1).putValue("Y");

// Random data shall be used for generating the chart
// Create random data and save in the cells
for (let i = 1; i < 21; i++) {
worksheet.getCells().get(i, 0).putValue(i);
worksheet.getCells().get(i, 1).putValue(0.8);
}

for (let i = 21; i < 41; i++) {
worksheet.getCells().get(i, 0).putValue(i - 20);
worksheet.getCells().get(i, 1).putValue(0.9);
}
// Add a chart to the worksheet
const idx = worksheet.getCharts().add(AsposeCells.ChartType.LineWithDataMarkers, 1, 3, 20, 20);

// Access the newly created chart
const chart = worksheet.getCharts().get(idx);

// Set chart style
chart.setStyle(3);

// Set autoscaling value to true
chart.setAutoScaling(true);

// Set foreground color white
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Set Properties of chart title
chart.getTitle().setText("Sample Chart");

// Set chart type
chart.setType(AsposeCells.ChartType.LineWithDataMarkers);

// Set Properties of categoryaxis title
chart.getCategoryAxis().getTitle().setText("Units");

//Set Properties of nseries
const s2_idx = chart.getNSeries().add("A2:A2", true);
const s3_idx = chart.getNSeries().add("A22:A22", true);

// Set IsColorVaried to true for varied points color
chart.getNSeries().setIsColorVaried(true);

// Set properties of background area and series markers
chart.getNSeries().get(s2_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s2_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Yellow);
chart.getNSeries().get(s2_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s2_idx).setXValues("A2:A21");
chart.getNSeries().get(s2_idx).setValues("B2:B21");

// Set properties of background area and series markers
chart.getNSeries().get(s3_idx).getArea().setFormatting(AsposeCells.FormattingType.Custom);
chart.getNSeries().get(s3_idx).getMarker().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(s3_idx).getMarker().getBorder().setIsVisible(false);

// Set X and Y values of series chart
chart.getNSeries().get(s3_idx).setXValues("A22:A41");
chart.getNSeries().get(s3_idx).setValues("B22:B41");

// Save the workbook
workbook.save(path.join(dataDir, "LineWithDataMarkerChart.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## **Sujets avancés**
- [Lire et manipuler les graphiques Excel 2016](/cells/fr/nodejs-cpp/read-and-manipulate-excel-2016-charts/)
- [Gérer les axes des graphiques Excel](/cells/fr/nodejs-cpp/chart-axes/)
- [Réglage de l’apparence du graphique](/cells/fr/nodejs-cpp/setting-chart-appearance/)
- [Types de graphiques](/cells/fr/nodejs-cpp/chart-types/)
- [Personnalisation des graphiques](/cells/fr/nodejs-cpp/customizing-charts/)
- [Définir la source de données pour le graphique](/cells/fr/nodejs-cpp/data-formatting-in-charts/)
- [Gérer les étiquettes de données des graphiques Excel](/cells/fr/nodejs-cpp/insert-datalabels-to-chart/)
- [Obtenir la feuille de calcul du graphique](/cells/fr/nodejs-cpp/get-worksheet-of-the-chart/)
- [Gérer la légende des graphiques Excel](/cells/fr/nodejs-cpp/chart-legend/)
- [Manipuler la position, la taille et le design du graphique](/cells/fr/nodejs-cpp/manipulate-position-size-and-designer-chart/)
- [Créer un graphique circulaire avec des lignes de repère](/cells/fr/nodejs-cpp/creating-pie-chart-with-leader-lines/)
- [Formes dans les graphiques](/cells/fr/nodejs-cpp/controls-in-charts/)
- [Gérer les titres des graphiques Excel](/cells/fr/nodejs-cpp/chart-and-axis-titles/)
- [Rendu du graphique](/cells/fr/nodejs-cpp/chart-rendering/)
- [Obtenir le texte de l'équation de la tendance du graphique](/cells/fr/nodejs-cpp/get-equation-text-of-chart-trendline/)
