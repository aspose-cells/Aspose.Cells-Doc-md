---
title: Öffnen von verschiedenen Microsoft Excel Versionen Dateien
type: docs
weight: 20
url: /de/net/opening-different-microsoft-excel-versions-files/
description: In diesem Artikel wird erklärt, wie man verschiedene Excel Versionen von Dateien mithilfe der Aspose.Cells for .NET API öffnet.
keywords: C# Öffnen einer unterschiedlichen Microsoft Excel Datei, Wie öffne ich verschlüsselte Excel Dateien.
---

{{% alert color="primary" %}}

Aspose.Cells kann eine Vielzahl von verschiedenen Microsoft Excel-Versionen-Dateien öffnen, wie z.B. Microsoft Excel 95/97 - 2003, SpreadsheetML, Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX oder verschlüsselten Excel-Dateien.

{{% /alert %}}

## **Wie man Dateien verschiedener Microsoft Excel-Versionen öffnet**

Eine Anwendung muss oft in der Lage sein, Microsoft Excel-Dateien aus verschiedenen Versionen zu öffnen, z. B. Microsoft Excel 95, 97 oder Microsoft Excel 2007/2010/2013/2016/2019 und Office 365. Sie müssen möglicherweise eine Datei in einem der verschiedenen Formate wie XLS, XLSX, XLSM, XLSB, SpreadsheetML, tabstoppgetrennt oder TSV, CSV, ODS und so weiter laden. Verwenden Sie den Konstruktor oder geben Sie den [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klassentypattribut an, das das Format mithilfe der [**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype) Aufzählung spezifiziert.

Die [**FileFormatType**](https://reference.aspose.com/cells/net/aspose.cells/fileformattype)-Enumeration enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

|**Dateiformat-Typen**|**Beschreibung**|
| :- | :- |
|Csv|Stellt eine CSV-Datei dar|
|Excel97To2003|Stellt eine Excel 97 - 2003-Datei dar|
|Xlsx|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 XLSX-Datei dar|
|Xlsm|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 XLSM-Datei dar|
|Xltx|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365-Vorlage XLTX-Datei dar|
|Xltm|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 makrofähige XLTM-Datei dar|
|Xlsb|Stellt eine Excel 2007/2010/2013/2016/2019 und Office 365 binäre XLSB-Datei dar|
|SpreadsheetML|Stellt eine SpreadsheetML-Datei dar|
|Tsv|Stellt eine Tabstoppwerte-Datei dar|
|TabDelimited|Stellt eine tabulatorgetrennte Textdatei dar|
|Ods|Stellt eine ODS-Datei dar|
|Html|Stellt eine HTML-Datei dar|
|Mhtml|Stellt eine MHTML-Datei dar|

### **Öffnen von Microsoft Excel 95/5.0-Dateien**

Um eine Microsoft Excel 95/5.0-Datei zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) und legen das zugehörige Attribut für die [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)-Klasse der zu ladenden Vorlagendatei fest. Eine Beispieldatei zur Überprüfung dieses Features können Sie von folgendem Link herunterladen:

[Excel95-Datei](Excel95.xls)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel95Files-1.cs" >}}

### **Öffnen von Microsoft Excel 97 - 2003-Dateien**

Um eine Microsoft Excel 97 - 2003-Datei zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) und legen das zugehörige Attribut für die [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)-Klasse der zu ladenden Vorlagendatei fest.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel972003Files-1.cs" >}}

### **Öffnen von Microsoft Excel 2007/2010/2013/2016/2019- und Office 365 XLSX-Dateien**

Um ein Microsoft Excel 2007/2010/2013/2016/2019 und Office 365-Format zu öffnen, d.h. XLSX oder XLSB, geben Sie den Dateipfad an. Sie können auch [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) verwenden und die zugehörigen Attribute/Optionen der [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions)-Klasse der zu ladenden Vorlagendatei festlegen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningMicrosoftExcel2007XlsxFiles-1.cs" >}}

### **Verschlüsselte Excel-Dateien öffnen**

Es ist möglich, verschlüsselte Excel-Dateien mit Microsoft Excel zu erstellen. Um eine verschlüsselte Datei zu öffnen, verwenden Sie die [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) und legen deren Attribute und Optionen fest (z. B. geben Sie ein Passwort) für die zu ladende Vorlagendatei.
Eine Beispieldatei zum Testen dieses Features kann über folgenden Link heruntergeladen werden:

[Encrypted Excel](EncryptedExcel.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningEncryptedExcelFiles-1.cs" >}}

Aspose.Cells unterstützt auch das Öffnen von passwortgeschützten Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-Dateien.


