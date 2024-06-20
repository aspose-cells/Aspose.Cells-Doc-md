---
title: Konfigurering av kryptering
type: docs
weight: 40
url: /sv/reportingservices/configuring-encryption/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services stöder kryptering och du kan rendra krypterade Microsoft Excel-filer. 

{{% /alert %}} 
### **Typer av kryptering**
Aspose.Cells for Reporting Services stöder kryptering vid export av Excel-filer. Det stöder tre typer av kryptering:

- XOR
- SVAG KRYPTERING
- Microsoft Strong Cryptographic Provider
### **Konfigurera information**
Det finns konfigureringsinformation för kryptering i filen **Aspose.Cells.ReportingServices.xml**. När värdet för kryptering är inställt på "av" stänger Aspose.Cells.ReportingServices av krypteringen.

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

När krypteringen är inställd på "på" aktiverar Aspose.Cells.ReportingServices kryptering.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Det finns fyra parametrar i avsnittet Kryptering: Rapportnamn, Lösenord, KrypteringsTyp och Nyckellängd.

- Rapportnamn – Anger rapporten som behöver krypteringsinställningar. En rapport använder samma krypteringssätt när parametern är tom.
- Lösenord – Anger lösenordet. Det kan inte lämnas tomt.
- KrypteringsTyp – Anger krypteringstyp. Den kan inte lämnas tom.
- Nyckellängd – Anger nyckellängden. Den kan inte lämnas tom. 

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
