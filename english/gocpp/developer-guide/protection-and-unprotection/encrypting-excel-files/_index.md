---
title: Encrypting Excel Files with Go
linktitle: Encrypting Excel Files
type: docs
weight: 90
url: /gocpp/encrypting-excel-files/
description: Learn how to encrypt and password protect Excel files using Aspose.Cells with Go.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel (97 – 365) enables you to encrypt and password‑protect your spreadsheets. It uses algorithms provided by a cryptographic service provider (CSP), a set of cryptographic algorithms with different properties. The default CSP is “Office 97/2000 Compatible” or “Weak Encryption (XOR)”. It’s important to choose the proper encryption key length. Some CSPs don’t support more than 40 or 56 bits. That’s considered weak encryption. For strong encryption, a minimum key length of 128 bits is required. Microsoft Windows contains CSPs that offer strong encryption types as well, for example the “Microsoft Strong Cryptographic Provider”. To give you an idea, 128‑bit encryption is what banks use to encrypt the connection with their Internet Banking systems.

Aspose.Cells allows you to encrypt and password‑protect Microsoft Excel files with your desired encryption type.

{{% /alert %}}

## **Using Microsoft Excel**

To set file encryption settings in Microsoft Excel (for example, Microsoft Excel 2003):

1. From the **Tools** menu, select **Options**. A dialog will appear.  
2. Select the **Security** tab.  
3. Input a password and click **Advanced**.  
4. Choose the encryption type and confirm the password.  

## **Encryption with Aspose.Cells**

The following example shows how to encrypt and password‑protect an Excel file using the Aspose.Cells API.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EncryptingExcelFiles01.go" >}}

### **Specifying Password to Modify Option**

The following example shows how to set the **Password to modify** Microsoft Excel option for an existing file using the Aspose.Cells API.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EncryptingExcelFiles02.go" >}}

## **Verify the Password of the Encrypted File**

To verify the password of the encrypted file, Aspose.Cells for Go provides the [**VerifyPassword**](https://reference.aspose.com/cells/gocpp/aspose.cells/fileformatutil/verifypassword/) method. This method accepts two parameters: the file stream and the password that needs to be verified. The following code snippet demonstrates the use of the [**VerifyPassword**](https://reference.aspose.com/cells/gocpp/aspose.cells/fileformatutil/verifypassword/) method to verify whether the provided password is valid or not.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EncryptingExcelFiles03.go" >}}

## **Encryption/Decryption of ODS Files with Aspose.Cells**

Aspose.Cells allows you to encrypt and decrypt ODS files. Decrypted ODS files can be opened both in Excel and OpenOffice; however, encrypted ODS files can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise a warning message. The encryption options are not applicable for ODS files, unlike other file types. For encrypting an ODS file, load the file and set the [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/gocpp/aspose.cells/workbooksettings/getpassword/) value to the actual password before saving it. The output encrypted ODS file can be opened in OpenOffice only.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EncryptingExcelFiles04.go" >}}

For decrypting an ODS file, load the file by providing a password in the [**LoadOptions.GetPassword()**](https://reference.aspose.com/cells/gocpp/aspose.cells/loadoptions/getpassword/). Once the file is loaded, set the [**WorkbookSettings.GetPassword()**](https://reference.aspose.com/cells/gocpp/aspose.cells/workbooksettings/getpassword/) string to `nullptr`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EncryptingExcelFiles05.go" >}}

{{< app/cells/assistant language="go" >}}