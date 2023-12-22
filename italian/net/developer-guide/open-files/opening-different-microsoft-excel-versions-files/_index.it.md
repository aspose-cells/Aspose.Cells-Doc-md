---
title: Apri diversi file di versioni Excel Microsoft
type: docs
weight: 20
url: /it/net/opening-different-microsoft-excel-versions-files/
description: Questo articolo spiega come aprire file di diverse versioni di Excel utilizzando Aspose.Cells for .NET API.
keywords: C# Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
---
{{% alert color="primary" %}}

Aspose.Cells può aprire una serie di diversi file di versioni Excel Microsoft, ad esempio Microsoft Excel 95/97 - 2003, SpreadsheetML, Apertura Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX o En File Excel crittografati.

{{% /alert %}}

##  **Come aprire file di diverse versioni di Excel Microsoft**

 Spesso un'applicazione deve essere in grado di aprire file Excel Microsoft creati in diverse versioni, ad esempio Microsoft Excel 95,97 o Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 . Potrebbe essere necessario caricare un file in uno qualsiasi dei diversi formati, inclusi XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited o TSV, CSV, ODS e così via. Utilizzare il costruttore o specificare il file**[Cartella di lavoro](https://reference.aspose.com/cells/net/aspose.cells/workbook)**classe'**[Formato file](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** type attributo che specifica il formato utilizzando l'**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**enumerazione.

 IL**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**l'enumerazione contiene molti formati di file predefiniti, alcuni dei quali sono riportati di seguito.

|**Tipi di formato file**|**Descrizione**|
| :- | :- |
|CSV|Rappresenta un file CSV|
|Excel97To2003|Rappresenta un file Excel 97 - 2003|
|Xlsx|Rappresenta un file Excel 2007/2010/2013/2016/2019 e Office 365 XLSX|
|Xlsm|Rappresenta un file Excel 2007/2010/2013/2016/2019 e Office 365 XLSM|
|Xltx|Rappresenta un file Excel 2007/2010/2013/2016/2019 e Office 365 modello XLTX|
|Xltm|Rappresenta un file XLTM con attivazione macro di Excel 2007/2010/2013/2016/2019 e Office 365|
|Xlsb|Rappresenta un file binario XLSB di Excel 2007/2010/2013/2016/2019 e Office 365|
|SpreadsheetML|Rappresenta un file SpreadsheetML|
|Tsv|Rappresenta un file di valori separati da tabulazioni|
|TabDelimited|Rappresenta un file di testo delimitato da tabulazioni|
|Odd|Rappresenta un file ODS|
|HTML|Rappresenta un file HTML|
|Mhtml|Rappresenta un file MHTML|

###  **Aprire i file Excel 95/5.0 Microsoft**

Per aprire un file Excel 95/5.0 Microsoft, utilizzare**[Opzioni di caricamento](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**e impostare l'attributo correlato per il**[Opzioni di caricamento](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**classe per il file modello da caricare. Un file di esempio per testare questa funzionalità può essere scaricato dal seguente collegamento:

[File Excel95](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

###  **Aprire i file Microsoft Excel 97 - 2003**

 Per aprire un file Microsoft Excel 97 - 2003, utilizzare**[Opzioni di caricamento](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** e impostare l'attributo correlato per il**[Opzioni di caricamento](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**classe per il file modello da caricare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

###  **Apri i file Microsoft Excel 2007/2010/2013/2016/2019 e Office 365 XLSX**

Per aprire un formato Microsoft Excel 2007/2010/2013/2016/2019 e Office 365, ovvero XLSX o XLSB, specificare il percorso del file. Puoi anche usare**[Opzioni di caricamento](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** e impostare gli attributi/opzioni correlati del**[Opzioni di caricamento](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**classe per il file modello da caricare.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

###  **Apri file Excel crittografati**

 È possibile creare file Excel crittografati utilizzando Microsoft Excel. Per aprire un file crittografato, utilizzare il file**[Opzioni di caricamento](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**e impostarne gli attributi e le opzioni (ad esempio, fornire una password) per il file modello da caricare.
Un file di esempio per testare questa funzionalità può essere scaricato dal seguente collegamento:

[Excel crittografato](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells supporta anche l'apertura di file Microsoft Excel 2007, 2010, 2013, 2016, 2019 e Office 365 protetti da password.


