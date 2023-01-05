---
title: Supporto per le firme digitali
type: docs
weight: 70
url: /it/reportingservices/support-for-digital-signatures/
---
{{% alert color="primary" %}} 

Una firma digitale garantisce che una cartella di lavoro sia valida e che nessuno l'abbia modificata. Allegare una firma digitale è simile a sigillare una busta. Se una busta arriva sigillata, hai un certo livello di sicurezza che nessuno ha manomesso il suo contenuto.

 Puoi creare una firma digitale personale utilizzando Microsoft Selfcert.exe o qualsiasi altro strumento, oppure puoi acquistare una firma digitale. Per firmare un foglio di calcolo, allegare una firma alle cartelle di lavoro dopo aver creato una firma digitale.

 Aspose.Cells for Reporting Services supporta le firme digitali.

{{% /alert %}} 
### **Lavorare con le firme digitali**
#### **Formati Excel supportati per le firme digitali**
Aspose.Cells for Reporting Services supporta le firme digitali durante l'esportazione nei formati di file Excel 2007 e ODS.
#### **Configurazione delle firme digitali**
 Il**Aspose.Cells.ReportingServices.xml** contiene le informazioni di configurazione e il testo di una firma digitale nel formato<DigitalSignature> etichetta:

- Quando DigitalSignature è disattivato, Aspose.Cells for Reporting Services disattiva la funzionalità di firma digitale.
Per esempio:

{{< highlight "java" >}}

 <DigitalSignature value="off">

<report name="" pfxFilename="" pfxPwd="" purpose=""/>

</DigitalSignature>

{{< /highlight >}}

- Quando il valore di DigitalSignature è attivo, Aspose.Cells.ReportingServices attiva la funzionalità della firma digitale.
Per esempio:

{{< highlight "java" >}}

 <DigitalSignature value="on">

{{< /highlight >}}

 Ci sono quattro parametri nella sezione Firma Digitale. Questi sono :

- name – Indica un report che necessita di una firma digitale. Il report utilizza un file PFX per la firma digitale quando il parametro è vuoto.
- pfxFilename – Punta al file PFX. Il nome file deve essere un nome file completo. Non può essere impostato su un valore vuoto.
- pfxPwd – Imposta la password. Non può essere lasciato vuoto.
- scopo – Spiega lo scopo della firma. Può essere vuoto.
Per esempio:

{{< highlight "java" >}}

 <DigitalSignature value="on">

<report name="TestReport" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

<report name="" pfxFilename="c:\MyKey.pfx" pfxPwd="tryto" purpose="test digital signature"/>

</DigitalSignature>

{{< /highlight >}}
