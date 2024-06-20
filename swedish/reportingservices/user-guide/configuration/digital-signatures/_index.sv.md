---
title: Digitala signaturer
type: docs
weight: 50
url: /sv/reportingservices/digital-signatures/
---

Aspose.Cells for Reporting Services stöder digitala signaturer vid export av Microsoft Excel 2007-filer eller ODS-filer. Vi har viss konfigurationsinformation för digitala signaturer som kan ställas in i filen **Aspose.Cells.ReportingServices.xml**.

När värdet av DigitalSignature är **av** stänger Aspose.Cells for Reporting Services av digitala signaturer.

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

När värdet av DigitalSignature är **på** aktiverar Aspose.Cells for Reporting Services digitala signaturer.

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Det finns fyra parametrar i avsnittet DigitalSignature. Dessa är: 

- **namn**: representerar en rapport som behöver en digital signatur. När parametern lämnas blank använder rapporterna en PFX-fil för digitala signaturer.
- **pfxFilename**: hänvisar till en PFX-fil. Filnamnet ska vara ett fullständigt kvalificerat filnamn, komplett med sökväg och filändelse. Får inte vara blank.
- **pfxPwd**: ställer in lösenordet. Får inte vara blank.
- **ändamål**: en beskrivning av vad signaturen används för. Kan vara blank.

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
