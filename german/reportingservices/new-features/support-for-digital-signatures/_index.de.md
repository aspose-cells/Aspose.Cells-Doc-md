---
title: Unterstützung für digitale Signaturen
type: docs
weight: 70
url: /de/reportingservices/support-for-digital-signatures/
---
{{% alert color="primary" %}} 

 Eine digitale Signatur stellt sicher, dass eine Arbeitsmappe gültig ist und niemand sie geändert hat. Das Anhängen einer digitalen Signatur ähnelt dem Verschließen eines Umschlags. Wenn ein Umschlag versiegelt ankommt, haben Sie ein gewisses Maß an Sicherheit, dass niemand seinen Inhalt manipuliert hat.

 Sie können eine persönliche digitale Signatur mit Microsoft Selfcert.exe oder einem anderen Tool erstellen oder eine digitale Signatur erwerben. Um eine Tabelle zu signieren, hängen Sie eine Signatur an Ihre Arbeitsmappen an, nachdem Sie eine digitale Signatur erstellt haben.

 Aspose.Cells für Reporting Services unterstützt digitale Signaturen.

{{% /alert %}} 
### **Arbeiten mit digitalen Signaturen**
#### **Unterstützte Excel-Formate für digitale Signaturen**
Aspose.Cells für Reporting Services unterstützt digitale Signaturen beim Exportieren in Excel 2007- und ODS-Dateiformate.
#### **Konfigurieren digitaler Signaturen**
 Das**Aspose.Cells.ReportingServices.xml** enthält die Konfigurationsinformationen und den Text einer digitalen Signatur in der<DigitalSignature> Schild:

- Wenn DigitalSignature deaktiviert ist, deaktiviert Aspose.Cells für Reporting Services die digitale Signaturfunktion.
 Zum Beispiel:

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- Wenn der Wert von DigitalSignature aktiviert ist, aktiviert Aspose.Cells.ReportingServices die Funktionalität der digitalen Signatur.
 Zum Beispiel:

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 Es gibt vier Parameter im Abschnitt DigitalSignature. Diese sind :

- name – Verweist auf einen Bericht, der eine digitale Signatur benötigt. Der Bericht verwendet eine PFX-Datei für die digitale Signatur, wenn der Parameter leer ist.
- pfxFilename – Zeigt auf die PFX-Datei. Der Dateiname muss ein vollständiger Dateiname sein. Es kann nicht auf einen leeren Wert gesetzt werden.
- pfxPwd – Legt das Passwort fest. Es darf nicht leer bleiben.
- Zweck – Erklärt den Zweck der Signatur. Es kann leer sein.
 Zum Beispiel:

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
