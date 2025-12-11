---
title: Encrypt and Decrypt Excel files
type: docs
weight: 10
url: /python-java/encrypt-and-decrypt-excel-files/
description: How to encrypt and decrypt excel files using Python. Lock and unlock Excel files.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) enables you to encrypt and password protect your spreadsheets. It uses algorithms provided by a cryptographic service provider, or CSP, a set of cryptographic algorithms with different properties. The default CSP is 'Office 97/2000 Compatible' or 'Weak Encryption (XOR)'. It's important to choose the proper encryption key length. Some CSPs don't support more than 40 or 56 bits. That's considered to be weak encryption. For strong encryption, a minimum key length of 128 bits is required. Microsoft Windows contains CSPs that offer strong encryption types as well, for example the 'Microsoft Strong Cryptographic Provider'. To give you an idea, 128-bit encryption is what banks use to encrypt the connection with their Internet Banking systems.

Aspose.Cells for Python allows you to encrypt and password protect Microsoft Excel files with your desired encryption type.

{{% /alert %}}

## **Using Microsoft Excel**

To set file encryption settings in Microsoft Excel (here Microsoft Excel 2003):

1. From the **Tools** menu, select **Options**. A dialog will appear.
2. Select the **Security** tab.
3. Input a password and click **Advanced**.
4. Choose the encryption type and confirm the password.

## **Encrypting Excel file with Aspose.Cells**

The following example shows how to encrypt and password protect an Excel file using the Aspose.Cells API.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-CSharp-Files-Utility-EncryptingFiles-1.py" >}}

## **Decrypting Excel file with Aspose.Cells**

It is very easy to open a password‑protected Excel file and decrypt it using the Aspose.Cells API, as shown in the following code:

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Decrypt-Excel-File.py" >}}
