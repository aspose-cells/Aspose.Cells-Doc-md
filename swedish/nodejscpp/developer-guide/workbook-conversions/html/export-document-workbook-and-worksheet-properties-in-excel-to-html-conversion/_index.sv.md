---  
title: Exportera dokumentarbetsbok och kalkylbladsegenskaper i konvertering av Excel till HTML med Node.js via C++  
linktitle: Exportera dokumentarbetsbok och arbetsbladsegenskaper i Excel till HTML omvandling  
type: docs  
weight: 50  
url: /sv/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/  
description: Lär dig hur du exporterar dokument , arbetsboks och kalkylblads egenskaper i Excel till HTML med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

När en Microsoft Excel-fil exporteras till HTML med Microsoft Excel eller Aspose.Cells for Node.js via C++, exporteras även olika typer av dokument-, arbetsboks- och kalkylbladsegenskaper som visas i följande skärmbild. Du kan undvika att exportera dessa egenskaper genom att ställa in [**HtmlSaveOptions.getExportDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportDocumentProperties--), [**HtmlSaveOptions.getExportWorkbookProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorkbookProperties--) och [**HtmlSaveOptions.getExportWorksheetProperties()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetProperties--) på **false**. Standardvärdet för dessa egenskaper är **true**. Följande skärmbild visar hur dessa egenskaper ser ut i den exporterade HTML:n.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **Exportera dokument-, arbetsboks- och arbetsbladsegenskaper i Excel till HTML-omvandling**  

Följande exempel kod laddar [exempel-Excel-filen](61767776.xlsx) och konverterar den till HTML utan att exportera dokument-, arbetsboks- och kalkylbladsattribut i [utdata-HTML](61767779.zip).  

## **Exempelkod**  

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
