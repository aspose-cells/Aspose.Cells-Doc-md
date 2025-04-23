---
title: Limitar el número de páginas generadas  Conversión de Excel a PDF con Node.js via C++
linktitle: Limitar el número de páginas generadas  Conversión de Excel a PDF
type: docs
weight: 180
url: /es/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Aprenda cómo limitar la cantidad de páginas generadas al convertir una hoja de cálculo de Excel a PDF usando Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

A veces, desea imprimir un rango de páginas en un archivo PDF de salida. Aspose.Cells for Node.js via C++ tiene la capacidad de establecer un límite en la cantidad de páginas que se generan al convertir una hoja de cálculo de Excel al formato PDF.

{{% /alert %}}

## **Limitar el número de páginas generadas**

El siguiente ejemplo muestra cómo renderizar un rango de páginas (3 y 4) en un archivo de Microsoft Excel a PDF.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Instantiate the PdfSaveOption
const options = new AsposeCells.PdfSaveOptions();

// Print only Page 3 and Page 4 in the output PDF
// Starting page index (0-based index)
options.setPageIndex(3);
// Number of pages to be printed
options.setPageCount(2);

// Save the PDF file
workbook.save(path.join(dataDir, "outPDF1.out.pdf"), options);
```

{{% alert color="primary" %}}

Si la hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) justo antes de renderizarla a PDF. Hacer esto asegura que los valores dependientes de fórmulas se recalculen y que los valores correctos se rendericen en el archivo de salida.

{{% /alert %}}
