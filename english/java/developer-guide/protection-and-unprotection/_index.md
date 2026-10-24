---
title: Encrypt, decrypt, protect and unprotect Excel files
linktitle: Encryption And Protection
type: docs
weight: 68
url: /java/protect-and-unprotect/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/java/security-features/]
description: This section introduces how to encrypt and decrypt Excel files and protect Excel data, covering file encryption, read-only protection, workbook structure protection, worksheet protection, and digital signatures using Java code
keywords: Aspose.Cells, Java, encrypt, decrypt, password, protect, unprotect, workbook protection, worksheet protection, read-only, digital signature
---

Excel workbooks often store sensitive financial, business, or personal information that must be kept from unauthorized access. Aspose.Cells for Java provides a comprehensive set of protection features that mirrors the capabilities of Microsoft Excel, allowing you to secure your data at the file level, the workbook level, and the worksheet level.

{{% alert color="primary" %}}
Aspose.Cells for Java offers a wide range of protection features, from file-level to data-level, similar to MS Excel. These capabilities include encrypting files with a password, enforcing read-only access through a password to modify, protecting workbook structure, protecting worksheets, and digitally signing workbooks.
{{% /alert %}}

## Encrypt and decrypt Excel files
A password set on an Excel file prevents unauthorized users from opening or viewing the workbook content. To encrypt a workbook, assign a password string to `Workbook.Settings.Password` (accessed via `workbook.getSettings().setPassword(...)`) and then save the workbook. Aspose.Cells writes the file in encrypted form. To open an encrypted workbook for decryption, instantiate a `LoadOptions` object, set `LoadOptions.Password` (via `loadOptions.setPassword(...)`) to the same password that was used during encryption, and pass it to the `Workbook` constructor. Aspose.Cells applies the supplied password transparently so that the rest of your code can interact with the decrypted content as if the file were a regular workbook.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cell cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.setPassword("OpenPassword123");
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
System.out.println("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Read-only protection (password to modify)
Excel supports two distinct password layers. The first is a password to open, which encrypts the file itself and is covered in the previous section. The second is a password to modify, which does not block users from opening the workbook; instead, Excel recommends opening the file in read-only mode unless the modify password is supplied. Configure this behavior in Aspose.Cells through `Workbook.Settings.WriteProtection` (accessed via `workbook.getSettings().getWriteProtection()`). Set its `Password` property (via `writeProtection.setPassword(...)`) to the modify password and its `Author` property (via `writeProtection.setAuthor(...)`) to identify who applied the protection. Use the `WriteProtection.validatePassword(String)` method to check whether a supplied modify password is correct, returning `true` for a match and `false` otherwise.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
workbook.save("WriteProtectedWorkbook.xlsx");
boolean isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
System.out.println("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
boolean isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
System.out.println("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Protect and unprotect workbook structure
Protecting the workbook structure prevents other users from viewing hidden worksheets, adding new worksheets, moving worksheets, deleting worksheets, hiding worksheets, or renaming worksheets. The protected state applies to the sheet structure rather than the cell contents inside any sheet. To apply structure protection, call `workbook.protect(ProtectionType.STRUCTURE, "password")`. To remove the protection, call `workbook.unprotect("password")` and supply the correct password. The `ProtectionType.STRUCTURE` enum value is used here and is distinct from other protection types such as `ProtectionType.WINDOWS`.

```java
import com.aspose.cells.*;
// Create a new workbook
Workbook workbook = new Workbook();
// Add a second worksheet
workbook.getWorksheets().add();
// Write a sample value to cell A1 of the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Protect the workbook structure
workbook.protect(ProtectionType.STRUCTURE, "StructPwd");
// Save the workbook as structure_protected.xlsx
String filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Reload the file into a new Workbook instance
Workbook loadedWorkbook = new Workbook(filePath);
// Remove the structure protection
loadedWorkbook.unprotect("StructPwd");
// Print confirmation message
System.out.println("Structure protection has been successfully removed from the workbook.");
```

## Protect and unprotect worksheets
Worksheet protection locks the cells of a worksheet against accidental or deliberate changes. Users cannot edit locked cells without supplying the password. This is the typical protection used to guard formulas, headers, or designated data-entry areas in shared spreadsheets. To protect a worksheet, call `worksheet.protect(ProtectionType.ALL, "password")`. Using `ProtectionType.ALL` enables every available protection option such as selecting locked cells, formatting cells, inserting rows and columns, and deleting rows and columns. To remove the protection, call `worksheet.unprotect("password")` with the correct password. Finer-grained control is available by combining other protection types such as `CONTENTS`, `OBJECTS`, and `SCENARIOS` using bitwise OR.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(ProtectionType.ALL, "SheetPwd", "SheetPwd");
workbook.save("sheet_protected.xlsx");
Workbook workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
System.out.println("Worksheet protection removed successfully.");
```

## Add and validate digital signatures
A digital signature assures recipients that the workbook content is authentic and has not been altered since it was signed. Aspose.Cells provides digital signature support through the `com.aspose.cells.DigitalSignatures` package. The typical workflow loads a `.pfx` certificate file through the Java security APIs (such as `java.security.KeyStore` and `java.security.cert.X509Certificate`), wraps it in an `com.aspose.cells.DigitalSignatures.DigitalSignature`, adds the signature to a `DigitalSignatureCollection`, and applies the collection to the workbook through `workbook.addDigitalSignature(DigitalSignatureCollection)`. The `DigitalSignature.getComments()` property can record signing context such as signing time and purpose. Any modification made to the workbook after signing invalidates the signature, so a validation step on the receiving side can detect tampering.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
import java.security.KeyStore;
KeyStore pfxKeyStore = KeyStore.getInstance("PKCS12");
pfxKeyStore.load(new FileInputStream("signature.pfx"), "pfx-password".toCharArray());
DigitalSignature signature = new DigitalSignature(pfxKeyStore, "pfx-password", "Signed by Aspose.Cells", new DateTime());
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.add(signature);
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
System.out.println("The workbook has been digitally signed.");
```

## Related Articles
- [Encrypt and Decrypt Excel files](/cells/java/encrypt-and-decrypt-excel-files/)
- [Protect and Unprotect Workbook Structure](/cells/java/protect-and-unprotect-workbook-structure/)
- [Protect and Unprotect Worksheet](/cells/java/protect-and-unprotect-worksheet/)
- [Password Protect or Unprotect the Shared Workbook](/cells/java/password-protect-or-unprotect-the-shared-workbook/)
- [Assign and Validate Digital Signatures](/cells/java/assign-and-validate-digital-signatures/)
- [Detect File Format of Encrypted Office Open XML - OOXML Files](/cells/java/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [How to Detect a File Format and Check if the File is Encrypted](/cells/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="java" >}}