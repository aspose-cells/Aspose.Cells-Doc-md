---
title: Standard Schriftart beim Rendern von Tabellenblättern zu Bildern mit Node.js über C++ festlegen
linktitle: Standardfont beim Rendern von Tabellenkalkulationen in Bilder festlegen
type: docs
weight: 360
url: /de/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: Lernen Sie, wie man beim Rendern von Tabellenblättern zu Bildern mit Aspose.Cells for Node.js via C++ die Standard Schriftart festlegt. 
---

{{% alert color="primary" %}}

Bitte verwenden Sie die Eigenschaft [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--), um die Standard-Schriftart beim Rendern von Tabellenkalkulationen als Bilder festzulegen. Diese Eigenschaft ist nur wirksam, wenn die Standard-Schriftart der Arbeitsmappe Ihre Zeichen nicht rendern kann. Die mit der Eigenschaft [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) festgelegte Standard-Schriftart wird für alle Zellen verwendet, die ungültige oder nicht vorhandene Schriftarten haben.

{{% /alert %}}

## Standard-Schriftart beim Rendern von Tabellenkalkulationen als Bilder festlegen

Der folgende Beispielcode erstellt eine Arbeitsmappe, fügt Text in Zelle A4 des ersten Arbeitsblatts ein und setzt die Schriftart auf eine ungültige oder nicht vorhandene Schriftart. Dann werden zwei Bilder des Arbeitsblatts aufgenommen. Das erste Bild wird durch Setzen der [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)-Eigenschaft auf *Courier New* aufgenommen, das zweite durch Setzen der [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)-Eigenschaft auf *Times New Roman*.

Dies ist das Ausgabebild nach Setzen der [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)-Eigenschaft auf *Courier New*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Dies ist das Ausgabebild nach Setzen der [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)-Eigenschaft auf *Times New Roman*.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## Beispielcode

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
