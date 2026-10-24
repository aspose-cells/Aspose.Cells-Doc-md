---
title: Protect and Unprotect
linktitle: Encryption and Protection
type: docs
weight: 68
url: /nodejs-java/protect-and-unprotect/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/nodejs-java/security-features/]
description: This section introduces how to encrypt and decrypt Excel files and protect Excel data, covering file encryption, read-only protection, workbook structure protection, worksheet protection, and digital signatures using JavaScript code
keywords: Aspose.Cells, Node.js via Java, encrypt, decrypt, password, protect, unprotect, workbook protection, worksheet protection, read-only, digital signature, JavaScript
---

Excel workbooks often store sensitive financial, business, or personal information that must be kept from unauthorized access. Aspose.Cells for Node.js via Java provides a comprehensive set of protection features that mirrors the capabilities of Microsoft Excel, allowing you to secure your data at the file level, the workbook level, and the worksheet level.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java offers a wide range of protection features, from file-level to data-level, similar to MS Excel. These capabilities include encrypting files with a password, enforcing read-only access through a password to modify, protecting workbook structure, protecting worksheets, and digitally signing workbooks.
{{% /alert %}}

## Encrypt and decrypt Excel files
A password set on an Excel file prevents unauthorized users from opening or viewing the workbook content. To encrypt a workbook, assign a password string to `workbook.getSettings().setPassword(...)` and then save the workbook. Aspose.Cells writes the file in encrypted form. To open an encrypted workbook for decryption, instantiate a `LoadOptions` object, set `loadOptions.setPassword(...)` to the same password that was used during encryption, and pass it to the `Workbook` constructor. Aspose.Cells applies the supplied password transparently so that the rest of your code can interact with the decrypted content as if the file were a regular workbook.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
let loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("OpenPassword123");
let decryptedWorkbook = new AsposeCells.Workbook("encrypted.xlsx", loadOptions);
console.log("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Read-only protection (password to modify)
Excel supports two distinct password layers. The first is a password to open, which encrypts the file itself and is covered in the previous section. The second is a password to modify, which does not block users from opening the workbook; instead, Excel recommends opening the file in read-only mode unless the modify password is supplied. Configure this behavior in Aspose.Cells through `workbook.getSettings().getWriteProtection()`. Set its `Password` property to the modify password and its `Author` property to identify who applied the protection. Use the `writeProtection.validatePassword(string)` method to check whether a supplied modify password is correct, returning `true` for a match and `false` otherwise.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Write a sample value to cell A1 of the first worksheet
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// Configure the write protection: set the password to modify and the author
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// Save the workbook so the write protection is persisted
workbook.save("WriteProtectedWorkbook.xlsx");
// Validate the password to modify using the correct password
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Validate the password to modify using an incorrect password to demonstrate the other branch
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Protect and unprotect workbook structure
Protecting the workbook structure prevents other users from viewing hidden worksheets, adding new worksheets, moving worksheets, deleting worksheets, hiding worksheets, or renaming worksheets. The protected state applies to the sheet structure rather than the cell contents inside any sheet. To apply structure protection, call `workbook.protect(ProtectionType.Structure, "password")`. To remove the protection, call `workbook.unprotect("password")` and supply the correct password. The `ProtectionType.Structure` enum value is used here and is distinct from other protection types such as `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Add a second worksheet
workbook.getWorksheets().add();
// Write a sample value to cell A1 of the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Protect the workbook structure
workbook.protect(AsposeCells.ProtectionType.STRUCTURE, "StructPwd");
// Save the workbook as structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Reload the file into a new Workbook instance
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Remove the structure protection
loadedWorkbook.unprotect("StructPwd");
// Print confirmation message
console.log("Structure protection has been successfully removed from the workbook.");
```

## Protect and unprotect worksheets
Worksheet protection locks the cells of a worksheet against accidental or deliberate changes. Users cannot edit locked cells without supplying the password. This is the typical protection used to guard formulas, headers, or designated data-entry areas in shared spreadsheets. To protect a worksheet, call `worksheet.protect(ProtectionType.All, "password")`. Using `ProtectionType.All` enables every available protection option such as selecting locked cells, formatting cells, inserting rows and columns, and deleting rows and columns. To remove the protection, call `worksheet.unprotect("password")` with the correct password. Finer-grained control is available by combining other protection types such as `Contents`, `Objects`, and `Scenarios` using bitwise OR.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.ALL, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Add and validate digital signatures
A digital signature assures recipients that the workbook content is authentic and has not been altered since it was signed. Aspose.Cells provides digital signature support through classes such as `AsposeCells.DigitalSignature` and `AsposeCells.DigitalSignatureCollection`. The typical workflow creates an `AsposeCells.DigitalSignature` directly from a `.pfx` certificate file together with its password and signing comments, adds the signature to a `DigitalSignatureCollection`, and applies the collection to the workbook through `workbook.addDigitalSignature(DigitalSignatureCollection)`. The `DigitalSignature.Comments` property can record signing context such as signing time and purpose. Any modification made to the workbook after signing invalidates the signature, so a validation step on the receiving side can detect tampering.

```javascript
const AsposeCells = require("aspose.cells");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

{{< app/cells/assistant language="nodejs-java" >}}