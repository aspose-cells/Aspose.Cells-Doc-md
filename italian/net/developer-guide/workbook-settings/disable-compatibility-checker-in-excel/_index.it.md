---
title: Disattiva Verifica compatibilità in Excel
type: docs
weight: 170
url: /it/net/disable-compatibility-checker-in-excel/
keywords: c# excel disable compatibility checke
---
## Disattiva Verifica compatibilità nei fogli di lavoro Excel in C#

{{% alert color="primary" %}}

Microsoft I contrassegni di Verifica compatibilità di Excel durante il salvataggio di un file in un formato di file precedente potrebbero causare problemi di funzionalità o perdita di fedeltà. Verifica compatibilità è una funzionalità di Microsoft Office Excel 2007 e Microsoft Excel 2010.

Quando si salva una cartella di lavoro in una versione precedente, da Excel 97 a Excel 2003, da Excel 2007 o Excel 2010, Verifica compatibilità analizza la cartella di lavoro per verificare se contiene funzionalità non supportate dalla versione precedente. Per aiutarti a prendere decisioni su come gestire i problemi di compatibilità, Verifica compatibilità visualizza finestre di dialogo con opzioni. Può anche essere utilizzato per creare un rapporto su eventuali problemi nella cartella di lavoro o disabilitare la funzione.

volte, è necessario disabilitare Verifica compatibilità per un particolare foglio di calcolo. Con le API Aspose.Cells puoi farlo a livello di codice in modo che gli utenti non siano frustrati o confusi dalla finestra di dialogo Verifica compatibilità che si apre quando salvano nuovamente il file in Microsoft Excel manualmente.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per disabilitare Verifica compatibilità in Microsoft Excel (ad esempio Microsoft Excel 2007/2010):

-  (Excel 2007) Sul pulsante Office, fare clic su**Preparare** , poi**Esegui Verifica compatibilità** , quindi deselezionare il file**Verifica la compatibilità quando salvi questa cartella di lavoro** opzione.
-  (Excel 2010) Nella scheda File, fare clic su**Informazioni** , poi**Verifica la presenza di problemi** , fare clic**Verifica compatibilità** e, infine, deselezionare il file**Verifica la compatibilità quando salvi questa cartella di lavoro** opzione.

## **Utilizzo delle API Aspose.Cells**

 Impostare il[**Workbook.Settings.CheckComptiliblity**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) proprietà a**Falso** per disabilitare Microsoft Verifica compatibilità di Excel.

### **Esempi di codice**

Gli esempi di codice che seguono mostrano come disabilitare Verifica compatibilità con Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
