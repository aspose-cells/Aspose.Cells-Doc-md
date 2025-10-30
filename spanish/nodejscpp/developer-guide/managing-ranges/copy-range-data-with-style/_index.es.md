---  
title: Copiar rango de datos con estilo usando Node.js vía C++  
linktitle: Copiar Datos de Rango con Estilo  
type: docs  
weight: 610  
url: /es/nodejs-cpp/copy-range-data-with-style/  
description: Aprende cómo copiar un rango de celdas con formato usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

[Copiar solo datos del rango](/cells/es/nodejs-cpp/copy-range-data-only/) explicado cómo copiar los datos de un rango de celdas a otro. Específicamente, aplica un nuevo conjunto de estilos a las celdas copidas. Aspose.Cells también puede copiar un rango completo con formato. Este artículo explica cómo.  

{{% /alert %}}  

Aspose.Cells proporciona una variedad de clases y métodos para trabajar con rangos, por ejemplo, [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/) y [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#applyStyle-style-styleflag-).  

Este ejemplo:  

1. Crea un libro de trabajo.  
2. Llena varias celdas en la primera hoja con datos.  
3. Crea un [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/).  
4. Crea un objeto [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style/) con atributos de formato especificados.  
5. Aplica el estilo al rango de datos.  
6. Crea un segundo rango de celdas.  
7. Copia datos con el formato del primer rango al segundo rango.  

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
