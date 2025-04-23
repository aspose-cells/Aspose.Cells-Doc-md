---
title: Apertura dei file con formati diversi
type: docs
weight: 30
url: /it/go-cpp/opening-files-with-different-formats/

description: L API Aspose.Cells for .NET consente di aprire/leggere diversi formati come XLSX, HTML, CSV, ODS, TSV, SXC, FODS, ecc.
keywords: Aprire file xlsx, aprire file html, leggere file fods, leggere file ods, leggere file sxc, aprire file csv, Separato da tabulazione, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Usando Aspose.Cells, è possibile aprire file con diversi formati. **Aspose.Cells** può aprire una vasta gamma di formati di file come fogli di calcolo Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valori separati da virgola (CSV), file delimitati da tab o valori delimitati da tab (TSV), e altri.

Se hai bisogno di conoscere tutti i formati di file supportati, consulta le seguenti pagine:
[Formati di File Supportati](https://docs.aspose.com/cells/go-cpp/supported-file-formats/)

{{% /alert %}}

## **Apertura di file con formati diversi**

Aspose.Cells permette agli sviluppatori di aprire file di fogli di calcolo con diversi formati come SpreadsheetML, valori separati da virgola (CSV), valori delimitati da tab o TSV, e file ODS. Per aprire tali file, gli sviluppatori possono usare la stessa metodologia usata per aprire file di diverse versioni di Microsoft Excel.

### **Apertura dei file SpreadsheetML**

I file SpreadsheetML sono rappresentazioni XML dei fogli di calcolo che includono tutte le informazioni relative, come formattazione, formule, ecc. Da Microsoft Excel XP, è stata aggiunta un’opzione di esportazione XML che consente di esportare i fogli di calcolo nei file SpreadsheetML.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSpreadsheetMLFile.go" >}}

### **Apertura dei file HTML**

Aspose.Cells consente l'apertura di file HTML nell'oggetto Workbook. Il file HTML dovrebbe essere orientato a Microsoft Excel, cioè MS-Excel dovrebbe essere in grado di aprirlo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenHTMLFile.go" >}}

### **Apertura dei file CSV**

I file di valori separati da virgola (CSV) contengono record in cui i valori sono separati da virgole. I dati sono memorizzati come una tabella in cui ciascuna colonna è separata dal carattere virgola e citata dal carattere virgoletta doppia. Se un valore di campo contiene un carattere di virgoletta doppia, viene eseguito l'escape con una coppia di caratteri virgoletta doppia. È anche possibile utilizzare Microsoft Excel per esportare i dati del foglio di calcolo in CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFile.go" >}}

#### **Apertura dei file CSV e sostituzione dei caratteri non validi**

In Excel, quando si apre un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. Lo stesso è fatto dall'API Aspose.Cells, come dimostrato nell'esempio di codice qui sotto.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenCSVFileAndReplaceInvalidCharacters.go" >}}

Il file di origine di esempio può essere scaricato dai seguenti link per testare questa funzione.

[InvalidCharacters.csv](InvalidCharacters.csv)

### **Apertura dei file di testo con separatore personalizzato**

I file di testo vengono utilizzati per contenere dati dei fogli elettronici senza formattazione. Il file è un tipo di file di testo semplice che può avere delimitatori personalizzati.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTextFilewithCustomSeparator.go" >}}

I file di esempio del codice sorgente possono essere scaricati dai link seguenti per testare questa funzionalità.

[CustomSeparator.txt](CustomSeparator.txt)

### **Apertura dei file delimitati da tabulazione**

Il file di valori delimitati da tab (Testo) contiene dati di foglio di calcolo, ma senza alcuna formattazione. I dati sono disposti in righe e colonne come in tabelle e fogli di calcolo. Fondamentalmente, un file delimitato da tab è un tipo speciale di file di testo semplice con un tab tra ogni colonna.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTabDelimitedFile.go" >}}

### **Apertura dei file di valori separati da tabulazione (TSV)**

Un file di valori separati da tab (TSV) contiene dati di foglio di calcolo, ma senza alcuna formattazione. È lo stesso di un file delimitato da tab, in cui i dati sono disposti in righe e colonne come in tabelle e fogli di calcolo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenTSVFile.go" >}}

### **Apertura dei file SXC**

StarOffice Calc è simile a Microsoft Excel e supporta formule, grafici, funzioni e macro. I fogli di calcolo creati con questo software vengono salvati con estensione SXC. Il file SXC viene utilizzato anche per i file di fogli di calcolo di OpenOffice.org Calc. Aspose.Cells può leggere i file SXC, come dimostrato dal seguente esempio di codice.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenSXCFile.go" >}}

### **Apertura dei file FODS**

Il file FODS è un foglio di calcolo salvato in OpenDocument XML senza compressione. Aspose.Cells può leggere i file FODS, come dimostrato dal seguente esempio di codice.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenFODSFile.go" >}}
