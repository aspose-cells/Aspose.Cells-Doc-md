---
title: Gestire i Fogli di Lavoro
linktitle: Fogli di lavoro
type: docs
weight: 60
url: /it/java/manage-worksheets/
---

{{% alert color="primary" %}}

Gli sviluppatori possono facilmente creare e gestire i fogli di lavoro nei loro file Excel in modo programmato utilizzando la flessibile API di Aspose.Cells. In questo argomento, discuteremo alcuni approcci per aggiungere e rimuovere eventuali fogli di lavoro nei file Excel.

{{% /alert %}}

Gestire i fogli di lavoro utilizzando Aspose.Cells è facile come ABC. In questa sezione, descriveremo come possiamo:

1. Creare un nuovo file Excel da zero e aggiungere un foglio di lavoro ad esso
1. Aggiungere fogli di lavoro ai fogli di progettazione
1. Accesso ai fogli di lavoro utilizzando il nome del foglio
1. Rimuovere un foglio di lavoro da un file Excel utilizzando il suo nome del foglio
1. Rimuovere un foglio di lavoro da un file Excel utilizzando il suo indice del foglio

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contiene un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) che consente l'accesso a ciascun foglio di lavoro nel file Excel.

Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fornisce una vasta gamma di proprietà e metodi per gestire un foglio di lavoro. Vediamo come possiamo utilizzare questi semplici set di API.

## **Aggiungere fogli di lavoro a un nuovo file Excel**

Per creare un nuovo file Excel tramite programmazione, gli sviluppatori devono creare un oggetto della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel. Quindi gli sviluppatori possono chiamare il metodo [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--) della classe [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). Quando chiamiamo il metodo [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--), viene aggiunto automaticamente un foglio di lavoro vuoto al file Excel, che può essere referenziato passando l'indice del foglio appena aggiunto al [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). Dopo aver ottenuto il riferimento al foglio di lavoro, gli sviluppatori possono lavorare sui fogli di lavoro secondo le proprie esigenze. Dopo aver lavorato sui fogli di lavoro, gli sviluppatori possono salvare il nuovo file Excel con i nuovi fogli di lavoro chiamando il metodo [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Aggiunta di fogli di lavoro a un foglio di lavoro progettato**

Il processo di aggiunta di fogli di lavoro a un foglio di calcolo designer è del tutto simile a quello dell'approccio sopra, tranne che il file Excel è già creato e occorre aprirlo prima di aggiungere un foglio di lavoro. Un foglio di calcolo designer può essere aperto passando il percorso del file o il flusso durante l'inizializzazione della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Accesso ai fogli di lavoro utilizzando il nome del foglio**

Gli sviluppatori possono accedere o ottenere qualsiasi foglio di lavoro specificando il suo nome o indice.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Rimozione dei fogli di lavoro utilizzando il nome del foglio**

A volte, gli sviluppatori possono avere la necessità di rimuovere fogli di lavoro da file Excel esistenti e tale operazione può essere eseguita chiamando il metodo [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) della collezione [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). Possiamo passare il nome del foglio al metodo [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) per rimuovere un foglio di lavoro specifico.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Rimozione dei fogli di lavoro utilizzando l'indice del foglio**

L'approccio precedente alla rimozione dei fogli di lavoro funziona bene se gli sviluppatori conoscono già i nomi dei fogli di lavoro da eliminare. Ma, cosa fare se non si conosce il nome del foglio di lavoro che si desidera rimuovere dal proprio file Excel?

Bene, in tali circostanze, gli sviluppatori possono utilizzare una versione sovraccaricata del metodo [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)) che prende l'indice del foglio di lavoro invece del suo nome del foglio.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Argomenti avanzati**
- [Attivazione dei fogli e attivazione di una cella nel foglio di lavoro](/cells/it/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Copia e Sposta fogli di lavoro all'interno e tra i cartelle di lavoro](/cells/it/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Copia e Sposta Fogli di Lavoro](/cells/it/java/copying-and-moving-worksheets/)
- [Contare il numero di celle nel foglio di lavoro](/cells/it/java/count-number-of-cells-in-the-worksheet/)
- [Rilevamento di fogli di lavoro vuoti](/cells/it/java/detecting-empty-worksheets/)
- [Trova se il foglio di lavoro è un foglio di dialogo](/cells/it/java/find-if-the-worksheet-is-dialog-sheet/)
- [Ottieni l'ID univoco del foglio di lavoro](/cells/it/java/get-worksheet-unique-id/)
- [Inserisci immagine di sfondo in Excel](/cells/it/java/insert-background-image-to-excel/)
- [Creare, Manipolare o Rimuovere scenari dai fogli di lavoro](/cells/it/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestione interruzioni di pagina](/cells/it/java/managing-page-breaks/)
- [Funzionalità Impostazioni pagina](/cells/it/java/page-setup-features/)
- [Aggiorna i riferimenti in altri fogli di lavoro mentre elimini colonne e righe vuote in un foglio di lavoro](/cells/it/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Utilizza la proprietà Sheet.SheetId di OpenXml utilizzando Aspose.Cells](/cells/it/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Lavorare con lo sfondo nei file ODS](/cells/it/java/working-with-background-in-ods-files/)
- [Visualizzazioni del foglio di lavoro](/cells/it/java/worksheet-views/)
