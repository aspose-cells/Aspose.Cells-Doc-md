---  
title: Rita tidslinje medan du renderar Excel till PDF med Node.js via C++  
linktitle: Rita tidslinje vid rendering av Excel till PDF  
type: docs  
weight: 60  
url: /sv/nodejs-cpp/draw-timeline-while-rendering-excel-to-pdf/  
description: Hantera tidslinjer för Excel filer med Aspose.Cells for Node.js via C++.  
keywords: Rendera tidslinjen till PDF utan Office 2013, Office 2016, Office 2019 och Office 365 Node.js via C++  
---  

## **Rita tidslinje vid rendering av Excel till PDF**  
Om du har en Excel-fil som har en tidslinje tillagd och du vill exportera Excel till PDF med tidslinjeinställningarna, stöder Aspose.Cells for Node.js via C++ detta nu som standard. Exportera helt enkelt Excel-filen med tidslinje till PDF, och den genererade PDF:en visar den tillagda tidslinjen.  

Följande exempelkod laddar in den [exempel-Excel-filen](input.xlsx) som innehåller en befintlig tidslinje. Sedan sparar den arbetsboken som [utmatnings-PDF-filen](out.pdf). Följande skärmbild jämför käll-Excel-filen och den genererade PDF-filen.  

<img src="out.png" width="60%">  

## **Exempelkod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load sample Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Save file to pdf
workbook.save("out.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
