---
title: Kryptering
type: docs
weight: 40
url: /sv/reportingservices/encryption/
---

Aspose.Cells for Reporting Services stöder tre typer av kryptering: XOR, SVAG KRYPTERING och Microsoft Strong Cryptographic Provider. Se krypteringskonfigurationsinformationen i filen **Aspose.Cells.ReportingServices.xml**.

När värdet av Encryption är **av** stänger Aspose.Cells for Reporting Services av krypteringsfunktionerna.

{{< highlight java >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

När värdet av Encryption är **på** aktiverar Aspose.Cells for Reporting Services kryptering.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Det finns fyra parametrar i krypteringsavsnittet:

- **ReportName**: pekar på en rapport som behöver kryptering. Om parametern lämnas blank, använder alla rapporter samma krypteringsmetod.
- **Lösenord**: ställer in lösenordet. Får inte vara blank.
- **EncryptionType**: ställer in en krypteringstyp. Får inte vara blank.
- **Nyckellängd**: ställer in nyckellängden. Får inte vara blank.

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
