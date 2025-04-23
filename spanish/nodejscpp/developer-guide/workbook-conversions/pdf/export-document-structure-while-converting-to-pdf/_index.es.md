---
title: Exportar estructura del documento al convertir a PDF con Node.js a través de C++
linktitle: Exportar la Estructura del Documento al Convertir a PDF
type: docs
weight: 360
url: /es/nodejs-cpp/export-document-structure-while-converting-to-pdf/
description: Aprende cómo exportar la estructura del documento al convertir un archivo de Excel a un PDF etiquetado usando Aspose.Cells for Node.js via C++. 
---

Las facilidades de estructura lógica del PDF proporcionan un mecanismo para incorporar información sobre la estructura del contenido del documento en un archivo PDF. Aspose.Cells for Node.js via C++ mantiene la información sobre la estructura desde un documento de Microsoft Excel, como celda, fila, tabla, hoja de cálculo, imagen, forma, encabezado/pie de página, etc.

Con la opción [PdfSaveOptions.getExportDocumentStructure()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getExportDocumentStructure--) puedes guardar en un PDF etiquetado con la estructura del documento exportada.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "document-structure-example.xlsx");
// Open the excel file with image, shape, chart, etc.
const wb = new AsposeCells.Workbook(filePath);

// Set to export document structure.
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setExportDocumentStructure(true);

// Save the pdf file with PdfSaveOptions
wb.save("output.pdf", pdfSaveOptions);
```

