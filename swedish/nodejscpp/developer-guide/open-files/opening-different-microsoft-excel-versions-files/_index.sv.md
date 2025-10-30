---
title: Öppna filer i olika Microsoft Excel versioner med Node.js via C++
linktitle: Öppna olika Microsoft Excel versioners filer
type: docs
weight: 20
url: /sv/nodejs-cpp/opening-different-microsoft-excel-versions-files/
description: Denna artikel förklarar hur du öppnar filer i olika Excel versioner med Aspose.Cells for Node.js via C++.
keywords: Node.js Öppna olika Microsoft Excel filer via C++, Hur öppnar jag krypterade Excel filer med Node.js via C++
---

{{% alert color="primary" %}}

Aspose.Cells kan öppna olika Microsoft Excel-versioner filer, som Microsoft Excel 95/97 - 2003, SpreadsheetML, Öppning av Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX eller Krypterade Excel-filer.

{{% /alert %}}

## **Hur man öppnar filer av olika Microsoft Excel-versioner**

En applikation måste ofta kunna öppna Microsoft Excel-filer skapade i olika versioner, till exempel Microsoft Excel 95, 97 eller Microsoft Excel 2007/2010/2013/2016/2019 och Office 365. Du kan behöva ladda en fil i någon av flera format, inklusive XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited eller TSV, CSV, ODS och så vidare. Använd konstruktorn, eller ange klassens [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) [**getFileFormat()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFileFormat--)-egenskaps attribut som anger formatet med hjälp av [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype)-uppräkningen.

Uppräkningen [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) innehåller många fördefinierade filformat, varav några är listade nedan.

|**Filtyp**|**Beskrivning**|
| :- | :- |
|Csv|Representerar en CSV-fil|
|Excel97To2003|Representerar en Excel 97 - 2003 fil|
|Xlsx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSX fil|
|Xlsm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 XLSM fil|
|Xltx|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 mall XLTX fil|
|Xltm|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 makroaktiverad XLTM fil|
|Xlsb|Representerar en Excel 2007/2010/2013/2016/2019 och Office 365 binär XLSB fil|
|SpreadsheetML|Representerar en SpreadsheetML fil|
|Tsv|Representerar en tabb-separerad värden fil|
|TabDelimited|Representerar en Tabbavgränsad textfil|
|Ods|Representerar en ODS fil|
|Html|Representerar en HTML fil|
|Mhtml|Representerar en MHTML fil|

### **Öppna Microsoft Excel 95/5.0 filer**

För att öppna en Microsoft Excel 95/5.0-fil, använd [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) och ställ in den relaterade attributet för [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)-klassen för mallfilen som ska laddas. En exempel fil för att testa denna funktion kan laddas ner från följande länk:

[Excel95 fil](Excel95.xls)

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

### **Öppna Microsoft Excel 97-2003 filer**

För att öppna en Microsoft Excel 97 - 2003-fil, använd [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) och ställ in det relaterade attributet för [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)-klassen för mallfilen som ska laddas.

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

### **Öppna Microsoft Excel 2007/2010/2013/2016/2019 och Office 365 XLSX-filer**

För att öppna ett Microsoft Excel 2007/2010/2013/2016/2019 och Office 365-format, det vill säga XLSX eller XLSB, ange filens sökväg. Du kan även använda [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) och ställa in de relaterade attributen/alternativen för [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)-klassen för mallfilen som ska laddas.

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

### **Öppna krypterade Excel-filer**

Det är möjligt att skapa krypterade Excel-filer med Microsoft Excel. För att öppna en krypterad fil, använd [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) och ställ in dess attribut och alternativ (till exempel, ge ett lösenord) för mallfilen som ska laddas.
En testfil för att testa den här funktionen kan laddas ner från följande länk:

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

Aspose.Cells stöder också öppning av lösenordsskyddade Microsoft Excel 2007, 2010, 2013, 2016, 2019, Office 365 filer.


{{< app/cells/assistant language="nodejs-cpp" >}}
