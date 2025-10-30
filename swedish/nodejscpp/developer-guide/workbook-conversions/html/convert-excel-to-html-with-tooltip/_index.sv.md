---  
title: Konvertera Excel till HTML med tooltip med Node.js via C++  
linktitle: Konvertera Excel till HTML med verktygstips  
type: docs  
weight: 200  
url: /sv/nodejs-cpp/convert-excel-to-html-with-tooltip/  
description: Lär dig hur du konverterar Excel filer till HTML format med verktyg för tooltip för fullständig textvisning med Aspose.Cells for Node.js via C++.  
---  

## **Konvertera Excel till HTML med verktygstips**

Det kan finnas situationer där texten blir avklippt i den genererade HTML-koden och du vill visa hela texten som ett tooltip vid hover. Aspose.Cells for Node.js via C++ stöder detta genom att tillhandahålla [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--) egenskapen. Att sätta [**HtmlSaveOptions.getAddTooltipText()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getAddTooltipText--) egenskapen till **true** kommer att lägga till hela texten som ett tooltip i den genererade HTML-koden.

Följande bild visar tooltipen i den genererade HTML-filen.

![todo:image_alt_text](convert-excel-to-html-with-tooltip_1.jpg)

Följande kodexempel laddar [käll-Excel-filen](98107416.xlsx) och genererar [utdata-HTML-filen](98107417.zip) med verktygstips.

Exempelkod

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "AddTooltipToHtmlSample.xlsx"));

const options = new AsposeCells.HtmlSaveOptions();
options.setAddTooltipText(true);

// Save as Markdown
workbook.save(path.join(outputDir, "AddTooltipToHtmlSample_out.html"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
