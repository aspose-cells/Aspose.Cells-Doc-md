---
title: Comment créer un graphique en cascade avec Node.js via C++
linktitle: Comment créer un diagramme en cascade
type: docs
weight: 160
url: /fr/nodejs-cpp/creating-waterfall-chart/
description: Créer des graphiques en cascade dans Excel avec Node.js et Aspose.Cells for Node.js via C++.
keywords: créer un graphique en cascade dans Excel Node.js via C++, création de graphique en cascade dans Excel Node.js via C++, comment créer un graphique en cascade dans Excel Node.js via C++
---

{{% alert color="primary" %}}

Un graphique en cascades est un type particulier de graphique utilisé généralement pour démontrer comment la position de départ augmente ou diminue. Microsoft Excel propose de nombreux types de graphiques prédéfinis, y compris colonnes, lignes, pie, barres, radar, etc., mais le graphique en cascades dépasse les graphiques de base et peut être créé en utilisant les types de graphiques existants avec peu ou beaucoup de personnalisation.

{{% /alert %}} 

Les API Aspose.Cells permettent de créer un graphique en cascades avec l'aide du graphique linéaire. L'API permet également de personnaliser l'apparence du graphique pour lui donner la forme d'une cascade en réglant les propriétés [**Series.getUpBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getUpBars--) et [**Series.getDownBars()**](https://reference.aspose.com/cells/nodejs-cpp/series/#getDownBars--).

Le code ci-dessous montre comment utiliser Aspose.Cells for Node.js via C++ pour créer un graphique en cascades à partir de zéro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an instance of Workbook
const workbook = new AsposeCells.Workbook();

// Retrieve the first Worksheet in Workbook
const worksheet = workbook.getWorksheets().get(0);

// Retrieve the Cells of the first Worksheet
const cells = worksheet.getCells();

// Input some data which chart will use as source
cells.get("A1").putValue("Previous Year");
cells.get("A2").putValue("January");
cells.get("A3").putValue("March");
cells.get("A4").putValue("August");
cells.get("A5").putValue("October");
cells.get("A6").putValue("Current Year");

cells.get("B1").putValue(8.5);
cells.get("B2").putValue(1.5);
cells.get("B3").putValue(7.5);
cells.get("B4").putValue(7.5);
cells.get("B5").putValue(8.5);
cells.get("B6").putValue(3.5);

cells.get("C1").putValue(1.5);
cells.get("C2").putValue(4.5);
cells.get("C3").putValue(3.5);
cells.get("C4").putValue(9.5);
cells.get("C5").putValue(7.5);
cells.get("C6").putValue(9.5);

// Add a Chart of type Waterfall in same worksheet as of data
const idx = worksheet.getCharts().add(AsposeCells.ChartType.Waterfall, 4, 4, 25, 13);

// Retrieve the Chart object
const chart = worksheet.getCharts().get(idx);

// Add Series
chart.getNSeries().add("$B$1:$C$6", true);

// Add Category Data
chart.getNSeries().setCategoryData("$A$1:$A$6");

// Series has Up Down Bars
chart.getNSeries().get(0).setHasUpDownBars(true);

// Set the colors of Up and Down Bars
chart.getNSeries().get(0).getUpBars().getArea().setForegroundColor(AsposeCells.Color.Green);
chart.getNSeries().get(0).getDownBars().getArea().setForegroundColor(AsposeCells.Color.Red);

// Make both Series Lines invisible
chart.getNSeries().get(0).getBorder().setIsVisible(false);
chart.getNSeries().get(1).getBorder().setIsVisible(false);

// Set the Plot Area Formatting Automatic
chart.getPlotArea().getArea().setFormatting(AsposeCells.FormattingType.Automatic);

// Delete the Legend
chart.getLegend().getLegendEntries().get(0).setIsDeleted(true);
chart.getLegend().getLegendEntries().get(1).setIsDeleted(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## Articles Connexes

- [Création de graphiques](/cells/fr/nodejs-cpp/creating-charts/)
- [Personnalisation des graphiques](/cells/fr/nodejs-cpp/customizing-charts/)
