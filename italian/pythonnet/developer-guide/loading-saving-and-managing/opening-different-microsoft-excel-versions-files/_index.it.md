---
title: Apertura di file di diverse versioni di Microsoft Excel
type: docs
weight: 20
url: /it/python-net/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells può aprire una serie di diversi file di versioni di Microsoft Excel, come Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura di file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX o file di Excel crittografati.

{{% /alert %}}

## **Apertura di file di diverse versioni di Microsoft Excel**

Un'applicazione spesso deve essere in grado di aprire file Microsoft Excel creati in diverse versioni, ad esempio, Microsoft Excel 95, 97, o Microsoft Excel 2007/2010/2013/2016/2019 e Office 365. Potrebbe essere necessario caricare un file in uno qualsiasi dei vari formati, inclusi XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited or TSV, CSV, ODS e così via. Utilizzare il costruttore, o specificare l'attributo di tipo **file_format** della classe **Workbook** utilizzando l'enumerazione **FileFormatType**.

L'enumerazione **FileFormatType** contiene molti formati file predefiniti, alcuni dei quali sono riportati di seguito.

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
| CSV | Rappresenta un file CSV |
|EXCEL_97_TO_2003|Rappresenta un file Excel 97 - 2003|
|XLSX|Rappresenta un file XLSX Excel 2007/2010/2013/2016/2019 e Office 365|
|XLSM|Rappresenta un file XLSM Excel 2007/2010/2013/2016/2019 e Office 365|
|Xltx|Rappresenta un file modello XLTX di Excel 2007/2010/2013/2016/2019 e Office 365|
|XLTX|Rappresenta un file XLTM abilitato per macro Excel 2007/2010/2013/2016/2019 e Office 365|
|XLSB|Rappresenta un file XLSB binario Excel 2007/2010/2013/2016/2019 e Office 365|
|SPREADSHEET_ML|Rappresenta un file SpreadsheetML|
|TSV|Rappresenta un file di valori separati da tabulazione|
|TAB_DELIMITED|Rappresenta un file di testo delimitato da tabulazioni|
|ODS|Rappresenta un file ODS|
|HTML|Rappresenta un file HTML|
|M_HTML|Rappresenta un file MHTML|

### **Apertura di file Microsoft Excel 95/5.0**

Per aprire un file Microsoft Excel 95/5.0, utilizzare **LoadOptions** e impostare l'attributo correlato per la classe **LoadOptions**.

[File di Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Apertura dei file Microsoft Excel 97 - 2003**

Per aprire un file Microsoft Excel 97 - 2003, utilizzare **LoadOptions** e impostare l'attributo relativo per la classe **LoadOptions** per il file del modello da caricare.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Apertura dei file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX**

Per aprire un formato Microsoft Excel 2007/2010/2013/2016/2019 e Office 365, cioè XLSX o XLSB, specificare il percorso del file. È anche possibile utilizzare **LoadOptions** e impostare l'attributo/opzioni correlati della classe **LoadOptions** per il file del modello da caricare.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **Apertura di file Excel criptati**

È possibile creare file Excel criptati utilizzando Microsoft Excel. Per aprire un file criptato, utilizzare **LoadOptions** e impostare i relativi attributi e opzioni (ad esempio, dare una password) per il file del modello da caricare.
Un file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells supporta anche l'apertura di file Microsoft Excel 2007, 2010, 2013, 2016, 2019 e Office 365 protetti da password.


