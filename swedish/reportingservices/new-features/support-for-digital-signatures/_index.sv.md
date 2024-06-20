---
title: Stöd för digitala signaturer
type: docs
weight: 70
url: /sv/reportingservices/support-for-digital-signatures/
---

{{% alert color="primary" %}} 

En digital signatur ger försäkran om att en arbetsbok är giltig och att ingen har ändrat den. Att bifoga en digital signatur är liknande att försegla ett kuvert. Om ett förseglad kuvert anländer har du viss säkerhet om att ingen har manipulerat innehållet. 

Du kan skapa en personlig digital signatur genom att använda Microsoft Selfcert.exe eller något annat verktyg, eller så kan du köpa en digital signatur. För att signera en kalkylblad, bifoga en signatur till dina arbetsböcker när du har skapat en digital signatur. 

Aspose.Cells for Reporting Services stöder digitala signaturer. 

{{% /alert %}} 
### **Arbeta med digitala signaturer**
#### **Stödda Excel-format för digitala signaturer**
Aspose.Cells for Reporting Services stöder digitala signaturer vid export till Excel 2007 och ODS filformat.
#### **Konfigurera digitala signaturer**
The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the <DigitalSignature> tag:

- När DigitalSignature är avstängd, inaktiverar Aspose.Cells for Reporting Services funktionaliteten för digitala signaturer.
  Exempelvis: 

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- När värdet för DigitalSignature är på, aktiverar Aspose.Cells.ReportingServices funktionaliteten för digitala signaturer.
  Exempelvis: 

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Det finns fyra parametrar i avsnittet för DigitalSignature. Dessa är: 

- name – pekar på en rapport som behöver en digital signatur. Rapporten använder en PFX-fil för digital signatur när parametern är tom.
- pfxFilename – pekar på PFX-filen. Filnamnet måste vara ett komplett filnamn. Det kan inte vara inställt på ett tomt värde.
- pfxPwd – Anger lösenordet. Det kan inte lämnas tomt.
- purpose – Förklarar signaturens syfte. Det kan vara tomt.
  Exempelvis: 

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
