---
title: Öffnen verschiedener Microsoft Excel-Versionsdateien
type: docs
weight: 20
url: /de/python-net/opening-different-microsoft-excel-versions-files/
---
{{% alert color="primary" %}}

Aspose.Cells kann eine Reihe verschiedener Microsoft Excel-Versionsdateien öffnen, wie z.

{{% /alert %}}

## **Öffnen von Dateien verschiedener Microsoft Excel-Versionen**

 Eine Anwendung muss häufig Microsoft Excel-Dateien öffnen können, die in verschiedenen Versionen erstellt wurden, z. B. Microsoft Excel 95,97 oder Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 . Möglicherweise müssen Sie eine Datei in einem von mehreren Formaten laden, einschließlich XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited oder TSV, CSV, ODS und so weiter. Verwenden Sie den Konstruktor oder geben Sie die an**Arbeitsmappe** Klasse'**Datei Format**type-Attribut, das das Format mithilfe von angibt**Dateiformattyp**Aufzählung.

 Das**Dateiformattyp**Enumeration enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

|**Dateiformattypen**|**Beschreibung**|
|:- |:- |
|CSV|Stellt eine CSV-Datei dar|
|AUSGEZEICHNET_97_BIS_2003|Stellt eine Excel 97-2003-Datei dar|
|XLSX|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-XLSX-Datei dar|
|XLSM|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-XLSM-Datei dar|
|Xltx|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Vorlagendatei XLTX dar|
|XLTX|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Makro-aktivierte XLTM-Datei dar|
|XLSB|Stellt eine Excel 2007/2010/2013/2016/2019- und Office 365-Binärdatei XLSB dar|
|SPREADSHEET_ML|Stellt eine SpreadsheetML-Datei dar|
|TSV|Stellt eine tabulatorgetrennte Wertedatei dar|
|TAB_DELIMITED|Stellt eine tabulatorgetrennte Textdatei dar|
|ODS|Stellt eine ODS-Datei dar|
|HTML|Stellt eine HTML-Datei dar|
|M_HTML|Stellt eine MHTML-Datei dar|

### **Öffnen von Microsoft Excel 95/5.0-Dateien**

Um eine Microsoft Excel 95/5.0-Datei zu öffnen, verwenden Sie**Ladeoptionen**und setzen Sie das zugehörige Attribut für die**Ladeoptionen**Klasse für die zu ladende Vorlagendatei. Eine Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[Excel95-Datei](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Öffnen von Microsoft Excel 97 - 2003-Dateien**

 Verwenden Sie zum Öffnen einer Microsoft Excel 97 - 2003-Datei**Ladeoptionen** und setzen Sie das zugehörige Attribut für die**Ladeoptionen**Klasse für die zu ladende Vorlagendatei.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX Dateien**

Um ein Microsoft Excel 2007/2010/2013/2016/2019- und Office 365-Format zu öffnen, d. h. XLSX oder XLSB, geben Sie den Dateipfad an. Sie können auch verwenden**Ladeoptionen** und legen Sie die zugehörigen Attribute/Optionen der fest**Ladeoptionen**Klasse für die zu ladende Vorlagendatei.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **Öffnen verschlüsselter Excel-Dateien**

 Es ist möglich, verschlüsselte Excel-Dateien mit Microsoft Excel zu erstellen. Um eine verschlüsselte Datei zu öffnen, verwenden Sie die**Ladeoptionen**und seine Attribute und Optionen (z. B. ein Passwort vergeben) für die zu ladende Vorlagendatei festlegen.
Eine Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[Verschlüsseltes Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells unterstützt auch das Öffnen passwortgeschützter Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-Dateien.


