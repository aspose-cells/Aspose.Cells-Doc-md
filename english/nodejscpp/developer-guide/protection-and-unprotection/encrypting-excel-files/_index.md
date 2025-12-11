---  
title: Encrypting Excel Files with Node.js via C++  
linktitle: Encrypting Excel Files  
type: docs  
weight: 90  
url: /nodejs-cpp/encrypting-excel-files/  
description: Learn how to encrypt and password‑protect Excel files using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

{{% alert color="primary" %}}  

Microsoft Excel (97 – 365) enables you to encrypt and password‑protect your spreadsheets. It uses algorithms provided by a cryptographic service provider (CSP), a set of cryptographic algorithms with different properties. The default CSP is **Office 97/2000 Compatible** or **Weak Encryption (XOR)**. It’s important to choose the proper encryption key length. Some CSPs don’t support more than 40 or 56 bits; that is considered weak encryption. For strong encryption, a minimum key length of 128 bits is required. Microsoft Windows contains CSPs that offer strong encryption types as well, for example the **Microsoft Strong Cryptographic Provider**. To give you an idea, 128‑bit encryption is what banks use to protect the connection with their Internet‑banking systems.  

Aspose.Cells allows you to encrypt and password‑protect Microsoft Excel files with your desired encryption type.  

{{% /alert %}}  

## **Using Microsoft Excel**  

To set file encryption settings in Microsoft Excel (here Microsoft Excel 2003):  

1. From the **Tools** menu, select **Options**. A dialog will appear.  
2. Select the **Security** tab.  
3. Enter a password and click **Advanced**.  
4. Choose the encryption type and confirm the password.  

## **Encryption with Aspose.Cells for Node.js via C++**  

The following example shows how to encrypt and password‑protect an Excel file using the Aspose.Cells API.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an Excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);

// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password‑protect the file.
workbook.getSettings().setPassword("1234");

// Save the Excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```  

### **Specifying the “Password to Modify” Option**  

The following example shows how to set the **Password to modify** Microsoft Excel option for an existing file using the Aspose.Cells API.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an Excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the Excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```  

## **Verify the Password of an Encrypted File**  

To verify the password of an encrypted file, Aspose.Cells for Node.js via C++ provides the **FileFormatUtil.verifyPassword(Uint8Array, string)** method. This method accepts two parameters: the file stream and the password that needs to be verified.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "EncryptedBook1.xlsx");

// Create a Stream object
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(fstream, "1234");

console.log("Password is valid: " + isPasswordValid);
```  

## **Encryption/Decryption of ODS Files with Aspose.Cells**  

Aspose.Cells allows you to encrypt and decrypt ODS files. A decrypted ODS file can be opened both in Excel and OpenOffice; however, an encrypted ODS file can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise a warning message. Encryption options are not applicable to ODS files, unlike other file types.  

For encrypting an ODS file, load the file and set the **WorkbookSettings.getPassword()** value to the desired password before saving it. The output encrypted ODS file can be opened in OpenOffice only.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = RunExamples.Get_SourceDirectory();
// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password‑protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```  

For decrypting an ODS file, load the file by providing a password in **LoadOptions.getPassword()**. Once the file is loaded, set the **WorkbookSettings.getPassword()** string to `null`.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

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
workbook.save(outputDir + "/outputDecryptedODSFile.ods");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
