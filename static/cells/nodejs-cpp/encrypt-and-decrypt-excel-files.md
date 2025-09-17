##Encrypt and Decrypt Excel files with Node.js via C++
How to encrypt and decrypt Excel files using Node.js via C++. Lock and unlock Excel files.
Microsoft Excel (97 - 365) enables you to encrypt and password protect your spreadsheets. It uses algorithms provided by a cryptographic service provider, or CSP, a set of cryptographic algorithms with different properties. The default CSP is 'Office 97/2000 Compatible' or 'Weak Encryption (XOR)'. It's important to choose the proper encryption key length. Some CSPs don't support more than 40 or 56 bits. That's considered to be weak encryption. For strong encryption, a minimum key length of 128 bits is required. Microsoft Windows contains CSPs that offer strong encryption types as well, for example the 'Microsoft Strong Cryptographic Provider'. To give you an idea, 128 bits encryption is what banks use to encrypt the connection with their Internet Banking systems.
Aspose.Cells allows you to encrypt and password protect Microsoft Excel files with your desired encryption type.
## **Using Microsoft Excel**
To set file encryption settings in Microsoft Excel (here Microsoft Excel 2003):
1. From the **Tools** menu, select **Options**. A dialog will appear.
2. Select the **Security** tab.
3. Input a password and click **Advanced**
4. Choose the encryption type and confirm the password.
## **Encrypting Excel file with Aspose.Cells for Node.js via C++**
The following example shows how to encrypt and password protect an Excel file using the Aspose.Cells API.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");
// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);
// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);
// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);
// Password protect the file.
workbook.getSettings().setPassword("1234");
// Save the excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```
### **Specifying Password to Modify Option**
The following example shows how to set the **Password to modify** Microsoft Excel option for an existing file using the Aspose.Cells API.
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));
// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");
// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```
## **Decrypting Excel file with Aspose.Cells for Node.js via C++**
It is very easy to open a password-protected Excel file and decrypt it using the Aspose.Cells API as shown in the following code:
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Open encrypted file with password.
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("password");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);
// Remove password.
workbook.getSettings().setPassword(null);
// Save the file.
workbook.save(filePath);
```
## **Advance topics**
- [Encrypt And Decrypt ODS files](https://docs.aspose.com/cells/nodejs-cpp/encrypt-and-decrypt-ods-files/)
- [Setting Strong Encryption Type](https://docs.aspose.com/cells/nodejs-cpp/setting-strong-encryption-type/)
- [Specify Author while Write Protecting Workbook](https://docs.aspose.com/cells/nodejs-cpp/specify-author-while-write-protecting-workbook/)
- [Verify Password of Encrypted Files](https://docs.aspose.com/cells/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/)
