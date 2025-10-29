---
title: Détecter les cellules fusionnées dans une feuille de calcul avec Node.js via C++
linktitle: Détecter les cellules fusionnées dans une feuille de calcul
description: Apprenez comment détecter les cellules fusionnées dans une feuille de calcul en utilisant Aspose.Cells for Node.js via C++. Cet article vous montrera comment utiliser la bibliothèque pour identifier et manipuler les cellules fusionnées.
keywords: Aspose.Cells, Feuille de calcul, Fusionner des cellules, Détecter, Identifier, Opérer Node.js via C++
type: docs
weight: 80
url: /fr/nodejs-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Cet article fournit des informations sur la manière d'obtenir les zones de cellules fusionnées dans une feuille de calcul.

Aspose.Cells for Node.js via C++ permet d'obtenir les zones de cellules fusionnées dans une feuille de calcul. Vous pouvez aussi les dissocier (diviser). Cet article montre le code le plus simple utilisant l'API **Aspose.Cells** pour effectuer cette tâche.

{{% /alert %}}

La composante fournit la méthode [**Cells.getMergedAreas()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMergedAreas--) qui peut obtenir toutes les cellules fusionnées. L'exemple de code ci-dessous montre comment détecter les cellules fusionnées dans une feuille de calcul.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleInput.xlsx");

// Instantiate a new Workbook
// Open an existing excel file
const wkBook = new AsposeCells.Workbook(filePath);
// Get a worksheet in the workbook
const wkSheet = wkBook.getWorksheets().get("Sheet2");
// Clear its contents
wkSheet.getCells().clear();

// Get merged areas
const areas = wkSheet.getCells().getMergedAreas();

// Check if areas is null or not
if (!areas || areas.length === 0) {
console.warn("No merged areas to unmerge.");
return;
}

// Define some variables
let frow, fcol, erow, ecol, trows, tcols;
// Loop through the arraylist and get each cellarea
// To unmerge it
for (let i = 0; i < areas.length; i++) {
frow = areas[i].startRow;
fcol = areas[i].startColumn;
erow = areas[i].endRow;
ecol = areas[i].endColumn;

trows = erow - frow + 1;
tcols = ecol - fcol + 1;
wkSheet.getCells().unMerge(frow, fcol, trows, tcols);
}

const outputFilePath = path.join(dataDir, "MergeTrial.out.xlsx");
// Save the excel file
wkBook.save(outputFilePath);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
