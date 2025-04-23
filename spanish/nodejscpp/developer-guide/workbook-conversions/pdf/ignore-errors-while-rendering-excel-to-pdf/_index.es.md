---  
title: Ignorar errores al renderizar Excel a PDF con Node.js a través de C++  
linktitle: Ignorar Errores al Renderizar Excel a PDF  
type: docs  
weight: 80  
url: /es/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/  
description: Aprenda cómo ignorar errores durante la conversión de archivos Excel a PDF usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

A veces, al convertir su archivo Excel a PDF, ocurren errores o excepciones y el proceso de conversión termina. Puede ignorar todos esos errores durante la conversión usando la propiedad [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--). De esta manera, el proceso de conversión se completará sin lanzar ningún error o excepción, pero puede ocurrir pérdida de datos. Por lo tanto, utilice esta propiedad solo si la pérdida de datos no es crítica para usted.  

## **Ignorar errores al renderizar Excel a PDF**  

El siguiente código carga el [archivo Excel de ejemplo](55541778.xlsx), pero el archivo de ejemplo tiene errores y lanza un error durante la [conversión a PDF](55541779.pdf) en 17.11, pero como estamos usando la propiedad [**PdfSaveOptions.getIgnoreError()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getIgnoreError--), no lanza error. Sin embargo, una *forma en forma de flecha roja redonda* como se muestra en esta captura de pantalla se pierde.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleErrorExcel2Pdf.xlsx");
// Load the Sample Workbook that throws Error on Excel2Pdf conversion
const wb = new AsposeCells.Workbook(filePath);

// Specify Pdf Save Options - Ignore Error
const opts = new AsposeCells.PdfSaveOptions();
opts.IgnoreError = true;

// Save the Workbook in Pdf with Pdf Save Options
wb.save("outputErrorExcel2Pdf.pdf", opts);
```  

