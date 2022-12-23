---
title: Converti CSV, TSV e TXT in Excel
type: docs
weight: 30
url: /it/net/convert-csv-tsv-and-txt-to-excel/
---
{{% alert color="primary" %}}

Usando Aspose.Cells, puoi convertire il file CSV in Excel, OpenOffice, Pdf, Json e molti formati diversi.

{{% /alert %}}


## **Apertura file CSV**

file Comma Separated Values (CSV) contengono record in cui i valori sono separati da virgole. I dati vengono archiviati come una tabella in cui ogni colonna è separata dal carattere virgola e quotata dal carattere virgoletta doppia. Se un valore di campo contiene un carattere di doppia virgoletta, viene preceduto da una coppia di caratteri di doppia virgoletta. Puoi anche utilizzare Microsoft Excel per esportare i dati del foglio di calcolo in CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **Apertura di file CSV e sostituzione di caratteri non validi**

In Excel, quando viene aperto il file CSV con caratteri speciali, i caratteri vengono sostituiti automaticamente. Lo stesso viene fatto da Aspose.Cells API che è dimostrato nell'esempio di codice fornito di seguito.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Utilizzo del parser preferito**

Questo non è sempre necessario per utilizzare le impostazioni predefinite del parser per aprire i file CSV. A volte l'importazione del file CSV non crea l'output previsto come il formato della data non è come previsto o i campi vuoti vengono gestiti in modo diverso. Per questo scopo**TxtLoadOptions.PreferredParsers**è disponibile per fornire il proprio parser preferito per analizzare diversi tipi di dati secondo il requisito. Il seguente codice di esempio illustra l'utilizzo del parser preferito.

Il file sorgente di esempio e i file di output possono essere scaricati dai seguenti collegamenti per testare questa funzione.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Apertura di file di testo con separatore personalizzato**

I file di testo vengono utilizzati per contenere i dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Apertura di file delimitati da tabulazioni**

Il file delimitato da tabulazioni (testo) contiene i dati del foglio di calcolo ma senza alcuna formattazione. I dati sono disposti in righe e colonne come nelle tabelle e nei fogli di calcolo. Fondamentalmente, un file delimitato da tabulazioni è un tipo speciale di file di testo normale con una tabulazione tra ogni colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Apertura di file con valori separati da tabulazioni (TSV).**

Il file con valori separati da tabulazioni (TSV) contiene i dati del foglio di calcolo ma senza alcuna formattazione. È lo stesso con il file delimitato da tabulazioni in cui i dati sono disposti in righe e colonne come nelle tabelle e nei fogli di calcolo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Argomenti avanzati**
- [Carica o importa il file CSV con le formule](/cells/it/net/load-or-import-csv-file-with-formulas/)
- [Lettura del file CSV con codifiche multiple](/cells/it/net/reading-csv-file-with-multiple-encodings/)

