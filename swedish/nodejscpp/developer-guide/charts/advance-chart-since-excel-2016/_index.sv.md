---  
title: Läs och hantera Excel 2016 diagram med Node.js via C++  
linktitle: Läs och hantera Excel 2016 diagram  
description: Lär dig hur man läser och manipulerar Excel 2016 diagram med Aspose.Cells for Node.js via C++. Denna guide visar hur man får tillgång till och ändrar olika diagramegenskaper.  
keywords: Aspose.Cells för Node.js, Excel 2016 diagram, läsa, manipulera, dataetiketter, serie färger, layout, hierarkisk diagrammering, cirkulär diagrammering.  
type: docs  
weight: 48  
url: /sv/nodejs-cpp/read-and-manipulate-excel-2016-charts/  
---  

## **Möjliga användningsscenario**  
Aspose.Cells stöder nu läsning och hantering av Microsoft Excel 2016-diagram som inte finns i Microsoft Excel 2013 eller äldre versioner.  
## **Läs och hantera Excel 2016-diagram**  
Följande exempelkod laddar [källexcelfilen](22774101.xlsx) som innehåller Excel 2016-diagram i det första arbetsbladet. Den läser alla diagram en efter en och ändrar deras titel i enlighet med diagramtypen. Följande skärmdump visar källexcelfilen före kodens utförande. Som du kan se är diagramtiteln densamma för alla diagram.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

Följande skärmbild visar den [slutgiltiga Excel-filen](22774104.xlsx) efter körningen av koden. Som du kan se har diagramrubriken ändrats enligt dess diagramtyp.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)  
## **Exempelkod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "excel2016Charts.xlsx");

// Load source excel file containing excel 2016 charts
const workbook = new AsposeCells.Workbook(filePath);

// Access the first worksheet which contains the charts
const sheet = workbook.getWorksheets().get(0);

// Access all charts one by one and read their types
for (let i = 0; i < sheet.getCharts().getCount(); i++) {
// Access the chart
const ch = sheet.getCharts().get(i);

// Print chart type
console.log(ch.getType());

// Change the title of the charts as per their types
ch.getTitle().setText("Chart Type is " + ch.getType().toString());
}

// Save the workbook
workbook.save(path.join(dataDir, "out_excel2016Charts.xlsx"));
```  
## **Konsoloutput**  
Här är konsolens utdata för den ovanstående exempelkoden när den körs med den tillhandahållna [källa Excel-filen](22774101.xlsx).

{{< highlight javascript >}}  

 Waterfall  

Treemap  

Sunburst  

Histogram  

BoxWhisker  

{{< /highlight >}}  

## **Fortsatta ämnen**  
- [Skapa vattenfalldiagram](/cells/sv/nodejs-cpp/creating-waterfall-chart/)  
- [Skapa treemap-diagram](/cells/sv/nodejs-cpp/creating-treemap-chart/)  
- [Skapa sunburst-diagram](/cells/sv/nodejs-cpp/creating-sunburst-chart/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
