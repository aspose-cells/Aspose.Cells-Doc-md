---
title: Apertura di diversi file di versioni di Excel Microsoft
type: docs
weight: 20
url: /it/net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells può aprire una gamma di diversi file di versioni di Excel Microsoft, come Microsoft Excel 95/97 - 2003, SpreadsheetML, Apertura Microsoft di Excel 2007/2010/2013/2016/2019 e Office 365 XLSX o file Excel crittografati.

{{% /alert %}}

## **Apertura di file di diverse versioni di Excel Microsoft**

 Un'applicazione spesso deve essere in grado di aprire file Excel Microsoft creati in versioni diverse, ad esempio Microsoft Excel 95,97 o Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 . Potrebbe essere necessario caricare un file in uno dei diversi formati, inclusi XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS e così via. Utilizzare il costruttore o specificare il**[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** classe'**[Formato file](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)**type attributo che specifica il formato utilizzando l'**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**enumerazione.

 Il**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**L'enumerazione contiene molti formati di file predefiniti, alcuni dei quali sono riportati di seguito.

|**Tipi di formati di file**|**Descrizione**|
|:- |:- |
|Csv|Rappresenta un file CSV|
|Excel97To2003|Rappresenta un file Excel 97 - 2003|
|Xlsx|Rappresenta un file Excel 2007/2010/2013/2016/2019 e Office 365 XLSX|
|XLSM|Rappresenta un file Excel 2007/2010/2013/2016/2019 e Office 365 XLSM|
|XLTX|Rappresenta un file modello XLTX di Excel 2007/2010/2013/2016/2019 e Office 365|
|Xltm|Rappresenta un file XLTM abilitato per le macro di Excel 2007/2010/2013/2016/2019 e Office 365|
|Xlsb|Rappresenta un file binario XLSB di Excel 2007/2010/2013/2016/2019 e Office 365|
|SpreadsheetML|Rappresenta un file SpreadsheetML|
|Tsv|Rappresenta un file di valori separati da tabulazioni|
|TabDelimited|Rappresenta un file di testo delimitato da tabulazioni|
|Odd|Rappresenta un file ODS|
|HTML|Rappresenta un file HTML|
|HTML|Rappresenta un file MHTML|

### **Apertura di file Excel 95/5.0 Microsoft**

Per aprire un file Excel 95/5.0 Microsoft, utilizzare**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**e impostare l'attributo correlato per the**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**class per il file modello da caricare. Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[File Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Apertura Microsoft Excel 97 - 2003 File**

 Per aprire un file Microsoft Excel 97 - 2003, utilizzare**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** e impostare l'attributo correlato per the**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**class per il file modello da caricare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Apertura Microsoft File Excel 2007/2010/2013/2016/2019 e Office 365 XLSX**

Per aprire un formato Microsoft Excel 2007/2010/2013/2016/2019 e Office 365, ovvero XLSX o XLSB, specificare il percorso del file. Puoi anche usare**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** e impostare i relativi attributi/opzioni del file**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**class per il file modello da caricare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Apertura di file Excel crittografati**

 È possibile creare file Excel crittografati utilizzando Microsoft Excel. Per aprire un file crittografato, utilizzare l'estensione**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**e impostarne gli attributi e le opzioni (ad esempio, fornire una password) per il file modello da caricare.
Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[Excel crittografato](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells supporta anche l'apertura di file Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protetti da password.


