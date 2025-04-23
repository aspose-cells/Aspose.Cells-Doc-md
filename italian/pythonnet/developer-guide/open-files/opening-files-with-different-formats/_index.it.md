---
title: Apertura dei file con formati diversi
type: docs
weight: 30
url: /it/python-net/opening-files-with-different-formats/
description: L API di Aspose.Cells for Python via .NET consente di aprire/leggere vari formati come XLSX, HTML, CSV, ODS, TSV, SXC, FODS, ecc.
keywords: Aprire file xlsx, aprire file html, leggere file fods, leggere file ods, leggere file sxc, aprire file csv, Separato da tabulazione, SpreadsheetML, tsv, mhtml
---

{{% alert color="primary" %}}

Usando Aspose.Cells for Python via .NET puoi aprire file con formati diversi. Aspose.Cells for Python via .NET può aprire una vasta gamma di formati di file come fogli di calcolo di Microsoft Excel (XLS, XLSX, XLSM, XLSB), SpreadsheetML, valori separati da virgola (CSV), file delimitati da tabulazioni (TSV), ecc.

Se hai bisogno di conoscere tutti i formati di file supportati, consulta le seguenti pagine:
[Formati di file supportati](https://docs.aspose.com/cells/python-net/supported-file-formats/)

{{% /alert %}}

## **Apertura di file con formati diversi**

Aspose.Cells per Python via .NET consente agli sviluppatori di aprire file di fogli di calcolo con formati diversi come SpreadsheetML, valori separati da virgola (CSV), delimitati da tabulazione o valori separati da tabulazione (TSV), file ODS. Per aprire tali file, gli sviluppatori possono usare la stessa metodologia che usano per aprire file di diverse versioni di Microsoft Excel.

### **Apertura dei file SpreadsheetML**

I file SpreadsheetML sono rappresentazioni XML di fogli di calcolo che includono tutte le informazioni ad esse relative, come formattazione, formule, ecc. Dall'introduzione di Microsoft Excel XP, è stata aggiunta un'opzione di esportazione XML a Microsoft Excel che esporta i fogli di calcolo in file SpreadsheetML.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSpreadsheetMLFiles-1.py" >}}

### **Apertura dei file HTML**

Aspose.Cells per Python via .NET ti consente di aprire un file HTML in un oggetto Workbook. Il file HTML dovrebbe essere orientato a Microsoft Excel, cioè MS-Excel dovrebbe essere in grado di aprirlo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningHTMLFile-1.py" >}}

### **Apertura dei file CSV**

I file di valori separati da virgola (CSV) contengono record in cui i valori sono separati da virgole. I dati sono memorizzati come una tabella in cui ciascuna colonna è separata dal carattere virgola e citata dal carattere virgoletta doppia. Se un valore di campo contiene un carattere di virgoletta doppia, viene eseguito l'escape con una coppia di caratteri virgoletta doppia. È anche possibile utilizzare Microsoft Excel per esportare i dati del foglio di calcolo in CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFiles-1.py" >}}

#### **Apertura dei file CSV e sostituzione dei caratteri non validi**

In Excel, quando si apre un file CSV con caratteri speciali, i caratteri vengono automaticamente sostituiti. Lo stesso avviene con l'API Aspose.Cells per Python via .NET, come dimostrato nell'esempio di codice sottostante.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningCSVFilesAndReplacingInvalidCharacters-1.py" >}}



### **Apertura dei file delimitati da tabulazione**

Il file delimitato da tabulazione (Testo) contiene dati del foglio elettronico ma senza alcuna formattazione. I dati sono disposti in righe e colonne come nelle tabelle e nei fogli elettronici. Fondamentalmente, un file delimitato da tabulazione è un tipo speciale di file di testo semplice con una tabulazione tra ogni colonna.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTabDelimitedFiles-1.py" >}}

### **Apertura dei file di valori separati da tabulazione (TSV)**

Il file di valori separati da tabulazione (TSV) contiene dati del foglio elettronico ma senza alcuna formattazione. È lo stesso con il file delimitato da tabulazione dove i dati sono disposti in righe e colonne come nelle tabelle e nei fogli elettronici.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningTSVFiles-1.py" >}}

### **Apertura dei file SXC**

StarOffice Calc è simile a Microsoft Excel e supporta formule, grafici, funzioni e macro. I fogli di calcolo creati con questo software vengono salvati con l’estensione SXC. Il file SXC è anche utilizzato per i file di spreadsheet di OpenOffice.org Calc. Aspose.Cells per Python via .NET può leggere i file SXC come mostrato nell'esempio di codice seguente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningSXCFiles-1.py" >}}

### **Apertura dei file FODS**

Il file FODS è un foglio di calcolo salvato in OpenDocument XML senza compressione. Aspose.Cells per Python via .NET può leggere i file FODS come dimostrato dall'esempio di codice seguente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFODSFiles-1.py" >}}
