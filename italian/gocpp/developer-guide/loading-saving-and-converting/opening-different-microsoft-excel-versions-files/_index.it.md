---
title: Apertura di file di diverse versioni di Microsoft Excel
type: docs
weight: 20
url: /it/go-cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells può aprire una serie di diversi file di versioni di Microsoft Excel, come Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura di file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX o file di Excel crittografati.

{{% /alert %}}

## **Apertura di file di diverse versioni di Microsoft Excel**

Un’applicazione deve spesso essere in grado di aprire file Microsoft Excel creati in versioni diverse, ad esempio Microsoft Excel 95, 97, o Microsoft Excel 2007/2010/2013/2016/2019 e Office 365. Potresti aver bisogno di caricare un file in uno dei diversi formati, inclusi XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS, e altri. Utilizzare il costruttore o specificare il metodo [**SetFileFormat**](https://reference.aspose.com/cells/go-cpp/workbook/setfileformat/) della classe [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) per determinare il formato usando l’enumerazione [**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/).

L’enumerazione [**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/) contiene molti formati di file predefiniti, alcuni dei quali sono elencati di seguito.

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
|FileFormatType_CSV|Rappresenta un file CSV|
|FileFormatType_Excel97To2003|Rappresenta un file Excel 97 - 2003|
|FileFormatType_Xlsx|Rappresenta un file XLSX di Excel 2007/2010/2013/2016/2019 e Office 365|
|FileFormatType_Xlsm|Rappresenta un file XLSM di Excel 2007/2010/2013/2016/2019 e Office 365|
|FileFormatType_Xltx|Rappresenta un file XLTX di modello di Excel 2007/2010/2013/2016/2019 e Office 365|
|FileFormatType_Xltm|Rappresenta un file XLTM abilitato per macro di Excel 2007/2010/2013/2016/2019 e Office 365|
|FileFormatType_Xlsb|Rappresenta un file XLSB binario di Excel 2007/2010/2013/2016/2019 e Office 365|
|FileFormatType_SpreadsheetML|Rappresenta un file SpreadsheetML|
|FileFormatType_Tsv|Rappresenta un file di valori separati da tabulazioni|
|FileFormatType_TabDelimited|Rappresenta un file di testo delimitato da tabulazioni|
|FileFormatType_Ods|Rappresenta un file ODS|
|FileFormatType_Html|Rappresenta un file HTML|
|FileFormatType_MHtml|Rappresenta un file MHTML|

### **Apertura di file Microsoft Excel 95/5.0**

Per aprire un file di Microsoft Excel 95/5.0, utilizza [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) e imposta l'attributo relativo per la classe [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) per il file modello da caricare. Un file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[File di Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel95Files.go" >}}

### **Apertura dei file Microsoft Excel 97 - 2003**

Per aprire un file di Microsoft Excel 97 - 2003, utilizza [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) e imposta l'attributo relativo per la classe [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) per il file modello da caricare.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel97-2003Files.go" >}}

### **Apertura dei file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX**

Per aprire un file in formato Microsoft Excel 2007/2010/2013/2016/2019 e Office 365, cioè XLSX o XLSB, specifica il percorso del file. Puoi anche utilizzare [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) e impostare l'attributo/opzioni correlati della classe [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) per il file modello da caricare.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel2007Files.go" >}}

Aspose.Cells supporta anche l'apertura di file Microsoft Excel protetti da password.
