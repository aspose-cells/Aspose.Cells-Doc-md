---
title: Protect and Unprotect
linktitle: Encryption and Protection
type: docs
weight: 68
url: /net/protect-and-unprotect/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/net/security-features/]
description: This section introduces how to encrypt and decrypt Excel files and protect Excel data, covering file encryption, read-only protection, workbook structure protection, worksheet protection, and digital signatures using C# code
keywords: Aspose.Cells, .NET, encrypt, decrypt, password, protect, unprotect, workbook protection, worksheet protection, read-only, digital signature, C#
---

Excel workbooks often store sensitive financial, business, or personal information that must be kept from unauthorized access. Aspose.Cells for .NET provides a comprehensive set of protection features that mirrors the capabilities of Microsoft Excel, allowing you to secure your data at the file level, the workbook level, and the worksheet level.

{{% alert color="primary" %}}
Aspose.Cells for .NET offers a wide range of protection features, from file-level to data-level, similar to MS Excel. These capabilities include encrypting files with a password, enforcing read-only access through a password to modify, protecting workbook structure, protecting worksheets, and digitally signing workbooks.
{{% /alert %}}

## Encrypt and decrypt Excel files
A password set on an Excel file prevents unauthorized users from opening or viewing the workbook content. To encrypt a workbook, assign a password string to `Workbook.Settings.Password` and then save the workbook. Aspose.Cells writes the file in encrypted form. To open an encrypted workbook for decryption, instantiate a `LoadOptions` object, set `LoadOptions.Password` to the same password that was used during encryption, and pass it to the `Workbook` constructor. Aspose.Cells applies the supplied password transparently so that the rest of your code can interact with the decrypted content as if the file were a regular workbook.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cell cell = sheet.Cells["A1"];
cell.PutValue("Confidential Data");
workbook.Settings.Password = "OpenPassword123";
workbook.Save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.Password = "OpenPassword123";
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
Console.WriteLine("Decrypted cell A1 value: " + decryptedWorkbook.Worksheets[0].Cells["A1"].StringValue);
```

## Read-only protection (password to modify)
Excel supports two distinct password layers. The first is a password to open, which encrypts the file itself and is covered in the previous section. The second is a password to modify, which does not block users from opening the workbook; instead, Excel recommends opening the file in read-only mode unless the modify password is supplied. Configure this behavior in Aspose.Cells through `Workbook.Settings.WriteProtection`. Set its `Password` property to the modify password and its `Author` property to identify who applied the protection. Use the `WriteProtection.ValidatePassword(string)` method to check whether a supplied modify password is correct, returning `true` for a match and `false` otherwise.

```csharp
using System;
using Aspose.Cells;
// Create a new workbook from scratch
Workbook workbook = new Workbook();
// Write a sample value to cell A1 of the first worksheet
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Data");
// Configure the write protection: set the password to modify and the author
workbook.Settings.WriteProtection.Password = "ModifyPwd";
workbook.Settings.WriteProtection.Author = "AuthorName";
// Save the workbook so the write protection is persisted
workbook.Save("WriteProtectedWorkbook.xlsx");
// Validate the password to modify using the correct password
bool isCorrectValid = workbook.Settings.WriteProtection.ValidatePassword("ModifyPwd");
Console.WriteLine("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Validate the password to modify using an incorrect password to demonstrate the other branch
bool isWrongValid = workbook.Settings.WriteProtection.ValidatePassword("WrongPwd");
Console.WriteLine("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Protect and unprotect workbook structure
Protecting the workbook structure prevents other users from viewing hidden worksheets, adding new worksheets, moving worksheets, deleting worksheets, hiding worksheets, or renaming worksheets. The protected state applies to the sheet structure rather than the cell contents inside any sheet. To apply structure protection, call `workbook.Protect(ProtectionType.Structure, "password")`. To remove the protection, call `workbook.Unprotect("password")` and supply the correct password. The `ProtectionType.Structure` enum value is used here and is distinct from other protection types such as `ProtectionType.Windows`.

```csharp
using System;
using Aspose.Cells;
// Create a new workbook
Workbook workbook = new Workbook();
// Add a second worksheet
workbook.Worksheets.Add();
// Write a sample value to cell A1 of the first worksheet
workbook.Worksheets[0].Cells[0, 0].PutValue("Sample Data");
// Protect the workbook structure
workbook.Protect(ProtectionType.Structure, "StructPwd");
// Save the workbook as structure_protected.xlsx
string filePath = "structure_protected.xlsx";
workbook.Save(filePath);
// Reload the file into a new Workbook instance
Workbook loadedWorkbook = new Workbook(filePath);
// Remove the structure protection
loadedWorkbook.Unprotect("StructPwd");
// Print confirmation message
Console.WriteLine("Structure protection has been successfully removed from the workbook.");
```

## Protect and unprotect worksheets
Worksheet protection locks the cells of a worksheet against accidental or deliberate changes. Users cannot edit locked cells without supplying the password. This is the typical protection used to guard formulas, headers, or designated data-entry areas in shared spreadsheets. To protect a worksheet, call `worksheet.Protect(ProtectionType.All, "password")`. Using `ProtectionType.All` enables every available protection option such as selecting locked cells, formatting cells, inserting rows and columns, and deleting rows and columns. To remove the protection, call `worksheet.Unprotect("password")` with the correct password. Finer-grained control is available by combining other protection types such as `Contents`, `Objects`, and `Scenarios` using bitwise OR.

```csharp
using System;
using Aspose.Cells;
var workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
sheet.Cells["A1"].PutValue("Sample Data");
sheet.Protect(ProtectionType.All, "SheetPwd");
workbook.Save("sheet_protected.xlsx");
var workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.Worksheets[0];
sheetReloaded.Unprotect("SheetPwd");
Console.WriteLine("Worksheet protection removed successfully.");
```

## Add and validate digital signatures
A digital signature assures recipients that the workbook content is authentic and has not been altered since it was signed. Aspose.Cells provides digital signature support through the `Aspose.Cells.DigitalSignatures` namespace. The typical workflow loads a `.pfx` certificate file through `System.Security.Cryptography.X509Certificates.X509Certificate2`, wraps it in an `Aspose.Cells.DigitalSignatures.DigitalSignature`, adds the signature to a `DigitalSignatureCollection`, and applies the collection to the workbook through `Workbook.AddDigitalSignature(DigitalSignatureCollection)`. The `DigitalSignature.Comments` property can record signing context such as signing time and purpose. Any modification made to the workbook after signing invalidates the signature, so a validation step on the receiving side can detect tampering.

```csharp
using System;
using System.IO;
using System.Security.Cryptography.X509Certificates;
using Aspose.Cells;
using Aspose.Cells.DigitalSignatures;
X509Certificate2 certificate = new X509Certificate2("signature.pfx", "pfx-password");
DigitalSignature signature = new DigitalSignature(certificate, "Signed by Aspose.Cells", DateTime.Now);
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.Add(signature);
Workbook workbook = new Workbook();
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Value");
workbook.AddDigitalSignature(signatures);
workbook.Save("signed_workbook.xlsx");
Console.WriteLine("The workbook has been digitally signed.");
```

## Related Articles
- [Encrypt and Decrypt Excel files](/cells/net/encrypt-and-decrypt-excel-files/)
- [Protect and Unprotect Workbook Structure](/cells/net/protect-and-unprotect-workbook-structure/)
- [Protect and Unprotect Worksheet](/cells/net/protect-and-unprotect-worksheets/)
- [Password Protect or Unprotect the Shared Workbook](/cells/net/password-protect-or-unprotect-the-shared-workbook/)
- [Assign and Validate Digital Signatures](/cells/net/assign-and-validate-digital-signatures/)
- [Check Password to modify using Aspose.Cells](/cells/net/check-password-to-modify-using-aspose-cells/)
- [Detect File Format of Encrypted Office Open XML - OOXML Files](/cells/net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Encrypting Excel Files](/cells/net/encrypting-excel-files/)
- [How to Detect a File Format and Check if the File is Encrypted](/cells/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="csharp" >}}