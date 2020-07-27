+++
title = "Configuring Encryption" 
description = "" 
weight = 8108 
+++

Aspose.Cells for Reporting Services : Configuring Encryption  

# Aspose.Cells for Reporting Services : Configuring Encryption


Aspose.Cells for Reporting Services supports encryption and you may render encrypted Microsoft Excel files.

### Types of Encryption

Aspose.Cells for Reporting Services supports encryption when exporting Excel files. It supports three encryption types:

*   XOR
*   WEAK ENCRYPTION
*   Microsoft Strong Cryptographic Provider

### Configuring Information

There is configuring information for encryption in the **Aspose.Cells.ReportingServices.xml** file. When the value of `Encryption` is set to "off", the Aspose.Cells.ReportingServices turns encryption off.

**XML**

{{< code lang="xml" >}}
<Encryption value="off">
<Report name="" >
<Password value=""/>
<EncryptionType value="Microsoft Strong Cryptographic Provider"/>
<KeyLength value="128"/>
</Report>
</ Encryption >
 
{{< /code >}}

When `Encryption` is set to "on", Aspose.Cells.ReportingServices turns on encryption.

{{< code lang="cs" >}}
<Encryption value="on">
{{< /code >}}

There are four parameters in the Encryption section: ReportName, Password, EncryptionType and KeyLength.

*   `ReportName` – Sets the report that needs encryption settings. A report uses the same encryption way when the parameter is blank.
*   `Password` – Sets the password. It cannot be left blank.
*   `EncryptionType` – Sets encryption type. It cannot be left blank.
*   `KeyLength` – Sets the key length. It cannot be left blank.
    
    **XML**
    
{{< code lang="xml" >}}
<Encryption value="on">
<Report name="Test" >
<Password value="12345"/>
<EncryptionType value="Microsoft Strong Cryptographic Provider"/>
<KeyLength value="128"/>
</Report>

<Report name="" >
<Password value="123456"/>
<EncryptionType value="XOR"/>
<KeyLength value="128"/>
</Report>
</Encryption>
 
{{< /code >}}
    

