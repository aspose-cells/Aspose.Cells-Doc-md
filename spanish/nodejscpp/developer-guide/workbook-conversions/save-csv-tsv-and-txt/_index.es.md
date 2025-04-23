---
title: Convertir Excel a CSV, TSV y Txt con Node.js vía C++
linktitle: Guardar como CSV, TSV y Txt
type: docs
weight: 40
url: /es/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/
description: Aprende cómo convertir archivos de Excel a formatos CSV, TSV y TXT usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells hace posible convertir archivos de Excel, ODS, JSON y otros formatos a CSV, TSV y TXT.

{{% /alert %}}

## **Guardar libro de trabajo en formato de texto o CSV**

A veces, quieres convertir o guardar un libro con múltiples hojas en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), por defecto, tanto Microsoft Excel como Aspose.Cells guardan solo el contenido de la hoja activa.

El siguiente ejemplo de código explica cómo guardar un libro completo en formato de texto. Carga el libro fuente, que puede ser cualquier archivo de hoja de cálculo de Microsoft Excel u OpenOffice (como XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro de trabajo al formato TXT.

Puedes modificar el mismo ejemplo para guardar tu archivo en CSV. Por defecto, [**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--) es una coma, así que no especifiques un separador al guardar en formato CSV.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **Guardar archivos de texto con separador personalizado**

Los archivos de texto contienen datos de la hoja de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```


## **Temas avanzados**
- [Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV](/cells/es/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Recortar filas y columnas en blanco al exportar hojas de cálculo al formato CSV](/cells/es/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
