---
title: Verschlüsselung konfigurieren
type: docs
weight: 40
url: /de/reportingservices/configuring-encryption/
---
{{% alert color="primary" %}} 

 Aspose.Cells for Reporting Services unterstützt Verschlüsselung und Sie können verschlüsselte Microsoft Excel-Dateien rendern.

{{% /alert %}} 
### **Arten der Verschlüsselung**
Aspose.Cells for Reporting Services unterstützt die Verschlüsselung beim Export von Excel-Dateien. Es unterstützt drei Verschlüsselungsarten:

- XOR
- SCHWACHE VERSCHLÜSSELUNG
- Microsoft Starker Kryptografieanbieter
### **Informationen konfigurieren**
 Es gibt Konfigurationsinformationen für die Verschlüsselung in der**Aspose.Cells.ReportingServices.xml** Datei. Wenn der Wert von Encryption auf „off“ gesetzt ist, schaltet Aspose.Cells.ReportingServices die Verschlüsselung aus.

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

Wenn die Verschlüsselung aktiviert ist, aktiviert Aspose.Cells.ReportingServices die Verschlüsselung.

{{< highlight "java" >}}

 <Encryption value="on">

{{< /highlight >}}

Im Abschnitt Encryption gibt es vier Parameter: ReportName, Password, EncryptionType und KeyLength.

- ReportName – Legt den Bericht fest, der Verschlüsselungseinstellungen benötigt. Ein Bericht verwendet dieselbe Verschlüsselungsmethode, wenn der Parameter leer ist.
- Passwort – Legt das Passwort fest. Es darf nicht leer bleiben.
- EncryptionType – Legt den Verschlüsselungstyp fest. Es darf nicht leer bleiben.
-  KeyLength – Legt die Schlüssellänge fest. Es darf nicht leer bleiben.

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
