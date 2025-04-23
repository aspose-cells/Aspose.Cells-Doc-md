---  
title: Bereichsdaten mit Stil mit Node.js über C++ kopieren  
linktitle: Bereichsdaten mit Format kopieren  
type: docs  
weight: 610  
url: /de/nodejs-cpp/copy-range-data-with-style/  
description: Lernen Sie, wie man einen Zellbereich mit Formatierung mit Aspose.Cells for Node.js via C++ kopiert.  
---  

{{% alert color="primary" %}}  

[Nur Bereichsdaten kopieren](/cells/de/nodejs-cpp/copy-range-data-only/) erklärt, wie man die Daten eines Zellbereichs in einen anderen kopiert. Es wendet speziell einen neuen Satz von Stilen auf die kopierten Zellen an. Aspose.Cells kann auch einen Bereich vollständig mit Formatierung kopieren. Dieser Artikel erklärt wie.  

{{% /alert %}}  

Aspose.Cells bietet eine Reihe von Klassen und Methoden zur Arbeit mit Bereichen, z.B. [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/) und [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#applyStyle-style-styleflag-).  

Dieses Beispiel:  

1. Erstellt ein Arbeitsblatt.  
2. Füllt eine Anzahl von Zellen im ersten Arbeitsblatt mit Daten.  
3. Erstellt ein [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/).  
4. Erstellt ein [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style/)-Objekt mit angegebenen Formatierungsattributen.  
5. Wendet den Stil auf den Datenbereich an.  
6. Erstellt einen zweiten Zellbereich.  
7. Kopiert Daten mit Formatierung vom ersten Bereich zum zweiten.  

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
cells.get(i, j).putValue(`${i},${j}`);
}
}

// Create a range (A1:D3).
const range = cells.createRange("A1", "D3");

// Create a style object.
let style = workbook.createStyle();
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

// Create a second range (C10:F12).
const range2 = cells.createRange("C10", "F12");

// Copy the range data with formatting.
range2.copy(range);

const outputFilePath = path.join(dataDir, "CopyRange.out.xlsx");
// Save the excel file.
workbook.save(outputFilePath);
```  

