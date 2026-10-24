---
title: Protect and Unprotect
linktitle: Encryption and Protection
type: docs
weight: 68
url: /python-net/protect-and-unprotect/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/python-net/security-features/]
description: This section introduces how to encrypt and decrypt Excel files and protect Excel data, covering file encryption, read-only protection, workbook structure protection, worksheet protection, and digital signatures using Python code
keywords: Aspose.Cells, Python via .NET, encrypt, decrypt, password, protect, unprotect, workbook protection, worksheet protection, read-only, digital signature, Python
---

Excel workbooks often store sensitive financial, business, or personal information that must be kept from unauthorized access. Aspose.Cells for Python via .NET provides a comprehensive set of protection features that mirrors the capabilities of Microsoft Excel, allowing you to secure your data at the file level, the workbook level, and the worksheet level.

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET offers a wide range of protection features, from file-level to data-level, similar to MS Excel. These capabilities include encrypting files with a password, enforcing read-only access through a password to modify, protecting workbook structure, protecting worksheets, and digitally signing workbooks.
{{% /alert %}}

## Encrypt and decrypt Excel files
A password set on an Excel file prevents unauthorized users from opening or viewing the workbook content. To encrypt a workbook, assign a password string to `workbook.settings.password` and then save the workbook. Aspose.Cells writes the file in encrypted form. To open an encrypted workbook for decryption, instantiate a `LoadOptions` object, set `load_options.password` to the same password that was used during encryption, and pass it to the `Workbook` constructor. Aspose.Cells applies the supplied password transparently so that the rest of your code can interact with the decrypted content as if the file were a regular workbook.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cell = sheet.cells.get("A1")
cell.put_value("Confidential Data")
workbook.settings.password = "OpenPassword123"
workbook.save("encrypted.xlsx")
load_options = ac.LoadOptions()
load_options.password = "OpenPassword123"
decrypted_workbook = ac.Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.worksheets[0].cells.get("A1").string_value)
```

## Read-only protection (password to modify)
Excel supports two distinct password layers. The first is a password to open, which encrypts the file itself and is covered in the previous section. The second is a password to modify, which does not block users from opening the workbook; instead, Excel recommends opening the file in read-only mode unless the modify password is supplied. Configure this behavior in Aspose.Cells through `workbook.settings.write_protection`. Set its `password` property to the modify password and its `author` property to identify who applied the protection. Use the `write_protection.validate_password(string)` method to check whether a supplied modify password is correct, returning `true` for a match and `false` otherwise.

```python
import aspose.cells as ac
# Create a new workbook from scratch
workbook = ac.Workbook()
# Write a sample value to cell A1 of the first worksheet
workbook.worksheets[0].cells.get("A1").put_value("Sample Data")
# Configure the write protection: set the password to modify and the author
workbook.settings.write_protection.password = "ModifyPwd"
workbook.settings.write_protection.author = "AuthorName"
# Save the workbook so the write protection is persisted
workbook.save("WriteProtectedWorkbook.xlsx")
# Validate the password to modify using the correct password
is_correct_valid = workbook.settings.write_protection.validate_password("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Validate the password to modify using an incorrect password to demonstrate the other branch
is_wrong_valid = workbook.settings.write_protection.validate_password("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
```

## Protect and unprotect workbook structure
Protecting the workbook structure prevents other users from viewing hidden worksheets, adding new worksheets, moving worksheets, deleting worksheets, hiding worksheets, or renaming worksheets. The protected state applies to the sheet structure rather than the cell contents inside any sheet. To apply structure protection, call `workbook.protect(ProtectionType.STRUCTURE, "password")`. To remove the protection, call `workbook.unprotect("password")` and supply the correct password. The `ProtectionType.STRUCTURE` enum value is used here and is distinct from other protection types such as `ProtectionType.WINDOWS`.

```python
import aspose.cells as ac
# Create a new workbook
workbook = ac.Workbook()
# Add a second worksheet
workbook.worksheets.add()
# Write a sample value to cell A1 of the first worksheet
workbook.worksheets[0].cells.get(0, 0).put_value("Sample Data")
# Protect the workbook structure
workbook.protect(ac.ProtectionType.STRUCTURE, "StructPwd")
# Save the workbook as structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Reload the file into a new Workbook instance
loaded_workbook = ac.Workbook(file_path)
# Remove the structure protection
loaded_workbook.unprotect("StructPwd")
# Print confirmation message
print("Structure protection has been successfully removed from the workbook.")
```

## Protect and unprotect worksheets
Worksheet protection locks the cells of a worksheet against accidental or deliberate changes. Users cannot edit locked cells without supplying the password. This is the typical protection used to guard formulas, headers, or designated data-entry areas in shared spreadsheets. To protect a worksheet, call `worksheet.protect(ProtectionType.ALL, "password")`. Using `ProtectionType.ALL` enables every available protection option such as selecting locked cells, formatting cells, inserting rows and columns, and deleting rows and columns. To remove the protection, call `worksheet.unprotect("password")` with the correct password. Finer-grained control is available by combining other protection types such as `Contents`, `Objects`, and `Scenarios` using bitwise OR.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
sheet.cells.get("A1").put_value("Sample Data")
sheet.protect(ac.ProtectionType.ALL, "SheetPwd")
workbook.save("sheet_protected.xlsx")
workbook_reloaded = ac.Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.worksheets[0]
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
```

## Add and validate digital signatures
A digital signature assures recipients that the workbook content is authentic and has not been altered since it was signed. Aspose.Cells provides digital signature support through the `aspose.cells.digital_signatures` namespace. The typical workflow loads a `.pfx` certificate file through `System.Security.Cryptography.X509Certificates.X509Certificate2`, wraps it in an `aspose.cells.digital_signatures.DigitalSignature`, adds the signature to a `DigitalSignatureCollection`, and applies the collection to the workbook through `workbook.add_digital_signature(DigitalSignatureCollection)`. The `digital_signature.comments` property can record signing context such as signing time and purpose. Any modification made to the workbook after signing invalidates the signature, so a validation step on the receiving side can detect tampering.

```python
from datetime import datetime
import aspose.cells as ac
from aspose.cells.digitalsignatures import DigitalSignature, DigitalSignatureCollection
with open("signature.pfx", "rb") as certificate_file:
    certificate = certificate_file.read()
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", datetime.now())
signatures = DigitalSignatureCollection()
signatures.add(signature)
workbook = ac.Workbook()
workbook.worksheets[0].cells.get("A1").put_value("Sample Value")
workbook.add_digital_signature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
```

## Related Articles
- [Encrypt and Decrypt Excel files](/cells/python-net/encrypt-and-decrypt-excel-files/)
- [Protect and Unprotect Workbook Structure](/cells/python-net/protect-and-unprotect-workbook-structure/)
- [Protect and Unprotect Worksheet](/cells/python-net/protect-and-unprotect-worksheets/)
- [Password Protect or Unprotect the Shared Workbook](/cells/python-net/password-protect-or-unprotect-the-shared-workbook/)
- [Assign and Validate Digital Signatures](/cells/python-net/assign-and-validate-digital-signatures/)
- [Check Password to modify using Aspose.Cells](/cells/python-net/check-password-to-modify-using-aspose-cells/)
- [Detect File Format of Encrypted Office Open XML - OOXML Files](/cells/python-net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Encrypting Excel Files](/cells/python-net/encrypting-excel-files/)
- [How to Detect a File Format and Check if the File is Encrypted](/cells/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="python-net" >}}