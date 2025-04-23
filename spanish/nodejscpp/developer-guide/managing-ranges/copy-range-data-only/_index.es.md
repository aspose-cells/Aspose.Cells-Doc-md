---  
title: Copiar solo datos del rango con Node.js vía C++  
linktitle: Copiar Solo Datos de Rango  
type: docs  
weight: 600  
url: /es/nodejs-cpp/copy-range-data-only/  
description: Aprende cómo copiar datos de un rango de celdas a otro usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
A veces, necesitas copiar datos de un rango de celdas a otro, copiando solo los datos, no el formato. Aspose.Cells ofrece esta función.  

Este artículo proporciona un código de ejemplo que utiliza Aspose.Cells para copiar un rango de datos.  
{{% /alert %}}  

Este ejemplo muestra cómo:  

1. Crear un libro de trabajo.  
1. Agregar datos a las celdas en la primera hoja de cálculo.  
1. Crear un [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range).  
1. Crea un objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) con atributos de formato especificados.  
1. Aplica el formato de estilo al rango.  
1. Crear otro rango de celdas.  
1. Copiar datos del primer rango a este segundo rango.  

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

