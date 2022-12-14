---
title: Salvataggio di file Excel in CSV, PDF e altri formati
linktitle: Salva file
type: docs
weight: 20
url: /it/java/saving-excel-files-to-csv-pdf-and-other-formats/
---
{{% alert color="primary" %}}

**Aspose.Cells**consente agli sviluppatori di creare file Excel da zero utilizzando il suo flessibile API. Una volta creati i file Excel, dovrai anche salvare la tua cartella di lavoro (file). Aspose.Cells fornisce una varietà di modi per salvare questi file. In questo argomento tratteremo tutti quei possibili modi che possono essere adottati dagli sviluppatori per salvare i propri file.

{{% /alert %}}

## **Diversi modi per salvare i tuoi file**

 Aspose.Cells API fornisce una classe denominata[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)che rappresenta un file Excel e fornisce tutte le proprietà e i metodi necessari di cui gli sviluppatori potrebbero aver bisogno per lavorare con i propri file Excel. Il[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la classe fornisce a[**Salva**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) metodo utilizzato per salvare i file Excel. Il[**Salva**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) ha molti overload che vengono utilizzati per salvare i file Excel in modi diversi.

 Gli sviluppatori possono anche specificare il formato di file in cui devono essere salvati i loro file. I file possono essere salvati in diversi formati come XLS, SpreadsheetML, CSV, delimitato da tabulazioni, valori separati da tabulazioni TSV, XPS e molti altri. Questi formati di file vengono specificati utilizzando l'estensione[**SalvaFormato**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) enumerazione.

[**SalvaFormato**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)enumeration contiene molti formati di file predefiniti (che possono essere scelti dall'utente) come segue:

|**Tipi di formati di file**|**Descrizione**|
|:- |:- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API tenta di rilevare il formato appropriato dall'estensione file specificata nel primo parametro al metodo di salvataggio|
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Rappresenta un file CSV|
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Rappresenta un file Office Open XML SpreadsheetML|
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Rappresenta il file XLSM basato su XML|
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Rappresenta un file modello di Excel|
|[**XL™**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Rappresenta un file modello abilitato per le macro di Excel|
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Rappresenta un file XLAM di Excel|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Rappresenta un file di valori separati da tabulazioni|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Rappresenta un file di testo delimitato da tabulazioni|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Rappresenta uno o più file HTML|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Rappresenta uno o più file MHTML|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Rappresenta un file OpenDocument Spreadsheet|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Rappresenta un file XLS che è il formato predefinito per le revisioni di Excel da 1997 a 2003|
|[**FOGLIO DI CALCOLO_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Rappresenta un file SpreadSheetML|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Rappresenta un file XLSB binario di Excel 2007|
|[**SCONOSCIUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Rappresenta un formato non riconosciuto, non può essere salvato.|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Rappresenta un documento PDF|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Rappresenta un file XML Paper Specification (XPS).|
|[**TIPO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Rappresenta un file TIFF (Tagged Image File Format).|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Rappresenta un file SVG (Scalable Vector Graphics) basato su XML|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Rappresenta il formato di interscambio dati.|
|[**NUMERI**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Rappresenta un file di numeri.|
|[**RITARDO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Rappresenta un documento markdown.|
**Normalmente, ci sono due modi per salvare i file Excel come segue:**

1. **Salvataggio del file in una posizione**
1. **Salvataggio del file in un flusso**

## **Salvataggio del file in una posizione**

 Se gli sviluppatori devono salvare i propri file in una posizione di archiviazione, possono semplicemente specificare il nome del file (con il relativo percorso di archiviazione completo) e il formato del file desiderato (utilizzando il[**SalvaFormato**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) enumerazione) mentre si chiama il[**Salva**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) metodo di[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)oggetto.

**Esempio:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Salvataggio della cartella di lavoro in formato testo o CSV**

A volte, vuoi convertire o salvare una cartella di lavoro con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV ecc.), per impostazione predefinita sia Microsoft Excel che Aspose.Cells salvano solo il contenuto del foglio di lavoro attivo.

L'esempio di codice seguente spiega come salvare un'intera cartella di lavoro in formato testo. Carica la cartella di lavoro di origine che potrebbe essere qualsiasi file di foglio di calcolo Excel o OpenOffice Microsoft (quindi XLS, XLSX, XLSM, XLSB, ODS e così via) con qualsiasi numero di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli nella cartella di lavoro in formato TXT.

 Puoi modificare lo stesso esempio per salvare il tuo file in formato CSV. Per impostazione predefinita,[**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) è una virgola, quindi non specificare un separatore se si salva in formato CSV.

**Esempio:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Salvataggio di file di testo con separatore personalizzato**

I file di testo contengono dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati tra i suoi dati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Salvataggio di file in un flusso**

 Se gli sviluppatori devono salvare i propri file in un file**Flusso** quindi dovrebbero creare un file**FileOutputStream** oggetto e quindi salvare il file in quello**Flusso** oggetto chiamando il[**Salva**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) metodo di[**Cartella di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)oggetto. Gli sviluppatori possono anche specificare il formato di file desiderato (utilizzando l'estensione[**SalvaFormato**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) enumerazione) mentre si chiama il[**Salva**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) metodo.

**Esempio:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Salvataggio del file in un altro formato**

### **File XLS**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **File XLSX**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **File PDF**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Imposta l'opzione ContentCopyForAccessibility**

 Con il[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) class, è possibile ottenere o impostare il PDF[**Accessibilità Estrai contenuto**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) opzione per controllare l'accesso al contenuto nel PDF convertito. Significa che consente al software di lettura dello schermo di utilizzare il testo all'interno del file PDF per leggere il file PDF. Puoi disabilitarlo applicando una password di modifica dei permessi e deselezionando i due elementi nello screenshot[qui](71630877.png).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Esporta le proprietà personalizzate in PDF**

Con il[**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions) class, è possibile esportare le proprietà personalizzate nella cartella di lavoro di origine nel PDF.[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport)enumeratore viene fornito per specificare il modo in cui le proprietà vengono esportate. Queste proprietà possono essere osservate in Adobe Acrobat Reader facendo clic su File e quindi sull'opzione proprietà come mostrato nell'immagine seguente. È possibile scaricare il file modello "sourceWithCustProps.xlsx".[qui](sourceWithCustProps.xlsx)per il test e l'output è disponibile il file PDF "outSourceWithCustProps".[qui](outSourceWithCustProps.pdf)per analisi.

![cose da fare:immagine_alt_testo](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Converti la cartella di lavoro di Excel in Markdown**

Il Aspose.Cells API fornisce supporto per l'esportazione di fogli di calcolo in formato Markdown. Per esportare il foglio di lavoro attivo in Markdown, passare[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)come secondo parametro di[**Cartella di lavoro.Salva**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)) metodo. Puoi anche usare[**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions)class per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in Markdown.

L'esempio di codice seguente illustra l'esportazione del foglio di lavoro attivo in Markdown utilizzando[**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)membro di enumerazione. Si prega di consultare il[output file Markdown](Book1.txt)generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Argomenti avanzati**
- [Regola il livello di compressione della cartella di lavoro](/cells/it/java/adjust-workbook-compression-level/)
- [Conversione della cartella di lavoro in diversi formati](/cells/it/java/converting-workbook-to-different-formats/)
- [Salva cartella di lavoro in formato foglio di calcolo XML aperto rigoroso](/cells/it/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Tieni traccia dell'avanzamento della conversione di Excel in TIFF](/cells/it/java/track-conversion-progress-of-excel-to-tiff/)
- [Tieni traccia dell'avanzamento della conversione del documento](/cells/it/java/track-document-conversion-progress/)
