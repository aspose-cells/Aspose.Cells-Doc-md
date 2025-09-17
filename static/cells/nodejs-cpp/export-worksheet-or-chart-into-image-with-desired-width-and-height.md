##Export Worksheet or Chart into Image with Desired Width and Height via Node.js
Learn how to export a worksheet or chart to an image with specified width and height using Aspose.Cells for Node.js via C++.
You can use Aspose.Cells for Node.js via C++ to export your worksheet or chart into an image with the desired width and height. It provides [**ImageOrPrintOptions.setDesiredSize(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#setDesiredSize-number-number-boolean-) method to set the desired width and height of the exported image. The width and height are specified in the unit of pixels.
The following code exports the worksheet into an image with 400x400 size.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");
// Create workbook object from source file
const filePath = path.join(sourceDir, "sampleWorksheetToImageDesiredSize.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Set image or print options we want one page per sheet. The image format is in png and desired dimensions are 400x400
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);
opts.setDesiredSize(400, 400, false);
// Render sheet into image
const sr = new AsposeCells.SheetRender(worksheet, opts);
sr.toImage(0, path.join(outputDir, "outputWorksheetToImageDesiredSize.png"));
```
