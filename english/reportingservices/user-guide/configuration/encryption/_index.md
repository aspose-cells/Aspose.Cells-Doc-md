---
title: Encryption
type: docs
weight: 40
url: /reportingservices/encryption/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Aspose.Cells for Reporting Services supports three kinds of encryption: XOR, WEAK ENCRYPTION, and Microsoft Strong Cryptographic Provider. See the encryption configuration information in the **Aspose.Cells.ReportingServices.xml** file.

When the value of Encryption is **off**, Aspose.Cells for Reporting Services turns off encryption features.

{{< highlight java >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

When the value of Encryption is **on**, Aspose.Cells for Reporting Services turns encryption on.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

There are four parameters in the encryption section:

- **ReportName**: points to a report that needs encryption. If the parameter is left blank, all reports use the same encryption method.
- **Password**: sets the password. Cannot be blank.
- **EncryptionType**: sets an encryption type. Cannot be blank.
- **KeyLength**: sets the key length. Cannot be blank.

{{< highlight java >}}

 <Encryption value="on">

  <Report name="Test" >

      <Password value="12345"/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  	  <Report name="" >

      <Password value="123456"/>

      <EncryptionType value=" XOR "/>

      <KeyLength value="128"/>

    </Report>

 </Encryption>

{{< /highlight >}}
