---  
title: Automatiskt uppdatera OLE objekt via Microsoft Excel med Aspose.Cells for Node.js via C++  
linktitle: Automatisk uppdatering av OLE objekt via Microsoft Excel med Aspose.Cells  
type: docs  
weight: 270  
url: /sv/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/  
description: Lär dig hur du automatiskt uppdaterar OLE objekt i Excel med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells tillhandahåller [**OleObject.getAutoLoad()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getAutoLoad--)-egenskapen för att uppdatera OLE-objektet när Excel-filen öppnas i Microsoft Excel. På grund av denna egenskap kommer OLE-objektet att visa korrekt OLE-bild som genererats av Microsoft Excel.  
{{% /alert %}}  

Följande provkod laddar [provexempel Excel-filen](5115231.xlsx) som har en icke verklig OLE-bild. OLE-objektet är faktiskt ett Microsoft Word-dokument men provexempelfilen visar djurbilden istället för Microsoft Word-bilden. Men om du öppnar [utmatningsexelfilen](5115225.xlsx) kommer du att se att Microsoft Excel visar den korrekta OLE-bilden.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from your sample excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_oleobject.xlsx"));

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Set auto load property of first ole object to true
sheet.getOleObjects().get(0).setAutoLoad(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "RefreshOLEObjects_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
