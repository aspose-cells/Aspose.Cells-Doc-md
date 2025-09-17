##Convert Revision of XLSB to XLSM with Node.js via C++
Learn how to fully convert revisions of XLSB files into XLSM format using Aspose.Cells for Node.js via C++.
Aspose.Cells now supports fully converting revisions of XLSB files into XLSM files. Revisions are found inside the path \xl\revisions. You can view them by changing your XLSB file extension to ZIP. The \xl\revisions path contains files ending with .bin extensions.
When you convert your XLSB file into an XLSM file using Aspose.Cells, these .bin files successfully convert to .xml files as shown in these two screenshots.
The following code sample shows you how to convert the XLSB file into XLSM format using Aspose.Cells for Node.js via C++.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");
// Open workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```
