---
title: Beräkna sidinställningens skalningsfaktor med Node.js via C++
linktitle: Beräkna siduppsättningsskalningsfaktorn
type: docs
weight: 300
url: /sv/nodejs-cpp/calculate-page-setup-scaling-factor/
description: Denna artikel ger exempel på kod som förklarar hur man använder Node.js API med C++ för att beräkna sidinställningens skalningsfaktor med Passa till n sida(n) bred och m skål alternativet för Excel arbetsblad programatiskt.
keywords: Passa till n sida(n) bred och m hög excel Node.js via C++, beräkna sidinställningens skalningsfaktor med Node.js via C++
---

{{% alert color="primary" %}}

 När du ställer in sidinställningens skalningsfaktor med **Passa till n sida(n) bred och m hög**-alternativet, beräknar Microsoft Excel sidinställningens skalningsfaktor. Du kan beräkna samma sak med [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--)-egenskapen. Den här egenskapen returnerar ett dubbelt värde som kan omvandlas till procentandel. Om den till exempel returnerar 0,5 betyder det att skalningsfaktorn är 50 %.

{{% /alert %}}

Följande exempelkod illustrerar hur man beräknar sidlayoutskalningsfaktorn med hjälp av [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--)-egenskapen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");

// Set paper size
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);

// Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);

// Calculate page scale via sheet render
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());

// Convert page scale double value to percentage
const strPageScale = (sr.getPageScale() * 100).toFixed(0) + "%";

// Write the page scale value
console.log(strPageScale);
```
