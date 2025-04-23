---
title: Eliminar conexión de Pivote con Node.js a través de C++
linktitle: Eliminar conexión de tabla dinámica
type: docs
weight: 30
url: /es/nodejs-cpp/remove-pivot-connection/
description: Aprende cómo eliminar la conexión de pivote usando Aspose.Cells for Node.js via C++.
keywords: Eliminar conexión de pivote sin Office 2013, Office 2016, Office 2019 y Office 365 con Node.js a través de C++.
---

## **Escenarios de uso posibles**

Si deseas disociar un segmentador y una tabla dinámica en Excel, debes hacer clic derecho en el segmentador y seleccionar la opción "Conexiones de informe...". En la lista de opciones, puedes operar en la casilla de verificación. De manera similar, si quieres disociar un segmentador y una tabla dinámica usando la API de Aspose.Cells programáticamente, usa el método [**Slicer.removePivotConnection(PivotTable)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#removePivotConnection-pivottable-). Esto disociará el segmentador y la tabla dinámica.

## **Desasociar filtro y tabla dinámica**

El siguiente código de ejemplo carga el [archivo Excel de muestra](remove-pivot-connection.xlsx) que contiene un segmentador existente. Accede a los segmentadores y luego disocia el segmentador y la tabla dinámica. Finalmente, guarda el libro como [archivo Excel de salida](remove-pivot-connection-out.xlsx).

## **Código de muestra**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "remove-pivot-connection.xlsx");
// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0);
// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);
// Remove PivotTable connection.
slicer.removePivotConnection(pivotTable);
// Save the workbook in output XLSX format.
workbook.save(path.join(dataDir, "remove-pivot-connection-out.xlsx"));
``` 
