---
title: Apertura di file di diverse versioni di Microsoft Excel
type: docs
weight: 20
url: /it/python-java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells può aprire una serie di diversi file di versioni di Microsoft Excel, come Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura di file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX o file di Excel crittografati.

{{% /alert %}}

## **Apertura di file di diverse versioni di Microsoft Excel**

Spesso un'applicazione deve essere in grado di aprire file Microsoft Excel creati in diverse versioni, ad esempio Microsoft Excel 95, 97, o Microsoft Excel 2007/2010/2013/2016/2019 e Office 365. Potrebbe essere necessario caricare un file in uno dei vari formati, tra cui XLS, XLSX, XLSM, XLSB, SpreadsheetML, tabulati o TSV, CSV, ODS e così via. Utilizzare il costruttore, o specificare il metodo [**setFileFormat**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#FileFormat) della classe [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) per specificare il formato utilizzando l'enumerazione [**FileFormatType**](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType).

L'enumerazione [**FileFormatType**](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType) contiene molti formati di file predefiniti alcuni dei quali sono elencati di seguito.

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

Per aprire un file Microsoft Excel 95/5.0, utilizzare [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) e impostare l'attributo correlato per la classe **LoadOptions** per il file del modello da caricare. È possibile scaricare un file di esempio per testare questa funzionalità dal seguente link:

[File di Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel95Files.py" >}}

### **Apertura dei file Microsoft Excel 97 - 2003**

Per aprire un file Microsoft Excel 97 - 2003, utilizzare [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) e impostare l'attributo correlato per la classe **LoadOptions** per il file del modello da caricare.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel97-2003Files.py" >}}

### **Apertura dei file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX**

Per aprire un file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365, cioè XLSX o XLSB, specificare il percorso del file. È inoltre possibile utilizzare [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) e impostare gli attributi/opzioni correlati della classe **LoadOptions** per il file del modello da caricare.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel2007Files.py" >}}

### **Apertura di file Excel criptati**

È possibile creare file Excel crittografati utilizzando Microsoft Excel. Per aprire un file crittografato, utilizzare [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) e impostare i suoi attributi e opzioni (ad esempio, fornire una password) per il file del modello da caricare.
Un file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells supporta anche l'apertura di file Microsoft Excel 2007, 2010, 2013, 2016, 2019 e Office 365 protetti da password.


