---
title: Converti CSV, TSV e TXT in Excel con Golang via C++
linktitle: Converti CSV, TSV e TXT in Excel
type: docs
weight: 30
url: /it/go-cpp/convert-csv-tsv-and-txt-to-excel/
description: Impara come convertire file CSV, TSV e TXT in Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Usando Aspose.Cells for C++, puoi convertire file CSV in Excel, OpenOffice, PDF, JSON e molti altri formati.

{{% /alert %}}

## **Apertura dei file CSV**

I file di valori separati da virgola (CSV) contengono record dove i valori sono separati da virgole. I dati vengono archiviati come una tabella in cui ogni colonna è separata dal carattere virgola e quotata con il carattere virgolette doppie. Se un valore di campo contiene un carattere virgolette doppie, viene escapato con una coppia di caratteri virgolette doppie. Puoi anche usare Microsoft Excel per esportare i dati del foglio di calcolo in CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel.go" >}}
## **Aprire file CSV e sostituire caratteri non validi**

In Excel, quando si apre un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. Lo stesso fa l'API Aspose.Cells, come dimostrato nell'esempio di codice sotto.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-1.go" >}}
## **Usando Preferred Parser**

Non è sempre necessario utilizzare le impostazioni del parser predefinito per aprire file CSV. A volte, l'importazione di un file CSV non produce l'output previsto, ad esempio quando il formato della data non è quello atteso o i campi vuoti vengono gestiti diversamente. A tale scopo, **TxtLoadOptions.PreferredParsers** è disponibile per fornire il proprio parser preferito per analizzare diversi tipi di dati come richiesto. Il seguente esempio di codice dimostra l'uso di un parser preferito.

È possibile scaricare il file di origine di esempio e i file di output dai seguenti collegamenti per testare questa funzionalità.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-2.go" >}}
### **Apertura dei file di testo con separatore personalizzato**

I file di testo vengono utilizzati per contenere dati dei fogli elettronici senza formattazione. Il file è un tipo di file di testo semplice che può avere delimitatori personalizzati.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-3.go" >}}
### **Apertura di file delimitati da tabulazione**

I file delimitati da tabulazione (Testo) contengono dati del foglio di calcolo ma senza formattazione. I dati sono disposti in righe e colonne come in tabelle e fogli di calcolo. Fondamentalmente, un file delimitato da tabulazione è un tipo speciale di file di testo semplice con una tabulazione tra ogni colonna.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-4.go" >}}
### **Apertura dei file di valori separati da tabulazione (TSV)**

I file di valori separati da tabulazione (TSV) contengono dati del foglio di calcolo ma senza formattazione. È lo stesso di un file delimitato da tabulazione, dove i dati sono disposti in righe e colonne come in tabelle e fogli di calcolo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-5.go" >}}
## **Argomenti avanzati**
- [Carica o importa file CSV con formule](/cells/it/cpp/load-or-import-csv-file-with-formulas/)
- [Lettura del file CSV con codifiche multiple](/cells/it/cpp/reading-csv-file-with-multiple-encodings/)
