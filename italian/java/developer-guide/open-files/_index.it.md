---
title: Apertura di file con formati diversi
linktitle: Apri file
type: docs
weight: 10
url: /it/java/opening-files-with-different-formats/
---
{{% alert color="primary" %}}

Gli sviluppatori utilizzano Aspose.Cells per aprire file per scopi diversi. Ad esempio, apri un file per recuperare i dati da esso o utilizza un file di foglio di calcolo predefinito per designer per velocizzare il processo di sviluppo. Aspose.Cells consente agli sviluppatori di aprire diversi tipi di file sorgente. Questi file di origine possono essere report di Microsoft Excel, SpreadsheetML, file con valori separati da virgola (CSV), delimitati da tabulazioni o con valori separati da tabulazioni (TSV). Questo articolo illustra l'apertura di questi diversi file di origine utilizzando Aspose.Cells.

Se hai bisogno di conoscere tutti i formati di file supportati, fai riferimento alle seguenti pagine:
[Formati di file supportati](https://docs.aspose.com/cells/java/supported-file-formats/)

{{% /alert %}}

## **Semplici modi per aprire i file Excel**

### **Apertura attraverso il percorso**

Per aprire un file Microsoft Excel utilizzando il percorso file, passare il percorso del file come parametro durante la creazione dell'istanza di**[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**classe. Il codice di esempio seguente illustra l'apertura di un file di Excel utilizzando il percorso del file.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughPath-OpeningFilesThroughPath.java" >}}

### **Apertura tramite Stream**

A volte, il file Excel che desideri aprire viene archiviato come flusso. In tal caso, analogamente all'apertura di un file utilizzando il percorso del file, passare lo stream come parametro durante l'istanziazione del file**[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**classe. Il codice di esempio seguente illustra l'apertura di un file Excel tramite stream.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningFilesThroughStream-OpeningFilesThroughStream.java" >}}

### **Apertura di file di diverse versioni di Microsoft Excel**

 L'utente può utilizzare il**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** class per specificare il formato del file Excel utilizzando l'**[Carica formato](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumerazione.

 Il**[Carica formato](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**L'enumerazione contiene molti formati di file predefiniti, alcuni dei quali sono riportati di seguito.

|**Tipi di formato**|**Descrizione**|
|:- |:- |
|Csv|Rappresenta un file CSV|
|Excel97To2003|Rappresenta un file Excel 97 - 2003|
|Xlsx|Rappresenta un file XLSX di Excel 2007/2010/2013/2016/2019 e Office 365|
|XLSM|Rappresenta un file XLSM di Excel 2007/2010/2013/2016/2019 e Office 365|
|XLTX|Rappresenta un file XLTX modello Excel 2007/2010/2013/2016/2019 e Office 365|
|Xltm|Rappresenta un file XLTM abilitato per le macro di Excel 2007/2010/2013/2016/2019 e Office 365|
|Xlsb|Rappresenta un file XLSB binario di Excel 2007/2010/2013/2016/2019 e Office 365|
|Foglio di calcoloML|Rappresenta un file SpreadsheetML|
|Tsv|Rappresenta un file di valori separati da tabulazioni|
|Tab Delimitato|Rappresenta un file di testo delimitato da tabulazioni|
|Odd|Rappresenta un file ODS|
|HTML|Rappresenta un file HTML|
|HTML|Rappresenta un file MHTML|

### **Apertura di file Microsoft Excel 95/5.0**

 Per aprire i file di Microsoft Excel 95, creare un'istanza del file**[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**instance con il percorso o il flusso del file modello. Il file di esempio per testare il codice può essere scaricato dal seguente link:

[Excel95_5.0.xls](Excel95_5.0.xls)

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningExcel95_5_0XLSFiles-1.java" >}}

### **Apertura di file XLS di Microsoft Excel 97 o versioni successive**

 Per aprire i file XLS di Microsoft Excel XLS 97 o versioni successive, creare un'istanza del file**[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** instance con il percorso o il flusso del file modello. Oppure usa il**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** metodo e selezionare il**[EXCEL_97_TO_2003](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#EXCEL_97_TO_2003)** valore in**[Carica formato](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumerazione.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel972003Files-OpeningMicrosoftExcel972003Files.java" >}}

### **Apertura di file XLSX di Microsoft Excel 2007 o versioni successive**

 Per aprire i file XLSX di Microsoft Excel 2007 o versioni successive, creare un'istanza del file**[Cartella di lavoro](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**instance con il percorso o il flusso del file modello. Oppure usa il**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe e selezionare il**[XLSX](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#XLSX)** valore in**[Carica formato](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumerazione.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningMicrosoftExcel2007XlsxFiles-OpeningMicrosoftExcel2007XlsxFiles.java" >}}

### **Apertura di file con formati diversi**

Aspose.Cells consente agli sviluppatori di aprire file di fogli di calcolo con diversi formati come SpreadsheetML, CSV, file delimitati da tabulazioni. Per aprire tali file, gli sviluppatori possono utilizzare la stessa metodologia utilizzata per aprire file di diverse versioni di Microsoft Excel.

### **Apertura di file SpreadsheetML**

I file SpreadsheetML sono le rappresentazioni XML dei tuoi fogli di calcolo che includono tutte le informazioni sul foglio di calcolo come formattazione, formule, ecc. A partire da Microsoft Excel XP, a Microsoft Excel viene aggiunta un'opzione di esportazione XML che esporta i tuoi fogli di calcolo in file SpreadsheetML.

Per aprire i file SpreadsheetML, utilizzare l'estensione**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe e selezionare il**[SPREADSHEET_ML](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#SPREADSHEET_ML)** valore in**[Carica formato](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumerazione.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningSpreadsheetMLFiles-OpeningSpreadsheetMLFiles.java" >}}

### **Apertura di file CSV**

I file CSV (Comma Separated Values) contengono record i cui valori sono delimitati o separati da virgole. Nei file CSV, i dati vengono archiviati in un formato tabulare con campi separati dal carattere virgola e quotati dal carattere virgolette. Se il valore di un campo contiene un carattere di doppia virgoletta, viene preceduto da una coppia di caratteri di doppia virgoletta. Puoi anche utilizzare Microsoft Excel per esportare i dati del foglio di calcolo in un file CSV.

Per aprire i file CSV, utilizzare il file**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe e selezionare il**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** valore, predefinito nel**[Carica formato](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumerazione.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Apertura di file CSV e sostituzione di caratteri non validi**

In Excel, quando viene aperto un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. Lo stesso viene fatto dall'API Aspose.Cells che è dimostrato nell'esempio di codice fornito di seguito.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

### **Apertura di file CSV utilizzando il parser preferito**

Questo non è sempre necessario per utilizzare le impostazioni predefinite del parser per l'apertura dei file CSV. A volte l'importazione di file CSV non crea l'output previsto come il formato della data non è come previsto o i campi vuoti vengono gestiti in modo diverso. Per questo scopo**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**è disponibile per fornire il proprio parser preferito per analizzare diversi tipi di dati secondo il requisito. Il seguente codice di esempio illustra l'utilizzo del parser preferito.

Il file sorgente di esempio e i file di output possono essere scaricati dai seguenti collegamenti per testare questa funzione.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Apertura di file TSV (delimitati da tabulazioni).**

file delimitati da tabulazioni contengono dati del foglio di calcolo ma senza alcuna formattazione. I dati sono disposti in righe e colonne come tabelle e fogli di calcolo. In breve, un file delimitato da tabulazioni è un tipo speciale di file di testo semplice con una tabulazione tra ogni colonna del testo.

Per aprire file delimitati da tabulazioni, gli sviluppatori dovrebbero utilizzare l'estensione**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe e selezionare il**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** valore, predefinito nel**[Carica formato](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumerazione.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

### **Apertura di file Excel crittografati**

Sappiamo che è possibile creare file Excel crittografati utilizzando Microsoft Excel. Per aprire tali file crittografati, gli sviluppatori devono chiamare uno speciale metodo LoadOptions con overload e selezionare il valore DEFAULT, predefinito nell'enumerazione FileFormatType. Questo metodo prenderebbe anche la password per il file crittografato come mostrato di seguito nell'esempio.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningEncryptedExcelFiles-OpeningEncryptedExcelFiles.java" >}}

Aspose.Cells supporta anche l'apertura di file MS Excel 2013 protetti da password.

{{% alert color="primary" %}}

Ci sono buone possibilità che il costruttore di Workbook possa generare System.OutOfMemoryException durante il caricamento di fogli di calcolo di grandi dimensioni. Questa eccezione suggerisce che la memoria disponibile non è sufficiente per caricare completamente il foglio di calcolo nella memoria, pertanto il foglio di calcolo deve essere caricato abilitando il[Preferenze di memoria](/cells/it/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}

### **Apertura di file SXC**

StarOffice Calc è simile a Microsoft Excel e supporta formule, grafici, funzioni e macro. I fogli di calcolo creati con questo software vengono salvati con l'estensione SXC. Il file SXC viene utilizzato anche per i file del foglio di calcolo di OpenOffice.org Calc. Aspose.Cells può leggere i file SXC come dimostrato dal seguente esempio di codice.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningSXCFiles-1.java" >}}

### **Apertura di file FODS**

Il file FODS è un foglio di calcolo salvato in OpenDocument XML senza alcuna compressione. Aspose.Cells può leggere i file FODS come dimostrato dal seguente esempio di codice.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Files-Handling-OpeningFODSFiles-1.java" >}}

## **Argomenti avanzati**
- [Filtra i nomi definiti durante il caricamento della cartella di lavoro](/cells/it/java/filter-defined-names-while-loading-workbook/)
- [Filtra gli oggetti durante il caricamento della cartella di lavoro o del foglio di lavoro](/cells/it/java/filter-objects-while-loading-workbook-or-worksheet/)
- [Ricevi avvisi durante il caricamento del file Excel](/cells/it/java/get-warnings-while-loading-excel-file/)
- [Mantieni i separatori per le righe vuote durante l'esportazione dei fogli di calcolo in formato CSV](/cells/it/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Carica la cartella di lavoro con il formato carta della stampante specificato](/cells/it/java/load-workbook-with-specified-printer-paper-size/)
- [Apertura di diversi file di versioni di Microsoft Excel](/cells/it/java/opening-different-microsoft-excel-versions-files/)
- [Ottimizzazione dell'utilizzo della memoria mentre si lavora con file di grandi dimensioni con set di dati di grandi dimensioni](/cells/it/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Leggi il foglio di calcolo dei numeri sviluppato da Apple Inc. utilizzando Aspose.Cells](/cells/it/java/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Lettura di file CSV con codifiche multiple](/cells/it/java/reading-csv-file-with-multiple-encodings/)
- [Interrompi la conversione o il caricamento utilizzando InterruptMonitor quando impiega troppo tempo](/cells/it/java/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Utilizzo dell'API LightCells](/cells/it/java/using-lightcells-api/)
