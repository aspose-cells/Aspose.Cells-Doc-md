---  
title: Kopiera intervalldata med stil med Node.js via C++  
linktitle: Kopiera dataområde med stil  
type: docs  
weight: 610  
url: /sv/nodejs-cpp/copy-range-data-with-style/  
description: Lär dig hur man kopierar ett cellområde med formatering med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

[Kopiera endast intervalldata](/cells/sv/nodejs-cpp/copy-range-data-only/) förklarar hur man kopierar data från ett område till ett annat. Speciellt tillämpar det en ny uppsättning stilar på de kopierade cellerna. Aspose.Cells kan också kopiera ett område komplett med formatering. Denna artikel förklarar hur.  

{{% /alert %}}  

Aspose.Cells erbjuder en serie klasser och metoder för att arbeta med områden, till exempel [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/) och [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#applyStyle-style-styleflag-).  

Detta exempel:  

1. Skapar en arbetsbok.  
2. Fyller ett antal celler i det första kalkbladet med data.  
3. Skapar en [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/).  
4. Skapar ett [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style/)-objekt med angivna formateringsattribut.  
5. Tillämpar stilen på dataområdet.  
6. Skapar ett andra cellområde.  
7. Kopierar data med formatering från det första området till det andra området.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
