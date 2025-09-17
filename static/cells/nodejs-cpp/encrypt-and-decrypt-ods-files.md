##Encrypt And Decrypt ODS files with Node.js via C++
Password-protect and encrypt ODS files using Aspose.Cells for Node.js via C++.
OpenOffice.org is a full-featured office suite which supports password-protecting and encrypting files. However, an encrypted ODS file can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise warning messages. The Encryption options are not applicable for ODS files unlike other file types.
Aspose.Cells allows you to encrypt and decrypt ODS files. Decrypted ODS files can be opened both in Excel and OpenOffice.
## **Encrypt with OpenOffice Calc**
1. Select **Save as** and click the **Save With Password** box.
1. Click the **Save** button.
1. Type your desired password into both the **Enter Password to Open** and **Confirm Password** fields in the Set Password window that opens.
1. Click the **OK** button to save the file.
## **Encrypt ODS file with Aspose.Cells for Node.js via C++**
To encrypt an ODS file, load the file and set the [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) value to the actual password before saving it. The output encrypted ODS file can be opened in OpenOffice only.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const sourceDir = path.join(__dirname, "source");
const outputDir = path.join(__dirname, "output");
// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));
// Password protect the file
workbook.getSettings().setPassword("1234");
// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```
## **Decrypt ODS file with Aspose.Cells for Node.js via C++**
To decrypt an ODS file, load the file by providing a password in the [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--). Once the file is loaded, set the [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) string to null.
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");
// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");
// Open an encrypted ODS file
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Ods);
// Set original password
loadOptions.setPassword("1234");
// Load the encrypted ODS file with the appropriate load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleEncryptedODSFile.ods"), loadOptions);
// Set the password to null
workbook.getSettings().setPassword(null);
// Save the decrypted ODS file
workbook.save(outputDir + "outputDecryptedODSFile.ods");
```
