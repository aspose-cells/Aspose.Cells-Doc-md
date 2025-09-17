##Encrypt and Decrypt Excel files
How to encrypt and decrypt excel files using java. Lock and unlock Excel files.
Microsoft Excel (97 - 365 ) enables you to encrypt / password protect your spreadsheets. It utilizes algorithms provided by Crypto Service Provider. A Crypto Service Provider or CSP is a set of cryptographic algorithms with different properties. The default CSP is "Office 97/2000 Compatible" or " Week Encryption (XOR) ". It's also important to choose a proper encryption key length. Some of the Crypto Service Providers don't support more than 40 or 56 bits. That's considered to be a weak encryption type. But, for strong encryption type, a minimum key length of 128 bits is required. Microsoft Windows contains Crypto Service Providers that offer strong encryption types as well, for example, the 'Microsoft Strong Cryptographic Provider'. To give an idea, 128 bits encryption is what banks use to encrypt the connection with their Internet Banking Systems. Aspose.Cells allows you to encrypt / password protect your excel files with your desired encryption type.
## **Using MS Excel**
In MS Excel (e.g MS Excel 2003), to implement file encryption settings, you may try:
- From the **Tools** menu, select **Options**, and then select the **Security** tab.
- Input **Password to open** and click the **Advanced** button.
- Choose the encryption type and confirm the password.
![todo:image_alt_text](encrypting-excel-files_1.png)
**Figure: Options dialog**
![todo:image_alt_text](encrypting-excel-files_2.png)
**Figure: Encryption Type dialog**
## **Encrypting Excel file**
The following example shows how you can encrypt / password protect an excel file using the Aspose.Cells API.
### **Sample Code:**
## **Decrypting Excel file with Aspose.Cells**
It is very to open password-protect excel file and decrypt using the Aspose.Cells API as following codes:
