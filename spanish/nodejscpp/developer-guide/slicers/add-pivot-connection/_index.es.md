---
title: Agregar conexión de Pivote con Node.js a través de C++
linktitle: Agregar conexión de tabla dinámica
type: docs
weight: 30
url: /es/nodejs-cpp/add-pivot-connection/
description: Aprende cómo agregar conexión de pivote usando Aspose.Cells for Node.js via C++.
keywords: Agregar conexión de pivote sin Office 2013, Office 2016, Office 2019 y Office 365 con Node.js a través de C++.
---

## **Escenarios de uso posibles**

Si deseas asociar un segmentador y una tabla dinámica en Excel, debes hacer clic derecho en el segmentador y seleccionar la opción "Conexiones de informe...". En la lista de opciones, puedes operar con la casilla de verificación. De manera similar, si quieres asociar un segmentador y una tabla dinámica mediante la API de Aspose.Cells programáticamente, usa el método [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#addPivotConnection-PivotTable-). Esto asociará el segmentador y la tabla dinámica.

## **Asociar filtro y tabla dinámica**

El siguiente código de ejemplo carga el [archivo Excel de muestra](add-pivot-connection.xlsx) que contiene un segmentador existente. Accede al segmentador y luego asocia el segmentador con la tabla dinámica. Finalmente, guarda el libro como [archivo Excel de salida](add-pivot-connection-out.xlsx).

## **Código de muestra**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "add-pivot-connection.xlsx");

// Load sample Excel file containing slicer.
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);

// Access the first PivotTable inside the PivotTable collection.
const pivotTable = worksheet.getPivotTables().get(0); 

// Access the first slicer inside the slicer collection.
const slicer = worksheet.getSlicers().get(0);

// Adds PivotTable connection.
slicer.addPivotConnection(pivotTable);

workbook.save(path.join(dataDir, "add-pivot-connection-out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
