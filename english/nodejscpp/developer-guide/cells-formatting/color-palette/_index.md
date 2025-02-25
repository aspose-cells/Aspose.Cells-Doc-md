---  
title: How to Use Color Palette with Node.js via C++  
linktitle: How to Use Color Palette  
type: docs  
weight: 80  
url: /nodejs-cpp/excel-color-palette/  
description: Node.js code to add custom colors to the palette and use Excel color palette with Aspose.Cells for Node.js via C++.  
keywords: node.js add custom colors to the palette, node.js programmatically excel color palette, programmatically how to use color palette in workbook, node.js how to use color palette in excel  
---  
  
## **Colors and Palette**  
  
A palette is the number of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97-2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills and lines in a chart.  
  
With Aspose.Cells for Node.js via C++, it is possible not only to use the palette's existing colors but also custom colors. Before using a custom color, add it to the palette first.  
  
This topic discusses how to add custom colors to the palette.  
  
## **Add Custom Colors to Palette**  
  
Aspose.Cells supports Microsoft Excel's 56 color palette. To use a custom color that is not defined in the palette, add the color to the palette.  
  
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook/) class provides a [**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-customColor-number-) method that takes the following parameters to add a custom color to modify the palette:  
  
- Custom Color, the custom color to be added.  
- Index, the index of the color in the palette that the custom color will replace. Should be between 0-55.  
  
The example below adds a custom color (Orchid) to the palette before applying it on a font.  
  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Checks if a color is in the palette for the spreadsheet.
console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

// Adding Orchid color to the palette at 55th index
workbook.changePalette(AsposeCells.Color.Orchid, 55);

console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

// Adding a new worksheet to the Excel object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Accessing the "A1" cell from the worksheet
const cell = worksheet.getCells().get("A1");

// Adding some value to the "A1" cell
cell.putValue("Hello Aspose!");

// Defining new Style object
const styleObject = workbook.createStyle();
// Setting the Orchid (custom) color to the font
styleObject.getFont().setColor(workbook.getColors()[55]);

// Applying the style to the cell
cell.setStyle(styleObject);

// Saving the Excel file
workbook.save("out.xlsx");
```  
  
{{% alert color="primary" %}}  
  
The palette only holds 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is changed. So, when you change the palette, please be very careful. Moreover, this is the limitation in XLS (Excel 97 - 2003) file format only as there is no such limitation for XLSX or other advanced MS Excel (2007/2010 or 2013) file formats.  
  
{{% /alert %}}  
  