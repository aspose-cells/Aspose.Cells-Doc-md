---  
title: Ställ in flikfärg med Node.js via C++  
linktitle: Ställ in färg på arbetsbladets flik  
type: docs  
weight: 120  
url: /sv/nodejs-cpp/set-worksheet-tab-color/  
description: Denna artikel visar kodexempel som ställer in Excel arksbladets flikfärg programmatiskt med Node.js via C++.  
keywords: ställ in excel flikfärg Node.js via C++, kod för att ställa in excel flikfärg Node.js via C++  
---  

{{% alert color="primary" %}}  

Aspose.Cells låter dig ändra färgen på individuella arbetsbladsflikar för att göra dem framträdande från resten. Till exempel kan du göra Utgifter röda, Försäljning gröna, Tillgångar blå, osv.

{{% /alert %}}  
## **Ställa in färg på arbetsbladets flik i Microsoft Excel**  
1. Högerklicka på en flik i flikarket längst ned på det aktuella arbetsbladet.  
1. Välj **Flikfärg**.  
1. Välj en färg från paletten.  
1. Klicka på **OK**.  
## **Ställa in färg på arbetsbladets flik med Aspose.Cells**  
Exempelkoden nedan visar hur man ställer in flikfärg med Aspose.Cells.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));

// Get the first worksheet in the book
const worksheet = workbook.getWorksheets().get(0);

// Set the tab color
worksheet.setTabColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "worksheettabcolor.out.xls"));
```  

