##Encrypt and Decrypt Excel files
How to encrypt and decrypt excel files using Python. Lock and unlock Excel files.
Microsoft Excel (97 - 365) enables you to encrypt and password protect your spreadsheets. It uses algorithms provided by a cryptographic service provider, or CSP, a set of cryptographic algorithms with different properties. The default CSP is 'Office 97/2000 Compatible' or 'Weak Encryption (XOR)'. It's important to choose the proper encryption key length. Some CSPs don't support more than 40 or 56 bits. That's considered to be weak encryption. For strong encryption, a minimum key length of 128 bits is required. Microsoft Windows contains CSPs that offer strong encryption types as well, for example the 'Microsoft Strong Cryptographic Provider'. To give you an idea, 128 bits encryption is what banks use to encrypt the connection with their Internet Banking systems.
Aspose.Cells for Python allows you to encrypt and password protect Microsoft Excel files with your desired encryption type.
## **Using Microsoft Excel**
To set file encryption settings in Microsoft Excel (here Microsoft Excel 2003):
1. From the **Tools** menu, select **Options**. A dialog will appear.
1. Select the **Security** tab.
1. Input a password and click **Advanced**
1. Choose the encryption type and confirm the password.
## **Encrypting Excel file with Aspose.Cells**
The following example shows how to encrypt and password protect an excel file using the Aspose.Cells API.
## **Decrypting Excel file with Aspose.Cells**
It is very to open password-protect excel file and decrypt using the Aspose.Cells API as following codes:
