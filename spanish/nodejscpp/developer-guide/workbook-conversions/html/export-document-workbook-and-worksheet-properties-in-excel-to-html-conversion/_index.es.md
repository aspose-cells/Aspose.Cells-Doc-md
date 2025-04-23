---  
title: Exportar propiedades del documento, libro de trabajo y hoja de cálculo en la conversión de Excel a HTML con Node.js a través de C++  
linktitle: Exportar Propiedades del Documento, Libro y Hoja de Excel a HTML  
type: docs  
weight: 50  
url: /es/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/  
description: Aprende cómo exportar propiedades del Documento, Libro de trabajo y Hoja de cálculo en Excel a HTML usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Cuando un archivo de Microsoft Excel se exporta a HTML usando Microsoft Excel o Aspose.Cells for Node.js via C++, también se exportan diversos tipos de propiedades del Documento, Libro de trabajo y Hoja, como se muestra en la captura. Puedes evitar la exportación de estas propiedades configurando [**HtmlSaveOptions.getExportDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportDocumentProperties--), [**HtmlSaveOptions.getExportWorkbookProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorkbookProperties--) y [**HtmlSaveOptions.getExportWorksheetProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetProperties--) en **false**. El valor predeterminado de estas propiedades es **true**. La siguiente captura muestra cómo se ven estas propiedades en el HTML exportado.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Exportar Propiedades del Documento, Libro y Hoja de Excel a HTML**  

El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767776.xlsx) y lo convierte a HTML sin exportar las propiedades del Documento, Libro y Hoja en el [HTML de salida](61767779.zip).  

## **Código de muestra**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportDocumentWorkbookAndWorksheetPropertiesInHTML.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify Html Save Options
const options = new AsposeCells.HtmlSaveOptions();

// We do not want to export document, workbook and worksheet properties
options.setExportDocumentProperties(false);
options.setExportWorkbookProperties(false);
options.setExportWorksheetProperties(false);

// Export the Excel file to Html with Html Save Options
workbook.save("outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html", options);
```  

