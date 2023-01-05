---
title: Öffnen verschiedener Microsoft Excel-Versionsdateien
type: docs
weight: 20
url: /de/net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells kann eine Reihe verschiedener Microsoft Excel-Versionsdateien öffnen, wie z.

{{% /alert %}}

## **Öffnen von Dateien verschiedener Microsoft Excel-Versionen**

 Eine Anwendung muss häufig Microsoft Excel-Dateien öffnen können, die in verschiedenen Versionen erstellt wurden, z. B. Microsoft Excel 95,97 oder Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 . Möglicherweise müssen Sie eine Datei in einem von mehreren Formaten laden, einschließlich XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited oder TSV, CSV, ODS und so weiter. Verwenden Sie den Konstruktor oder geben Sie die an**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)** Klasse'**[Dateiformat](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)**type-Attribut, das das Format mithilfe von angibt**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**Aufzählung.

 Das**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**Enumeration enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

|**Dateiformattypen**|**Beschreibung**|
|:- |:- |
|CSV|Stellt eine CSV-Datei dar|
|Excel97To2003|Stellt eine Excel 97-2003-Datei dar|
|XLSX|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-XLSX-Datei dar|
|XLSM|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-XLSM-Datei dar|
|Xltx|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Vorlagendatei XLTX dar|
|Xltm|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Makro-aktivierte XLTM-Datei dar|
|XLSB|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Binärdatei XLSB dar|
|SpreadsheetML|Stellt eine SpreadsheetML-Datei dar|
|Tsv|Stellt eine tabulatorgetrennte Wertedatei dar|
|TabDelimited|Stellt eine tabulatorgetrennte Textdatei dar|
|Odds|Stellt eine ODS-Datei dar|
|HTML|Stellt eine HTML-Datei dar|
|HTML|Stellt eine MHTML-Datei dar|

### **Öffnen von Microsoft Excel 95/5.0-Dateien**

Um eine Microsoft Excel 95/5.0-Datei zu öffnen, verwenden Sie**[Ladeoptionen](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**und setzen Sie das zugehörige Attribut für die**[Ladeoptionen](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**Klasse für die zu ladende Vorlagendatei. Eine Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[Excel95-Datei](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Öffnen von Microsoft Excel 97 - 2003-Dateien**

 Verwenden Sie zum Öffnen einer Microsoft Excel 97 - 2003-Datei**[Ladeoptionen](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** und setzen Sie das zugehörige Attribut für die**[Ladeoptionen](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**Klasse für die zu ladende Vorlagendatei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX Dateien**

Um ein Microsoft Excel 2007/2010/2013/2016/2019- und Office 365-Format zu öffnen, d. h. XLSX oder XLSB, geben Sie den Dateipfad an. Sie können auch verwenden**[Ladeoptionen](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** und legen Sie die zugehörigen Attribute/Optionen der fest**[Ladeoptionen](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**Klasse für die zu ladende Vorlagendatei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Öffnen verschlüsselter Excel-Dateien**

 Es ist möglich, verschlüsselte Excel-Dateien mit Microsoft Excel zu erstellen. Um eine verschlüsselte Datei zu öffnen, verwenden Sie die**[Ladeoptionen](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**und seine Attribute und Optionen (z. B. ein Passwort vergeben) für die zu ladende Vorlagendatei festlegen.
Eine Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[Verschlüsseltes Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells unterstützt auch das Öffnen passwortgeschützter Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-Dateien.


