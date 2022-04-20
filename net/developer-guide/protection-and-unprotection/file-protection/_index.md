---
title: Encrypt And Decrypt Excel files
type: docs
weight: 10
url: /net/encrypt-and-decrypt-excel-files/
aliases: [/net/encrypting-excel-files/]
description: How to encrypt and decrypt excel files using C#.
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) enables you to encrypt and password protect your spreadsheets. It uses algorithms provided by a cryptographic service provider, or CSP, a set of cryptographic algorithms with different properties. The default CSP is 'Office 97/2000 Compatible' or 'Weak Encryption (XOR)'. It's important to choose the proper encryption key length. Some CSPs don't support more than 40 or 56 bits. That's considered to be weak encryption. For strong encryption, a minimum key length of 128 bits is required. Microsoft Windows contains CSPs that offer strong encryption types as well, for example the 'Microsoft Strong Cryptographic Provider'. To give you an idea, 128 bits encryption is what banks use to encrypt the connection with their Internet Banking systems.

Aspose.Cells allows you to encrypt and password protect Microsoft Excel files with your desired encryption type.

{{% /alert %}}

## **Using Microsoft Excel**

To set file encryption settings in Microsoft Excel (here Microsoft Excel 2003):

1. From the **Tools** menu, select **Options**. A dialog will appear.
1. Select the **Security** tab.
1. Input a password and click **Advanced**
1. Choose the encryption type and confirm the password.

## **Encrypting Excel file with Aspose.Cells**

The following example shows how to encrypt and password protect an excel file using the Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **Specifying Password to modify Option**

The following example shows how to set the **Password to modify** Microsoft Excel option for an existing file using the Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}


## **Decrypting Excel file with Aspose.Cells**
It is very to open password-protect excel file and decrypt using the Aspose.Cells API as following codes:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Decrypt-Excel-File.cs" >}}


## **Verify the password of the encrypted file**

To verify the password of the encrypted file, Aspose.Cells for .NET provides the [**VerifyPassword**](https://apireference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) method. These methods accept two parameters, the file stream and the password that needs to be verified.
The following code snippet demonstrates the use of the [**VerifyPassword**](https://apireference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) method to verify whether the provided password is valid or not.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}


## **Advance topics**
- [Encrypt And Decrypt ODS files](/cells/cells/net/encrypt-and-decrypt-ods-files/)
- [Setting Strong Encryption Type](/cells/net/setting-strong-encryption-type/)
- [Specify Author while Write Protecting Workbook](/cells/net/specify-author-while-write-protecting-workbook/)