##Specify how to cross string in output HTML using HtmlCrossType with Node.js via C++
Learn how to control string overflow in HTML output by specifying HtmlCrossType in Aspose.Cells for Node.js via C++.
## **Possible Usage Scenarios**
When a cell contains text or string but it is larger than the width of the cell, the string overflows if the next cell in the next column is null or empty. When you save your Excel file into HTML, you can control this overflow by specifying the cross type using the [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) enumeration. It has the following values:
- **HtmlCrossType.Default**: Display like MS Excel; depends on the next cell. If the next cell is null, the string will cross or it will be truncated.
- **HtmlCrossType.MSExport**: Display the string like MS Excel exporting HTML.
- **HtmlCrossType.Cross**: Display HTML cross string; the performance for creating large HTML files will be more than ten times faster than setting the value to Default or FitToCell.
- **HtmlCrossType.FitToCell**: Only display the string within the width of the cell.
## **Specify how to cross string in output HTML using HtmlCrossType**
The following sample code loads the [sample Excel file](51740732.xlsx) and saves it to HTML format by specifying different [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Please download the [output HTMLs](51740734.zip) generated with this code. The sample Excel file contains the image bordered with red color as shown in this screenshot that shows the effect of the [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) values on output HTML.
![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)
## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");
// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);
// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);
// Output Html
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
