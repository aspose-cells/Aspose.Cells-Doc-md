##Filter VBA Project while loading a workbook with Node.js via C++
Learn how to filter VBA projects while loading Excel workbooks using Aspose.Cells for Node.js via C++.
## **Filter VBA Project while loading an Excel workbook in Node.js via C++**
Some .xlsm/.xslb files have an extremely large amount of macros (or very, very long macros). Aspose.Cells for Node.js via C++ will unconditionally load this (meta) data when opening such workbooks. You may require to control this though [**LoadDataFilterOptions**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions) when you really only need to extract sheet names for a large number of workbooks, thus skipping over such unneeded content. This filter is provided by introducing a new option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/nodejs-cpp/loaddatafilteroptions).
## **Sample Code**
The following sample code loads a workbook such that only VBA is filtered. A sample file for testing this feature can be downloaded from the following link:
[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
// Set the load options, we do not want to load VBA
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);
const loadFilter = new AsposeCells.LoadFilter(AsposeCells.LoadDataFilterOptions.All & ~AsposeCells.LoadDataFilterOptions.VBA);
loadOptions.setLoadFilter(loadFilter);
// Create workbook object from sample excel file using load options
const book = new AsposeCells.Workbook(path.join(sourceDir, "sampleMacroEnabledWorkbook.xlsm"), loadOptions);
// Save the output in pdf format
book.save(outputDir + "OutputSampleMacroEnabledWorkbook.xlsm", AsposeCells.SaveFormat.Xlsm);
```
