---
title: Unterstützung für digitale Signaturen
type: docs
weight: 70
url: /de/reportingservices/support-for-digital-signatures/
---

{{% alert color="primary" %}} 

Eine digitale Signatur gewährleistet, dass eine Arbeitsmappe gültig ist und niemand sie verändert hat. Das Anbringen einer digitalen Signatur ist ähnlich wie das Versiegeln eines Umschlags. Wenn ein versiegelter Umschlag ankommt, haben Sie eine gewisse Sicherheit, dass niemand den Inhalt manipuliert hat. 

Sie können eine persönliche digitale Signatur mit dem Microsoft Selfcert.exe oder einem anderen Tool erstellen oder eine digitale Signatur erwerben. Um eine Tabelle zu signieren, fügen Sie Ihren Arbeitsmappen einmal erstellte digitale Signatur hinzu. 

Aspose.Cells for Reporting Services unterstützt digitale Signaturen. 

{{% /alert %}} 
### **Arbeiten mit digitalen Signaturen**
#### **Unterstützte Excel-Formate für digitale Signaturen**
Aspose.Cells for Reporting Services unterstützt digitale Signaturen beim Exportieren in die Formate Excel 2007 und ODS.
#### **Konfigurieren von digitalen Signaturen**
The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the <DigitalSignature> tag:

- Wenn DigitalSignature auf off gesetzt ist, schaltet Aspose.Cells for Reporting Services die Funktion der digitalen Signatur aus.
  Zum Beispiel: 

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- Wenn der Wert von DigitalSignature eingeschaltet ist, aktiviert Aspose.Cells.ReportingServices die Funktion der digitalen Signatur.
  Zum Beispiel: 

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Es gibt vier Parameter im Abschnitt DigitalSignature. Diese sind: 

- Name – Verweist auf einen Bericht, der eine digitale Signatur benötigt. Der Bericht verwendet eine PFX-Datei für die digitale Signatur, wenn der Parameter leer ist.
- pfxDateiname – Verweist auf die PFX-Datei. Der Dateiname muss ein vollständiger Dateiname sein. Er kann nicht auf einen leeren Wert gesetzt werden.
- pfxPwd – Setzt das Passwort. Es darf nicht leer bleiben.
- Zweck – Erläutert den Zweck der Signatur. Er kann leer sein.
  Zum Beispiel: 

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
