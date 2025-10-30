---  
title: Flytta cellområde i ett kalkylblad med Node.js via C++  
linktitle: Flytta cellintervall i en arbetsbok  
type: docs  
weight: 370  
url: /sv/nodejs-cpp/move-range-of-cells-in-a-worksheet/  
description: Lär dig hur man flyttar ett cellområde i ett kalkylblad med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Den här artikeln visar hur man flyttar ett cellintervall i en arbetsbok.  
{{% /alert %}}  

## **Flytta cellområde i ett kalkylblad**  
Exempelkoden använder en mallfil för att demonstrera uppgiften.  

**Ingångsfilen**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)  

Se den genererade filen med intervallet A1:B5 flyttat till C1:D5 nedan.  

**Utgångsfilen**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Instantiate the workbook object. Open the Excel file
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells();

const range = cells.createRange("A1", "B5");
//move the range to right.
range.moveTo(0, 2);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
