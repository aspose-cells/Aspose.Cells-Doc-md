---
title: Exportera kommentarer när du sparar Excel filen till HTML med Node.js via C++
linktitle: Exportera kommentarer vid sparande av Excel fil till HTML
type: docs
weight: 40
url: /sv/nodejs-cpp/export-comments-while-saving-excel-file-to/
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML exporteras inte kommentarer. Men Aspose.Cells for Node.js via C++ tillhandahåller denna funktion med användning av [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/)-egenskapen. Om du ställer in den på **true** visas kommentarerna i HTML:n också.

## **Exportera kommentarer vid sparande av Excel-fil till HTML**

Följande exempelkod förklarar användningen av egenskapen [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). Skärmbilden visar effekten av koden på HTML när den är inställd på **true**. Var god ladda ner [exempel Excel-filen](50528260.xlsx) och [genererad HTML](5052826.txt) för referens.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const sourceDir = path.join(__dirname, "data");
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportCommentsHTML.xlsx"));

// Export comments - set IsExportComments property to true
const opts = new AsposeCells.HtmlSaveOptions();
opts.setIsExportComments(true);

// Save the Excel file to HTML
const outputDir = path.join(__dirname, "output");
wb.save(path.join(outputDir, "outputExportCommentsHTML.html"), opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
