##Rotate Text with Shape inside the Worksheet using Node.js via C++
Learn how to rotate text with shape inside an Excel worksheet using Aspose.Cells for Node.js via C++.
## **Possible Usage Scenarios**
You can add text inside any shape using Microsoft Excel. If you add a shape using the very old Microsoft Excel 2003, then the text will not rotate with the shape. But if you add a shape using newer versions of Microsoft Excel e.g. 2007, 2010, 2013 or 2016, etc. then the text will rotate with the shape. You can control if the text should rotate with the shape or not using the [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) property. The default value of it is **true** which means text will rotate with the shape but if you set it as **false**, then the text will not rotate with the shape.
## **Rotate Text with Shape inside the Worksheet**
The following sample code loads the [sample Excel file](64716896.xlsx) that has a triangle shape and its text rotates with the shape. If you open the sample Excel file in Microsoft Excel and rotate the triangle shape, the text will also rotate with it. The code then sets the [**ShapeTextAlignment.getRotateTextWithShape()**](https://reference.aspose.com/cells/nodejs-cpp/shapetextalignment/#getRotateTextWithShape--) property as **false** and saves it as [output Excel file](64716897.xlsx). If you now open the output Excel file in Microsoft Excel and rotate the triangle shape, the text will not rotate with it. Please see the following screenshot showing the effect of the code on the sample Excel file for reference.
![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)
## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleRotateTextWithShapeInsideWorksheet.xlsx");
// Load sample Excel file.
const workbook = new AsposeCells.Workbook(sourceFilePath);
// Access first worksheet.
const worksheet = workbook.getWorksheets().get(0);
// Access cell B4 and add message inside it.
const cellB4 = worksheet.getCells().get("B4");
cellB4.putValue("Text is not rotating with shape because RotateTextWithShape is false.");
// Access first shape.
const shape = worksheet.getShapes().get(0);
// Access shape text alignment.
const shapeTextAlignment = shape.getTextBody().getTextAlignment();
// Do not rotate text with shape by setting RotateTextWithShape as false.
shapeTextAlignment.setRotateTextWithShape(false);
// Save the output Excel file.
const outputFilePath = path.join(dataDir, "outputRotateTextWithShapeInsideWorksheet.xlsx");
workbook.save(outputFilePath);
```
