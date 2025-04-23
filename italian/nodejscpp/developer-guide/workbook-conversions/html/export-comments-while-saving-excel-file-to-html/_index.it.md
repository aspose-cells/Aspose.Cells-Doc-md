---
title: Esporta Commenti durante il salvataggio di Excel in HTML con Node.js tramite C++
linktitle: Esportazione dei commenti durante il salvataggio del file Excel in HTML
type: docs
weight: 40
url: /it/nodejs-cpp/export-comments-while-saving-excel-file-to/
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel in HTML, i commenti non vengono esportati. Tuttavia, Aspose.Cells for Node.js via C++ fornisce questa funzione usando la proprietà [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). Se imposti questa proprietà su **true**, l'HTML visualizzerà anche i commenti presenti nel file Excel.

## **Esporta commenti durante il salvataggio del file di Excel in HTML**

Il codice di esempio seguente spiega l'uso della proprietà [**HtmlSaveOptions.isExportComments**](https://docs.aspose.com/cells/nodejs-cpp/export-comments-while-saving-excel-file-to/). La schermata mostra l'effetto del codice sull'HTML quando è impostato su **true**. Puoi scaricare il [file di esempio di Excel](50528260.xlsx) e l'HTML [generato](5052826.txt) come riferimento.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Codice di Esempio**

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
