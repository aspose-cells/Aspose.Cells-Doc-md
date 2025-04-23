---
title: Disabilitare il verificatore di compatibilità in Excel
type: docs
weight: 170
url: /it/net/disable-compatibility-checker-in-excel/
description: Questo articolo mostra come disabilitare il controllo di compatibilità tramite l API Aspose.Cells for .NET.
keywords: C# Disabilita il controllo di compatibilità, Excel Disabilita il controllo di compatibilità in C#, Disabilita il controllo di compatibilità nella cartella di lavoro. 
---

## Disabilita il controllo di compatibilità nei fogli di lavoro di Excel in C# 

{{% alert color="primary" %}}

Il controllo di compatibilità di Microsoft Excel segnala quando il salvataggio di un file in un formato precedente potrebbe causare problemi di funzionalità o perdita di fedeltà. Il Controllo di compatibilità è una funzionalità di Microsoft Office Excel 2007 e Microsoft Excel 2010.

Quando si salva una cartella di lavoro in una versione precedente, da Excel 2007 o Excel 2010 a Excel 97 attraverso Excel 2003, il Verificatore di Compatibilità analizza la cartella di lavoro per vedere se contiene funzionalità non supportate dalla versione precedente. Per aiutarti a prendere decisioni su come gestire problemi di compatibilità, il Verificatore di Compatibilità visualizza finestre di dialogo con opzioni. Può anche essere utilizzato per creare un rapporto su eventuali problemi nella cartella di lavoro, o disabilitare la funzione.

A volte è necessario disabilitare il Controllo di compatibilità per un determinato foglio di calcolo. Con le API di Aspose.Cells puoi farlo in modo programmatico in modo che gli utenti non si sentano frustrati o confusi dalla comparsa della finestra di dialogo del Controllo di compatibilità quando salvano nuovamente il file in Microsoft Excel manualmente.

{{% /alert %}}

## **Come disabilitare il Controllo di compatibilità utilizzando Microsoft Excel**

Per disabilitare il Verificatore di compatibilità in Microsoft Excel (ad esempio Microsoft Excel 2007/2010):

- (Excel 2007) Fare clic sul pulsante Office, quindi su **Prepara**, poi su **Esegui controllo compatibilità**, e infine deselezionare l'opzione **Esegui controllo compatibilità al salvataggio di questo foglio di lavoro**.
- (Excel 2010) Nella scheda File, fare clic su **Informazioni**, quindi su **Verifica problemi**, fare clic su **Verifica compatibilità** e, infine, deselezionare l'opzione **Verifica compatibilità quando si salva questa cartella di lavoro**.

## **Come disabilitare il Controllo di compatibilità utilizzando le API di Aspose.Cells**

Impostare la proprietà [**Workbook.Settings.CheckComptiliblity**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) su **False** per disabilitare il Verificatore di compatibilità di Microsoft Excel.

### **Esempi di codice**

Gli esempi di codice seguenti mostrano come disabilitare il Controllo di compatibilità con Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
