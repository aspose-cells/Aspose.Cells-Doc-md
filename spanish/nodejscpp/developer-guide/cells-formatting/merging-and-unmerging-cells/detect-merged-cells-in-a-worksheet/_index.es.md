---
title: Detectar celdas combinadas en una hoja de cálculo con node.js vía C++
linktitle: Detectar Celdas Fusionadas en una Hoja de Trabajo
description: Aprende cómo detectar celdas combinadas en una hoja de cálculo usando Aspose.Cells for Node.js via C++. Este artículo te mostrará cómo usar la biblioteca para identificar y manipular celdas combinadas.
keywords: Aspose.Cells, Hoja de cálculo, Combinar celdas, Detectar, Identificar, Operar en Node.js vía C++
type: docs
weight: 80
url: /es/nodejs-cpp/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Este artículo proporciona información sobre cómo obtener áreas de celdas fusionadas en una hoja de cálculo.

Aspose.Cells for Node.js via C++ te permite obtener áreas de celdas combinadas en una hoja de cálculo. También puedes deshacer la combinación (dividirlas). Este artículo muestra el código más sencillo usando **Aspose.Cells API** para realizar la tarea.

{{% /alert %}}

El componente ofrece el método [**Cells.getMergedAreas()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getMergedAreas--) que puede obtener todas las celdas combinadas. El siguiente ejemplo de código muestra cómo detectar celdas combinadas en una hoja de cálculo.

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
