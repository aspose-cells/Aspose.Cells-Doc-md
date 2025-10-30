---  
title: Exportera Arbetsblad CSS separat i utdata HTML med Node.js via C++  
linktitle: Exportera arbetsbladets CSS separat i utdata HTML filen  
type: docs  
weight: 80  
url: /sv/nodejs-cpp/export-worksheet-css-separately-in-output/  
description: Lär dig hur du exporterar arbetsblad CSS separat vid konvertering av en Excel fil till HTML med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**

Aspose.Cells for Node.js via C++ ger funktionen att exportera arbetsblad CSS separat när du konverterar din Excel-fil till HTML. Använd [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--)-egenskapen för detta ändamål och ställ in den på **true** vid sparning av Excel-filen i HTML-format.

## **Exportera arbetsbladets CSS separat i utdata-HTML-filen**

Följande exempel kod skapar en Excel-fil, lägger till lite text i cell **B5** i **röd** färg, och sparar sedan den i HTML-format med [**HtmlSaveOptions.getExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportWorksheetCSSSeparately--)-egenskapen. Se [utdata HTML](60489766.zip) genererat av koden för referens. Du hittar **stylesheet.css** inuti den som ett resultat av exempel koden.

## **Exempelkod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - export worksheet css separately
const opts = new AsposeCells.HtmlSaveOptions();
opts.setExportWorksheetCSSSeparately(true);

// Save the workbook in html 
wb.save("outputExportWorksheetCSSSeparately.html", opts);
```

## **Exportera arbetsbok med enkelt blad till HTML**

När ett arbetsbok med flera blad konverteras till HTML med Aspose.Cells for Node.js via C++, skapas en HTML-fil tillsammans med en mapp som innehåller CSS och flera HTML-filer. När denna HTML-fil öppnas i webbläsaren är flikarna synliga. Samma beteende krävs för ett arbetsbok med ett enda blad när det konverteras till HTML. Tidigare skapades ingen separat mapp för arbetsböcker med enkelt blad, och endast en HTML-fil skapades. Sådan en HTML-fil visar inte flikar när den öppnas i webbläsaren. MS Excel skapar en riktig mapp och HTML för ett enskilt blad, och därför är samma beteende implementerat med Aspose.Cells API:er. Exempelfilen kan laddas ner från följande länk för användning i exemplet nedan:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleSingleSheet.xlsx");
// Load the sample Excel file containing single sheet only
const wb = new AsposeCells.Workbook(sourceFilePath);

// Specify HTML save options
const options = new AsposeCells.HtmlSaveOptions();

// Set optional settings if required
options.setEncoding(AsposeCells.EncodingType.UTF8);
options.setExportImagesAsBase64(true);
options.setExportGridLines(true);
options.setExportSimilarBorderStyle(true);
options.setExportBogusRowData(true);
options.setExcludeUnusedStyles(true);
options.setExportHiddenWorksheet(true);

// Save the workbook in Html format with specified Html Save Options
wb.save(path.join(dataDir, "outputSampleSingleSheet.htm"), options);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
