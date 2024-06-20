---
title: Converti CSV, TSV e TXT in Excel
type: docs
weight: 30
url: /it/net/convert-csv-tsv-and-txt-to-excel/
---

{{% alert color="primary" %}}

Utilizzando Aspose.Cells, è possibile convertire file CSV in Excel, OpenOffice, Pdf, Json e molti altri formati diversi.

{{% /alert %}}


## **Apertura dei file CSV**

I file di valori separati da virgola (CSV) contengono record in cui i valori sono separati da virgole. I dati sono memorizzati come una tabella in cui ciascuna colonna è separata dal carattere virgola e citata dal carattere virgoletta doppia. Se un valore di campo contiene un carattere di virgoletta doppia, viene eseguito l'escape con una coppia di caratteri virgoletta doppia. È anche possibile utilizzare Microsoft Excel per esportare i dati del foglio di calcolo in CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFiles-1.cs" >}}

## **Apertura dei file CSV e sostituzione dei caratteri non validi**

In Excel, quando si apre un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. Lo stesso è fatto dall'API Aspose.Cells, come dimostrato nell'esempio di codice qui sotto.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesAndReplacingInvalidCharacters-1.cs" >}}

## **Utilizzo del parser preferito**

Non è sempre necessario utilizzare le impostazioni predefinite del parser per aprire i file CSV. A volte l'importazione del file CSV non crea l'output atteso, ad esempio il formato data non è come previsto o i campi vuoti vengono gestiti in modo diverso. A questo scopo è disponibile **TxtLoadOptions.PreferredParsers** per fornire un proprio parser preferito per analizzare diversi tipi di dati secondo i requisiti. Il codice di esempio seguente dimostra l'uso del parser preferito.  

È possibile scaricare il file di origine di esempio e i file di output dai seguenti collegamenti per testare questa funzionalità.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningCSVFilesWithPreferredParser-1.cs" >}}

### **Apertura dei file di testo con separatore personalizzato**

I file di testo vengono utilizzati per contenere dati dei fogli elettronici senza formattazione. Il file è un tipo di file di testo semplice che può avere delimitatori personalizzati.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTextFilewithCustomSeparator-1.cs" >}}

### **Apertura dei file delimitati da tabulazione**

Il file delimitato da tabulazione (Testo) contiene dati del foglio elettronico ma senza alcuna formattazione. I dati sono disposti in righe e colonne come nelle tabelle e nei fogli elettronici. Fondamentalmente, un file delimitato da tabulazione è un tipo speciale di file di testo semplice con una tabulazione tra ogni colonna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTabDelimitedFiles-1.cs" >}}

### **Apertura dei file di valori separati da tabulazione (TSV)**

Il file di valori separati da tabulazione (TSV) contiene dati del foglio elettronico ma senza alcuna formattazione. È lo stesso con il file delimitato da tabulazione dove i dati sono disposti in righe e colonne come nelle tabelle e nei fogli elettronici.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningTSVFiles-1.cs" >}}


## **Argomenti avanzati**
- [Carica o importa file CSV con formule](/cells/it/net/load-or-import-csv-file-with-formulas/)
- [Lettura del file CSV con codifiche multiple](/cells/it/net/reading-csv-file-with-multiple-encodings/)

