---
title: Eliminar filas duplicadas en una hoja de cálculo con Node.js vía C++
linktitle: Eliminar filas duplicadas en una hoja de cálculo
type: docs
weight: 370
url: /es/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/
description: Aprenda cómo eliminar filas duplicadas en una hoja de cálculo usando Aspose.Cells for Node.js via C++ y seleccionar columnas específicas para verificar duplicados.
---


Eliminar filas duplicadas es una de las muchas funciones útiles de Microsoft Excel. Permite a los usuarios eliminar filas duplicadas en una hoja de cálculo, y puede escoger qué columnas deben verificarse para información duplicada.

Aspose.Cells for Node.js via C++ proporciona el método `Cells.removeDuplicates()` para este propósito. También puede establecer `startRow`, `startColumn`, `endRow` y `endColumn` para especificar el rango de columnas a verificar para duplicados.

A continuación se muestran los archivos de muestra que se pueden descargar para probar esta característica:

[removeduplicates.xlsx](removeduplicates.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "removeduplicates.xlsx");

// Create workbook
const book = new AsposeCells.Workbook(filePath);

// Remove Duplicate
book.getWorksheets().get(0).getCells().removeDuplicates(0, 0, 5, 3);

// Save result
book.save("removeduplicates-result.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
