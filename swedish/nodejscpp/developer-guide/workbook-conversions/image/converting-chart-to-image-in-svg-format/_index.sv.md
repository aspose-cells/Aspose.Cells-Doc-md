---  
title: Konvertering av diagram till bild i SVG format med Node.js via C++  
linktitle: Konvertera diagram till bild i SVG format  
type: docs  
weight: 240  
url: /sv/nodejs-cpp/converting-chart-to-image-in-svg-format/  
description: Lär dig hur man konverterar ett diagram till SVG format bilden med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Scalable Vector Graphics (SVG) är ett XML-baserat vektorbildformat för tvådimensionell grafik som också stöder interaktivitet och animation. SVG-specifikationen är en öppen standard som utvecklats av World Wide Web Consortium (W3C) sedan 1999.  

SVG-bilder och deras beteenden definieras i XML-textfiler. Detta innebär att de kan sökas, indexeras, skriptas och komprimeras. Som XML-filer kan SVG-bilder skapas och redigeras med vilken textredigerare som helst, men skapas oftare med ritprogram.  

Aspose.Cells kan spara diagram till bilder i olika format som BMP, JPEG, PNG, GIF, SVG osv. Denna artikel förklarar hur man sparar ett diagram i SVG-format.  

{{% /alert %}}  

Följande exempelkod förklarar hur man använder Aspose.Cells för att konvertera ett diagram till en bild i SVG-format. Koden laddar den ursprungliga Microsoft Excel-filen och sparar sedan det första diagrammet som hittas på den första arbetsbladet till SVG.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from source file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "SampleChartBook.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart inside the worksheet
const chart = worksheet.getCharts().get(0);

// Set image or print options
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Svg);

// Save the chart to svg format
chart.toImage(path.join(dataDir, "Image_out.svg"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
