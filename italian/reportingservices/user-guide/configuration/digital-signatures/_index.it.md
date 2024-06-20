---
title: Firme digitali
type: docs
weight: 50
url: /it/reportingservices/digital-signatures/
---

Aspose.Cells for Reporting Services supporta firme digitali durante l'esportazione di file Microsoft Excel 2007 o file ODS. Abbiamo alcune informazioni di configurazione per le firme digitali che possono essere impostate nel file **Aspose.Cells.ReportingServices.xml**.

Quando il valore di DigitalSignature è **off**, Aspose.Cells for Reporting Services disattiva le firme digitali.

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

Quando il valore di DigitalSignature è **on**, Aspose.Cells for Reporting Services attiva le firme digitali.

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Ci sono quattro parametri nella sezione DigitalSignature. Questi sono: 

- **nome**: rappresenta un report che necessita di una firma digitale. Quando il parametro è lasciato vuoto, i report utilizzano un file PFX per le firme digitali.
- **pfxFilename**: si riferisce a un file PFX. Il nome del file dovrebbe essere un nome di file completo, completo di percorso ed estensione del file. Non deve essere vuoto.
- **pfxPwd**: imposta la password. Non deve essere vuota.
- **scopo**: una descrizione di ciò per cui è la firma. Può essere vuoto.

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
