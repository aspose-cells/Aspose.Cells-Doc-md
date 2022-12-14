---
title: Firme digitali
type: docs
weight: 50
url: /it/reportingservices/digital-signatures/
---
 Aspose.Cells per Reporting Services supporta le firme digitali durante l'esportazione di file Microsoft Excel 2007 o file ODS. Abbiamo alcune informazioni di configurazione per le firme digitali che possono essere impostate nel file**Aspose.Cells.ReportingServices.xml** file.

 Quando il valore di DigitalSignature è**spento**, Aspose.Cells per Reporting Services disattiva le firme digitali.

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

 Quando il valore di DigitalSignature è**Su**, Aspose.Cells per Reporting Services attiva le firme digitali.

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 Ci sono quattro parametri nella sezione Firma Digitale. Questi sono:

- **nome**rappresenta un report che necessita di firma digitale. Quando il parametro viene lasciato vuoto, i report utilizzano un file PFX per le firme digitali.
- **pfxNome file**: fa riferimento a un file PFX. Il nome file deve essere un nome file completo, completo di percorso ed estensione file. Non deve essere vuoto.
- **pfxPwd**: imposta la password. Non deve essere vuoto.
- **scopo**: una descrizione dello scopo della firma. Può essere vuoto.

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
