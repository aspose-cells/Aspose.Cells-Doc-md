---  
title: Kopiera Sparkline genom att specificera dataområde och plats för Sparkline grupp med Node.js via C++  
linktitle: Kopiera sparkline genom att ange dataområde och plats för sparklinegrupp  
type: docs  
weight: 300  
url: /sv/nodejs-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/  
description: Lär dig hur du kopierar en sparkline i Excel genom att specificera dataområde och plats för sparkline grupp med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Microsoft Excel tillåter dig att kopiera en sparkline genom att ange dataområde och plats för en sparklinegrupp. Aspose.Cells stöder denna funktion.  
{{% /alert %}}  

För att kopiera en sparkline till andra celler i Microsoft Excel:  

1. Välj cellen som innehåller sparklinen.  
2. Välj **Redigera data** från **Sparkline**-avsnittet på fliken **Design**.  
3. Välj **Redigera gruppplats och data**.  
4. Ange dataområdet och platsen.  
1. Klicka på **OK**.  

Aspose.Cells tillhandahåller `SparklineCollection.add(dataRange, row, column)`-metoden för att ange dataintervall och plats för ett sparkline-grupp. Följande exempel kod laddar källfärgboken som visas i skärmbilden ovan, och tillgår sedan den första sparkline-gruppen och lägger till dataintervall och platsar i sparkline-gruppen. Slutligen skriver den ut resultatet som en Excel-fil på disken, vilket också visas i skärmbilden ovan.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "copy_sparkline.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first sparkline group
const group = worksheet.getSparklineGroups().get(0);

// Add Data Ranges and Locations inside this sparkline group
group.getSparklines().add("Sheet1!D5:O5", 4, 15);
group.getSparklines().add("Sheet1!D6:O6", 5, 15);
group.getSparklines().add("Sheet1!D7:O7", 6, 15);
group.getSparklines().add("Sheet1!D8:O8", 7, 15);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

