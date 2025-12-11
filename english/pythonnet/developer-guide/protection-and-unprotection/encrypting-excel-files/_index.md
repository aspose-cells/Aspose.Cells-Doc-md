---
title: Encrypting Excel Files
type: docs
weight: 90
url: /python-net/encrypting-excel-files/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) enables you to encrypt and password protect your spreadsheets. It uses algorithms provided by a cryptographic service provider, or CSP, a set of cryptographic algorithms with different properties. The default CSP is **'Office 97/2000 Compatible'** or **'Weak Encryption (XOR)'**. It’s important to choose the proper encryption key length. Some CSPs don’t support more than 40 or 56 bits. That’s considered weak encryption. For strong encryption, a minimum key length of 128 bits is required. Microsoft Windows contains CSPs that offer strong encryption types as well, for example the **'Microsoft Strong Cryptographic Provider'**. To give you an idea, **128‑bit encryption** is what banks use to encrypt connections with their internet banking systems.

Aspose.Cells for Python via .NET allows you to encrypt and password protect Microsoft Excel files with your desired encryption type.

{{% /alert %}}

## **Using Microsoft Excel**

To set file encryption settings in Microsoft Excel (here Microsoft Excel 2003):

1. From the **Tools** menu, select **Options**. A dialog will appear.  
2. Select the **Security** tab.  
3. Input a password and click **Advanced**.  
4. Choose the encryption type and confirm the password.

## **Encryption with Aspose.Cells**

The following example shows how to encrypt and password protect an **Excel** file using the Aspose.Cells for Python via .NET API.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **Specifying Password to modify Option**

The following example shows how to set the **Password to modify** Microsoft Excel option for an existing file using the Aspose.Cells for Python via .NET API.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}

## **Verify the password of the encrypted file**

To verify the password of the encrypted file, Aspose.Cells for Python via .NET provides the [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) method. This method accepts two parameters, the file stream and the password that needs to be verified.  
The following code snippet demonstrates the use of the [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) method to verify whether the provided password is valid or not.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}

## **Encryption/Decryption of ODS file**

Aspose.Cells for Python via .NET allows you to encrypt and decrypt ODS files. A decrypted ODS file can be opened both in Excel and OpenOffice; however, an encrypted ODS file can only be opened by OpenOffice after providing the password. Excel cannot open the encrypted ODS file and may raise a warning message. The encryption options are not applicable to ODS files, unlike other file types. For encrypting an ODS file, load the file and set the [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) value to the actual password before saving it. The output encrypted ODS file can be opened in OpenOffice only.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

For decrypting an ODS file, load the file by providing a password in the [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). Once the file is loaded, set the [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) string to **null**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
