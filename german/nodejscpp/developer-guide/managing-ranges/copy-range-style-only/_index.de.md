---
title: Nur Bereichsstil mit Node.js über C++ kopieren
linktitle: Nur Bereichsstil kopieren
type: docs
weight: 620
url: /de/nodejs-cpp/copy-range-style-only/
description: Lernen Sie, wie man nur den Stil eines Bereichs kopiert, während man Daten mit Aspose.Cells for Node.js via C++ manipuliert. 
---

{{% alert color="primary" %}}

[Nur Bereichsdaten kopieren](/cells/de/nodejs-cpp/copy-range-data-only/) und [Bereichsdaten mit Stil kopieren](/cells/de/nodejs-cpp/copy-range-data-with-style/) erklären, wie man Daten von einem Bereich in einen anderen kopiert, entweder alleine oder vollständig mit Formatierung. Es ist auch möglich, nur die Formatierung zu kopieren. Dieser Artikel zeigt wie.

{{% /alert %}} 

Dieses Beispiel erstellt ein Arbeitsblatt, füllt es mit Daten und kopiert nur den Stil eines Bereichs.

1. Erstellen Sie einen Bereich.
1. Erstellen Sie ein `Style`-Objekt mit angegebenen Formatierungsattributen.
1. Wenden Sie die Formatierung des Stils auf den Bereich an.
1. Erstellen Sie einen zweiten Zellenbereich.
1. Kopieren Sie die Formatierung des ersten Bereichs in den zweiten Bereich.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook();

// Get the first Worksheet Cells.
const cells = workbook.getWorksheets().get(0).getCells();

// Fill some sample data into the cells.
for (let i = 0; i < 50; i++)
{
for (let j = 0; j < 10; j++) 
{
cells.get(i, j).putValue(i.toString() + "," + j.toString());
}
}

// Create a range (A1:D3).
const range = cells.createRange("A1", "D3");

// Create a style object.
const style = workbook.createStyle();
// Specify the font attribute.
style.getFont().setName("Calibri");
// Specify the shading color.
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
// Specify the border attributes.
const top = style.getBorders().get(AsposeCells.BorderType.TopBorder);
top.setLineStyle(AsposeCells.CellBorderType.Thin);
top.setColor(AsposeCells.Color.Blue);

const bottom = style.getBorders().get(AsposeCells.BorderType.BottomBorder);
bottom.setLineStyle(AsposeCells.CellBorderType.Thin);
bottom.setColor(AsposeCells.Color.Blue);

const left = style.getBorders().get(AsposeCells.BorderType.LeftBorder);
left.setLineStyle(AsposeCells.CellBorderType.Thin);
left.setColor(AsposeCells.Color.Blue);

const right = style.getBorders().get(AsposeCells.BorderType.RightBorder);
right.setLineStyle(AsposeCells.CellBorderType.Thin);
right.setColor(AsposeCells.Color.Blue);


// Create the styleflag object.
const flag1 = new AsposeCells.StyleFlag();
// Implement font attribute
flag1.setFontName(true);
// Implement the shading / fill color.
flag1.setCellShading(true);
// Implement border attributes.
flag1.setBorders(true);
// Set the Range style.
range.applyStyle(style, flag1);

// Create a second range (C10:E13).
const range2 = cells.createRange("C10", "E13");

// Copy the range style only.
range2.copyStyle(range);

const outputFilePath = path.join(dataDir, "copyrangestyle.out.xls");
// Save the excel file.
workbook.save(outputFilePath);
```
