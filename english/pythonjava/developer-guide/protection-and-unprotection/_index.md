---
title: Protect and Unprotect
linktitle: Protection
type: docs
weight: 68
url: /python-java/protect-and-unprotect/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/python-java/security-features/]
description: This section introduces how to encrypt and decrypt Excel files and protect Excel data, covering file encryption, read-only protection, workbook structure protection, worksheet protection, and digital signatures using Python code
keywords: Aspose.Cells, Python via Java, encrypt, decrypt, password, protect, unprotect, workbook protection, worksheet protection, read-only, digital signature, Python
---

Excel workbooks often store sensitive financial, business, or personal information that must be kept from unauthorized access. Aspose.Cells for Python via Java provides a comprehensive set of protection features that mirrors the capabilities of Microsoft Excel, allowing you to secure your data at the file level, the workbook level, and the worksheet level.

{{% alert color="primary" %}}
Aspose.Cells for Python via Java offers a wide range of protection features, from file-level to data-level, similar to MS Excel. These capabilities include encrypting files with a password, enforcing read-only access through a password to modify, protecting workbook structure, protecting worksheets, and digitally signing workbooks.
{{% /alert %}}

## Encrypt and decrypt Excel files
A password set on an Excel file prevents unauthorized users from opening or viewing the workbook content. To encrypt a workbook, assign a password string to `workbook.getSettings().setPassword(...)` and then save the workbook. Aspose.Cells writes the file in encrypted form. To open an encrypted workbook for decryption, instantiate a `LoadOptions` object, set the password via `load_options.setPassword(...)` to the same password that was used during encryption, and pass it to the `Workbook` constructor. Aspose.Cells applies the supplied password transparently so that the rest of your code can interact with the decrypted content as if the file were a regular workbook.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cell, LoadOptions
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cell = sheet.getCells().get("A1")
cell.putValue("Confidential Data")
workbook.getSettings().setPassword("OpenPassword123")
workbook.save("encrypted.xlsx")
load_options = LoadOptions()
load_options.setPassword("OpenPassword123")
decrypted_workbook = Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.getWorksheets().get(0).getCells().get("A1").getStringValue())
jpype.shutdownJVM()
```

## Read-only protection (password to modify)
Excel supports two distinct password layers. The first is a password to open, which encrypts the file itself and is covered in the previous section. The second is a password to modify, which does not block users from opening the workbook; instead, Excel recommends opening the file in read-only mode unless the modify password is supplied. Configure this behavior in Aspose.Cells through `workbook.getSettings().getWriteProtection()`. Set the password via `setPassword(...)` to the modify password and the author via `setAuthor(...)` to identify who applied the protection. Use the `writeProtection.validatePassword(String)` method to check whether a supplied modify password is correct, returning `true` for a match and `false` otherwise.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Create a new workbook from scratch
workbook = Workbook()
# Write a sample value to cell A1 of the first worksheet
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data")
# Configure the write protection: set the password to modify and the author
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd")
workbook.getSettings().getWriteProtection().setAuthor("AuthorName")
# Save the workbook so the write protection is persisted
workbook.save("WriteProtectedWorkbook.xlsx")
# Validate the password to modify using the correct password
is_correct_valid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Validate the password to modify using an incorrect password to demonstrate the other branch
is_wrong_valid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
jpype.shutdownJVM()
```

## Protect and unprotect workbook structure
Protecting the workbook structure prevents other users from viewing hidden worksheets, adding new worksheets, moving worksheets, deleting worksheets, hiding worksheets, or renaming worksheets. The protected state applies to the sheet structure rather than the cell contents inside any sheet. To apply structure protection, call `workbook.protect(ProtectionType.STRUCTURE, "password")`. To remove the protection, call `workbook.unprotect("password")` and supply the correct password. The `ProtectionType.STRUCTURE` enum value is used here and is distinct from other protection types such as `ProtectionType.WINDOWS`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, ProtectionType
# Create a new workbook
workbook = Workbook()
# Add a second worksheet
workbook.getWorksheets().add()
# Write a sample value to cell A1 of the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data")
# Protect the workbook structure
workbook.protect(ProtectionType.STRUCTURE, "StructPwd")
# Save the workbook as structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Reload the file into a new Workbook instance
loaded_workbook = Workbook(file_path)
# Remove the structure protection
loaded_workbook.unprotect("StructPwd")
# Print confirmation message
print("Structure protection has been successfully removed from the workbook.")
jpype.shutdownJVM()
```

## Protect and unprotect worksheets
Worksheet protection locks the cells of a worksheet against accidental or deliberate changes. Users cannot edit locked cells without supplying the password. This is the typical protection used to guard formulas, headers, or designated data-entry areas in shared spreadsheets. To protect a worksheet, call `worksheet.protect(ProtectionType.ALL, "password")`. Using `ProtectionType.ALL` enables every available protection option such as selecting locked cells, formatting cells, inserting rows and columns, and deleting rows and columns. To remove the protection, call `worksheet.unprotect("password")` with the correct password. Finer-grained control is available by combining other protection types such as `ProtectionType.CONTENTS`, `ProtectionType.OBJECTS`, and `ProtectionType.SCENARIOS` using bitwise OR.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, ProtectionType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sample Data")
worksheet.protect(ProtectionType.ALL, "SheetPwd", None)
workbook.save("sheet_protected.xlsx")
workbook_reloaded = Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.getWorksheets().get(0)
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
jpype.shutdownJVM()
```

## Add and validate digital signatures
A digital signature assures recipients that the workbook content is authentic and has not been altered since it was signed. Aspose.Cells provides digital signature support through the `Aspose.Cells.DigitalSignatures` namespace. The typical workflow loads a `.pfx` certificate file through `java.security.KeyStore`, wraps it in an `Aspose.Cells.DigitalSignatures.DigitalSignature`, adds the signature to a `DigitalSignatureCollection`, and applies the collection to the workbook through `workbook.addDigitalSignature(digitalSignatureCollection)`. The `digitalSignature.getComments()` property can record signing context such as signing time and purpose. Any modification made to the workbook after signing invalidates the signature, so a validation step on the receiving side can detect tampering.

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, DigitalSignature, DigitalSignatureCollection
from java.security import KeyStore
from java.io import FileInputStream
from java.util import Date
# Load certificate from PFX file using Java KeyStore
key_store = KeyStore.getInstance("PKCS12")
fis = FileInputStream("signature.pfx")
key_store.load(fis, "pfx-password")
fis.close()
# Get the certificate
alias = key_store.aliases().nextElement()
certificate = key_store.getCertificate(alias)
# Create digital signature
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", Date())
signatures = DigitalSignatureCollection()
signatures.add(signature)
# Create workbook and add signature
workbook = Workbook()
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value")
workbook.addDigitalSignature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
jpype.shutdownJVM()
```

## Related Articles
- [Encrypt and Decrypt Excel files](/cells/python-java/encrypt-and-decrypt-excel-files/)
- [Protect and Unprotect Workbook Structure](/cells/python-java/protect-and-unprotect-workbook-structure/)
- [Protect and Unprotect Worksheet](/cells/python-java/protect-and-unprotect-worksheet/)
- [Check Password to modify using Aspose.Cells](/cells/python-java/check-password-to-modify-using-aspose-cells/)

{{< app/cells/assistant language="python" >}}