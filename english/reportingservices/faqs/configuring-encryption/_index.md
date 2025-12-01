---
title: Configuring Encryption
type: docs
weight: 40
url: /reportingservices/configuring-encryption/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services supports encryption and you may render encrypted Microsoft Excel files. 

{{% /alert %}} 
### **Types of Encryption**
Aspose.Cells for Reporting Services supports encryption when exporting Excel files. It supports three encryption types:

- XOR
- WEAK ENCRYPTION
- Microsoft Strong Cryptographic Provider
### **Configuring Information**
There is configuring information for encryption in the **Aspose.Cells.ReportingServices.xml** file. When the value of Encryption is set to "off", the Aspose.Cells.ReportingServices turns encryption off.

**XML**

{{< highlight csharp >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

When Encryption is set to "on", Aspose.Cells.ReportingServices turns on encryption.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

There are four parameters in the Encryption section: ReportName, Password, EncryptionType and KeyLength.

- ReportName – Sets the report that needs encryption settings. A report uses the same encryption way when the parameter is blank.
- Password – Sets the password. It cannot be left blank.
- EncryptionType – Sets encryption type. It cannot be left blank.
- KeyLength – Sets the key length. It cannot be left blank. 

**XML**

{{< highlight csharp >}}

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



{{< /highlight >}}
