---
title: Konfigurera kryptering
type: docs
weight: 40
url: /sv/reportingservices/configuring-encryption/
---
{{% alert color="primary" %}} 

 Aspose.Cells for Reporting Services stöder kryptering och du kan rendera krypterade Microsoft Excel-filer.

{{% /alert %}} 
### **Typer av kryptering**
Aspose.Cells for Reporting Services stöder kryptering vid export av Excel-filer. Den stöder tre krypteringstyper:

- XOR
- SVAG KRYPTERING
- Microsoft Stark kryptografisk leverantör
### **Konfigurera information**
 Det finns konfigurationsinformation för kryptering i**Aspose.Cells.ReportingServices.xml** fil. När värdet för kryptering är inställt på "av", stänger Aspose.Cells.ReportingServices kryptering av.

**XML**

{{< highlight "csharp" >}}

 <Encryption value="off">

<Report name="" >

<Password value=""/>

<EncryptionType value="Microsoft Strong Cryptographic Provider"/>

<KeyLength value="128"/>

</Report>

</ Encryption >



{{< /highlight >}}

När kryptering är inställt på "på", aktiverar Aspose.Cells.ReportingServices kryptering.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Det finns fyra parametrar i avsnittet Kryptering: ReportName, Password, EncryptionType och KeyLength.

- ReportName – Anger rapporten som behöver krypteringsinställningar. En rapport använder samma krypteringssätt när parametern är tom.
- Lösenord – Ställer in lösenordet. Det kan inte lämnas tomt.
- EncryptionType – Anger krypteringstyp. Det kan inte lämnas tomt.
-  KeyLength – Ställer in nyckellängden. Det kan inte lämnas tomt.

**XML**

{{< highlight "csharp" >}}

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
