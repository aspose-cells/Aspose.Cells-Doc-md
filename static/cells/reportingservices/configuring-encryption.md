##Configuring Encryption
Aspose.Cells for Reporting Services supports encryption and you may render encrypted Microsoft Excel files.
### **Types of Encryption**
Aspose.Cells for Reporting Services supports encryption when exporting Excel files. It supports three encryption types:
- XOR
- WEAK ENCRYPTION
- Microsoft Strong Cryptographic Provider
### **Configuring Information**
There is configuring information for encryption in the **Aspose.Cells.ReportingServices.xml** file. When the value of Encryption is set to "off", the Aspose.Cells.ReportingServices turns encryption off.
**XML**
When Encryption is set to "on", Aspose.Cells.ReportingServices turns on encryption.
There are four parameters in the Encryption section: ReportName, Password, EncryptionType and KeyLength.
- ReportName – Sets the report that needs encryption settings. A report uses the same encryption way when the parameter is blank.
- Password – Sets the password. It cannot be left blank.
- EncryptionType – Sets encryption type. It cannot be left blank.
- KeyLength – Sets the key length. It cannot be left blank.
**XML**
