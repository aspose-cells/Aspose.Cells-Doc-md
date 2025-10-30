---  
title: Renderizar una página PDF por hoja de cálculo de Excel  Conversión de Excel a PDF con Node.js a través de C++  
linktitle: Renderizar una página de PDF por hoja de cálculo de Excel  Conversión de Excel a PDF  
type: docs  
weight: 100  
url: /es/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
---  

{{% alert color="primary" %}}  

Cuando trabaja con archivos grandes de Microsoft Excel (por ejemplo, un libro con muchas hojas, cada una con 50 columnas y 300 o más filas de datos), es posible que desee que la salida en PDF muestre una página por hoja, independientemente del tamaño de la hoja. Esto significa que cada página probablemente tendrá un tamaño de página muy diferente. Esto se puede lograr utilizando Aspose.Cells for Node.js via C++.  

{{% /alert %}}  

Consulte el siguiente código de ejemplo que convierte un archivo de Excel con varias hojas de cálculo a PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Implement one page per worksheet option
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setOnePagePerSheet(true);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile.out.pdf"), pdfSaveOptions);
```  

{{% alert color="primary" %}}  

Si la opción [PdfSaveOptions.getOnePagePerSheet()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) está configurada en **true**, todo el contenido de la hoja se representará en una sola página PDF.  

{{% /alert %}} {{% alert color="primary" %}}  

Si tu hoja de cálculo contiene fórmulas, es mejor llamar a [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) justo antes de renderizar la hoja de cálculo a PDF. Esto garantiza que los valores dependientes de fórmulas sean recalculados y que se muestren los valores correctos en el PDF.  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
