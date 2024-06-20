---
title: Öffnen von verschiedenen Microsoft Excel Versionen Dateien
type: docs
weight: 20
url: /de/python-net/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells kann eine Vielzahl von verschiedenen Microsoft Excel-Versionen-Dateien öffnen, wie z.B. Microsoft Excel 95/97 - 2003, SpreadsheetML, Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX oder verschlüsselten Excel-Dateien.

{{% /alert %}}

## **Öffnen von Dateien verschiedener Microsoft Excel-Versionen**

Eine Anwendung muss oft in der Lage sein, Microsoft Excel-Dateien zu öffnen, die in verschiedenen Versionen erstellt wurden, z. B. Microsoft Excel 95, 97, oder Microsoft Excel 2007/2010/2013/2016/2019 und Office 365. Es kann erforderlich sein, eine Datei in einem bestimmten Format zu laden, darunter XLS, XLSX, XLSM, XLSB, SpreadsheetML, Tabulatorgetrennt oder TSV, CSV, ODS usw. Verwenden Sie den Konstruktor oder geben Sie das Attribut **file_format** der **Workbook**-Klasse an, das das Format mithilfe der **FileFormatType**-Enumeration festlegt.

Die Enumeration **FileFormatType** enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

|**Dateiformat-Typen**|**Beschreibung**|
| :- | :- |
|CSV|Repräsentiert eine CSV-Datei|
|EXCEL_97_TO_2003|Repräsentiert eine Excel 97 - 2003 Datei|
|XLSX|Repräsentiert eine Excel 2007/2010/2013/2016/2019 und Office 365 XLSX-Datei|
|XLSM|Repräsentiert eine Excel 2007/2010/2013/2016/2019 und Office 365 XLSM-Datei|
|Xltx|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365-Vorlage XLTX-Datei dar|
|XLTX|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 makrofähige XLTM-Datei dar|
|XLSB|Repräsentiert eine Excel 2007/2010/2013/2016/2019 und Office 365 binäre XLSB-Datei|
|SPREADSHEET_ML|Repräsentiert eine SpreadsheetML-Datei|
|TSV|Repräsentiert eine durch Tabulatoren getrennte Werte-Datei|
|TAB_DELIMITED|Repräsentiert eine tabulatorgetrennte Textdatei|
|ODS|Repräsentiert eine ODS-Datei|
|HTML|Repräsentiert eine HTML-Datei|
|M_HTML|Repräsentiert eine MHTML-Datei|

### **Öffnen von Microsoft Excel 95/5.0-Dateien**

Um eine Microsoft Excel 95/5.0-Datei zu öffnen, verwenden Sie **LoadOptions** und legen Sie das entsprechende Attribut für die **LoadOptions**-Klasse der zu ladenden Vorlagendatei fest. Eine Beispieldatei zur Überprüfung dieser Funktion kann von folgendem Link heruntergeladen werden:

[Excel95-Datei](Excel95.xls)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel95Files.py" >}}

### **Öffnen von Microsoft Excel 97 - 2003-Dateien**

Um eine Microsoft Excel 97 - 2003-Datei zu öffnen, verwenden Sie **LoadOptions** und legen Sie das entsprechende Attribut für die **LoadOptions**-Klasse der zu ladenden Vorlagendatei fest.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel97-2003Files.py" >}}

### **Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX-Dateien**

Um ein Microsoft Excel 2007/2010/2013/2016/2019 und Office 365-Format, das heißt XLSX oder XLSB, zu öffnen, geben Sie den Dateipfad an. Sie können auch ** LoadOptions ** verwenden und das zugehörige Attribut/Optionen der ** LoadOptions ** Klasse für die zu ladende Vorlagendatei festlegen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenExcel2007Files.py" >}}

### **Öffnen verschlüsselter Excel-Dateien**

Es ist möglich, verschlüsselte Excel-Dateien mit Microsoft Excel zu erstellen. Um eine verschlüsselte Datei zu öffnen, verwenden Sie die ** LoadOptions ** und setzen Sie deren Attribute und Optionen (zum Beispiel ein Passwort) für die zu ladende Vorlagendatei.
Eine Beispieldatei zum Testen dieses Features kann über folgenden Link heruntergeladen werden:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells unterstützt auch das Öffnen von passwortgeschützten Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-Dateien.


