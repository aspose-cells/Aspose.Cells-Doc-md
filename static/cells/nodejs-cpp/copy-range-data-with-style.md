##Copy Range Data with Style using Node.js via C++
Learn how to copy a range of cells with formatting using Aspose.Cells for Node.js via C++.
[Copy Range Data Only](https://docs.aspose.com/cells/nodejs-cpp/copy-range-data-only/) explained how to copy the data from a range of cells to another range. Specifically, it applies a new set of styles to the copied cells. Aspose.Cells can also copy a range complete with formatting. This article explains how.
Aspose.Cells provides a range of classes and methods for working with ranges, for example, [**createRange(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-), [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag/) and [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#applyStyle-style-styleflag-).
This example:
1. Creates a workbook.
2. Fills a number of cells in the first worksheet with data.
3. Creates a [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range/).
4. Creates a [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style/) object with specified formatting attributes.
5. Applies the style to the data range.
6. Creates a second range of cells.
7. Copies data with the formatting from the first range to the second range.
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
