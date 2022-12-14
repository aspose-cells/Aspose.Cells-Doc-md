---
title: Apertura di file con formati diversi
type: docs
weight: 30
url: /it/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API consente di aprire/leggere diversi formati come XLSX, HTML, CSV, ODS, TSV, SXC, FODS, ecc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Utilizzando Aspose.Cells è possibile aprire file con diversi formati.**Aspose.Cells** può aprire una gamma di formati di file come fogli di calcolo Excel Microsoft (XLS, XLSX, XLSM, XLSB), SpreadsheetML, file con valori separati da virgola (CSV), delimitati da tabulazioni o con valori separati da tabulazioni (TSV) ecc.

Se hai bisogno di conoscere tutti i formati di file supportati, fai riferimento alle seguenti pagine:
[Formati di file supportati](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

## **Apertura di file con formati diversi**

Aspose.Cells consente agli sviluppatori di aprire file di fogli di calcolo con diversi formati come SpreadsheetML, valori separati da virgola (CSV), valori delimitati da tabulazioni o separati da tabulazioni (TSV), file ODS. Per aprire tali file, gli sviluppatori possono utilizzare la stessa metodologia utilizzata per aprire file di diverse versioni di Excel Microsoft.

### **Apertura di file SpreadsheetML**

I file SpreadsheetML sono rappresentazioni XML di fogli di calcolo che includono tutte le informazioni su di esso, come formattazione, formule ecc. A partire da Microsoft Excel XP, a Microsoft Excel viene aggiunta un'opzione di esportazione XML che esporta i fogli di calcolo in file SpreadsheetML.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile.cpp" >}}

### **Apertura di file HTML**

Aspose.Cells consente di aprire il file HTML nell'oggetto cartella di lavoro. Il file HTML dovrebbe Microsoft orientato a Excel, ovvero MS-Excel dovrebbe essere in grado di aprirlo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile.cpp" >}}

### **Apertura di file CSV**

file CSV (Comma Separated Values) contengono record in cui i valori sono separati da virgole. I dati vengono archiviati come una tabella in cui ogni colonna è separata dal carattere virgola e quotata dal carattere virgoletta doppia. Se un valore di campo contiene un carattere di doppia virgoletta, viene preceduto da una coppia di caratteri di doppia virgoletta. Puoi anche utilizzare Microsoft Excel per esportare i dati del foglio di calcolo in CSV.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile.cpp" >}}

#### **Apertura di file CSV e sostituzione di caratteri non validi**

In Excel, quando viene aperto un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. Lo stesso viene fatto da Aspose.Cells API che è dimostrato nell'esempio di codice riportato di seguito.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters.cpp" >}}

Il file sorgente di esempio può essere scaricato dai seguenti collegamenti per testare questa funzione.

[CaratteriInvalidi.csv](InvalidCharacters.csv)

### **Apertura di file di testo con separatore personalizzato**

I file di testo vengono utilizzati per contenere i dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator.cpp" >}}

Il file sorgente di esempio può essere scaricato dai seguenti collegamenti per testare questa funzione.

[CustomSeparator.txt](CustomSeparator.txt)

### **Apertura di file delimitati da tabulazioni**

Il file delimitato da tabulazioni (testo) contiene i dati del foglio di calcolo ma senza alcuna formattazione. I dati sono disposti in righe e colonne come nelle tabelle e nei fogli di calcolo. Fondamentalmente, un file delimitato da tabulazioni è un tipo speciale di file di testo normale con una tabulazione tra ogni colonna.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile.cpp" >}}

### **Apertura di file con valori separati da tabulazioni (TSV).**

Il file con valori separati da tabulazioni (TSV) contiene i dati del foglio di calcolo ma senza alcuna formattazione. È lo stesso con il file delimitato da tabulazioni in cui i dati sono disposti in righe e colonne come nelle tabelle e nei fogli di calcolo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile.cpp" >}}

### **Apertura di file SXC**

StarOffice Calc è simile a Microsoft Excel e supporta formule, grafici, funzioni e macro. I fogli di calcolo creati con questo software vengono salvati con l'estensione SXC. Il file SXC viene utilizzato anche per i file del foglio di calcolo di OpenOffice.org Calc. Aspose.Cells può leggere i file SXC come dimostrato dal seguente esempio di codice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile.cpp" >}}

### **Apertura di file FODS**

Il file FODS è un foglio di calcolo salvato in OpenDocument XML senza alcuna compressione. Aspose.Cells può leggere i file FODS come dimostrato dal seguente esempio di codice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile.cpp" >}}
