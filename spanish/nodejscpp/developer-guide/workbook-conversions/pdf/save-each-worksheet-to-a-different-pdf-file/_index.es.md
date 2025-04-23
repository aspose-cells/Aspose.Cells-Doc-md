---  
title: Guardar cada hoja en un archivo PDF diferente con Node.js vía C++  
linktitle: Guardar Cada Hoja de Cálculo en un Archivo PDF Diferente  
type: docs  
weight: 130  
url: /es/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/  
---  

{{% alert color="primary" %}}  
Aspose.Cells soporta convertir archivos XLS (que contienen imágenes, gráficas, etc.) en documentos PDF. Aspose.Cells for Node.js via C++ puede trabajar de manera independiente para convertir una hoja de cálculo a PDF, y no necesitas usar Aspose.PDF para Node.js vía C++ para la conversión. La conversión no requiere que el software cree o use archivos temporales, ya que todo el proceso se realiza en memoria.  
{{% /alert %}}  

## **Guardar cada hoja de cálculo en un archivo PDF diferente**  
Si necesitas guardar cada hoja de cálculo en tu archivo Excel plantilla para generar diferentes archivos PDF, puedes lograrlo fácilmente. Puedes intentar establecer un índice de hoja a la opción [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/nodejs-cpp/pdfs saveoptions/#sheetSet) a la vez para renderizar a PDF.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Get the Excel file path
const filePath = path.join(dataDir, "input.xlsx");

// Instantiate a new workbook and open the Excel file from its location
const workbook = new AsposeCells.Workbook(filePath);

// Get the count of the worksheets in the workbook
const sheetCount = workbook.getWorksheets().getCount();

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Take PDFs of each sheet
for (let j = 0; j < sheetCount; j++) {
const ws = workbook.getWorksheets().get(j);

// set worksheet to output
const sheetSet = new AsposeCells.SheetSet([ws.getIndex()]);
pdfSaveOptions.setSheetSet(sheetSet);

workbook.save(path.join(dataDir, `worksheet-${ws.getName()}.out.pdf`), pdfSaveOptions);
}
```  

{{% alert color="primary" %}}  
Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.  
{{% /alert %}}  

