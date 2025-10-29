---
title: Fusionner plusieurs feuilles de calcul en une seule avec Node.js via C++
linktitle: Combiner plusieurs feuilles de calcul en une seule feuille de calcul
type: docs
weight: 160
url: /fr/nodejs-cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Découvrez comment combiner plusieurs feuilles de calcul en une seule en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}} 

Parfois, il est nécessaire de combiner plusieurs feuilles de calcul en une seule. Cela peut être facilement réalisé à l'aide de l'API Aspose.Cells. Cet article vous montrera un exemple de code qui lit un classeur source et combine les données de toutes les feuilles de calcul source en une seule feuille de calcul à l'intérieur d'un classeur de destination.

{{% /alert %}} 

Le code d'exemple suivant vous montre comment combiner plusieurs feuilles de calcul en une seule feuille de calcul.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const destWorkbook = new AsposeCells.Workbook();
const destSheet = destWorkbook.getWorksheets().get(0);

let TotalRowCount = 0;

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
const sourceSheet = workbook.getWorksheets().get(i);

const sourceRange = sourceSheet.getCells().getMaxDisplayRange();
const destRange = destSheet.getCells().createRange(
sourceRange.getFirstRow() + TotalRowCount,
sourceRange.getFirstColumn(),
sourceRange.getRowCount(),
sourceRange.getColumnCount()
);

destRange.copy(sourceRange);
TotalRowCount += sourceRange.getRowCount();
}

const outputFilePath = path.join(dataDir, "Output.out.xlsx");
destWorkbook.save(outputFilePath);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
