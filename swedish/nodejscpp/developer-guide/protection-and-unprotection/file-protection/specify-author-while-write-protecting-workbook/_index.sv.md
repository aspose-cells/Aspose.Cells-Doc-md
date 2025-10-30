---  
title: Ange författare vid skrivskydd av arbetsbok med Node.js via C++  
linktitle: Ange författare vid skrivskydd av arbetsbok  
type: docs  
weight: 40  
url: /sv/nodejs-cpp/specify-author-while-write-protecting-workbook/  
description: Ange ett författarnamn vid skrivskydd av arbetsbok med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**

Du kan ange ett författarnamn vid skrivskydd av din arbetsbok med Aspose.Cells API. Använd [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--)-egenskapen för detta ändamål.

## **Ange författare vid skrivskydd av arbetsbok**

Följande exempel förklarar användningen av [**Workbook.getAuthor()**](https://reference.aspose.com/cells/nodejs-cpp/writeprotection/#getAuthor--)-egenskapen. Koden skapar en tom arbetsbok, skrivskyddar den med ett lösenord, anger författarnamnet och sparar den som [utdata Excel-fil](67338582.xlsx). Följande skärmbild illustrerar effekten av kodexemplet på utdata Excel-filen för ditt referens.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Create empty workbook.
const workbook = new AsposeCells.Workbook();

// Write protect workbook with password.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Specify author while write protecting workbook.
workbook.getSettings().getWriteProtection().setAuthor("SimonAspose");

// Save the workbook in XLSX format.
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
