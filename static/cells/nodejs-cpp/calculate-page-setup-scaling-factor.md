##Calculate Page Setup Scaling Factor with Node.js via C++
This article provides sample code explaining how to use the Node.js API with C++ to calculate Page Setup scaling factor using Fit to n page(s) wide by m tall option of Excel worksheet programmatically.
When you set Page Setup Scaling using **Fit to n page(s) wide by m tall** option, Microsoft Excel calculates the Page Setup Scaling Factor. You can calculate the same thing using [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--) property. This property returns a double value that can be converted to percentage value. For example, if it returns 0.5 then it means scaling factor is 50%.
The following sample code illustrates how to calculate page setup scaling factor using [**SheetRender.getPageScale()**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#getPageScale--) property.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Put some data in these cells
worksheet.getCells().get("A4").putValue("Test");
worksheet.getCells().get("S4").putValue("Test");
// Set paper size
worksheet.getPageSetup().setPaperSize(AsposeCells.PaperSizeType.PaperA4);
// Set fit to pages wide as 1
worksheet.getPageSetup().setFitToPagesWide(1);
// Calculate page scale via sheet render
const sr = new AsposeCells.SheetRender(worksheet, new AsposeCells.ImageOrPrintOptions());
// Convert page scale double value to percentage
const strPageScale = (sr.getPageScale() * 100).toFixed(0) + "%";
// Write the page scale value
console.log(strPageScale);
```
