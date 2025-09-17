##Determine if Shape is Smart Art Shape with Node.js via C++
Learn how to determine if a shape in Excel is a Smart Art shape using Aspose.Cells for Node.js via C++.
## **Possible Usage Scenarios**
Smart Art Shapes are special shapes in Microsoft Excel that allow you to create complex diagrams automatically. You can find if the shape is a smart art shape or normal shape using [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--) property.
## **Determine if Shape is Smart Art Shape**
The following sample code loads the [sample Excel file](55541792.xlsx) containing a smart art shape as shown in this screenshot. It then prints the value of [**Shape.isSmartArt()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#isSmartArt--) property of the first shape. Please see the console output of the sample code given below.
![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)
## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSmartArtShape.xlsx");
// Load the sample smart art shape - Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Access first shape
const shape = worksheet.getShapes().get(0);
// Determine if shape is smart art
console.log("Is Smart Art Shape: " + shape.isSmartArt());
```
## **Console Output**
Is Smart Art Shape: True
