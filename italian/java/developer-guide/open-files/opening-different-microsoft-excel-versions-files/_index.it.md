---
title: Apertura di file di diverse versioni di Microsoft Excel
type: docs
weight: 20
url: /it/java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells può aprire una serie di diversi file di versioni di Microsoft Excel, come Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura di file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX o file di Excel crittografati.

{{% /alert %}}

## **Apertura di file di diverse versioni di Microsoft Excel**

Un'applicazione deve essere in grado di aprire file Microsoft Excel creati in diverse versioni, ad esempio, Microsoft Excel 95,97 o Microsoft Excel 2007/2010/2013/2016/2019 e Office 365. Potresti aver bisogno di caricare un file in uno qualsiasi dei diversi formati, inclusi XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS e così via. Usa il costruttore, o utilizza il metodo [**setFileFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat) della classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) per specificare il formato usando l'enumerazione [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType).

L'enumerazione [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType) contiene molti formati di file predefiniti alcuni dei quali sono elencati di seguito.

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
| CSV | Rappresenta un file CSV |
|EXCEL_97_TO_2003|Rappresenta un file Excel 97 - 2003|
|XLSX|Rappresenta un file XLSX Excel 2007/2010/2013/2016/2019 e Office 365|
|XLSM|Rappresenta un file XLSM Excel 2007/2010/2013/2016/2019 e Office 365|
|XLTX|Rappresenta un file modello XLTX di Excel 2007/2010/2013/2016/2019 e Office 365|
|XLTM|Rappresenta un file XLTM abilitato per macro di Excel 2007/2010/2013/2016/2019 e Office 365|
|XLSB|Rappresenta un file XLSB binario Excel 2007/2010/2013/2016/2019 e Office 365|
|SPREADSHEET_ML|Rappresenta un file SpreadsheetML|
|TSV|Rappresenta un file di valori separati da tabulazione|
|TAB_DELIMITED|Rappresenta un file di testo delimitato da tabulazioni|
|ODS|Rappresenta un file ODS|
|HTML|Rappresenta un file HTML|
|M_HTML|Rappresenta un file MHTML|

### **Apertura di file Microsoft Excel 95/5.0**

Per aprire un file di Microsoft Excel 95/5.0, utilizza [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) e imposta l'attributo relativo per la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) per il file modello da caricare. Un file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[File di Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **Apertura dei file Microsoft Excel 97 - 2003**

Per aprire un file di Microsoft Excel 97 - 2003, utilizza [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) e imposta l'attributo relativo per la classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) per il file modello da caricare.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **Apertura dei file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX**

Per aprire un file in formato Microsoft Excel 2007/2010/2013/2016/2019 e Office 365, cioè XLSX o XLSB, specifica il percorso del file. Puoi anche utilizzare [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) e impostare l'attributo/opzioni correlati della classe [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) per il file modello da caricare.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **Apertura di file Excel criptati**

È possibile creare file Excel crittografati utilizzando Microsoft Excel. Per aprire un file crittografato, utilizzare [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) e impostare i suoi attributi e opzioni (ad esempio, fornire una password) per il file del modello da caricare. 
Un file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

Aspose.Cells supporta anche l'apertura di file Microsoft Excel 2007, 2010, 2013, 2016, 2019 e Office 365 protetti da password.
