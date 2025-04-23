---
title: Lire le sous titre du graphique depuis un fichier ODS en utilisant Node.js via C++
linktitle: Lire le sous titre du graphique à partir du fichier ODS
description: Apprenez à utiliser Aspose.Cells for Node.js via C++ pour lire le sous titre du graphique à partir d un fichier OpenDocument Spreadsheet (ODS). Notre guide vous montrera comment extraire et accéder au sous titre pour une analyse ou affichage ultérieur.
keywords: Aspose.Cells for Node.js via C++, Lire le sous titre du graphique, OpenDocument Spreadsheet, fichier ODS, extraction de graphique, analyse de données.
type: docs
weight: 160
url: /fr/nodejs-cpp/read-chart-subtitle-from-ods-file/
---

## **Lire le sous-titre du graphique à partir du fichier ODS**

Aspose.Cells vous permet de lire les sous-titres des graphiques dans les fichiers ODS en utilisant la propriété [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--). Le code exemple suivant charge le [fichier ODS d'exemple](89620481.ods) et lit le sous-titre du graphique en utilisant la propriété [**Chart.getSubTitle()**](https://reference.aspose.com/cells/nodejs-cpp/chart/#getSubTitle--) et l'affiche dans la fenêtre de console. Veuillez consulter la sortie console du code ci-dessous pour référence.

## **Code d'exemple**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Load excel file containing charts
const filePath = path.join(sourceDir, "SampleChart.ods");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

console.log("Chart Subtitle: " + chart.getSubTitle().getText());
```

## **Sortie console**

{{< highlight javascript >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
