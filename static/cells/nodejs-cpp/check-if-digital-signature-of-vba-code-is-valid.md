##Check if Digital Signature of VBA Code is Valid with Node.js via C++
Learn how to check the validity of a digital signature of VBA code using Aspose.Cells for Node.js via C++.
Aspose.Cells allows you to check if the digital signature of the VBA code is valid using the [**Workbook.isValidSigned()**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#isValidSigned--) property. It will return **true** if the signature is valid otherwise it will return **false**. The digital signature of the VBA code becomes invalid when you change the VBA code.
## **Check if Digital Signature of VBA Code is Valid in Node.js**
The following code demonstrates the usage of this property using the [sample excel file](5115030.xlsm) which you can download from the provided link. The same excel file has a valid signature but when we modify its VBA code and save the workbook and then recheck, we find its signature has become invalid.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleVBAProjectSigned.xlsm");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Signature is valid
console.log("Is VBA Code Project Valid Signed: " + workbook.getVbaProject().isValidSigned());
// Modify the VBA Code, save the workbook then reload
// VBA Code Signature will now be invalid
let code = workbook.getVbaProject().getModules().get(1).getCodes();
code = code.replace("Welcome to Aspose", "Welcome to Aspose.Cells");
workbook.getVbaProject().getModules().get(1).setCodes(code);
// Save
workbook.save(path.join(dataDir, "output_out.xlsm"));
// Reload
workbook = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsm"));
// Now the signature is invalid
console.log("Is VBA Code Project Valid Signed: " + workbook.getVbaProject().isValidSigned());
```
