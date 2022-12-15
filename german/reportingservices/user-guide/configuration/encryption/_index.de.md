---
title: Verschlüsselung
type: docs
weight: 40
url: /de/reportingservices/encryption/
---
 Aspose.Cells for Reporting Services unterstützt drei Arten der Verschlüsselung: XOR, WEAK ENCRYPTION und Microsoft Strong Cryptographic Provider. Siehe die Informationen zur Verschlüsselungskonfiguration in der**Aspose.Cells.ReportingServices.xml** Datei.

 Wenn der Wert von Encryption ist**aus**, Aspose.Cells for Reporting Services schaltet die Verschlüsselungsfunktionen aus.

{{< highlight "java" >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

 Wenn der Wert von Encryption ist**an**, Aspose.Cells for Reporting Services schaltet die Verschlüsselung ein.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Es gibt vier Parameter im Verschlüsselungsabschnitt:

- **Berichtsname**: verweist auf einen Bericht, der verschlüsselt werden muss. Wenn der Parameter leer gelassen wird, verwenden alle Berichte dieselbe Verschlüsselungsmethode.
- **Passwort**Legt das Passwort fest. Darf nicht leer sein.
- **Verschlüsselungstyp**: legt einen Verschlüsselungstyp fest. Darf nicht leer sein.
- **Schlüssellänge**: Legt die Schlüssellänge fest. Darf nicht leer sein.

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
