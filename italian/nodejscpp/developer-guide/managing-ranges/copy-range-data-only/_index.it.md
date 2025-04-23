---  
title: Copia solo i dati dell intervallo con Node.js via C++  
linktitle: Copia solo i dati dell intervallo.  
type: docs  
weight: 600  
url: /it/nodejs-cpp/copy-range-data-only/  
description: Impara come copiare i dati da un intervallo di celle a un altro utilizzando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
A volte è necessario copiare i dati da un intervallo di celle a un altro, copiando solo i dati, non la formattazione. Aspose.Cells offre questa funzionalità.  

Questo articolo fornisce un codice di esempio che utilizza Aspose.Cells per copiare un intervallo di dati.  
{{% /alert %}}  

Questo esempio mostra come:  

1. Crea un libro di lavoro.  
1. Aggiungi dati alle celle nel primo foglio di lavoro.  
1. Crea un [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
1. Crea un oggetto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) con attributi di formattazione specificati.  
1. Applica la formattazione di stile all'intervallo.  
1. Crea un altro intervallo di celle.  
1. Copiare i dati del primo intervallo in questo secondo intervallo.  

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

