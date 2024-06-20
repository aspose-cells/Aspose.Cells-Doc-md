---
title: Öffnen von verschiedenen Microsoft Excel Versionen Dateien
type: docs
weight: 20
url: /de/cpp/opening-different-microsoft-excel-versions-files/
---

{{% alert color="primary" %}}

Aspose.Cells kann eine Vielzahl von verschiedenen Microsoft Excel-Versionen-Dateien öffnen, wie z.B. Microsoft Excel 95/97 - 2003, SpreadsheetML, Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX oder verschlüsselten Excel-Dateien.

{{% /alert %}}

## **Öffnen von Dateien verschiedener Microsoft Excel-Versionen**

Eine Anwendung muss oft in der Lage sein, Microsoft Excel-Dateien in verschiedenen Versionen zu öffnen, z. B. Microsoft Excel 95, 97 oder Microsoft Excel 2007/2010/2013/2016/2019 und Office 365. Möglicherweise müssen Sie eine Datei in einem der verschiedenen Formate laden, darunter XLS, XLSX, XLSM, XLSB, SpreadsheetML, Tab-getrennt oder TSV, CSV, ODS und so weiter. Verwenden Sie den Konstruktor oder geben Sie die Methode der Klasse [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) an, um das Format mit der [**SetFileFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setfileformat/)-Enumeration anzugeben.

Die [**FileFormatType**](https://reference.aspose.com/cells/cpp/aspose.cells/fileformattype/)-Enumeration enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

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

Um eine Microsoft Excel 95/5.0-Datei zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) und legen das zugehörige Attribut für die [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)-Klasse der zu ladenden Vorlagendatei fest. Eine Beispieldatei zur Überprüfung dieses Features können Sie von folgendem Link herunterladen:

[Excel95-Datei](Excel95.xls)

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel95Files-new.cpp" >}}

### **Öffnen von Microsoft Excel 97 - 2003-Dateien**

Um eine Microsoft Excel 97 - 2003-Datei zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) und legen das zugehörige Attribut für die [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)-Klasse der zu ladenden Vorlagendatei fest.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel97-2003Files-new.cpp" >}}

### **Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX-Dateien**

Um ein Microsoft Excel 2007/2010/2013/2016/2019 und Office 365-Format zu öffnen, d.h. XLSX oder XLSB, geben Sie den Dateipfad an. Sie können auch [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/) verwenden und die zugehörigen Attribute/Optionen der [**LoadOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/)-Klasse der zu ladenden Vorlagendatei festlegen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "OpenExcel2007Files-new.cpp" >}}

Aspose.Cells unterstützt auch das Öffnen von passwortgeschützten Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-Dateien.


