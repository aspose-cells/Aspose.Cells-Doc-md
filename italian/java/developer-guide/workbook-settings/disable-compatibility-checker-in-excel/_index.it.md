---
title: Disattiva Verifica compatibilità in Excel
type: docs
weight: 270
url: /it/java/disable-compatibility-checker-in-excel/
---
{{% alert color="primary" %}}

Microsoft Verifica compatibilità di Excel segnala quando si salva un file in un formato di file precedente che il salvataggio del file potrebbe causare problemi di funzionalità o perdita di fedeltà. Verifica compatibilità è una funzionalità di Microsoft Office Excel 2007, 2010 e 2013.

Quando si salva una cartella di lavoro in una versione precedente, da Excel 97 a Excel 2003, da Excel 2007 o Excel 2010, Verifica compatibilità analizza la cartella di lavoro per verificare se contiene funzionalità non supportate dalla versione precedente. Per aiutarti a prendere decisioni su come gestire i problemi di compatibilità, Verifica compatibilità visualizza finestre di dialogo con opzioni. Può anche essere utilizzato per creare un rapporto su eventuali problemi nella cartella di lavoro o disabilitare la funzione.

A volte, è necessario disabilitare Verifica compatibilità per un particolare foglio di calcolo. Con le API Aspose.Cells puoi farlo in modo dinamico in modo che gli utenti non siano frustrati o confusi dalla finestra di dialogo Verifica compatibilità che si apre quando salvano nuovamente il file in Microsoft Excel manualmente.

{{% /alert %}}

## **Utilizzando Microsoft Excel**

Per disabilitare Verifica compatibilità in Microsoft Excel (ad esempio Microsoft Excel 2007/2010):

-  (Excel 2007) Sul pulsante Office, fare clic su**Preparare** , poi**Esegui Verifica compatibilità** , quindi deselezionare il file**Verifica la compatibilità quando salvi questa cartella di lavoro** opzione.
-  (Excel 2010 e 2013) Nella scheda File, fare clic su**Informazioni** , poi**Verifica la presenza di problemi** , fare clic**Verifica compatibilità** e, infine, deselezionare il file**Verifica la compatibilità quando salvi questa cartella di lavoro** opzione.

## **Utilizzo delle API Aspose.Cells**

 Impostare il[**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) proprietà a**Falso** per disabilitare Microsoft Verifica compatibilità di Excel.

Supponiamo di avere un file modello XLS. Quando un utente lo salva o lo salva nuovamente in MS Excel 2007/2010/2013, viene visualizzata la finestra di dialogo Verifica compatibilità, come mostrato nello screenshot seguente.

![cose da fare:immagine_alt_testo](disable-compatibility-checker-in-excel_1.png)

Il codice seguente mostra come disabilitare Verifica compatibilità con Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
