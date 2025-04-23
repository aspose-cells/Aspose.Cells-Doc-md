---
title: Comment gérer un PivotChart avec PivotOptions pour Node.js via C++
linktitle: Options de pivot
type: docs
weight: 10
url: /fr/nodejs-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Comment gérer un PivotChart avec PivotOptions dans Node.js via C++.
keywords: PivotChart Node.js via C++
---
## Qu'est-ce qu'un tableau croisé dynamique

Un tableau croisé dynamique dans Excel est une représentation graphique des données créée à partir d'un tableau croisé dynamique. Il permet aux utilisateurs de visualiser et d'analyser les données de manière dynamique en résumant et en affichant les informations sous forme de graphique. Les tableaux croisés dynamiques sont interactifs et peuvent être facilement modifiés pour montrer différentes perspectives des données, ce qui en fait un outil puissant pour l'analyse et la présentation de données dans Excel.

## Comment gérer un PivotChart avec PivotOptions

En utilisant Aspose.Cells for Node.js via C++, vous pouvez utiliser [**PivotOptions**](https://reference.aspose.com/cells/nodejs-cpp/pivotoptions/) pour gérer PivotChart.

Fichier et code d'exemple :
[Fichier d'exemple](Sample.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const chart = workbook.getWorksheets().get(0).getCharts().get(0);
const opt = chart.getPivotOptions();

// Hide ZoneFilter in PivotChart
opt.setDropZoneFilter(false); // HideZoneFilter

// You can set more properties, try them!
// opt.setDropZoneCategories(false); // HideZoneCategories
// opt.setDropZoneData(false); // HideZoneData
// opt.setDropZoneSeries(false); // HideZoneSeries
// opt.setDropZonesVisible(false); // Hide All

// Save the file and see the effect.
workbook.save(path.join(dataDir, "HideZoneFilter.xlsx"));
```

Avec le code d'exemple ci-dessus, vous pouvez vérifier le fichier résultant avec l'effet suivant, tel qu'illustré dans la figure :

**![Résultat](Output.png)**
