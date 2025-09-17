##Convert Excel to High-Resolution Image with Node.js via C++
Learn how to convert Excel files to high-resolution images using Aspose.Cells for Node.js via C++.
With the increasing prevalence of high-resolution screens, images generated at the default 96 DPI often appear blurry and unclear. To ensure clarity on high-resolution screens, it's essential to generate images at a higher DPI. Aspose.Cells for Node.js via C++ offers the functionality to set [**ImageOrPrintOptions.getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--) and [**ImageOrPrintOptions.getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--), allowing you to create high-quality images from Excel files that look sharp on high-resolution displays.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
// Load the Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Create an instance of ImageOrPrintOptions
const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(300);
options.setVerticalResolution(300);
options.setImageType(AsposeCells.ImageType.Png);
// Get the worksheet
const sheet = workbook.getWorksheets().get(0);
// Create a SheetRender instance
const render = new AsposeCells.SheetRender(sheet, options);
// Generate and save the image
render.toImage(0, "output.png");
```
