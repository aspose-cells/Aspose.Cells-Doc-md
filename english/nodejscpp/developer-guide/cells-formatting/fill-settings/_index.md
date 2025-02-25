---  
title: Fill Settings with Node.js via C++  
linktitle: Fill Settings  
description: Learn how to customize the fill settings, background, and style of cells using the Aspose.Cells library for Node.js via C++.  
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style, Node.js via C++  
type: docs  
weight: 50  
url: /nodejs-cpp/cells-fill-settings/  
---  

## **Colors and Background Patterns**  

Microsoft Excel can set the foreground (outline) and background (fill) colors of cells and background patterns.  

Aspose.Cells also supports these features in a flexible manner. In this topic, we learn to use these features using Aspose.Cells.  

### **Setting Colors and Background Patterns**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class.  

The [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) has the [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle) and [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle) methods that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) class provides properties for setting the foreground and background colors of the cells. Aspose.Cells provides a [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) enumeration that contains a set of pre-defined types of background patterns which are given below.  

|**Background Patterns**|**Description**|  
| :- | :- |  
|DiagonalCrosshatch|Represents diagonal crosshatch pattern|  
|DiagonalStripe|Represents diagonal stripe pattern|  
|Gray6|Represents 6.25% gray pattern|  
|Gray12|Represents 12.5% gray pattern|  
|Gray25|Represents 25% gray pattern|  
|Gray50|Represents 50% gray pattern|  
|Gray75|Represents 75% gray pattern|  
|HorizontalStripe|Represents horizontal stripe pattern|  
|None|Represents no background|  
|ReverseDiagonalStripe|Represents reverse diagonal stripe pattern|  
|Solid|Represents solid pattern|  
|ThickDiagonalCrosshatch|Represents thick diagonal crosshatch pattern|  
|ThinDiagonalCrosshatch|Represents thin diagonal crosshatch pattern|  
|ThinDiagonalStripe|Represents thin diagonal stripe pattern|  
|ThinHorizontalCrosshatch|Represents thin horizontal crosshatch pattern|  
|ThinHorizontalStripe|Represents thin horizontal stripe pattern|  
|ThinReverseDiagonalStripe|Represents thin reverse diagonal stripe pattern|  
|ThinVerticalStripe|Represents thin vertical stripe pattern|  
|VerticalStripe|Represents vertical stripe pattern|  

In the example below, the foreground color of the A1 cell is set but A2 is configured to have both foreground and background colors with a vertical stripe background pattern.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)){
    fs.mkdirSync(dataDir);
}

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook();

// Adding a new worksheet to the Workbook object
const i = workbook.getWorksheets().add();

// Obtaining the reference of the newly added worksheet by passing its sheet index
const worksheet = workbook.getWorksheets().get(i);

// Define a Style and get the A1 cell style
let style = worksheet.getCells().get("A1").getStyle();

// Setting the foreground color to yellow
style.setForegroundColor(AsposeCells.Color.Yellow);

// Setting the background pattern to vertical stripe
style.setPattern(AsposeCells.BackgroundType.VerticalStripe);

// Apply the style to A1 cell
worksheet.getCells().get("A1").setStyle(style);

// Get the A2 cell style
style = worksheet.getCells().get("A2").getStyle();

// Setting the foreground color to blue
style.setForegroundColor(AsposeCells.Color.Blue);

// Setting the background color to yellow
style.setBackgroundColor(AsposeCells.Color.Yellow);

// Setting the background pattern to vertical stripe
style.setPattern(AsposeCells.BackgroundType.VerticalStripe);

// Apply the style to A2 cell
worksheet.getCells().get("A2").setStyle(style);

// Saving the Excel file
workbook.save(path.join(dataDir, "book1.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```  

### **Important to Know**  

{{% alert color="primary" %}}  

- To set a cell's foreground or background color, use the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**ForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#foregroundColor) or [**BackgroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#backgroundColor) properties. Both properties will take effect only if the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#pattern) property is configured.  
- The [**ForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#foregroundColor) property sets the cell's shade color.  
  The [**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#pattern) property specifies the type of background pattern used for the foreground or background color. Aspose.Cells provides an enumeration, [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype). that contains a set of pre-defined types of background patterns.  
- If you select *BackgroundType.None* value from the [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) enumeration, the foreground color is not applied.  
  Likewise, the background color is not applied if you select the *BackgroundType.None* or *BackgroundType.Solid* values.  
- When retrieving cell's shading/fill color, if [**Style.Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#pattern) is *BackgroundType.None*, [**Style.ForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#foregroundColor) will return *Color.Empty*.  

{{% /alert %}}  

### **Applying Gradient Fill Effects**  

To apply your desired Gradient Fill Effects to the cell, use the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**setTwoColorGradient**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTwoColorGradient) method accordingly.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook();

// Get the first worksheet (default) in the workbook
const worksheet = workbook.getWorksheets().get(0);

// Input a value into B3 cell
worksheet.getCells().get(2, 1).putValue("test");

// Get the Style of the cell
const style = worksheet.getCells().get("B3").getStyle();

// Set Gradient pattern on
style.setIsGradient(true);
// Specify two color gradient fill effects
style.setTwoColorGradient(new AsposeCells.Color(255, 255, 255), new AsposeCells.Color(79, 129, 189), AsposeCells.GradientStyleType.Horizontal, 1);
// Set the color of the text in the cell
style.getFont().setColor(AsposeCells.Color.Red);
// Specify horizontal and vertical alignment settings
style.setHorizontalAlignment(AsposeCells.TextAlignmentType.Center);
style.setVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Apply the style to the cell
worksheet.getCells().get("B3").setStyle(style);

// Set the third row height in pixels
worksheet.getCells().setRowHeightPixel(2, 53);

// Merge the range of cells (B3:C3)
worksheet.getCells().merge(2, 1, 1, 2);

// Save the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```  

## **Colors and Palette**  

A palette is the number of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97-2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills and lines in a chart.  

With Aspose.Cells it is possible not only to use the palette's existing colors but also custom colors. Before using a custom color, add it to the palette first.  

This topic discusses how to add custom colors to the palette.  

### **Adding Custom Colors to Palette**  

Aspose.Cells supports Microsoft Excel's 56 color palette. To use a custom color that is not defined in the palette, add the color to the palette.  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class provides a [**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette) method that takes the following parameters to add a custom color to modify the palette:  

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
  