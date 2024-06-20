---
title: Supporto per le Firme Digitali
type: docs
weight: 70
url: /it/reportingservices/support-for-digital-signatures/
---

{{% alert color="primary" %}} 

Una firma digitale fornisce l'assicurazione che un foglio di calcolo sia valido e che nessuno lo abbia alterato. Allegare una firma digitale è simile a sigillare una busta. Se una busta arriva sigillata, hai un certo livello di assicurazione che nessuno abbia manomesso i suoi contenuti. 

Puoi creare una firma digitale personale utilizzando il Microsoft Selfcert.exe o qualsiasi altro strumento, oppure puoi acquistare una firma digitale. Per firmare un foglio di calcolo, allega una firma ai tuoi report una volta creata una firma digitale. 

Aspose.Cells for Reporting Services supporta le firme digitali. 

{{% /alert %}} 
### **Lavorare con le Firme Digitali**
#### **Formati Excel supportati per le Firme Digitali**
Aspose.Cells for Reporting Services supporta le firme digitali quando si esporta in formato file Excel 2007 e ODS.
#### **Configurazione delle firme digitali**
The **Aspose.Cells.ReportingServices.xml** file holds the configuration information and text of a digital signature in the <DigitalSignature> tag:

- Quando DigitalSignature è impostato su off, Aspose.Cells for Reporting Services disattiva la funzionalità della firma digitale.
  Per esempio: 

{{< highlight java >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- Quando il valore di DigitalSignature è attivo, Aspose.Cells.ReportingServices attiva la funzionalità della firma digitale.
  Per esempio: 

{{< highlight java >}}

 <DigitalSignature value="on">

{{< /highlight >}}

Ci sono quattro parametri nella sezione DigitalSignature. Questi sono : 

- nome – Punti a un report che richiede una firma digitale. Il report utilizza un file PFX per la firma digitale quando il parametro è vuoto.
- pfxFilename – Punti al file PFX. Il nome file deve essere un nome completo. Non può essere impostato su un valore vuoto.
- pfxPwd – Imposta la password. Non può essere lasciato vuoto.
- scopo – Spiega lo scopo della firma. Può essere vuoto.
  Per esempio: 

{{< highlight java >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
