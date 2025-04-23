---
title: Öffnen von verschiedenen Microsoft Excel Versionen Dateien
type: docs
weight: 20
url: /de/go-cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells kann eine Vielzahl von verschiedenen Microsoft Excel-Versionen-Dateien öffnen, wie z.B. Microsoft Excel 95/97 - 2003, SpreadsheetML, Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX oder verschlüsselten Excel-Dateien.

{{% /alert %}}

## **Öffnen von Dateien verschiedener Microsoft Excel-Versionen**

Eine Anwendung muss oft in der Lage sein, Microsoft Excel-Dateien zu öffnen, die in verschiedenen Versionen erstellt wurden, zum Beispiel Microsoft Excel 95, 97 oder Microsoft Excel 2007/2010/2013/2016/2019 und Office 365. Es könnte erforderlich sein, eine Datei in einem beliebigen der mehreren Formate zu laden, einschließlich XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited oder TSV, CSV, ODS und so weiter. Verwenden Sie den Konstruktor oder spezifizieren Sie die [**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) Klasse's [**SetFileFormat**](https://reference.aspose.com/cells/go-cpp/workbook/setfileformat/) Methode, um das Format mithilfe des [**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/) Aufzählungstyp zu bestimmen.

Die [**FileFormatType**](https://reference.aspose.com/cells/go-cpp/fileformattype/) Aufzählung enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

|**Dateiformat-Typen**|**Beschreibung**|
| :- | :- |
|FileFormatType_CSV|Stellt eine CSV-Datei dar|
|FileFormatType_Excel97To2003|Stellt eine Excel 97 - 2003-Datei dar|
|FileFormatType_Xlsx|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 XLSX-Datei dar|
|FileFormatType_Xlsm|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 XLSM-Datei dar|
|FileFormatType_Xltx|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 Vorlage XLTX-Datei dar|
|FileFormatType_Xltm|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 makrofähige XLTM-Datei dar|
|FileFormatType_Xlsb|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 binäre XLSB-Datei dar|
|FileFormatType_SpreadsheetML|Stellt eine SpreadsheetML-Datei dar|
|FileFormatType_Tsv|Stellt eine durch Tabulatoren getrennte Werte-Datei dar|
|FileFormatType_TabDelimited|Stellt eine Tabstopp-Delimited-Textdatei dar|
|FileFormatType_Ods|Stellt eine ODS-Datei dar|
|FileFormatType_Html|Stellt eine HTML-Datei dar|
|FileFormatType_MHtml|Stellt eine MHTML-Datei dar|

### **Öffnen von Microsoft Excel 95/5.0-Dateien**

Um eine Microsoft Excel 95/5.0-Datei zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) und legen das zugehörige Attribut für die [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/)-Klasse der zu ladenden Vorlagendatei fest. Eine Beispieldatei zur Überprüfung dieses Features können Sie von folgendem Link herunterladen:

[Excel95-Datei](Excel95.xls)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel95Files.go" >}}

### **Öffnen von Microsoft Excel 97 - 2003-Dateien**

Um eine Microsoft Excel 97 - 2003-Datei zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) und legen das zugehörige Attribut für die [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/)-Klasse der zu ladenden Vorlagendatei fest.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel97-2003Files.go" >}}

### **Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX-Dateien**

Um ein Microsoft Excel 2007/2010/2013/2016/2019 und Office 365-Format zu öffnen, d.h. XLSX oder XLSB, geben Sie den Dateipfad an. Sie können auch [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/) verwenden und die zugehörigen Attribute/Optionen der [**LoadOptions**](https://reference.aspose.com/cells/go-cpp/loadoptions/)-Klasse der zu ladenden Vorlagendatei festlegen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-OpenExcel2007Files.go" >}}

Aspose.Cells unterstützt auch das Öffnen passwortgeschützter Microsoft Excel 2007, 2010, 2013, 2016, 2019 und Office 365 Dateien.
