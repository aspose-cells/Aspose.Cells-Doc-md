##Convert Worksheet to Image - Remove whitespace around data with Node.js via C++
Learn how to convert Microsoft Excel worksheets to images and remove whitespace around data using Aspose.Cells for Node.js via C++.
Sometimes, you need to present worksheet images in applications or web pages. For example, you might need to insert images into a Word document, a PDF file, a PowerPoint presentation, or some other document. Basically, you want to render a worksheet as an image so that it can be pasted into other applications. Aspose.Cells allows you to convert Microsoft Excel worksheets to images.
## **Remove Whitespace around Data**
The [**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender) API converts a worksheet to an image file with any specified attributes, for example, image format, paginated sheets, etc. Several image formats are supported, including BMP, GIF, JPG, TIFF, and EMF.
When you use the sheet-to-image feature, the output image has whitespace, that is, a border, around it by default. You can remove this by setting the top, bottom, left and right page setup margins for the source worksheet to 0 and specify [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions) attributes accordingly.
The following code snippet removes the whitespace around the data in the output image.
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");
// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
const options = new AsposeCells.LoadOptions();
options.setLoadFilter(new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All));
// Specify your print area if you want
// sheet.getPageSetup().setPrintArea("A1:H8");
// To remove the white border around the image.
sheet.getPageSetup().setLeftMargin(0);
sheet.getPageSetup().setRightMargin(0);
sheet.getPageSetup().setBottomMargin(0);
sheet.getPageSetup().setTopMargin(0);
// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setImageType(AsposeCells.ImageType.Emf);
// Set only one page would be rendered for the image
imgOptions.setOnePagePerSheet(true);
imgOptions.setPrintingPage(AsposeCells.PrintingPageType.IgnoreBlank);
// Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
const sr = new AsposeCells.SheetRender(sheet, imgOptions);
// Convert the image
sr.toImage(0, path.join(outputDir, "outputRemoveWhitespaceAroundData.emf"));
```
