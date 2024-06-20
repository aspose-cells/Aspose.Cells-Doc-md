---
title: Öffnen von verschiedenen Microsoft Excel Versionen Dateien
type: docs
weight: 20
url: /de/java/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells kann eine Vielzahl von verschiedenen Microsoft Excel-Versionen-Dateien öffnen, wie z.B. Microsoft Excel 95/97 - 2003, SpreadsheetML, Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX oder verschlüsselten Excel-Dateien.

{{% /alert %}}

## **Öffnen von Dateien verschiedener Microsoft Excel-Versionen**

Eine Anwendung muss oft in der Lage sein, Microsoft Excel-Dateien in verschiedenen Versionen zu öffnen, beispielsweise Microsoft Excel 95, 97 oder Microsoft Excel 2007/2010/2013/2016/2019 und Office 365. Sie müssen möglicherweise eine Datei in einem von mehreren Formaten laden, einschließlich XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited oder TSV, CSV, ODS usw. Verwenden Sie den Konstruktor oder verwenden Sie die [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-Methode der Klasse [**setFileFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#FileFormat), um das Format unter Verwendung der Enumerierung [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType) anzugeben.

Die [**FileFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFormatType)-Enumeration enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

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

Um eine Microsoft Excel 95/5.0-Datei zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) und legen das zugehörige Attribut für die [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)-Klasse der zu ladenden Vorlagendatei fest. Eine Beispieldatei zur Überprüfung dieses Features können Sie von folgendem Link herunterladen:

[Excel95-Datei](Excel95.xls)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel95Files.java" >}}

### **Öffnen von Microsoft Excel 97 - 2003-Dateien**

Um eine Microsoft Excel 97 - 2003-Datei zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) und legen das zugehörige Attribut für die [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)-Klasse der zu ladenden Vorlagendatei fest.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel97-2003Files.java" >}}

### **Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX-Dateien**

Um ein Microsoft Excel 2007/2010/2013/2016/2019 und Office 365-Format zu öffnen, d.h. XLSX oder XLSB, geben Sie den Dateipfad an. Sie können auch [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) verwenden und die zugehörigen Attribute/Optionen der [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions)-Klasse der zu ladenden Vorlagendatei festlegen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenExcel2007Files.java" >}}

### **Öffnen verschlüsselter Excel-Dateien**

Es ist möglich, verschlüsselte Excel-Dateien mit Microsoft Excel zu erstellen. Um eine verschlüsselte Datei zu öffnen, verwenden Sie die [**LoadOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/LoadOptions) und legen deren Attribute und Optionen fest (z. B. geben Sie ein Passwort) für die zu ladende Vorlagendatei. 
Eine Beispieldatei zum Testen dieses Features kann über folgenden Link heruntergeladen werden:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "OpenEncryptedExcelFiles.java" >}}

Aspose.Cells unterstützt auch das Öffnen von passwortgeschützten Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-Dateien.
