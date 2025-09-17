##Support for XAdES Signature with Node.js via C++
This article describes support for XAdES Signature using Node.js via C++ with Aspose.Cells.
## **Introduction**
Aspose.Cells provides support for signing workbooks with XAdES Signature. For this, the API provides the [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) class and [**XAdESType**](https://reference.aspose.com/cells/nodejs-cpp/xadestype) enumeration.
## **How to Add XAdES Signature for Excel**
The following code snippet demonstrates the use of the [**DigitalSignature**](https://reference.aspose.com/cells/nodejs-cpp/digitalsignature) class to sign the [source](101089323.xlsx) workbook.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");
const filePath = path.join(sourceDir, "sourceFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const password = "pfxPassword";
const pfx = path.join(sourceDir, "AsposeDemo.pfx");
const signature = new AsposeCells.DigitalSignature(pfx, "aspose", "testXAdES", new Date());
signature.setXAdESType(AsposeCells.XAdESType.XAdES);
const dsCollection = new AsposeCells.DigitalSignatureCollection();
dsCollection.add(signature);
workbook.setDigitalSignature(dsCollection);
workbook.save(outputDir + "XAdESSignatureSupport_out.xlsx");
```
