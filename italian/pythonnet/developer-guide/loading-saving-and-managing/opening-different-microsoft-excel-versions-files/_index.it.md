---
title: Apertura di diversi file di versioni di Microsoft Excel
type: docs
weight: 20
url: /it/python-net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells può aprire una gamma di diversi file di versioni di Microsoft Excel, come Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura di Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX o file Excel crittografati.

{{% /alert %}}

## **Apertura di file di diverse versioni di Microsoft Excel**

Un'applicazione deve spesso essere in grado di aprire file Microsoft Excel creati in versioni diverse, ad esempio Microsoft Excel 95,97 o Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 . Potrebbe essere necessario caricare un file in uno dei diversi formati, inclusi XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS e così via. Utilizzare il costruttore o specificare il**Cartella di lavoro** classe'**formato del file** type attributo che specifica il formato utilizzando l'**FileFormatType**enumerazione.

 Il**FileFormatType**L'enumerazione contiene molti formati di file predefiniti, alcuni dei quali sono riportati di seguito.

|**Tipi di formati di file**|**Descrizione**|
|:- |:- |
|CSV|Rappresenta un file CSV|
|ECCELLERE_97_TO_2003|Rappresenta un file Excel 97 - 2003|
|XLSX|Rappresenta un file XLSX di Excel 2007/2010/2013/2016/2019 e Office 365|
|XLSM|Rappresenta un file XLSM di Excel 2007/2010/2013/2016/2019 e Office 365|
|XLTX|Rappresenta un file XLTX modello Excel 2007/2010/2013/2016/2019 e Office 365|
|XLTX|Rappresenta un file XLTM abilitato per le macro di Excel 2007/2010/2013/2016/2019 e Office 365|
|XLSB|Rappresenta un file XLSB binario di Excel 2007/2010/2013/2016/2019 e Office 365|
|FOGLIO DI CALCOLO_ML|Rappresenta un file SpreadsheetML|
|TSV|Rappresenta un file di valori separati da tabulazioni|
|TAB_DELIMITED|Rappresenta un file di testo delimitato da tabulazioni|
|ODS|Rappresenta un file ODS|
|HTML|Rappresenta un file HTML|
|M_HTML|Rappresenta un file MHTML|

### **Apertura di file Microsoft Excel 95/5.0**

Per aprire un file Microsoft Excel 95/5.0, utilizzare**LoadOptions**e impostare l'attributo correlato per the**LoadOptions**class per il file modello da caricare. Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[File Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Apertura di file Microsoft Excel 97 - 2003**

 Per aprire un file Microsoft Excel 97 - 2003, utilizzare**LoadOptions** e impostare l'attributo correlato per the**LoadOptions**class per il file modello da caricare.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Apertura di file XLSX di Microsoft Excel 2007/2010/2013/2016/2019 e Office 365**

 Per aprire un formato Microsoft Excel 2007/2010/2013/2016/2019 e Office 365, ovvero XLSX o XLSB, specificare il percorso del file. Puoi anche usare**LoadOptions** e impostare i relativi attributi/opzioni del file**LoadOptions**class per il file modello da caricare.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **Apertura di file Excel crittografati**

 È possibile creare file Excel crittografati utilizzando Microsoft Excel. Per aprire un file crittografato, utilizzare l'estensione**LoadOptions**e impostarne gli attributi e le opzioni (ad esempio, fornire una password) per il file modello da caricare.
Un file di esempio per testare questa funzione può essere scaricato dal seguente link:

[Excel crittografato](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells supporta anche l'apertura di file Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 protetti da password.


