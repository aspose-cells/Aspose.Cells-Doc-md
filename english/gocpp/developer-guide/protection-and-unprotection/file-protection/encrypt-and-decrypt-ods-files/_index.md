---  
title: Encrypt And Decrypt ODS files with Golang via C++  
linktitle: Encrypt And Decrypt ODS files  
type: docs  
weight: 10  
url: /go-cpp/encrypt-and-decrypt-ods-files/  
description: Password-protect and encrypt ODS files using Aspose.Cells for Go via C++, which is a pure Go library.  
---  

{{% alert color="primary" %}}  
OpenOffice.org is a full-featured office suite that supports password‑protecting and encrypting files. However, an encrypted ODS file can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise a warning message. The encryption options are not applicable for ODS files unlike other file types.  
Aspose.Cells allows you to encrypt and decrypt ODS files. Decrypted ODS files can be opened in both Excel and OpenOffice.  
{{% /alert %}}  

## **Encrypt with OpenOffice Calc**  
1. Select **Save As** and click the **Save With Password** box.  
1. Click the **Save** button.  
1. Type your desired password into both the **Enter Password to Open** and **Confirm Password** fields in the Set Password window that opens.  
1. Click the **OK** button to save the file.  

## **Encrypt ODS file with Aspose.Cells for Go via C++**  
For encrypting an ODS file, load the file and set the [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getpassword/) value to the actual password before saving it. The resulting encrypted ODS file can be opened only in OpenOffice.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EncryptAndDecryptOdsFiles.go" >}}  

## **Decrypt ODS file with Aspose.Cells for Go via C++**  

For decrypting an ODS file, load the file by providing a password in the [**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getpassword/) property. Once the file is loaded, set the password to null.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EncryptAndDecryptOdsFiles-1.go" >}}  
{{< app/cells/assistant language="go" >}}
