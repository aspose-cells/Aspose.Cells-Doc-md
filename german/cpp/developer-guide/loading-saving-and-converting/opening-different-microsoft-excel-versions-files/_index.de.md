---
title: Öffnen verschiedener Microsoft Excel-Versionsdateien
type: docs
weight: 20
url: /de/cpp/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells kann eine Reihe verschiedener Microsoft Excel-Versionsdateien öffnen, wie z.

{{% /alert %}}

## **Öffnen von Dateien verschiedener Microsoft Excel-Versionen**

 Eine Anwendung muss häufig Microsoft Excel-Dateien öffnen können, die in verschiedenen Versionen erstellt wurden, z. B. Microsoft Excel 95,97 oder Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 . Möglicherweise müssen Sie eine Datei in einem von mehreren Formaten laden, einschließlich XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited oder TSV, CSV, ODS und so weiter. Verwenden Sie den Konstruktor oder geben Sie die an**[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)** Klasse'**[SetFileFormat](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#aa74a10e0aa88e3a8386ea328165896dc)**Methode bis gibt das Format unter Verwendung von an**[Dateiformattyp](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**Aufzählung.
	
 Das**[Dateiformattyp](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a7831f25a251b1cd95079f091aa1faf40)**Enumeration enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

|**Dateiformattypen**|**Beschreibung**|
|:- |:- |
|FileFormatType_CSV|Stellt eine CSV-Datei dar|
|FileFormatType_Excel97To2003|Stellt eine Excel 97-2003-Datei dar|
|FileFormatType_Xlsx|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-XLSX-Datei dar|
|FileFormatType_Xlsm|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-XLSM-Datei dar|
|FileFormatType_Xltx|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Vorlagendatei XLTX dar|
|FileFormatType_Xltm|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Makro-aktivierte XLTM-Datei dar|
|FileFormatType_Xlsb|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Binärdatei XLSB dar|
|FileFormatType_SpreadsheetML|Stellt eine SpreadsheetML-Datei dar|
|FileFormatType_Tsv|Stellt eine tabulatorgetrennte Wertedatei dar|
|FileFormatType_TabDelimited|Stellt eine tabulatorgetrennte Textdatei dar|
|FileFormatType_Ods|Stellt eine ODS-Datei dar|
|FileFormatType_Html|Stellt eine HTML-Datei dar|
|FileFormatType_MHtml|Stellt eine MHTML-Datei dar|

### **Öffnen von Microsoft Excel 95/5.0-Dateien**

Um eine Microsoft Excel 95/5.0-Datei zu öffnen, verwenden Sie**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)**und setzen Sie das zugehörige Attribut für die**ILoadOptions**Klasse für die zu ladende Vorlagendatei. Eine Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[Excel95-Datei](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files.cpp" >}}

### **Öffnen von Microsoft Excel 97 - 2003-Dateien**

 Verwenden Sie zum Öffnen einer Microsoft Excel 97 - 2003-Datei**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** und setzen Sie das zugehörige Attribut für die**ILoadOptions**Klasse für die zu ladende Vorlagendatei.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files.cpp" >}}

### **Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX Dateien**

Um ein Microsoft Excel 2007/2010/2013/2016/2019- und Office 365-Format zu öffnen, d. h. XLSX oder XLSB, geben Sie den Dateipfad an. Sie können auch verwenden**[ILoadOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_load_options)** und legen Sie die zugehörigen Attribute/Optionen der fest**ILoadOptions**Klasse für die zu ladende Vorlagendatei.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files.cpp" >}}

Aspose.Cells unterstützt auch das Öffnen passwortgeschützter Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-Dateien.


