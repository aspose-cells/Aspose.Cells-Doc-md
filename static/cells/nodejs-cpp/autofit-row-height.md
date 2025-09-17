##AutoFit Row Height Automatically When Loading file with Node.js via C++
Learn how to fit rows whose height is not customized when loading a file using Aspose.Cells for Node.js via C++.
## **Possible Usage Scenarios**
The height of the row automatically matches the font of the content, but when the height of the cached row does not match the height of the content in the file, MS Excel will automatically adjust the row height when loading the file, while Aspose.Cells for Node.js via C++ will not automatically adjust it to improve performance. If you need to use the Aspose.Cells program to automatically match line heights when loading files, you can achieve this through the parameter [setAutoFitterOptions(AutoFitterOptions) ](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) in your code.
Please refer to the following image data. We can observe that the cached row height in line 11 is 15, but Excel automatically adjusted the row height when loading the file.
## **Adjust Row Height using Aspose.Cells for Node.js via C++**
If you directly load the file and save it to PDF, the data will not be fully displayed in PDF because its cached line height is only 15.
If you set the parameter [setAutoFitterOptions(AutoFitterOptions) ](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) to true when loading the file, then Aspose.Cells will automatically adjust the row height. The adjusted line height can effectively meet the text display requirements.
## **Node.js Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
workbook.save(path.join(dataDir, "out.pdf"));
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setAutoFitterOptions(new AsposeCells.AutoFitterOptions());
loadOptions.getAutoFitterOptions().setOnlyAuto(true);
const book = new AsposeCells.Workbook(filePath, loadOptions);
book.save(path.join(dataDir, "out2.pdf"));
```
