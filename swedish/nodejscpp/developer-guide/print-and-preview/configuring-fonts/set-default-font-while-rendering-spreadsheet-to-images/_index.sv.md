---
title: Sätt standardfont när du renderar kalkylblad till bilder med Node.js via C++
linktitle: Ange standardfont medan du renderar kalkylblad till bilder
type: docs
weight: 360
url: /sv/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Lär dig att ange standardfonten när du renderar kalkylblad till bilder med Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Använd egenskapen [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) för att ange standardfont medan du renderar kalkylblad till bilder. Denna egenskap kommer bara att vara effektiv när arbetsbokens standardfont inte kan rendera dina tecken. Den standardfont som anges med egenskapen [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) används för alla de celler som har ogiltiga eller obefintliga teckensnitt.

{{% /alert %}}

## Ange standardfont medan du renderar kalkylblad till bilder

 Följande exempel skapar en arbetsbok, lägger till lite text i cell A4 i det första kalkylbladet och ställer in dess font till en ogiltig eller icke-existerande font. Sedan tar den två bilder av kalkylbladet. Den första bilden tas genom att ställa in [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)-egenskapen till *Courier New* och den andra genom att ställa in [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)-egenskapen till *Times New Roman*.

Detta är utdatabilden efter att ha ställt in [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)-egenskapen till *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Detta är utdatabilden efter att ha ställt in [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)-egenskapen till *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Exempelkod

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Set default font of the workbook to none
let s = wb.getDefaultStyle();
s.getFont().setName("");
wb.setDefaultStyle(s);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A4 and add some text inside it.
const cell = ws.getCells().get("A4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell A4 which is unknown.
let st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
st.setIsTextWrapped(true);
cell.setStyle(st);

// Set first column width and fourth column height
ws.getCells().setColumnWidth(0, 80);
ws.getCells().setRowHeight(3, 60);

// Create image or print options.
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);

// Render worksheet image with Courier New as default font.
opts.setDefaultFont("Courier New");
let sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "out_courier_new_out.png");

// Render worksheet image again with Times New Roman as default font.
opts.setDefaultFont("Times New Roman");
sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "times_new_roman_out.png");
```
