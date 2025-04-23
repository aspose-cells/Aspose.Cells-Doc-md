---
title: Öffnen verschiedener Microsoft Excel Versionen mit Node.js über C++
linktitle: Öffnen von verschiedenen Microsoft Excel Versionen Dateien
type: docs
weight: 20
url: /de/nodejs-cpp/opening-different-microsoft-excel-versions-files/
description: Dieser Artikel erklärt, wie man verschiedene Excel Versionen Dateien mit Aspose.Cells for Node.js via C++ öffnet.
keywords: Node.js öffnet verschiedene Microsoft Excel Dateien über C++, Wie öffne ich verschlüsselte Excel Dateien mit Node.js über C++
---

{{% alert color="primary" %}}

Aspose.Cells kann eine Vielzahl von verschiedenen Microsoft Excel-Versionen-Dateien öffnen, wie z.B. Microsoft Excel 95/97 - 2003, SpreadsheetML, Öffnen von Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 XLSX oder verschlüsselten Excel-Dateien.

{{% /alert %}}

## **Wie man Dateien verschiedener Microsoft Excel-Versionen öffnet**

Eine Anwendung muss oft in der Lage sein, Microsoft Excel-Dateien, die in verschiedenen Versionen erstellt wurden, zu öffnen, z.B. Microsoft Excel 95, 97 oder Microsoft Excel 2007/2010/2013/2016/2019 und Office 365. Es könnte notwendig sein, eine Datei in einem der vielen Formate zu laden, einschließlich XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited oder TSV, CSV, ODS usw. Verwenden Sie den Konstruktor oder geben Sie die Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) mit dem Attribut [**getFileFormat()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFileFormat--) des Typs an, das das Format unter Verwendung der Aufzählung [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) angibt.

Die Aufzählung [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) enthält viele vordefinierte Dateiformate, von denen einige unten aufgeführt sind.

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

Um eine Microsoft Excel 95/5.0-Datei zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) und setzen Sie das zugehörige Attribut für die [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)-Klasse für die zu ladende Vorlage-Datei.

[Excel95-Datei](Excel95.xls)

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Excel95_5.0.xls");

// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);

// Create a Workbook object and opening the file from the stream
const wbExcel95 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 95/5.0 workbook opened successfully!");
```

### **Öffnen von Microsoft Excel 97 - 2003-Dateien**

Um eine Microsoft Excel 97 - 2003-Datei zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) und setzen Sie das zugehörige Attribut für die [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)-Klasse für die zu ladende Vorlage-Datei.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_Excel97_2003.xls");
// Get the Excel file into stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Excel97To2003);

// Create a Workbook object and opening the file from the stream
const wbExcel97 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 97 - 2003 workbook opened successfully!");
```

### **Öffnen von Microsoft Excel 2007/2010/2013/2016/2019- und Office 365 XLSX-Dateien**

Um ein Microsoft Excel 2007/2010/2013/2016/2019 und Office 365 Format zu öffnen, das XLSX oder XLSB ist, geben Sie den Dateipfad an. Sie können auch [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) verwenden und das zugehörige Attribut/Optionen der [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)-Klasse für die zu ladende Vorlage-Datei setzen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Opening Microsoft Excel 2007 Xlsx Files
// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Create a Workbook object and opening the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book_Excel2007.xlsx"), loadOptions);
console.log("Microsoft Excel 2007 - Office365 workbook opened successfully!");
```

### **Verschlüsselte Excel-Dateien öffnen**

Es ist möglich, verschlüsselte Excel-Dateien mit Microsoft Excel zu erstellen. Um eine verschlüsselte Datei zu öffnen, verwenden Sie [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) und setzen Sie seine Attributen und Optionen (z.B. Passwort) für die zu ladende Vorlage-Datei.
Eine Beispieldatei zum Testen dieses Features kann über folgenden Link heruntergeladen werden:

[Encrypted Excel](EncryptedExcel.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "encryptedBook.xls");

// Instantiate LoadOptions
const loadOptions = new AsposeCells.LoadOptions();

// Specify the password
loadOptions.setPassword("1234");

// Create a Workbook object and opening the file from its path
const wbEncrypted = new AsposeCells.Workbook(filePath, loadOptions);
console.log("Encrypted excel file opened successfully!");
```

Aspose.Cells unterstützt auch das Öffnen von passwortgeschützten Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365-Dateien.


