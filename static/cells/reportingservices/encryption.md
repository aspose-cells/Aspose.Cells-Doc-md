##Encryption
Aspose.Cells for Reporting Services supports three kinds of encryption: XOR, WEAK ENCRYPTION, and Microsoft Strong Cryptographic Provider. See the encryption configuration information in the **Aspose.Cells.ReportingServices.xml** file.
When the value of Encryption is **off**, Aspose.Cells for Reporting Services turns off encryption features.
When the value of Encryption is **on**, Aspose.Cells for Reporting Services turns encryption on.
There are four parameters in the encryption section:
- **ReportName**: points to a report that needs encryption. If the parameter is left blank, all reports use the same encryption method.
- **Password**: sets the password. Cannot be blank.
- **EncryptionType**: sets an encryption type. Cannot be blank.
- **KeyLength**: sets the key length. Cannot be blank.
