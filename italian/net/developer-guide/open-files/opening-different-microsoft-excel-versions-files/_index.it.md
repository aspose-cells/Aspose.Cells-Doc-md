---
title: Apri diversi file di Microsoft Excel in versioni diverse
type: docs
weight: 20
url: /it/net/opening-different-microsoft-excel-versions-files/
description: Questo articolo spiega come aprire file di diverse versioni di Excel utilizzando l API Aspose.Cells for .NET.
keywords: Aprire diversi file di Microsoft Excel in C#, come apro file Excel criptati.
---

{{% alert color="primary" %}}

Aspose.Cells può aprire una serie di diversi file di versioni di Microsoft Excel, come Microsoft Excel 95/97 - 2003, SpreadsheetML, apertura di file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX o file di Excel crittografati.

{{% /alert %}}

## **Come aprire file di diverse versioni di Microsoft Excel**

Un'applicazione deve spesso essere in grado di aprire file di Microsoft Excel creati in diverse versioni, ad esempio, Microsoft Excel 95, 97, o Microsoft Excel 2007/2010/2013/2016/2019 e Office 365. Potrebbe essere necessario caricare un file in uno qualsiasi dei diversi formati, tra cui XLS, XLSX, XLSM, XLSB, SpreadsheetML, tabella delimitata o TSV, CSV, ODS e così via. Utilizzare il costruttore, o specificare l'attributo di tipo della classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) che specifica il formato usando l'enumerazione [**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype).

L'enumerazione [**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype) contiene molti formati di file predefiniti alcuni dei quali sono elencati di seguito.

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
|Csv|Rappresenta un file CSV|
|Excel97To2003| Rappresenta un file Excel 97 - 2003 |
|Xlsx|Rappresenta un file XLSX Excel 2007/2010/2013/2016/2019 e Office 365|
|Xlsm|Rappresenta un file XLSM Excel 2007/2010/2013/2016/2019 e Office 365|
|Xltx|Rappresenta un file modello XLTX di Excel 2007/2010/2013/2016/2019 e Office 365|
|Xltm|Rappresenta un file XLTM macro abilitato di Excel 2007/2010/2013/2016/2019 e Office 365|
|Xlsb|Rappresenta un file XLSB binario di Excel 2007/2010/2013/2016/2019 e Office 365|
|SpreadsheetML|Rappresenta un file SpreadsheetML|
|Tsv|Rappresenta un file di valori separati da tabulazioni|
|TabDelimited|Rappresenta un file di testo delimitato da tabulazioni|
|Ods|Rappresenta un file ODS|
|Html|Rappresenta un file HTML|
|Mhtml|Rappresenta un file MHTML|

### **Apri file Microsoft Excel 95/5.0**

Per aprire un file di Microsoft Excel 95/5.0, utilizza [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) e imposta l'attributo relativo per la classe [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) per il file modello da caricare. Un file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[File di Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Apri file Microsoft Excel 97 - 2003**

Per aprire un file di Microsoft Excel 97 - 2003, utilizza [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) e imposta l'attributo relativo per la classe [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) per il file modello da caricare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Apri file XLSX di Microsoft Excel 2007/2010/2013/2016/2019 e Office 365**

Per aprire un file in formato Microsoft Excel 2007/2010/2013/2016/2019 e Office 365, cioè XLSX o XLSB, specifica il percorso del file. Puoi anche utilizzare [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) e impostare l'attributo/opzioni correlati della classe [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) per il file modello da caricare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Apri file Excel criptati**

È possibile creare file Excel crittografati utilizzando Microsoft Excel. Per aprire un file crittografato, utilizzare [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) e impostare i suoi attributi e opzioni (ad esempio, fornire una password) per il file del modello da caricare.
Un file di esempio per testare questa funzionalità può essere scaricato dal seguente link:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells supporta anche l'apertura di file Microsoft Excel 2007, 2010, 2013, 2016, 2019 e Office 365 protetti da password.


