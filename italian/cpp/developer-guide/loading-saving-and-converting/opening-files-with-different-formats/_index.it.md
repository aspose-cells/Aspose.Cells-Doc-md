---
title: Apertura di file con formati diversi
type: docs
weight: 30
url: /it/cpp/opening-files-with-different-formats/
description: Aspose.Cells for .NET API consente di aprire/leggere diversi formati come XLSX, HTML, CSV, ODS, TSV, SXC, FODS, ecc.
keywords: open xlsx files, open html files, read fods files, read ods files, read sxc files, open csv files, Tab Delimited, SpreadsheetML, tsv, mhtml
---
{{% alert color="primary" %}}

 Utilizzando Aspose.Cells puoi aprire file con diversi formati.**Aspose.Cells** può aprire una gamma di formati di file come fogli di calcolo Excel Microsoft (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valori separati da virgola (CSV), file delimitati da tabulazioni o valori separati da tabulazioni (TSV) ecc.

Se hai bisogno di conoscere tutti i formati di file supportati, fai riferimento alle seguenti pagine:
[Formati di file supportati](https://docs.aspose.com/cells/cpp/supported-file-formats/)

{{% /alert %}}

##  **Apertura di file con formati diversi**

Aspose.Cells consente agli sviluppatori di aprire file di fogli di calcolo con formati diversi come SpreadsheetML, valori separati da virgole (CSV), valori delimitati da tabulazioni o valori separati da tabulazioni (TSV), file ODS. Per aprire tali file, gli sviluppatori possono utilizzare la stessa metodologia utilizzata per aprire file di diverse versioni di Excel Microsoft.

###  **Apertura file SpreadsheetML**

I file SpreadsheetML sono rappresentazioni XML di fogli di calcolo incluse tutte le informazioni su di essi, come formattazione, formule, ecc. A partire da Microsoft Excel XP, un'opzione di esportazione XML viene aggiunta a Microsoft Excel che esporta i tuoi fogli di calcolo nei file SpreadsheetML.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSpreadsheetMLFile-new.cpp" >}}

###  **Apertura file HTML**

Aspose.Cells consente di aprire il file HTML nell'oggetto cartella di lavoro. Il file HTML dovrebbe essere orientato a Microsoft Excel, ovvero MS-Excel dovrebbe essere in grado di aprirlo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenHTMLFile-new.cpp" >}}

###  **Apertura file CSV**

file Valori separati da virgola (CSV) contengono record in cui i valori sono separati da virgole. I dati vengono archiviati come una tabella in cui ciascuna colonna è separata dal carattere virgola e racchiusa tra virgolette doppie. Se il valore di un campo contiene virgolette doppie, viene preceduto da una coppia di virgolette doppie. Puoi anche utilizzare Microsoft Excel per esportare i dati del foglio di calcolo a CSV.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFile-new.cpp" >}}

####  **Apertura di file CSV e sostituzione di caratteri non validi**

In Excel, quando viene aperto il file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. Lo stesso viene fatto da Aspose.Cells API come dimostrato nell'esempio di codice riportato di seguito.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenCSVFileAndReplaceInvalidCharacters-new.cpp" >}}

Il file sorgente di esempio può essere scaricato dai seguenti collegamenti per testare questa funzionalità.

[Caratteri non validi.csv](InvalidCharacters.csv)

###  **Apertura di file di testo con separatore personalizzato**

I file di testo vengono utilizzati per contenere i dati del foglio di calcolo senza formattazione. Il file è una sorta di file di testo semplice che può avere alcuni delimitatori personalizzati.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTextFilewithCustomSeparator-new.cpp" >}}

Il file sorgente di esempio può essere scaricato dai seguenti collegamenti per testare questa funzionalità.

[CustomSeparator.txt](CustomSeparator.txt)

###  **Apertura di file delimitati da tabulazioni**

Il file delimitato da tabulazioni (testo) contiene dati del foglio di calcolo ma senza alcuna formattazione. I dati sono organizzati in righe e colonne come nelle tabelle e nei fogli di calcolo. Fondamentalmente, un file delimitato da tabulazioni è un tipo speciale di file di testo semplice con una tabulazione tra ciascuna colonna.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTabDelimitedFile-new.cpp" >}}

###  **Apertura di file con valori separati da tabulazioni (TSV).**

Il file con valori separati da tabulazioni (TSV) contiene dati del foglio di calcolo ma senza alcuna formattazione. È lo stesso con il file delimitato da tabulazioni in cui i dati sono disposti in righe e colonne come nelle tabelle e nei fogli di calcolo.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenTSVFile-new.cpp" >}}

###  **Apertura file SXC**

StarOffice Calc è simile a Microsoft Excel e supporta formule, grafici, funzioni e macro. I fogli di calcolo creati con questo software vengono salvati con l'estensione SXC. Il file SXC viene utilizzato anche per i file dei fogli di calcolo di OpenOffice.org Calc. Aspose.Cells può leggere i file SXC come dimostrato dal seguente esempio di codice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenSXCFile-new.cpp" >}}

###  **Apertura file FODS**

Il file FODS è un foglio di calcolo salvato in OpenDocument XML senza alcuna compressione. Aspose.Cells può leggere i file FODS come dimostrato dal seguente esempio di codice.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenFODSFile-new.cpp" >}}
