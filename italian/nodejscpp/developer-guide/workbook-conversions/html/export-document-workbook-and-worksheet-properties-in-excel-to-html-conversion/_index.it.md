---  
title: Esporta le proprietà del documento, della cartella di lavoro e del foglio di lavoro nella conversione di Excel in HTML con Node.js tramite C++  
linktitle: Esportare le proprietà del documento, del foglio di lavoro e del foglio di calcolo in HTML  
type: docs  
weight: 50  
url: /it/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/  
description: Impara come esportare le proprietà di Documento, Cartella di Lavoro e Foglio di Lavoro in Excel in HTML utilizzando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Quando si esporta un file Microsoft Excel in HTML usando Microsoft Excel o Aspose.Cells for Node.js via C++, vengono esportate anche varie proprietà di Documento, Cartella di Lavoro e Foglio di Lavoro come mostrato nella schermata seguente. Puoi evitare di esportare queste proprietà impostando [**HtmlSaveOptions.getExportDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportDocumentProperties--), [**HtmlSaveOptions.getExportWorkbookProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorkbookProperties--) e [**HtmlSaveOptions.getExportWorksheetProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetProperties--) su **false**. Il valore predefinito di queste proprietà è **true**. La schermata seguente mostra come appaiono in HTML esportato.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Esportare le proprietà del documento, del foglio di lavoro e del foglio di calcolo in HTML**  

Il codice di esempio di seguito carica il [file Excel di esempio](61767776.xlsx) e lo converte in HTML senza esportare le proprietà di Documento, Cartella di Lavoro e Foglio di Lavoro nell'[output HTML](61767779.zip).  

## **Codice di Esempio**  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
