---  
title: Exkludera oanvända stilar under konvertering av Excel till HTML med Node.js via C++  
linktitle: Exkludera oanvända stilar vid konvertering från Excel till HTML  
type: docs  
weight: 30  
url: /sv/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/  
description: Lär dig hur du exkluderar oanvända stilar vid konvertering av Excel till HTML med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Microsoft Excel-filer kan innehålla många oanvända stilar. När du exporterar Excel-filen till HTML-format exporteras även dessa oanvända stilar. Detta kan öka storleken på HTML-filen. Du kan exkludera oanvända stilar under konvertering av Excel till HTML med [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--)-egenskapen. När du ställer in den på **true** exkluderas alla oanvända stilar från den genererade HTML:n. Följande skärmbild visar en exempel oanvänd stil i den exporterade HTML:n.  

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)  

## **Uteslut oanvända stilar under Excel till HTML-konvertering**  

Följande kodexempel skapar en arbetsbok och skapar även en oanvänd namngiven stil. Eftersom [**HtmlSaveOptions.getExcludeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExcludeUnusedStyles--) är inställd på **true** kommer denna oanvända namngivna stil inte att exporteras till [utdata-HTML](61767778.zip). Men om du ställer in den på **false** kommer denna oanvända stil att finnas i den exporterade HTML:n som sedan kan ses i HTML-markup som visas i ovanstående skärmbild.  

## **Exempelkod**  

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

