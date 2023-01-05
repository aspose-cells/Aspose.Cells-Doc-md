---
title: Stöd för digitala signaturer
type: docs
weight: 70
url: /sv/reportingservices/support-for-digital-signatures/
---
{{% alert color="primary" %}} 

En digital signatur ger en garanti för att en arbetsbok är giltig och att ingen har ändrat den. Att fästa en digital signatur liknar att försegla ett kuvert. Om ett kuvert kommer förseglat har du en viss grad av säkerhet att ingen har manipulerat dess innehåll.

 Du kan skapa en personlig digital signatur genom att använda Microsoft Selfcert.exe eller något annat verktyg, eller så kan du köpa en digital signatur. För att signera ett kalkylblad, bifoga en signatur till dina arbetsböcker när du har skapat en digital signatur.

 Aspose.Cells for Reporting Services stöder digitala signaturer.

{{% /alert %}} 
### **Arbeta med digitala signaturer**
#### **Excel-format som stöds för digitala signaturer**
Aspose.Cells for Reporting Services stöder digitala signaturer vid export till Excel 2007 och ODS filformat.
#### **Konfigurera digitala signaturer**
 De**Aspose.Cells.ReportingServices.xml** filen innehåller konfigurationsinformationen och texten för en digital signatur i<DigitalSignature> märka:

- När DigitalSignature är avstängd stänger Aspose.Cells for Reporting Services av den digitala signaturfunktionen.
Till exempel:

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- När värdet för DigitalSignature är aktiverat, aktiverar Aspose.Cells.ReportingServices funktionaliteten för digital signatur.
Till exempel:

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 Det finns fyra parametrar i avsnittet DigitalSignatur. Dessa är :

- namn – Pekar på en rapport som behöver en digital signatur. Rapporten använder en PFX-fil för digital signatur när parametern är tom.
- pfxFilename – Pekar på PFX-filen. Filnamnet måste vara ett fullständigt filnamn. Det kan inte ställas in på ett tomt värde.
- pfxPwd – Ställer in lösenordet. Det kan inte lämnas tomt.
- syfte – Förklarar signaturens syfte. Det kan vara tomt.
Till exempel:

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
