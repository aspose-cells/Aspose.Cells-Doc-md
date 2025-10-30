---  
title: Exportera liknande kantlinjestil när kantlinjestil inte stöds av webbläsare med Node.js via C++  
linktitle: Exportera liknande kantsytel när kantsytele inte stöds av webbläsare  
type: docs  
weight: 70  
url: /sv/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/  
description: Lär dig hur du exporterar kanter som inte stöds av webbbläsare när du konverterar Excel filer till HTML med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Microsoft Excel stöder vissa typer av streckade kanter som inte stöds av webbläsare. När du konverterar en sådan Excel-fil till HTML med Aspose.Cells for Node.js via C++ tas dessa kanter bort. Men Aspose.Cells kan också visa sådana kanter med [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--)-egenskapen. Ställ in värdet på **true** och de icke-stödda kanterna exporteras även till HTML-filen.  

## **Exportera liknande kantstilmall när kantstil inte stöds av webbläsare**  

Följande exempel kod laddar den [exempel Excel-filen](64716806.xlsx) som innehåller några inte stödda gränser som visas i följande skärmbild. Skärmbilden illustrerar vidare effekten av [**HtmlSaveOptions.getExportSimilarBorderStyle()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportSimilarBorderStyle--)-egenskapen i den [utdata HTML](64716804.zip).  

![todo:image_alt_text](export-similar-border-style-when-border-style-is-not-supported-by-web-browsers_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExportSimilarBorderStyle.xlsx");

// Load the sample Excel file
const wb = new AsposeCells.Workbook(filePath);

// Specify Html Save Options - Export Similar Border Style
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportSimilarBorderStyle(true);

// Save the workbook in Html format with specified Html Save Options
wb.save("outputExportSimilarBorderStyle.html", opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
