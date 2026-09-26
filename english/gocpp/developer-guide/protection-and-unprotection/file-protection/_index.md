---
title: Encrypt and Decrypt Excel files with Golang via C++
linktitle: Encrypt and Decrypt Excel files
type: docs
weight: 10
url: /go-cpp/encrypt-and-decrypt-excel-files/
description: How to encrypt and decrypt Excel files using C++. Lock and unlock Excel files.
---

{{% alert color="primary" %}}

Microsoft Excel (97–365) enables you to encrypt and password‑protect your spreadsheets. It uses algorithms provided by a cryptographic service provider (CSP), a set of cryptographic algorithms with different properties. The default CSP is “Office 97/2000 Compatible” or “Weak Encryption (XOR)”. It’s important to choose the proper encryption key length. Some CSPs don’t support more than 40 or 56 bits. That is considered weak encryption. For strong encryption, a minimum key length of 128 bits is required. Microsoft Windows contains CSPs that offer strong encryption types as well, for example the “Microsoft Strong Cryptographic Provider”. To give you an idea, 128‑bit encryption is what banks use to secure connections with their online banking systems.

Aspose.Cells allows you to encrypt and password‑protect Microsoft Excel files with your desired encryption type.

{{% /alert %}}

## **Using Microsoft Excel**

To set file encryption settings in Microsoft Excel (here Microsoft Excel 2003):

1. From the **Tools** menu, select **Options**. A dialog will appear.  
2. Select the **Security** tab.  
3. Enter a password and click **Advanced**.  
4. Choose the encryption type and confirm the password.

## **Encrypting Excel file with Aspose.Cells**

The following example shows how to encrypt and password‑protect an Excel file using the Aspose.Cells API.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FileProtection.go" >}}

### **Specifying the “Password to modify” Option**

The following example shows how to set the **Password to modify** Microsoft Excel option for an existing file using the Aspose.Cells API.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FileProtection-1.go" >}}

## **Decrypting Excel file with Aspose.Cells**

It is very easy to open a password‑protected Excel file and decrypt it using the Aspose.Cells API, as shown in the following code:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FileProtection-2.go" >}}

## **Advanced topics**

- [Encrypt and Decrypt ODS files](/cells/go-cpp/encrypt-and-decrypt-ods-files/)
- [Setting Strong Encryption Type](/cells/go-cpp/setting-strong-encryption-type/)
- [Specify Author while Write‑Protecting Workbook](/cells/go-cpp/specify-author-while-write-protecting-workbook/)
- [Verify Password of Encrypted Files](/cells/go-cpp/verify-password-of-encrypted-excel-and-ods-files/)
{{< app/cells/assistant language="go" >}}
