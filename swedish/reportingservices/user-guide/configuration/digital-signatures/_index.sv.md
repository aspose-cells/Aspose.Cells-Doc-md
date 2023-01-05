---
title: Digitala signaturer
type: docs
weight: 50
url: /sv/reportingservices/digital-signatures/
---
Aspose.Cells for Reporting Services stöder digitala signaturer vid export av Microsoft Excel 2007-filer eller ODS-filer. Vi har en del konfigurationsinformation för digitala signaturer som kan ställas in i**Aspose.Cells.ReportingServices.xml** fil.

 När värdet på DigitalSignature är**av**, Aspose.Cells for Reporting Services stänger av digitala signaturer.

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

 När värdet på DigitalSignature är**på**, Aspose.Cells for Reporting Services aktiverar digitala signaturer.

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 Det finns fyra parametrar i avsnittet DigitalSignatur. Dessa är:

- **namn**: representerar en rapport som behöver en digital signatur. När parametern lämnas tom använder rapporterna en PFX-fil för digitala signaturer.
- **pfxFilnamn**: refererar till en PFX-fil. Filnamnet ska vara ett fullständigt kvalificerat filnamn, komplett med sökväg och filtillägg. Får inte vara tom.
- **pfxPwd**: ställer in lösenordet. Får inte vara tom.
- **syfte**: en beskrivning av vad signaturen är för. Kan vara tomt.

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
