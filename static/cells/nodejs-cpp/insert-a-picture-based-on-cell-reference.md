##Insert a Picture Based on Cell Reference with Node.js via C++
Learn how to insert a picture in a worksheet based on a cell reference using Aspose.Cells for Node.js via C++. Show cell data in a picture.
Sometimes you have an empty picture and need to show data or contents in the picture by setting a cell reference in the Formula Bar. Aspose.Cells supports this feature (Microsoft Excel 2010).
## Inserting a Picture Based on Cell Reference
Aspose.Cells for Node.js via C++ supports displaying the contents of a worksheet cell in an image shape. You can link the picture to the cell that contains the data that you want to display. Since the cell or cell range is linked to the graphic object, changes that you make to the data in that cell or cell range automatically appear in the graphic object. Add a picture to the worksheet by calling the [**ShapeCollection.addPicture(number, number, number, number, Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection/#addPicture-number-number-number-number-uint8array-) method of the [**ShapeCollection**](https://reference.aspose.com/cells/nodejs-cpp/shapecollection) collection (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) object). Specify the cell range by using the [**Picture.getFormula()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getFormula--) attribute of the [**Picture**](https://reference.aspose.com/cells/nodejs-cpp/picture) object.
### Code Example
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet's cells collection
const cells = workbook.getWorksheets().get(0).getCells();
// Add string values to the cells
cells.get("A1").putValue("A1");
cells.get("C10").putValue("C10");
// Get the conditional icon's image data
const imagedata = AsposeCells.ConditionalFormattingIcon.getIconImageData(AsposeCells.IconSetType.TrafficLights31, 0);
// Create a stream based on the image data
const stream = Uint8Array.from(imagedata);
// Add a blank picture to the D1 cell
const pic = workbook.getWorksheets().get(0).getShapes().addPicture(0, 3, stream, 10, 10);
// Specify the formula that refers to the source range of cells
pic.setFormula("A1:C10");
// Update the shapes selected value in the worksheet
workbook.getWorksheets().get(0).getShapes().updateSelectedValue();
// Save the Excel file.
workbook.save(path.join(dataDir, "referencedpicture.out.xlsx"));
```
