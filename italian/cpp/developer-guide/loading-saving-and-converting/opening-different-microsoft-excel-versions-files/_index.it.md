---
title: Apertura di diversi file di versioni Excel Microsoft
type: docs
weight: 20
url: /it/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells può aprire una serie di diversi file di versioni Excel Microsoft, ad esempio Microsoft Excel 95/97 - 2003, SpreadsheetML, Apertura Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX o En File Excel crittografati.

{{% /alert %}}

##  **Apertura di file di diverse versioni di Excel Microsoft**

 Spesso un'applicazione deve essere in grado di aprire file Excel Microsoft creati in diverse versioni, ad esempio Microsoft Excel 95,97 o Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 . Potrebbe essere necessario caricare un file in uno qualsiasi dei diversi formati, inclusi XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS e così via. Utilizzare il costruttore o specificare il file**[Cartella di lavoro](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)**classe'**[SetFileFormat](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)** metodo per specificare il formato utilizzando il metodo**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**enumerazione.
	
 IL**[FileFormatType](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)**l'enumerazione contiene molti formati di file predefiniti, alcuni dei quali sono riportati di seguito.

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
|FileFormatType_CSV|Rappresenta un file CSV|
|FileFormatType_Excel97To2003|Rappresenta un file Excel 97 - 2003|
|FileFormatType_Xlsx|Rappresenta un file Excel 2007/2010/2013/2016/2019 e Office 365 XLSX|
|FileFormatType_Xlsm|Rappresenta un file Excel 2007/2010/2013/2016/2019 e Office 365 XLSM|
|FileFormatType_Xltx|Rappresenta un file Excel 2007/2010/2013/2016/2019 e Office 365 modello XLTX|
|FileFormatType_Xltm|Rappresenta un file XLTM con attivazione macro di Excel 2007/2010/2013/2016/2019 e Office 365|
|FileFormatType_Xlsb|Rappresenta un file binario XLSB di Excel 2007/2010/2013/2016/2019 e Office 365|
|FileFormatType_SpreadsheetML|Rappresenta un file SpreadsheetML|
|FileFormatType_Tsv|Rappresenta un file di valori separati da tabulazioni|
|FileFormatType_TabDelimited|Rappresenta un file di testo delimitato da tabulazioni|
|FileFormatType_Ods|Rappresenta un file ODS|
|FileFormatType_Html|Rappresenta un file HTML|
|FileFormatType_MHtml|Rappresenta un file MHTML|

###  **Apertura dei file Microsoft Excel 95/5.0**

Per aprire un file Excel 95/5.0 Microsoft, utilizzare**[Opzioni di caricamento](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)**e impostare l'attributo correlato per il**Carica opzioni**classe per il file modello da caricare. Un file di esempio per testare questa funzionalità può essere scaricato dal seguente collegamento:

[File Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

###  **Apertura dei file Microsoft Excel 97 - 2003**

 Per aprire un file Microsoft Excel 97 - 2003, utilizzare**[Opzioni di caricamento](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** e impostare l'attributo correlato per il**Carica opzioni**classe per il file modello da caricare.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

###  **Apertura File Excel 2007/2010/2013/2016/2019 Microsoft e Office 365 XLSX**

Per aprire un formato Microsoft Excel 2007/2010/2013/2016/2019 e Office 365, ovvero XLSX o XLSB, specificare il percorso del file. Puoi anche usare**[Opzioni di caricamento](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)** e impostare gli attributi/opzioni correlati del**Carica opzioni**classe per il file modello da caricare.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells supporta anche l'apertura di file Microsoft Excel 2007, 2010, 2013, 2016, 2019 e Office 365 protetti da password.


