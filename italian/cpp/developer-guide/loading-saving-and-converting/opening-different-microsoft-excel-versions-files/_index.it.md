---
title: Apertura di diversi file di versioni di Excel Microsoft
type: docs
weight: 20
url: /it/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells può aprire una gamma di diversi file di versioni di Excel Microsoft, come Microsoft Excel 95/97 - 2003, SpreadsheetML, Apertura Microsoft di Excel 2007/2010/2013/2016/2019 e Office 365 XLSX o file Excel crittografati.

{{% /alert %}}

## **Apertura di file di diverse versioni di Excel Microsoft**

 Un'applicazione spesso deve essere in grado di aprire file Excel Microsoft creati in versioni diverse, ad esempio Microsoft Excel 95,97 o Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 . Potrebbe essere necessario caricare un file in uno dei diversi formati, inclusi XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS e così via. Utilizzare il costruttore o specificare il**[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)** classe'**[SetFileFormat](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#aa74a10e0aa88e3a8386ea328165896dc)**metodo per specificare il formato utilizzando il**[FileFormatType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**enumerazione.
	
 Il**[FileFormatType](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**L'enumerazione contiene molti formati di file predefiniti, alcuni dei quali sono riportati di seguito.

|**Tipi di formati di file**|**Descrizione**|
|:- |:- |
|FileFormatType_CSV|Rappresenta un file CSV|
|FileFormatType_Excel97To2003|Rappresenta un file Excel 97 - 2003|
|FileFormatType_Xlsx|Rappresenta un file Excel 2007/2010/2013/2016/2019 e Office 365 XLSX|
|FileFormatType_Xlsm|Rappresenta un file Excel 2007/2010/2013/2016/2019 e Office 365 XLSM|
|FileFormatType_Xltx|Rappresenta un file modello XLTX di Excel 2007/2010/2013/2016/2019 e Office 365|
|FileFormatType_Xltm|Rappresenta un file XLTM abilitato per le macro di Excel 2007/2010/2013/2016/2019 e Office 365|
|FileFormatType_Xlsb|Rappresenta un file binario XLSB di Excel 2007/2010/2013/2016/2019 e Office 365|
|FileFormatType_SpreadsheetML|Rappresenta un file SpreadsheetML|
|FileFormatType_Tsv|Rappresenta un file di valori separati da tabulazioni|
|FileFormatType_TabDelimitato|Rappresenta un file di testo delimitato da tabulazioni|
|FileFormatType_Ods|Rappresenta un file ODS|
|FileFormatType_Html|Rappresenta un file HTML|
|FileFormatType_MHtml|Rappresenta un file MHTML|

### **Apertura di file Excel 95/5.0 Microsoft**

Per aprire un file Excel 95/5.0 Microsoft, utilizzare**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)**e impostare l'attributo correlato per the**ILoadOptions**class per il file modello da caricare. Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[File Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files.cpp" >}}

### **Apertura Microsoft Excel 97 - 2003 File**

 Per aprire un file Microsoft Excel 97 - 2003, utilizzare**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** e impostare l'attributo correlato per the**ILoadOptions**class per il file modello da caricare.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files.cpp" >}}

### **Apertura Microsoft File Excel 2007/2010/2013/2016/2019 e Office 365 XLSX**

Per aprire un formato Microsoft Excel 2007/2010/2013/2016/2019 e Office 365, ovvero XLSX o XLSB, specificare il percorso del file. Puoi anche usare**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** e impostare i relativi attributi/opzioni del file**ILoadOptions**class per il file modello da caricare.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files.cpp" >}}

Aspose.Cells supporta anche l'apertura di file Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protetti da password.


