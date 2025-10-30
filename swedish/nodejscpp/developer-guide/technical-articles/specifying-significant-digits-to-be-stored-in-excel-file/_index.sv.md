---  
title: Specifikation av viktiga siffror som ska lagras i Excel fil med Node.js via C++  
linktitle: Ange signifikanta siffror som ska lagras i Excel fil  
type: docs  
weight: 30  
url: /sv/nodejs-cpp/specifying-significant-digits-to-be-stored-in-excel-file/  
description: Lär dig hur du specificerar viktiga siffror som ska lagras i en Excel fil med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Som standard lagrar Aspose.Cells for Node.js via C++ 17 signifikanta siffror av dubbelvärden i Excel-filen, till skillnad från MS-Excel som bara lagrar 15 signifikanta siffror. Du kan ändra standardbeteendet för Aspose.Cells från 17 till 15 signifikanta siffror med egenskapen [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--).  

## **Ange signifikanta siffror som ska lagras i Excel-fil**  

Följande exempel kod tvingar Aspose.Cells att använda 15 signifikanta siffror när du lagrar dubbla värden i Excel-filen. Kontrollera [utdata Excel-fil](22774105.xlsx). Byt ut dess extension till .zip och packa upp den, du kommer att se att endast 15 signifikanta siffror lagras i Excel-filin. Följande skärmbild förklarar effekten av [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--)-egenskapen på utdata Excel-filen.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Exempelkod**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
AsposeCells.CellsHelper.setSignificantDigits(15);

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const c = worksheet.getCells().get("A1");

// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.putValue(1234567890.123451711);

// Save the workbook
workbook.save(path.join(dataDir, "out_SignificantDigits.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
