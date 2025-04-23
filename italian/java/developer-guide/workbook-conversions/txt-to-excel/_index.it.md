---
title: Converti CSV, TSV e TXT in Excel
type: docs
weight: 50
url: /it/java/convert-csv-tsv-and-txt-to-excel/
---

## **Apertura dei file CSV**

I file CSV (Comma Separated Values) contengono record i cui valori sono delimitati o separati da virgole. Nei file CSV, i dati sono memorizzati in un formato tabellare che ha campi separati dal carattere virgola e racchiusi dal carattere virgolette doppie. Se il valore di un campo contiene un carattere di virgolette doppie, viene trasformato con una coppia di caratteri di virgolette doppie. È anche possibile utilizzare Microsoft Excel per esportare i dati del foglio di calcolo in un file CSV.

Per aprire file CSV, utilizza la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) e seleziona il valore [**CSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#CSV), predefinito nell'enumerazione [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

## **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningCSVFiles-OpeningCSVFiles.java" >}}

### **Apertura dei file CSV e sostituzione dei caratteri non validi**

In Excel, quando viene aperto un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. La stessa operazione viene eseguita dall'API Aspose.Cells che è dimostrata nell'esempio di codice riportato di seguito.

#### **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesAndReplacingInvalidCharacters-1.java" >}}

## **Apertura dei file CSV utilizzando il parser preferito**

Non sempre è necessario utilizzare le impostazioni del parser predefinito per aprire i file CSV. A volte l'importazione del file CSV non crea l'output previsto, ad esempio il formato data non corrisponde alle aspettative o i campi vuoti sono gestiti in modo diverso. A tale scopo è disponibile [**TxtLoadOptions.PreferredParsers**](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#PreferredParsers) per fornire un proprio parser preferito per analizzare diversi tipi di dati secondo le richieste. Il seguente esempio di codice dimostra l'uso del parser preferito.  

È possibile scaricare il file di origine di esempio e i file di output dai seguenti collegamenti per testare questa funzionalità.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

## **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-OpeningCSVFilesWithPreferredParser-1.java" >}}

### **Apertura dei file TSV (delimitati da tabulazione)**

I file delimitati da tabulazioni contengono dati di fogli elettronici ma senza alcuna formattazione. I dati sono disposti in righe e colonne come tabelle e fogli di calcolo. In breve, un file delimitato da tabulazioni è un tipo speciale di file di testo puro con una tabulazione tra ciascuna colonna nel testo.

Per aprire file delimitati da tabulazioni, i programmatori dovrebbero utilizzare la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) e selezionare il valore [**TSV**](https://reference.aspose.com/cells/java/com.aspose.cells/loadformat#TSV), predefinito nell'enumerazione [**LoadFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadFormat).

## **Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-OpeningTabDelimitedFiles-OpeningTabDelimitedFiles.java" >}}

## **Argomenti avanzati**
- [Carica o importa file CSV con formule](/cells/it/java/load-or-import-csv-file-with-formulas/)
- [Taglia righe e colonne vuote iniziali durante l'esportazione di fogli di calcolo nel formato CSV](/cells/it/java/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)

{{< app/cells/assistant language="java" >}}
