---  
title: Skapa delad arbetsbok med Aspose.Cells for Node.js via C++  
linktitle: Skapa Delad arbetsbok med Aspose.Cells  
type: docs  
weight: 40  
url: /sv/nodejs-cpp/create-shared-workbook-with-aspose-cells/  
description: Lär dig hur du skapar en delad arbetsbok med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Microsoft Excel tillåter att du delar arbetsboken som visas i följande skärmdump. När du delar arbetsboken kan fler än en användare redigera den på nätverket. Aspose.Cells for Node.js via C++ gör det möjligt att skapa en delad arbetsbok med [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--)-egenskapen.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Skapa Delad arbetsbok med Aspose.Cells**  

Följande exempel skapar en delad arbetsbok genom att ställa in [**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--)-egenskapen till **true**. När du öppnar [utdata Excel-filen](55541786.xlsx) i Microsoft Excel, kommer du att se **Shared** med arbetsbokens namn som visas i denna skärmdump.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Exempelkod**  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create Workbook object
const wb = new AsposeCells.Workbook();

// Share the Workbook
wb.getSettings().setShared(true);

// Save the Shared Workbook
wb.save("outputSharedWorkbook.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
