---  
title: Escludi Stili Non Utilizzati durante la conversione di Excel in HTML con Node.js tramite C++  
linktitle: Escludere Stili Non Utilizzati durante la conversione da Excel a HTML  
type: docs  
weight: 30  
url: /it/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/  
description: Impara come escludere gli stili inutilizzati durante la conversione di Excel in HTML usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

I file Microsoft Excel possono contenere molti stili inutilizzati. Quando esporti il file Excel in formato HTML, anche questi stili inutilizzati vengono esportati. Ciò può aumentare la dimensione dell'HTML. Puoi escludere gli stili inutilizzati durante la conversione di file Excel in HTML usando la proprietà [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--). Impostandola su **true**, tutti gli stili inutilizzati vengono esclusi dall'HTML di output. La schermata seguente mostra un esempio di stile inutilizzato all’interno dell’HTML di output.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Escludere Stili Non Utilizzati durante la conversione da Excel a HTML**  

Il codice di esempio seguente crea una cartella di lavoro e crea anche uno stile nominato inutilizzato. Poiché [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) è impostato su **true**, questo stile nominato inutilizzato non verrà esportato in [output HTML](61767778.zip). Se lo imposti su **false**, questo stile inutilizzato sarà presente nell’HTML di output, visibile nel markup HTML come mostrato nella schermata sopra.  

## **Codice di Esempio**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const wb = new AsposeCells.Workbook();

// Create an unused named style
wb.createStyle().setName("UnusedStyle_XXXXXXXXXXXXXX");

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Put some value in cell C7
ws.getCells().get("C7").putValue("This is sample text.");

// Specify html save options, we want to exclude unused styles
const opts = new AsposeCells.HtmlSaveOptions();

// Comment this line to include unused styles
opts.setExcludeUnusedStyles(true);

// Save the workbook in html format
wb.save("outputExcludeUnusedStylesInExcelToHTML.html", opts);
```  

