---
title: Verschlüsselung konfigurieren
type: docs
weight: 40
url: /de/reportingservices/configuring-encryption/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services unterstützt Verschlüsselung und Sie können verschlüsselte Microsoft Excel-Dateien rendern. 

{{% /alert %}} 
### **Arten von Verschlüsselung**
Aspose.Cells for Reporting Services unterstützt Verschlüsselung beim Exportieren von Excel-Dateien. Es unterstützt drei Verschlüsselungstypen:

- XOR
- SCHWACHE VERSCHLÜSSELUNG
- Microsoft Strong Cryptographic Provider
### **Informationen konfigurieren**
Es gibt Konfigurationsinformationen für die Verschlüsselung in der **Aspose.Cells.ReportingServices.xml**-Datei. Wenn der Wert von Verschlüsselung auf "aus" gesetzt ist, schaltet Aspose.Cells.ReportingServices die Verschlüsselung aus.

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

Wenn die Verschlüsselung auf "an" gesetzt ist, schaltet Aspose.Cells.ReportingServices die Verschlüsselung ein.

{{< highlight java >}}

 <Encryption value="on">

{{< /highlight >}}

Im Verschlüsselungsbereich gibt es vier Parameter: ReportName, Passwort, Verschlüsselungstyp und Schlüssellänge.

- ReportName – Legt den Bericht fest, für den Verschlüsselungseinstellungen erforderlich sind. Ein Bericht verwendet dieselbe Verschlüsselungsmethode, wenn der Parameter leer ist.
- Passwort – Legt das Passwort fest. Es darf nicht leer gelassen werden.
- Verschlüsselungstyp – Legt den Verschlüsselungstyp fest. Er darf nicht leer gelassen werden.
- Schlüssellänge – Legt die Schlüssellänge fest. Sie darf nicht leer gelassen werden. 

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
