---
title: Salvataggio di file Excel in CSV, PDF e altri formati
linktitle: Salva file
type: docs
weight: 20
url: /it/java/saving-excel-files-to-csv-pdf-and-other-formats/
---

{{% alert color="primary" %}}

**Aspose.Cells** consente ai programmatori di creare file Excel da zero utilizzando la sua API flessibile. Una volta creati i file Excel, sarà necessario salvare il proprio documento di lavoro (file). Aspose.Cells fornisce una varietà di modi per salvare questi file. In questo argomento, discuteremo tutti quei possibili modi che possono essere adottati dai programmatori per salvare i loro file.

{{% /alert %}}

## **Diversi modi per salvare i tuoi file**

L'API Aspose.Cells fornisce una classe denominata [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) che rappresenta un file Excel e fornisce tutte le proprietà e i metodi necessari che i programmatori possono avere bisogno per lavorare con i propri file Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) fornisce un metodo [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) che viene utilizzato per salvare i file Excel. Il metodo [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) ha molte sovraccariche che vengono utilizzate per salvare i file Excel in modi diversi.

I programmatori possono anche specificare il formato del file in cui i loro file dovrebbero essere salvati. I file possono essere salvati in diversi formati come XLS, SpreadsheetML, CSV, tabulato, valori separati da tabulazione TSV, XPS e molti altri. Questi formati di file sono specificati utilizzando l'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat).

L'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) contiene molti formati di file predefiniti (che possono essere scelti da te) come segue:

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
|[**AUTO**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#AUTO)|API cerca di rilevare il formato appropriato dall'estensione del file specificata nel primo parametro del metodo di salvataggio
|[**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#CSV)|Rappresenta un file CSV
|[**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSX)|Rappresenta un file di foglio di calcolo XML di Open Office
|[**XLSM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSM)|Rappresenta un file XLSM basato su XML
|[**XLTX**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTX)|Rappresenta un file di modello Excel
|[**XLTM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLTM)|Rappresenta un file di modello abilitato per macro Excel
|[**XLAM**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLAM)|Rappresenta un file Excel XLAM|
|[**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TSV)|Rappresenta un file con valori separati da tabulazioni|
|[**TAB_DELIMITED**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TAB_DELIMITED)|Rappresenta un file di testo delimitato da tabulazioni|
|[**HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)|Rappresenta un file HTML|
|[**M_HTML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#M_HTML)|Rappresenta file MHTML|
|[**ODS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#ODS)|Rappresenta un file di foglio di calcolo OpenDocument|
|[**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#EXCEL_97_TO_2003)|Rappresenta un file XLS, formato predefinito per le revisioni di Excel dal 1997 al 2003|
|[**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SPREADSHEET_ML)|Rappresenta un file SpreadSheetML|
|[**XLSB**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XLSB)|Rappresenta un file XLSB binario di Excel 2007|
|[**UNKNOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#UNKNOWN)|Rappresenta un formato non riconosciuto, non può essere salvato|
|[**PDF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)|Rappresenta un documento PDF|
|[**XPS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#XPS)|Rappresenta un file XML Paper Specification (XPS)|
|[**TIFF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#TIFF)|Rappresenta un file Tagged Image File Format (TIFF)|
|[**SVG**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#SVG)|Rappresenta un file basato su XML per Scalable Vector Graphics (SVG)|
|[**DIF**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#DIF)|Rappresenta un formato di scambio dati|
|[**NUMBERS**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#NUMBERS)|Rappresenta un file di numeri|
|[**MARKDOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN)|Rappresenta un documento di markdown|
**Normalmente, ci sono due modi per salvare i file Excel come segue:**

1. **Salvare il file in una determinata posizione**
1. **Salvare il file in uno stream**

## **Salvataggio del file in una determinata posizione**

Se gli sviluppatori devono salvare i propri file in qualche posizione di archiviazione, possono semplicemente specificare il nome del file (con il relativo percorso di archiviazione completo) e il formato desiderato del file (usando l'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)) durante la chiamata del metodo [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) dell'oggetto [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)

**Esempio:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoSomeLocation-SavingFiletoSomeLocation.java" >}}

## **Salvataggio Workbook in formato testo o CSV**

A volte si desidera convertire o salvare un workbook con più fogli di lavoro in formato testo. Per i formati di testo (ad esempio TXT, TabDelim, CSV ecc.), sia Microsoft Excel che Aspose.Cells di default salvano solo i contenuti del foglio di lavoro attivo

L'esempio di codice seguente spiega come salvare un intero workbook in formato testo. Carica il workbook di origine che potrebbe essere un file di fogli di calcolo Microsoft Excel o OpenOffice (quindi XLS, XLSX, XLSM, XLSB, ODS e così via) con un qualsiasi numero di fogli di lavoro.

Quando il codice viene eseguito, converte i dati di tutti i fogli del workbook nel formato TXT

Puoi modificare lo stesso esempio per salvare il tuo file in CSV. Per default, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#Separator) è una virgola, quindi non specificare un separatore se si salva nel formato CSV. Nota: Se stai utilizzando la versione di valutazione e anche se il parametro del metodo [**TxtSaveOptions.setExportAllSheets(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions/#setExportAllSheets-boolean-) è impostato su true, il programma esporterà comunque solo un foglio di lavoro.

**Esempio:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveWorkbookToTextCSVFormat-SaveWorkbookToTextCSVFormat.java" >}}

## **Salvataggio file di testo con separatore personalizzato**

I file di testo contengono dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati tra i suoi dati.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingTextFilewithCustomSeparator-SavingTextFilewithCustomSeparator.java" >}}

## **Salvataggio file in uno stream**

Se gli sviluppatori devono salvare i propri file su uno **Stream** allora dovrebbero creare un oggetto **FileOutputStream** e salvare il file in tale oggetto **Stream** chiamando il metodo [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions)) dell'oggetto [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Gli sviluppatori possono anche specificare il formato desiderato del file (usando l'enumerazione [**SaveFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat)) durante la chiamata del metodo [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))

**Esempio:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SavingFiletoStream-SavingFiletoStream.java" >}}

## **Salvataggio file in altro formato**

### **File XLS**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSFile-SaveXLSFile.java" >}}

### **File XLSX**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveXLSXFile-SaveXLSXFile.java" >}}

### **File PDF**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SaveInPdfFormat-SaveInPdfFormat.java" >}}

#### **Imposta l'opzione ContentCopyForAccessibility**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions), puoi ottenere o impostare l'opzione PDF [**AccessibilityExtractContent**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsecurityoptions#AccessibilityExtractContent) per controllare l'accesso al contenuto nel PDF convertito. Significa che consente al software screen reader di utilizzare il testo all'interno del file PDF per leggere il file PDF. Puoi disabilitarlo applicando una password di modifiche ai permessi e deselezionando i due elementi nello screenshot [qui](71630877.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ContentCopyForAccessibilityOption.java" >}}

#### **Esporta le proprietà personalizzate in PDF**

Con la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions), puoi esportare le proprietà personalizzate nel workbook di origine nel PDF. Viene fornita l'enumerazione [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfCustomPropertiesExport) per specificare il modo con cui le proprietà vengono esportate. Queste proprietà possono essere visualizzate in Adobe Acrobat Reader cliccando su File e quindi sull'opzione delle proprietà come mostrato nell'immagine seguente. Il file modello "sourceWithCustProps.xlsx" può essere scaricato [qui](sourceWithCustProps.xlsx) per il testing e il file PDF di output "outSourceWithCustProps" è disponibile [qui](outSourceWithCustProps.pdf) per l'analisi

![todo:image_alt_text](saving-excel-files-to-csv-pdf-and-other-formats_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportCustomPropertiesToPdf.java" >}}

## **Converti Workbook Excel in Markdown**

L'API di Aspose.Cells fornisce il supporto per esportare i fogli di calcolo in formato Markdown. Per esportare il foglio di lavoro attivo in Markdown, passa [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)). Puoi anche usare la classe [**MarkdownSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/MarkdownSaveOptions) per specificare impostazioni aggiuntive per esportare il foglio di lavoro in Markdown

L'esempio di codice seguente dimostra l'esportazione del foglio di lavoro attivo in Markdown utilizzando il membro di enumerazione [**SaveFormat.Markdown**](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#MARKDOWN). Si prega di consultare il [file Markdown di output](Book1.txt) generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToMarkdown-1.java" >}}

## **Argomenti avanzati**
- [Regola il livello di compressione del workbook](/cells/it/java/adjust-workbook-compression-level/)
- [Conversione del Workbook in diversi formati](/cells/it/java/converting-workbook-to-different-formats/)
- [Salva il foglio di lavoro nel formato Strict Open XML Spreadsheet](/cells/it/java/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [Monitora il progresso della conversione di Excel in TIFF](/cells/it/java/track-conversion-progress-of-excel-to-tiff/)
- [Monitorare il progresso della conversione dei documenti](/cells/it/java/track-document-conversion-progress/)
