---
title: Verschlüsselung
type: docs
weight: 40
url: /de/reportingservices/encryption/
---

Aspose.Cells for Reporting Services unterstützt drei Arten von Verschlüsselung: XOR, WEAK ENCRYPTION und Microsoft Strong Cryptographic Provider. Sehen Sie die Verschlüsselungskonfigurationsinformationen in der **Aspose.Cells.ReportingServices.xml**-Datei.

Wenn der Wert von Encryption auf **aus** steht, schaltet Aspose.Cells for Reporting Services die Verschlüsselungsfunktionen aus.

{{< highlight java >}}

   < Encryption value="off">

    <Report name="" >

      <Password value=""/>

      <EncryptionType value="Microsoft Strong Cryptographic Provider"/>

      <KeyLength value="128"/>

    </Report>

  </ Encryption >

{{< /highlight >}}

Wenn der Wert von Encryption auf **an** steht, schaltet Aspose.Cells for Reporting Services die Verschlüsselung ein.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Es gibt vier Parameter im Verschlüsselungsabschnitt:

- **ReportName**: verweist auf einen Bericht, der Verschlüsselung benötigt. Wenn der Parameter leer gelassen wird, verwenden alle Berichte die gleiche Verschlüsselungsmethode.
- **Password**: setzt das Passwort. Darf nicht leer sein.
- **EncryptionType**: setzt einen Verschlüsselungstyp. Darf nicht leer sein.
- **KeyLength**: setzt die Schlüssellänge. Darf nicht leer sein.

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
