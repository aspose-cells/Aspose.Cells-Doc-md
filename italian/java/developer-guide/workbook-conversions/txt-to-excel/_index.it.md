---
title: Converti CSV, TSV e TXT in Excel
type: docs
weight: 50
url: /it/java/convert-csv-tsv-and-txt-to-excel/
---
## **Apertura file CSV**

I file Comma Separated Values (CSV) contengono record i cui valori sono delimitati o separati da virgole. Nei file CSV, i dati vengono archiviati in un formato tabulare con campi separati dal carattere virgola e quotati dal carattere virgolette. Se il valore di un campo contiene un carattere di doppia virgoletta, viene preceduto da una coppia di caratteri di doppia virgoletta. Puoi anche utilizzare Microsoft Excel per esportare i dati del foglio di calcolo in un file CSV.

Per aprire i file CSV, utilizzare il file**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe e selezionare il**[CSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV)** valore, predefinito nel**[Carica formato](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumerazione.

## **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Apertura di file CSV e sostituzione di caratteri non validi**

In Excel, quando viene aperto il file CSV con caratteri speciali, i caratteri vengono sostituiti automaticamente. Lo stesso viene fatto da Aspose.Cells API che è dimostrato nell'esempio di codice fornito di seguito.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Apertura dei file CSV utilizzando il parser preferito**

Questo non è sempre necessario per utilizzare le impostazioni predefinite del parser per aprire i file CSV. A volte l'importazione del file CSV non crea l'output previsto come il formato della data non è come previsto o i campi vuoti vengono gestiti in modo diverso. Per questo scopo**[TxtLoadOptions.PreferredParsers](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers)**è disponibile per fornire il proprio parser preferito per analizzare diversi tipi di dati secondo il requisito. Il seguente codice di esempio illustra l'utilizzo del parser preferito.

Il file sorgente di esempio e i file di output possono essere scaricati dai seguenti collegamenti per testare questa funzione.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Apertura di file TSV (delimitati da tabulazioni).**

I file delimitati da tabulazioni contengono dati del foglio di calcolo ma senza alcuna formattazione. I dati sono disposti in righe e colonne come tabelle e fogli di calcolo. In breve, un file delimitato da tabulazioni è un tipo speciale di file di testo semplice con una tabulazione tra ogni colonna del testo.

Per aprire file delimitati da tabulazioni, gli sviluppatori dovrebbero utilizzare l'estensione**[LoadOptions](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)** classe e selezionare il**[TSV](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV)** valore, predefinito nel**[Carica formato](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat)**enumerazione.

## **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Argomenti avanzati**
- [Carica o importa il file CSV con le formule](/cells/it/java/load-or-import-csv-file-with-formulas/)
- [Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV](/cells/it/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

