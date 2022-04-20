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

## **Encrypt ODS file with Aspose.Cells for .Net**
For encrypting an ODS file, load the file and set the [**WorkbookSettings.Password**](https://apireference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) value to the actual password before saving it. The output encrypted ODS file can be opened in OpenOffice only.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

## **Decrypt ODS file with Aspose.Cells for .Net**

For decrypting an ODS file, load the file by providing a password in the [**LoadOptions.Password**](https://apireference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). Once the file is loaded, set the [**WorkbookSettings.Password**](https://apireference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) string to null.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
