---
title: Digitale Signaturen
type: docs
weight: 50
url: /de/reportingservices/digital-signatures/
---
 Aspose.Cells for Reporting Services unterstützt digitale Signaturen beim Export von Microsoft Excel 2007-Dateien oder ODS-Dateien. Wir haben einige Konfigurationsinformationen für digitale Signaturen, die in eingestellt werden können**Aspose.Cells.ReportingServices.xml** Datei.

 Wenn der Wert von DigitalSignature ist**aus**, Aspose.Cells for Reporting Services schaltet digitale Signaturen aus.

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

 Wenn der Wert von DigitalSignature ist**an**, Aspose.Cells for Reporting Services schaltet digitale Signaturen ein.

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
