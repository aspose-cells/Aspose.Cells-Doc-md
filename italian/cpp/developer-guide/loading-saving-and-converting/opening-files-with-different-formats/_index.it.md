---
title: Apertura dei file con formati diversi
type: docs
weight: 30
url: /it/cpp/opening-files-with-different-formats/

description: L API Aspose.Cells for C++ consente di aprire/leggere diversi formati come XLSX, HTML, CSV, ODS, TSV, SXC, FODS, ecc.
keywords: Aprire file xlsx, aprire file html, leggere file fods, leggere file ods, leggere file sxc, aprire file csv, Separato da tabulazione, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Utilizzando Aspose.Cells è possibile aprire file con formati diversi. **Aspose.Cells** può aprire una serie di formati di file come fogli di calcolo Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valori separati da virgola (CSV), valori delimitati da tabulazione o valori separati da tabulazione (TSV) ecc.

Se hai bisogno di conoscere tutti i formati di file supportati, consulta le seguenti pagine:
[Formati di file supportati](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

## **Apertura di file con formati diversi**

Aspose.Cells consente agli sviluppatori di aprire file di fogli di calcolo con formati diversi come SpreadsheetML, valori separati da virgola (CSV), valori delimitati da tabulazione o valori separati da tabulazione (TSV), file ODS. Per aprire tali file, gli sviluppatori possono utilizzare la stessa metodologia utilizzata per l'apertura di file di diverse versioni di Microsoft Excel.

### **Apertura dei file SpreadsheetML**

I file SpreadsheetML sono rappresentazioni XML di fogli di calcolo che includono tutte le informazioni ad esse relative, come formattazione, formule, ecc. Dall'introduzione di Microsoft Excel XP, è stata aggiunta un'opzione di esportazione XML a Microsoft Excel che esporta i fogli di calcolo in file SpreadsheetML.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

### **Apertura dei file HTML**

Aspose.Cells consente l'apertura di file HTML nell'oggetto Workbook. Il file HTML dovrebbe essere orientato a Microsoft Excel, cioè MS-Excel dovrebbe essere in grado di aprirlo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

### **Apertura dei file CSV**

I file di valori separati da virgola (CSV) contengono record in cui i valori sono separati da virgole. I dati sono memorizzati come una tabella in cui ciascuna colonna è separata dal carattere virgola e citata dal carattere virgoletta doppia. Se un valore di campo contiene un carattere di virgoletta doppia, viene eseguito l'escape con una coppia di caratteri virgoletta doppia. È anche possibile utilizzare Microsoft Excel per esportare i dati del foglio di calcolo in CSV.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

#### **Apertura dei file CSV e sostituzione dei caratteri non validi**

In Excel, quando si apre un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. Lo stesso è fatto dall'API Aspose.Cells, come dimostrato nell'esempio di codice qui sotto.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

Il file di origine di esempio può essere scaricato dai seguenti link per testare questa funzione.

[InvalidCharacters.csv](InvalidCharacters.csv)

### **Apertura dei file di testo con separatore personalizzato**

I file di testo vengono utilizzati per contenere dati dei fogli elettronici senza formattazione. Il file è un tipo di file di testo semplice che può avere delimitatori personalizzati.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

Il file di origine di esempio può essere scaricato dai seguenti link per testare questa funzione.

[CustomSeparator.txt](CustomSeparator.txt)

### **Apertura dei file delimitati da tabulazione**

Il file delimitato da tabulazione (Testo) contiene dati del foglio elettronico ma senza alcuna formattazione. I dati sono disposti in righe e colonne come nelle tabelle e nei fogli elettronici. Fondamentalmente, un file delimitato da tabulazione è un tipo speciale di file di testo semplice con una tabulazione tra ogni colonna.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

### **Apertura dei file di valori separati da tabulazione (TSV)**

Il file di valori separati da tabulazione (TSV) contiene dati del foglio elettronico ma senza alcuna formattazione. È lo stesso con il file delimitato da tabulazione dove i dati sono disposti in righe e colonne come nelle tabelle e nei fogli elettronici.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

### **Apertura dei file SXC**

StarOffice Calc è simile a Microsoft Excel e supporta formule, grafici, funzioni e macro. I fogli elettronici creati con questo software sono salvati con l'estensione SXC. Il file SXC è anche utilizzato per i file del foglio elettronico di OpenOffice.org Calc. Aspose.Cells può leggere i file SXC, come dimostrato dal seguente esempio di codice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

### **Apertura dei file FODS**

Il file FODS è un foglio elettronico salvato in OpenDocument XML senza alcuna compressione. Aspose.Cells può leggere i file FODS, come dimostrato dal seguente esempio di codice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
