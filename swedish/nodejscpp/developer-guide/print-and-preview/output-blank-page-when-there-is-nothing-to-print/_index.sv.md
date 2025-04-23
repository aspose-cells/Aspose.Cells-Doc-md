---
title: Utskrift av tom sida när det inte finns något att skriva ut med Node.js via C++
linktitle: Utdata tom sida när det inte finns något att skriva ut
type: docs
weight: 90
url: /sv/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **Möjliga användningsscenario**

Om bladet är tomt, kommer Aspose.Cells inte att skriva ut något när du exporterar arbetsbladet till en bild. Du kan ändra detta beteende genom att använda [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--) egenskapen. När du ställer in den till **true**, kommer det att skriva ut en tom sida.

## **Utdata tom sida när det inte finns något att skriva ut**

Följande exempel skapar ett tomt arbetsbok som har ett tomt arbetsblad och renderar det tomma arbetsbladet till en bild efter att ha ställt in [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--)-egenskapen till **true**. Därigenom genereras en tom sida eftersom det inte finns något att skriva ut, vilket du kan se i bilden nedan.

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **Exempelkod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet - it is empty sheet
const ws = wb.getWorksheets().get(0);

// Specify image or print options
// Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
// So that empty page gets printed
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);
opts.setOutputBlankPageWhenNothingToPrint(true);

// Render empty sheet to png image
const sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, path.join(outputDir, "OutputBlankPageWhenNothingToPrint.png"));
```
