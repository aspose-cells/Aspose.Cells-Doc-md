---
title: Disabilita il controllo compatibilità in Excel
type: docs
weight: 170
url: /it/net/disable-compatibility-checker-in-excel/
description: Questo articolo mostra come disabilitare il controllo compatibilità tramite Aspose.Cells for .NET API.
keywords: C# Disable Compatibility Checker, Excel Disable Compatibility Checker in C#, Disable Compatibility Checker in Workbook. 
---
##  Disabilita il controllo compatibilità nei fogli di lavoro Excel in C#

{{% alert color="primary" %}}

Microsoft I contrassegni del controllo compatibilità di Excel quando si salva un file in un formato di file precedente potrebbero causare problemi di funzionalità o perdita di fedeltà. Verifica compatibilità è una funzionalità di Microsoft Office Excel 2007 e Microsoft Excel 2010.

Quando si salva una cartella di lavoro in una versione precedente, da Excel 97 a Excel 2003, da Excel 2007 o Excel 2010, Verifica compatibilità esegue la scansione della cartella di lavoro per verificare se contiene funzionalità non supportate dalla versione precedente. Per aiutarti a prendere decisioni su come gestire i problemi di compatibilità, Verifica compatibilità visualizza finestre di dialogo con opzioni. Può anche essere utilizzato per creare un report su eventuali problemi nella cartella di lavoro o disabilitare la funzionalità.

A volte è necessario disabilitare la verifica compatibilità per un particolare foglio di calcolo. Con le API Aspose.Cells puoi farlo a livello di codice in modo che gli utenti non si sentano frustrati o confusi dalla finestra di dialogo Verifica compatibilità che appare quando salvano nuovamente il file manualmente in Microsoft Excel.

{{% /alert %}}

##  **Come disabilitare il controllo compatibilità utilizzando Microsoft Excel**

Per disabilitare il controllo compatibilità in Microsoft Excel (ad esempio Microsoft Excel 2007/2010):

-  (Excel 2007) Sul pulsante Office, fare clic su**Prepara**, quindi **Esegui verifica compatibilità** e deseleziona **Verifica compatibilità quando salvi la cartella di lavoro** opzione.
-  (Excel 2010) Nella scheda File, fare clic su**Informazioni**, quindi **Verifica problemi**, fai clic su **Verifica compatibilità** e, infine, deseleziona **Verifica compatibilità quando salvi questa cartella di lavoro** opzione.

##  **Come disabilitare il controllo compatibilità utilizzando le API Aspose.Cells**

 Impostare il[**Workbook.Settings.CheckComptiblity**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) proprietà a**Falso** per disabilitare Microsoft Controllo compatibilità di Excel.

###  **Esempi di codici**

Gli esempi di codice che seguono mostrano come disabilitare il controllo compatibilità con Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
