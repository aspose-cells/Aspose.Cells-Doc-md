---
title: Leer y Escribir Tabla con Fuente de Datos de Consulta a través de Node.js
linktitle: Leer y Escribir Tabla con Origen de Datos de Tabla de Consulta
type: docs
weight: 30
url: /es/nodejs-cpp/read-and-write-table-with-query-table-data-source/
description: Aprenda cómo leer y escribir una tabla con una fuente de datos QueryTable usando Aspose.Cells for Node.js via C++. 
---

## **Leer y Escribir Tabla con Origen de Datos de Tabla de Consulta**
Con Aspose.Cells for Node.js via C++, puede leer y escribir una tabla que tiene una QueryTable como fuente de datos. La compatibilidad con esta función también existe para archivos XLS. El siguiente fragmento de código demuestra cómo leer y escribir una tabla de este tipo primero leyendo la tabla y luego modificándola para agregar la fila de totales.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the source directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load workbook object
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "SampleTableWithQueryTable.xls"));

const worksheet = workbook.getWorksheets().get(0);

const table = worksheet.getListObjects().get(0);

// Check the data source type if it is query table
if (table.getDataSourceType() === AsposeCells.TableDataSourceType.QueryTable) {
table.setShowTotals(true);
}

// Save the file
workbook.save(path.join(outputDir, "SampleTableWithQueryTable_out.xls"));
```

Se adjuntan los archivos de Excel de origen y salida para referencia.

[Archivo de origen](96928091.xls)

[Archivo de salida](96928092.xls)
