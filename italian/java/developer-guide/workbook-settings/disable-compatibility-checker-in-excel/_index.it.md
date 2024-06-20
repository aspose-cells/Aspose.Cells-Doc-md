---
title: Disabilitare il verificatore di compatibilità in Excel
type: docs
weight: 270
url: /it/java/disable-compatibility-checker-in-excel/
---

{{% alert color="primary" %}}

Il verificatore di compatibilità di Microsoft Excel segnala quando si salva un file in un formato di file precedente che il salvataggio del file potrebbe causare problemi di funzionalità o perdita di fedeltà. Il verificatore di compatibilità è una funzionalità di Microsoft Office Excel 2007, 2010 e 2013.

Quando si salva una cartella di lavoro in una versione precedente, da Excel 2007 o Excel 2010 a Excel 97 attraverso Excel 2003, il Verificatore di Compatibilità analizza la cartella di lavoro per vedere se contiene funzionalità non supportate dalla versione precedente. Per aiutarti a prendere decisioni su come gestire problemi di compatibilità, il Verificatore di Compatibilità visualizza finestre di dialogo con opzioni. Può anche essere utilizzato per creare un rapporto su eventuali problemi nella cartella di lavoro, o disabilitare la funzione.

A volte è necessario disabilitare il verificatore di compatibilità per un foglio di calcolo particolare. Con le API di Aspose.Cells è possibile farlo in modo dinamico in modo che gli utenti non siano frustrati o confusi dall'apertura della finestra di dialogo del Verificatore di Compatibilità quando ri-salvano il file in Microsoft Excel manualmente.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per disabilitare il Verificatore di compatibilità in Microsoft Excel (ad esempio Microsoft Excel 2007/2010):

- (Excel 2007) Fare clic sul pulsante Office, quindi su **Prepara**, poi su **Esegui controllo compatibilità**, e infine deselezionare l'opzione **Esegui controllo compatibilità al salvataggio di questo foglio di lavoro**.
- (Excel 2010 e 2013) Sulla scheda File, fare clic su **Informazioni**, quindi su **Ricerca problemi**, fare clic su **Verifica compatibilità**, e infine deselezionare l'opzione **Verifica compatibilità al salvataggio di questo foglio di lavoro**.

## **Utilizzando le API di Aspose.Cells**

Impostare la proprietà [**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) su **False** per disabilitare il Verificatore di compatibilità di Microsoft Excel.

Supponiamo di avere un file XLS di modello. Quando un utente lo salva o lo ri-salva in MS Excel 2007/2010/2013, viene visualizzata la finestra di dialogo del Verificatore di compatibilità, come mostrato nello screenshot sottostante.

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

Il codice seguente mostra come disabilitare il Verificatore di compatibilità con Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
