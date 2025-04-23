---
title: Rendera kalkylblad till grafisk kontext med Node.js via C++
linktitle: Rendera arbetsblad till grafiskt sammanhang
type: docs
weight: 300
url: /sv/nodejs-cpp/render-worksheet-to-graphic-context/
description: Lär dig hur man renderar ett kalkylblad till en grafisk kontext med Aspose.Cells for Node.js via C++. Detta inkluderar rendering till bildfiler, skärmar och skrivare.
---

{{% alert color="primary" %}}

Aspose.Cells kan nu rendera kalkylblad till grafisk kontext. Grafisk kontext kan vara vad som helst, som en bildfil, skärm eller skrivare osv. Använd någon av följande två metoder för att rendera ett kalkylblad till grafisk kontext.

- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)
- [**SheetRender.toImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)

{{% /alert %}}

Följande kod visar hur man använder Aspose.Cells för att rendera ett kalkylblad till grafisk kontext. När du kör koden kommer den att skriva ut hela kalkylbladet och fylla återstående tomt utrymme med blå färg i den grafiska kontexten och spara bilden som **OutputImage_out_.png**. Du kan använda vilken Excel-fil som helst för att prova detta. Läs också gärna kommentarerna i koden för bättre förståelse.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleBook.xlsx");
// Create workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Create empty image buffer
const bmpOptions = new AsposeCells.ImageOrPrintOptions();
bmpOptions.setOnePagePerSheet(true);

// Render worksheet to image
const sheetRender = new AsposeCells.SheetRender(worksheet, bmpOptions);
sheetRender.toImage(0, dataDir + "/OutputImage_out.png");

// Save the image in Png format
```
