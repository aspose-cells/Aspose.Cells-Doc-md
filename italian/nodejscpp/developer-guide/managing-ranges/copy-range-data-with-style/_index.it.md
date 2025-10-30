---  
title: Copia i dati dell intervallo con stile usando Node.js via C++  
linktitle: Copia intervallo dati con stile.  
type: docs  
weight: 610  
url: /it/nodejs-cpp/copy-range-data-with-style/  
description: Impara come copiare un intervallo di celle con formattazione usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

[Copia solo i dati dell'intervallo](/cells/it/nodejs-cpp/copy-range-data-only/) spiegato come copiare i dati da un intervallo a un altro. In particolare, applica un nuovo set di stili alle celle copiate. Aspose.Cells può anche copiare un intervallo completo di formattazione. Questo articolo spiega come.  

{{% /alert %}}  

Aspose.Cells fornisce una serie di classi e metodi per lavorare con gli intervalli, ad esempio, [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/) e [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#applyStyle-style-styleflag-).  

Questo esempio:  

1. Crea un workbook.  
2. Riempe un numero di celle nel primo foglio di lavoro con dati.  
3. Crea un [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/).  
4. Crea un oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style/) con attributi di formattazione specificati.  
5. Applica lo stile all'intervallo di dati.  
6. Crea un secondo intervallo di celle.  
7. Copia i dati con la formattazione dal primo intervallo al secondo.  

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
