---
title: Disabilitare il verificatore di compatibilità in Excel
type: docs
weight: 170
url: /it/python-net/disable-compatibility-checker-in-excel/
description: Questo articolo mostra come disabilitare il verificatore di compatibilità attraverso l API Aspose.Cells for Python via .NET.
keywords: Python Disabilita il Verificatore di Compatibilità, Excel Disabilita il Verificatore di Compatibilità in C#, Disabilitare il Verificatore di Compatibilità in Workbook. 
---

## Disabilitare il Verificatore di Compatibilità nei Fogli di Lavoro Excel in Python 

{{% alert color="primary" %}}

Il controllo di compatibilità di Microsoft Excel segnala quando il salvataggio di un file in un formato precedente potrebbe causare problemi di funzionalità o perdita di fedeltà. Il Controllo di compatibilità è una funzionalità di Microsoft Office Excel 2007 e Microsoft Excel 2010.

Quando si salva una cartella di lavoro in una versione precedente, da Excel 2007 o Excel 2010 a Excel 97 attraverso Excel 2003, il Verificatore di Compatibilità analizza la cartella di lavoro per vedere se contiene funzionalità non supportate dalla versione precedente. Per aiutarti a prendere decisioni su come gestire problemi di compatibilità, il Verificatore di Compatibilità visualizza finestre di dialogo con opzioni. Può anche essere utilizzato per creare un rapporto su eventuali problemi nella cartella di lavoro, o disabilitare la funzione.

A volte, è necessario disabilitare il Verificatore di Compatibilità per un particolare foglio di calcolo. Con l'API Aspose.Cells for Python via .NET puoi farlo programmaticamente in modo che gli utenti non si frustrino o si confondano con la finestra di dialogo del Verificatore di Compatibilità che appare quando rieseguono manualmente il salvataggio del file in Microsoft Excel.

{{% /alert %}}

## **Come disabilitare il Controllo di compatibilità utilizzando Microsoft Excel**

Per disabilitare il Verificatore di compatibilità in Microsoft Excel (ad esempio Microsoft Excel 2007/2010):

- (Excel 2007) Fare clic sul pulsante Office, quindi su **Prepara**, poi su **Esegui controllo compatibilità**, e infine deselezionare l'opzione **Esegui controllo compatibilità al salvataggio di questo foglio di lavoro**.
- (Excel 2010) Nella scheda File, fare clic su **Informazioni**, quindi su **Verifica problemi**, fare clic su **Verifica compatibilità** e, infine, deselezionare l'opzione **Verifica compatibilità quando si salva questa cartella di lavoro**.

## **Come disabilitare il Controllo di compatibilità utilizzando le API di Aspose.Cells**

Impostare la proprietà [**Workbook.settings.check_compatibility**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_compatibility) su **False** per disabilitare il Verificatore di compatibilità di Microsoft Excel.

### **Esempi di codice**

Gli esempi di codice che seguono mostrano come disabilitare il Verificatore di Compatibilità con Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-DisableCompatibilityChecker-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
