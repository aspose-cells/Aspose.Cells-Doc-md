##Read Numbers Spreadsheet Developed by Apple Inc. using Aspose.Cells for Node.js via C++
Learn how to read Numbers spreadsheets developed by Apple Inc. using Aspose.Cells for Node.js via C++.
## **Possible Usage Scenarios**
Numbers is a spreadsheet application developed by Apple Inc. Aspose.Cells can read Numbers spreadsheets, but it does not support writing to them. It can read Numbers spreadsheets' Data, Style, and Formulas.
## **Read Numbers Spreadsheet Developed by Apple Inc. using Aspose.Cells for Node.js via C++**
The following sample code loads the [Sample Numbers Spreadsheet](sampleNumbersByAppleInc.numbers) and converts it to [Output PDF Format](outputNumbersByAppleInc.pdf). You will have to use the [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) class and specify [**LoadFormat.Numbers**](https://reference.aspose.com/cells/nodejs-cpp/loadformat) as a parameter in its constructor to load it successfully. Please download both of them from the given links. You can try the code with any Numbers spreadsheet. Please also read the comments of the code for more help.
## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceFilePath = path.join(dataDir, "sampleNumbersByAppleInc.numbers");
const outputFilePath = path.join(dataDir, "outputNumbersByAppleInc.pdf");
// Specify load options, we want to load Numbers spreadsheet
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Numbers);
// Load the Numbers spreadsheet in workbook with above load options
const wb = new AsposeCells.Workbook(sourceFilePath, opts);
// Save the workbook to pdf format
wb.save(outputFilePath, AsposeCells.SaveFormat.Pdf);
```
