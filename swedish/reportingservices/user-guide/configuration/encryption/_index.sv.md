---
title: Kryptering
type: docs
weight: 40
url: /sv/reportingservices/encryption/
---
 Aspose.Cells for Reporting Services stöder tre typer av kryptering: XOR, WEAK ENCRYPTION och Microsoft Strong Cryptographic Provider. Se krypteringskonfigurationsinformationen i**Aspose.Cells.ReportingServices.xml** fil.

 När värdet på kryptering är**av**, Aspose.Cells for Reporting Services stänger av krypteringsfunktioner.

{{< highlight "java" >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

 När värdet på kryptering är**på**, Aspose.Cells for Reporting Services aktiverar kryptering.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Det finns fyra parametrar i krypteringssektionen:

- **Rapportnamn**: pekar på en rapport som behöver kryptering. Om parametern lämnas tom använder alla rapporter samma krypteringsmetod.
- **Lösenord**ställer in lösenordet. Kan inte vara tom.
- **EncryptionType**: ställer in en krypteringstyp. Kan inte vara tom.
- **KeyLength**: ställer in nyckellängden. Kan inte vara tom.

{{< highlight "java" >}}

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
