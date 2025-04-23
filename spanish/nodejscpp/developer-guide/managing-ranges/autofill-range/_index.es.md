---
title: Autocompletar rango de archivo de Excel con Node.js mediante C++
linktitle: AutoRellenar Rango
type: docs
weight: 105
url: /es/nodejs-cpp/autofill-ranges/
description: Aprende cómo realizar una operación de autocompletado en un rango especificado de un archivo de Excel usando Aspose.Cells for Node.js via C++.
---

## **Realizar un autollenado en el rango especificado en Excel**

En Excel, selecciona un rango, mueve el ratón a la esquina inferior derecha y arrastra la "más" para autocompletar datos.

## **Autocompletar rangos con Aspose.Cells for Node.js via C++**

El siguiente ejemplo muestra cómo realizar una operación de autocompletado en un rango, y aquí está el archivo de ejemplo que se puede descargar para probar esta función:

[range_autofill.xlsx](range_autofill.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "range_autofill.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("C3:C4");
const dest = cells.createRange("C5:C10");
// AutoFill
src.autoFill(dest, AsposeCells.AutoFillType.Series);
// Save the Workbook
workbook.save("range_autofill_result.xlsx");
```

