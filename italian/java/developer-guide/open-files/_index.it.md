---
title: Apertura dei file con formati diversi
linktitle: Aprire i file
type: docs
weight: 10
url: /it/java/opening-files-with-different-formats/
---

{{% alert color="primary" %}}

Gli sviluppatori utilizzano Aspose.Cells per aprire file per scopi diversi. Ad esempio, aprire un file per recuperare dati da esso, o utilizzare un file di foglio di calcolo del designer predefinito per velocizzare il processo di sviluppo. Aspose.Cells consente agli sviluppatori di aprire diversi tipi di file di origine. Questi file di origine possono essere rapporti di Microsoft Excel, SpreadsheetML, valori separati da virgola (CSV), valori delimitati da tabulazioni o valori separati da tabulazioni (TSV). Questo articolo tratta dell'apertura di questi diversi file di origine utilizzando Aspose.Cells.

Se hai bisogno di conoscere tutti i formati di file supportati, consulta le seguenti pagine:
[Formati file supportati](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Modi semplici per aprire file Excel**

### **Apertura attraverso percorso**

Per aprire un file di Microsoft Excel utilizzando il percorso del file, passare il percorso del file come parametro durante la creazione dell'istanza della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Il seguente codice di esempio mostra come aprire un file Excel utilizzando il percorso del file.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Apertura tramite flusso**

A volte, il file Excel che si desidera aprire è archiviato come stream. In tal caso, simile all'apertura di un file utilizzando il percorso del file, passare lo stream come parametro durante l'istanziazione della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook). Il seguente codice di esempio dimostra l'apertura di un file Excel utilizzando lo stream.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Apertura di file di diverse versioni di Microsoft Excel**

L'utente può utilizzare la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) per specificare il formato del file Excel utilizzando l'enumerazione [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

L'enumerazione [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat) contiene molti formati di file predefiniti alcuni dei quali sono elencati di seguito.

|**Tipi di formato**|**Descrizione**|
| :- | :- |
|Csv|Rappresenta un file CSV|
|Excel97To2003| Rappresenta un file Excel 97 - 2003 |
|Xlsx|Rappresenta un file XLSX Excel 2007/2010/2013/2016/2019 e Office 365|
|Xlsm|Rappresenta un file XLSM Excel 2007/2010/2013/2016/2019 e Office 365|
|Xltx|Rappresenta un file modello XLTX di Excel 2007/2010/2013/2016/2019 e Office 365|
|Xltm|Rappresenta un file XLTM macro abilitato di Excel 2007/2010/2013/2016/2019 e Office 365|
|Xlsb|Rappresenta un file XLSB binario di Excel 2007/2010/2013/2016/2019 e Office 365|
|SpreadsheetML|Rappresenta un file SpreadsheetML|
|Tsv|Rappresenta un file di valori separati da tabulazioni|
|TabDelimited|Rappresenta un file di testo delimitato da tabulazioni|
|Ods|Rappresenta un file ODS|
|Html|Rappresenta un file HTML|
|Mhtml|Rappresenta un file MHTML|

### **Apertura di file Microsoft Excel 95/5.0**

Per aprire i file Microsoft Excel 95, istanziare l'istanza [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) con il percorso o lo stream del file di modello. Il file di esempio per testare il codice può essere scaricato dal seguente link:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Apertura di file XLS di Microsoft Excel 97 o versioni successive**

Per aprire file XLS di Microsoft Excel XLS 97 o versioni successive, istanzia l'istanza [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) con il percorso o lo stream del file modello. Oppure utilizza il metodo [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) e seleziona il valore [**EXCEL_97_TO_2003**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003) nell'enumerazione [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Apertura di file XLSX di Microsoft Excel 2007 o versioni successive**

Per aprire file XLSX di Microsoft Excel 2007 o versioni successive, istanzia l'istanza [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) con il percorso o lo stream del file modello. Oppure utilizza la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) e seleziona il valore [**XLSX**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX) nell'enumerazione [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Apertura di file con formati diversi**

Aspose.Cells consente ai programmatori di aprire file di fogli elettronici con diversi formati come SpreadsheetML, CSV, file delimitati da tabulazioni. Per aprire tali file, i programmatori possono utilizzare la stessa metodologia usata per aprire file di diverse versioni di Microsoft Excel.

### **Apertura dei file SpreadsheetML**

I file SpreadsheetML sono le rappresentazioni XML dei fogli elettronici, includendo tutte le informazioni sul foglio elettronico come formattazione, formule, ecc. Dal Microsoft Excel XP, è stata aggiunta un'opzione di esportazione XML a Microsoft Excel che esporta i fogli elettronici in file SpreadsheetML.

Per aprire file SpreadsheetML, utilizza la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) e seleziona il valore [**SPREADSHEET_ML**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML) nell'enumerazione [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Apertura dei file CSV**

I file CSV (Comma Separated Values) contengono record i cui valori sono delimitati o separati da virgole. Nei file CSV, i dati sono memorizzati in un formato tabellare che ha campi separati dal carattere virgola e racchiusi dal carattere virgolette doppie. Se il valore di un campo contiene un carattere di virgolette doppie, viene trasformato con una coppia di caratteri di virgolette doppie. È anche possibile utilizzare Microsoft Excel per esportare i dati del foglio di calcolo in un file CSV.

Per aprire file CSV, utilizza la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) e seleziona il valore [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV), predefinito nell'enumerazione [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Apertura dei file CSV e sostituzione dei caratteri non validi**

In Excel, quando viene aperto un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. La stessa operazione viene eseguita dall'API Aspose.Cells che è dimostrata nell'esempio di codice riportato di seguito.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Apertura dei file CSV utilizzando il parser preferito**

Non sempre è necessario utilizzare le impostazioni del parser predefinito per aprire i file CSV. A volte l'importazione del file CSV non crea l'output previsto, ad esempio il formato data non corrisponde alle aspettative o i campi vuoti sono gestiti in modo diverso. A tale scopo è disponibile [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) per fornire un proprio parser preferito per analizzare diversi tipi di dati secondo le richieste. Il seguente esempio di codice dimostra l'uso del parser preferito.  

È possibile scaricare il file di origine di esempio e i file di output dai seguenti collegamenti per testare questa funzionalità.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Apertura dei file TSV (delimitati da tabulazione)**

I file delimitati da tabulazioni contengono dati di fogli elettronici ma senza alcuna formattazione. I dati sono disposti in righe e colonne come tabelle e fogli di calcolo. In breve, un file delimitato da tabulazioni è un tipo speciale di file di testo puro con una tabulazione tra ciascuna colonna nel testo.

Per aprire file delimitati da tabulazioni, i programmatori dovrebbero utilizzare la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) e selezionare il valore [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV), predefinito nell'enumerazione [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Apertura di file Excel criptati**

Sappiamo che è possibile creare file Excel criptati utilizzando Microsoft Excel. Per aprire tali file criptati, i programmatori dovrebbero chiamare un metodo sovraccaricato speciale di LoadOptions e selezionare il valore DEFAULT, predefinito nell'enumerazione FileFormatType. Questo metodo richiederà anche la password per il file criptato come mostrato di seguito nell'esempio.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells supporta anche l'apertura di file MS Excel 2013 protetti da password.

{{% alert color="primary" %}}

È probabile che il costruttore del Workbook possa generare System.OutOfMemoryException durante il caricamento di fogli elettronici di grandi dimensioni. Questa eccezione suggerisce che la memoria disponibile non è sufficiente per caricare completamente il foglio elettronico in memoria, pertanto il foglio elettronico deve essere caricato abilitando le [Memory Preferences](/cells/it/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **Apertura dei file SXC**

StarOffice Calc è simile a Microsoft Excel e supporta formule, grafici, funzioni e macro. I fogli elettronici creati con questo software sono salvati con l'estensione SXC. Il file SXC è anche utilizzato per i file del foglio elettronico di OpenOffice.org Calc. Aspose.Cells può leggere i file SXC, come dimostrato dal seguente esempio di codice.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Apertura dei file FODS**

Il file FODS è un foglio elettronico salvato in formato OpenDocument XML senza alcuna compressione. Aspose.Cells può leggere i file FODS come dimostrato dal seguente esempio di codice.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Argomenti avanzati**
- [Filtra i nomi definiti durante il caricamento del foglio di lavoro](/cells/it/java/filter-defined-names-while-loading-workbook/)
- [Filtra gli oggetti durante il caricamento del foglio di lavoro o del foglio di calcolo](/cells/it/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Ottieni avvisi durante il caricamento del file Excel](/cells/it/java/get-warnings-while-loading-excel-file/)
- [Mantieni i separatori per le righe vuote durante l'esportazione di fogli di calcolo in formato CSV](/cells/it/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Carica il libro di lavoro con il formato di carta della stampante specificato](/cells/it/java/load-workbook-with-specified-printer-paper-size/)
- [Apertura di file di diverse versioni di Microsoft Excel](/cells/it/java/opening-different-microsoft-excel-versions-files/)
- [Ottimizzazione dell'utilizzo della memoria durante il lavoro con file grandi che contengono grandi set di dati](/cells/it/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Leggi i fogli di calcolo di Numbers sviluppati da Apple Inc. utilizzando Aspose.Cells](/cells/it/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Lettura del file CSV con codifiche multiple](/cells/it/java/reading-csv-file-with-multiple-encodings/)
- [Interrompere la conversione o il caricamento utilizzando InterruptMonitor quando sta impiegando troppo tempo](/cells/it/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Utilizzo di API LightCells](/cells/it/java/using-lightcells-api/)
