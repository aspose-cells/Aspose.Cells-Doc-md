---
title: Digitale Signaturen
type: docs
weight: 50
url: /de/reportingservices/digital-signatures/
---
 Aspose.Cells für Reporting Services unterstützt digitale Signaturen beim Exportieren von Microsoft Excel 2007-Dateien oder ODS-Dateien. Wir haben einige Konfigurationsinformationen für digitale Signaturen, die in eingestellt werden können**Aspose.Cells.ReportingServices.xml** Datei.

 Wenn der Wert von DigitalSignature ist**aus**, Aspose.Cells für Reporting Services deaktiviert digitale Signaturen.

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

 Wenn der Wert von DigitalSignature ist**an**, Aspose.Cells für Reporting Services aktiviert digitale Signaturen.

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 Es gibt vier Parameter im Abschnitt DigitalSignature. Diese sind:

- **Name**stellt einen Bericht dar, der eine digitale Signatur benötigt. Wenn der Parameter leer gelassen wird, verwenden Berichte eine PFX-Datei für digitale Signaturen.
- **pfxDateiname**: bezieht sich auf eine PFX-Datei. Der Dateiname sollte ein vollständig qualifizierter Dateiname sein, komplett mit Pfad und Dateierweiterung. Darf nicht leer sein.
- **pfxPwd**: Legt das Passwort fest. Darf nicht leer sein.
- **Zweck**: eine Beschreibung dessen, wofür die Signatur steht. Kann leer sein.

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
