---
title: Öffnen von verschiedenen Microsoft Excel Versionen Dateien
type: docs
weight: 20
url: /de/python-java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells kann eine Vielzahl von verschiedenen Microsoft Excel-Versionen-Dateien öffnen, wie z.B. Microsoft Excel 95/97 - 2003, SpreadsheetML, Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX oder verschlüsselten Excel-Dateien.

{{% /alert %}}

## **Öffnen von Dateien verschiedener Microsoft Excel-Versionen**

Eine Anwendung muss oft in der Lage sein, Microsoft Excel-Dateien in verschiedenen Versionen zu öffnen, z. B. Microsoft Excel 95, 97 oder Microsoft Excel 2007/2010/2013/2016/2019 und Office 365. Möglicherweise müssen Sie eine Datei in einem der verschiedenen Formate laden, darunter XLS, XLSX, XLSM, XLSB, SpreadsheetML, Tab-getrennt oder TSV, CSV, ODS und so weiter. Verwenden Sie den Konstruktor oder geben Sie die Methode der Klasse [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) an, um das Format mit der [**setFileFormat**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#FileFormat)-Enumeration anzugeben.

Die [**FileFormatType**](https://reference.aspose.com/cells/python-java/asposecells.api/FileFormatType)-Enumeration enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

|**Dateiformat-Typen**|**Beschreibung**|
| :- | :- |
|CSV|Repräsentiert eine CSV-Datei|
|EXCEL_97_TO_2003|Repräsentiert eine Excel 97 - 2003 Datei|
|XLSX|Repräsentiert eine Excel 2007/2010/2013/2016/2019 und Office 365 XLSX-Datei|
|XLSM|Repräsentiert eine Excel 2007/2010/2013/2016/2019 und Office 365 XLSM-Datei|
|XLTX|Repräsentiert eine Excel 2007/2010/2013/2016/2019 und Office 365 Vorlagen-XLTX-Datei|
|XLTM|Repräsentiert eine Excel 2007/2010/2013/2016/2019 und Office 365 makrofähige XLTM-Datei|
|XLSB|Repräsentiert eine Excel 2007/2010/2013/2016/2019 und Office 365 binäre XLSB-Datei|
|SPREADSHEET_ML|Repräsentiert eine SpreadsheetML-Datei|
|TSV|Repräsentiert eine durch Tabulatoren getrennte Werte-Datei|
|TAB_DELIMITED|Repräsentiert eine tabulatorgetrennte Textdatei|
|ODS|Repräsentiert eine ODS-Datei|
|HTML|Repräsentiert eine HTML-Datei|
|M_HTML|Repräsentiert eine MHTML-Datei|

### **Öffnen von Microsoft Excel 95/5.0-Dateien**

Um eine Datei von Microsoft Excel 95/5.0 zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) und setzen Sie das zugehörige Attribut für die Klasse **LoadOptions** für die zu ladende Vorlagendatei. Eine Beispieldatei zur Überprüfung dieses Features kann über den folgenden Link heruntergeladen werden:

[Excel95-Datei](Excel95.xls)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel95Files.py" >}}

### **Öffnen von Microsoft Excel 97 - 2003-Dateien**

Um eine Datei von Microsoft Excel 97 - 2003 zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) und setzen Sie das zugehörige Attribut für die Klasse **LoadOptions** für die zu ladende Vorlagendatei.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel97-2003Files.py" >}}

### **Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX-Dateien**

Um ein Microsoft Excel 2007/2010/2013/2016/2019 und Office 365-Format, d.h. XLSX oder XLSB, zu öffnen, geben Sie den Dateipfad an. Sie können auch [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) verwenden und das zugehörige Attribut/Optionen der Klasse **LoadOptions** für die zu ladende Vorlagendatei festlegen.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenExcel2007Files.py" >}}

### **Öffnen verschlüsselter Excel-Dateien**

Es ist möglich, verschlüsselte Excel-Dateien mit Microsoft Excel zu erstellen. Um eine verschlüsselte Datei zu öffnen, verwenden Sie die [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) und legen deren Attribute und Optionen fest (z. B. geben Sie ein Passwort) für die zu ladende Vorlagendatei.
Eine Beispieldatei zum Testen dieses Features kann über folgenden Link heruntergeladen werden:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenEncryptedExcelFiles.py" >}}

Aspose.Cells unterstützt auch das Öffnen von passwortgeschützten Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-Dateien.


