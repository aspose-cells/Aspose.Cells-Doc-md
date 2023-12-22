---
title: Öffnen Sie verschiedene Microsoft Excel-Versionsdateien
type: docs
weight: 20
url: /de/net/opening-different-microsoft-excel-versions-files/
description: In diesem Artikel wird erläutert, wie Sie verschiedene Excel-Versionsdateien mit Aspose.Cells, for .NET und API öffnen.
keywords: C# Open Different Microsoft Excel file, How do I open Encrypted Excel Files.
---
{{% alert color="primary" %}}

Aspose.Cells kann eine Reihe verschiedener Microsoft Excel-Versionsdateien öffnen, z. B. Microsoft Excel 95/97 - 2003, SpreadsheetML, Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX oder Encrypt ed Excel-Dateien.

{{% /alert %}}

##  **So öffnen Sie Dateien verschiedener Microsoft Excel-Versionen**

 Eine Anwendung muss oft in der Lage sein, Microsoft Excel-Dateien zu öffnen, die in verschiedenen Versionen erstellt wurden, zum Beispiel Microsoft Excel 95,97 oder Microsoft Excel 2007/2010/2013/2016/2019 und Office 365. Möglicherweise müssen Sie eine Datei in einem von mehreren Formaten laden, einschließlich XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited oder TSV, CSV, ODS und so weiter. Verwenden Sie den Konstruktor oder geben Sie den an**[Arbeitsmappe](https://reference.aspose.com/cells/net/aspose.cells/workbook)**Klasse'**[Dateiformat](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/fileformat)** Typattribut, das das Format mit dem angibt**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**Aufzählung.

 Der**[FileFormatType](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)**Die Aufzählung enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

|**Dateiformattypen**|**Beschreibung**|
| :- | :- |
|Csv|Stellt eine CSV-Datei dar|
|Excel97To2003|Stellt eine Excel 97 - 2003-Datei dar|
|Xlsx|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365 XLSX-Datei dar|
|Xlsm|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365 XLSM-Datei dar|
|Xltx|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Vorlagendatei XLTX dar|
|Xltm|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Makro-fähige XLTM-Datei dar|
|Xlsb|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Binärdatei XLSB dar|
|SpreadsheetML|Stellt eine SpreadsheetML-Datei dar|
|Tsv|Stellt eine tabulatorgetrennte Wertedatei dar|
|TabDelimited|Stellt eine tabulatorgetrennte Textdatei dar|
|Quoten|Stellt eine ODS-Datei dar|
|HTML|Stellt eine HTML-Datei dar|
|Mhtml|Stellt eine MHTML-Datei dar|

###  **Öffnen Sie Microsoft Excel 95/5.0-Dateien**

Um eine Microsoft Excel 95/5.0-Datei zu öffnen, verwenden Sie**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**und legen Sie das zugehörige Attribut für fest**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**Klasse für die zu ladende Vorlagendatei. Eine Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[Excel95-Datei](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

###  **Öffnen Sie Microsoft Excel 97 - 2003-Dateien**

 Um eine Microsoft Excel 97 - 2003-Datei zu öffnen, verwenden Sie**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** und legen Sie das zugehörige Attribut für fest**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**Klasse für die zu ladende Vorlagendatei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

###  **Öffnen Sie Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX Dateien**

Um ein Microsoft Excel 2007/2010/2013/2016/2019- und Office 365-Format zu öffnen, also XLSX oder XLSB, geben Sie den Dateipfad an. Sie können auch verwenden**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** und legen Sie die zugehörigen Attribute/Optionen fest**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**Klasse für die zu ladende Vorlagendatei.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

###  **Öffnen Sie verschlüsselte Excel-Dateien**

 Es ist möglich, verschlüsselte Excel-Dateien mit Microsoft Excel zu erstellen. Um eine verschlüsselte Datei zu öffnen, verwenden Sie die**[LoadOptions](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)**und legen Sie seine Attribute und Optionen fest (z. B. ein Passwort vergeben), damit die Vorlagendatei geladen werden kann.
Eine Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[Verschlüsseltes Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells unterstützt auch das Öffnen passwortgeschützter Microsoft Excel 2007, 2010, 2013, 2016, 2019 und Office 365-Dateien.


