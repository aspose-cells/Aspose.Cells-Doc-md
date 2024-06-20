---
title: Digitale Signaturen
type: docs
weight: 50
url: /de/reportingservices/digital-signatures/
---

Aspose.Cells for Reporting Services unterstützt digitale Signaturen beim Export von Microsoft Excel 2007-Dateien oder ODS-Dateien. Wir haben einige Konfigurationsinformationen für digitale Signaturen, die in der **Aspose.Cells.ReportingServices.xml**-Datei festgelegt werden können.

Wenn der Wert von DigitalSignature auf **aus** steht, schaltet Aspose.Cells for Reporting Services die digitale Signatur aus.

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

Wenn der Wert von DigitalSignature auf **an** steht, schaltet Aspose.Cells for Reporting Services digitale Signaturen ein.

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Es gibt vier Parameter im Abschnitt DigitalSignature. Diese sind: 

- **name**: repräsentiert einen Bericht, der eine digitale Signatur benötigt. Wenn der Parameter leer gelassen wird, verwenden Berichte eine PFX-Datei für digitale Signaturen.
- **pfxFilename**: bezieht sich auf eine PFX-Datei. Der Dateiname sollte ein vollqualifizierter Dateiname sein, komplett mit Pfad und Dateierweiterung. Darf nicht leer sein.
- **pfxPwd**: setzt das Passwort. Darf nicht leer sein.
- **purpose**: eine Beschreibung, wofür die Signatur gedacht ist. Kann leer sein.

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
