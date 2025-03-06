---
title: Encrypt And Decrypt ODS files
type: docs
weight: 10
url: /java/encrypt-and-decrypt-ods-files/
description: password-protect and encrypt ODS files using Aspose.Cells for Java which is a pure Java library.
---

{{% alert color="primary" %}}
OpenOffice.org is a full-featured office suite which supports password-protecting and encrypting files. However encrypted ODS file can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise warning message.The Encryption options are not applicable for ODS file unlike other file types. 
Aspose.Cells allows to encrypt and decrypt ODS file. Decrypted ODS file can be opened both in Excel and OpenOffice, 
{{% /alert %}}

## **Encrypt with OpenOffice Calc**
1. Select **Save as** and Click the **Save With Password** box.
1. Click the **Save** button.
1. Type your desired password into both the **Enter Password to Open** and **Confirm Password** fields in the Set Password window that opens. 
1. Click the **OK** button to save the file.

## **Encrypting/Decrypting ODS File:**

For encrypting an ODS file, load the file and pass the actual password to [**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) before saving it. The output encrypted ODS file can be opened in OpenOffice only. For decrypting an ODS file, load the file by providing the password in the [**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password). Once the file is loaded, call function [**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect-java.lang.String-) with actual password as argument and finally pass null to [**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **Sample Code:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
{{< app/cells/assistant language="java" >}}