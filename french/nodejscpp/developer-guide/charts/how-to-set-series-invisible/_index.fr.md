---
title: Comment définir une série comme invisible avec Node.js via C++
linktitle: Comment définir une série comme invisible
description: Apprenez à définir une série comme invisible dans un graphique Excel en utilisant Aspose.Cells for Node.js via C++. 
keywords: Graphique Excel, Série, Invisible, IsFiltered Node.js via C++.
type: docs
weight: 74
url: /fr/nodejs-cpp/how-to-set-series-invisible/
---

## Comment définir une série comme invisible dans un graphique Excel

Dans un graphique Excel, vous pouvez faire un clic droit sur un graphique, cliquer sur "Sélectionner des données", et dans la fenêtre contextuelle, vous pouvez définir si une série est visible en cochant ou décochant l’option. Vous pouvez télécharger le [fichier d’exemple]([SeriesFiltered.xlsx](https://example.com/SeriesFiltered.xlsx)) et l’opérer dans Excel comme indiqué dans la figure pour réaliser cette fonction. Ensuite, nous vous expliquerons comment faire cela en utilisant la bibliothèque Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Comment définir une série comme invisible en utilisant Aspose.Cells 

Nous utilisons le code suivant pour définir une série comme invisible en utilisant Aspose.Cells :

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SeriesFiltered.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const charts = workbook.getWorksheets().get(0).getCharts();
const chart = charts.get("Chart 1");
const nSeriesFiltered = chart.getFilteredNSeries();
const nSeries = chart.getNSeries();
nSeries.get(1).setIsColorVaried(true);
nSeries.get(0).setIsColorVaried(true);
workbook.save(path.join(dataDir, "output.xlsx"));
```

Vous pouvez obtenir le [Fichier d'entrée](SeriesFiltered.xlsx) et le [Fichier de sortie](output.xlsx).

Comme indiqué dans la figure ci-dessous, les deux premières séries qui étaient initialement visibles, sont devenues invisibles dans le fichier de sortie.
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="nodejs-cpp" >}}
