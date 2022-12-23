---
title: Gestisci fogli di lavoro
linktitle: Fogli di lavoro
type: docs
weight: 60
url: /it/java/manage-worksheets/
---
{{% alert color="primary" %}}

Gli sviluppatori possono facilmente creare e gestire i fogli di lavoro nei propri file Excel a livello di codice usando il flessibile API di Aspose.Cells. In questo argomento verranno illustrati alcuni approcci per aggiungere e rimuovere fogli di lavoro nei file Excel.

{{% /alert %}}

Gestire i fogli di lavoro utilizzando Aspose.Cells è facile come l'ABC. In questa sezione, descriveremo come possiamo:

1. Crea un nuovo file Excel da zero e aggiungi un foglio di lavoro
1. Aggiungi fogli di lavoro ai fogli di lavoro del designer
1. Accesso ai fogli di lavoro utilizzando il nome del foglio
1. Rimuovi un foglio di lavoro da un file Excel usando il nome del foglio
1. Rimuovi un foglio di lavoro da un file Excel utilizzando il relativo indice del foglio

 Aspose.Cells offre un corso,[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) che rappresenta un file Excel.[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) la classe contiene un[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)che consente l'accesso a ciascun foglio di lavoro nel file Excel.

 Un foglio di lavoro è rappresentato da[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classe.[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)class fornisce un'ampia gamma di proprietà e metodi per gestire un foglio di lavoro. Vediamo come possiamo utilizzare questi set base di API.

## **Aggiunta di fogli di lavoro a un nuovo file Excel**

 Per creare un nuovo file Excel a livello di codice, gli sviluppatori dovrebbero creare un oggetto di[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe che rappresenta un file Excel. Quindi gli sviluppatori possono chiamare[**Inserisci**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) metodo del[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . Quando chiamiamo[**Inserisci**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ), un foglio di lavoro vuoto viene aggiunto automaticamente al file Excel, a cui è possibile fare riferimento passando l'indice del foglio di lavoro appena aggiunto al[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . Dopo aver ottenuto il riferimento al foglio di lavoro, gli sviluppatori possono lavorare sui propri fogli di lavoro in base alle proprie esigenze. Al termine del lavoro sui fogli di lavoro, gli sviluppatori possono salvare il file Excel appena creato con nuovi fogli di lavoro chiamando il file[**Salva**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) metodo del[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)classe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Aggiunta di fogli di lavoro a un foglio di calcolo di Designer**

Il processo di aggiunta di fogli di lavoro a un foglio di calcolo del designer è del tutto uguale a quello dell'approccio precedente, tranne per il fatto che il file Excel è già stato creato e dobbiamo prima aprire quel file Excel prima di aggiungervi un foglio di lavoro. Un foglio di calcolo del designer può essere aperto passando il percorso del file o il flusso durante l'inizializzazione del file[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)classe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Accesso ai fogli di lavoro utilizzando il nome del foglio**

Gli sviluppatori possono accedere o ottenere qualsiasi foglio di lavoro specificandone il nome o l'indice.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Rimozione di fogli di lavoro utilizzando il nome del foglio**

 A volte, gli sviluppatori potrebbero dover rimuovere i fogli di lavoro dai file Excel esistenti e tale attività può essere eseguita chiamando il[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String) ) metodo del[**Raccolta di fogli di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) collezione. Possiamo passare il nome del foglio al file[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) metodo per rimuovere un foglio di lavoro specifico.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Rimozione di fogli di lavoro utilizzando l'indice dei fogli**

L'approccio sopra descritto per la rimozione dei fogli di lavoro funziona bene se gli sviluppatori conoscono già i nomi dei fogli di lavoro da eliminare. Ma cosa succede se non si conosce il nome del foglio di lavoro che si desidera rimuovere dal file Excel?

 Bene, in tali circostanze, gli sviluppatori possono utilizzare una versione sovraccaricata di[**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)che accetta l'indice del foglio di lavoro invece del nome del foglio.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Argomenti avanzati**
- [Attivazione di fogli e attivazione di un Cell nel foglio di lavoro](/cells/it/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Copia e sposta i fogli di lavoro all'interno e tra le cartelle di lavoro](/cells/it/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Copiare e spostare fogli di lavoro](/cells/it/java/copying-and-moving-worksheets/)
- [Contare il numero di celle nel foglio di lavoro](/cells/it/java/count-number-of-cells-in-the-worksheet/)
- [Rilevamento di fogli di lavoro vuoti](/cells/it/java/detecting-empty-worksheets/)
- [Trova se il foglio di lavoro è Foglio di dialogo](/cells/it/java/find-if-the-worksheet-is-dialog-sheet/)
- [Ottieni l'ID univoco del foglio di lavoro](/cells/it/java/get-worksheet-unique-id/)
- [Inserisci un'immagine di sfondo in Excel](/cells/it/java/insert-background-image-to-excel/)
- [Crea, manipola o rimuovi scenari dai fogli di lavoro](/cells/it/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Gestione delle interruzioni di pagina](/cells/it/java/managing-page-breaks/)
- [Funzioni di impostazione della pagina](/cells/it/java/page-setup-features/)
- [Aggiorna i riferimenti in altri fogli di lavoro eliminando colonne e righe vuote in un foglio di lavoro](/cells/it/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Utilizza la proprietà Sheet.SheetId di OpenXml utilizzando Aspose.Cells](/cells/it/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Lavorare con lo sfondo nei file ODS](/cells/it/java/working-with-background-in-ods-files/)
- [Viste del foglio di lavoro](/cells/it/java/worksheet-views/)
