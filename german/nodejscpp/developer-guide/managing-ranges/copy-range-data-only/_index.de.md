---  
title: Nur Bereichsdaten mit Node.js über C++ kopieren  
linktitle: Bereichsdaten nur kopieren  
type: docs  
weight: 600  
url: /de/nodejs-cpp/copy-range-data-only/  
description: Lernen Sie, wie man Daten aus einem Zellbereich mit Aspose.Cells for Node.js via C++ kopiert.  
---  

{{% alert color="primary" %}}  
Manchmal müssen Sie Daten von einem Zellenbereich in einen anderen kopieren und nur die Daten, nicht die Formatierung. Aspose.Cells bietet diese Funktion an.  

Dieser Artikel bietet einen Beispielcode, der Aspose.Cells verwendet, um einen Datenbereich zu kopieren.  
{{% /alert %}}  

Dieses Beispiel zeigt, wie Sie:  

1. Ein Arbeitsbuch erstellen.  
1. Daten zu Zellen im ersten Arbeitsblatt hinzufügen.  
1. [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) erstellen.  
1. Erstellen Sie ein [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt mit angegebenen Formatierungseigenschaften.  
1. Wenden Sie die Formatierung des Stils auf den Bereich an.  
1. Einen weiteren Zellenbereich erstellen.  
1. Kopieren Sie die Daten des ersten Bereichs in diesen zweiten Bereich.  

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
for (let i = 0; i < 50; i++) {
for (let j = 0; j < 10; j++) {
cells.get(i, j).putValue(`${i},${j}`);
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
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Blue);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Blue);

// Create the style flag object.
const flag1 = new AsposeCells.StyleFlag();
// Implement font attribute
flag1.setFontName(true);
// Implement the shading / fill color.
flag1.setCellShading(true);
// Implement border attributes.
flag1.setBorders(true);
// Set the Range style.
range.applyStyle(style, flag1);

// Create a second range (C10:F12).
const range2 = cells.createRange("C10", "F12");

// Copy the range data only.
range2.copyData(range);

const outputFilePath = path.join(dataDir, "CopyRangeData.out.xlsx");
// Save the excel file.
workbook.save(outputFilePath);
```  

