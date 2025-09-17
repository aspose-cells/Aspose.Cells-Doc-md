##Save as ODF 1.1, 1.2 and 1.3 with Node.js via C++
Convert Excel to ODF 1.1, 1.2 and 1.3 Specifications with Aspose.Cells for Node.js via C++.
Aspose.Cells supports saving an ODS file (**OpenDocument Spreadsheet**) in the ODF (**OpenDocument Format**) 1.1, 1.2 and 1.3 specifications. Aspose.Cells has [**OdsSaveOptions.getOdfStrictVersion()**](https://reference.aspose.com/cells/nodejs-cpp/odssaveoptions/#getOdfStrictVersion--) property that specifies the ODF version for saving ODS files. The default value of this property is [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/nodejs-cpp/opendocumentformatversiontype/), so the ODS file saved without this setting uses the 1.2 specifications.
The sample code below creates a workbook object, adds some value to cell A1 on the first worksheet and then saves the ODS file in ODF 1.1, 1.2 and 1.3 specifications. By default, the ODS file is saved in ODF 1.2 specification.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook
const workbook = new AsposeCells.Workbook();
// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Put some value in cell A1
const cell = worksheet.getCells().get("A1");
cell.putValue("Welcome to Aspose!");
// Save ODS in ODF 1.2 version which is default
let options = new AsposeCells.OdsSaveOptions();
workbook.save(path.join(dataDir, "ODF1.2_out.ods"), options);
// Save ODS in ODF 1.1 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf11);
workbook.save(path.join(dataDir, "ODF1.1_out.ods"), options);
// Save ODS in ODF 1.3 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf13);
workbook.save(path.join(dataDir, "ODF1.3_out.ods"), options);
```
