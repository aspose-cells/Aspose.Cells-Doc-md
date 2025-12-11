---
title: Open Different Microsoft Excel Version Files with Node.js via C++
linktitle: Open Different Microsoft Excel Version Files
type: docs
weight: 20
url: /nodejs-cpp/opening-different-microsoft-excel-versions-files/
description: This article explains how to open different Excel version files using Aspose.Cells for Node.js via C++.
keywords: Node.js Open Different Microsoft Excel file via C++, How do I open Encrypted Excel Files Node.js via C++
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells can open a range of different Microsoft Excel version files, such as Microsoft Excel 95/97‑2003, SpreadsheetML, Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX, or encrypted Excel files.

{{% /alert %}}

## **How to Open Files of Different Microsoft Excel Versions**

An application often has to be able to open Microsoft Excel files created in different versions, for example, Microsoft Excel 95, 97, or Microsoft Excel 2007/2010/2013/2016/2019 and Office 365. You might need to load a file in any one of several formats, including XLS, XLSX, XLSM, XLSB, SpreadsheetML, TabDelimited or TSV, CSV, ODS, and so on. Use the constructor, or specify the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class's [**getFileFormat()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFileFormat--) type attribute that specifies the format using the [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) enumeration.

The [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) enumeration contains many pre‑defined file formats, some of which are given below.

| **File Format Types** | **Description** |
| :- | :- |
| Csv | Represents a CSV file |
| Excel97To2003 | Represents an Excel 97‑2003 file |
| Xlsx | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSX file |
| Xlsm | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 XLSM file |
| Xltx | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 template XLTX file |
| Xltm | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 macro‑enabled XLTM file |
| Xlsb | Represents an Excel 2007/2010/2013/2016/2019 and Office 365 binary XLSB file |
| SpreadsheetML | Represents a SpreadsheetML file |
| Tsv | Represents a TSV file |
| TabDelimited | Represents a Tab‑Delimited text file |
| Ods | Represents an ODS file |
| Html | Represents an HTML file |
| Mhtml | Represents an MHTML file |

### **Open Microsoft Excel 95/5.0 Files**

To open a Microsoft Excel 95/5.0 file, use [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) and set the appropriate attribute for the file to be loaded. A sample file for testing this feature can be downloaded from the following link:

[Excel95 File](Excel95.xls)

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Excel95_5.0.xls");

// Get the Excel file into a stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Auto);

// Create a Workbook object and open the file from the stream
const wbExcel95 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 95/5.0 workbook opened successfully!");
```

### **Open Microsoft Excel 97‑2003 Files**

To open a Microsoft Excel 97‑2003 file, use [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) and set the appropriate attribute for the file to be loaded.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book_Excel97_2003.xls");

// Get the Excel file into a stream
const stream = fs.readFileSync(filePath);

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions1 = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Excel97To2003);

// Create a Workbook object and open the file from the stream
const wbExcel97 = new AsposeCells.Workbook(stream, loadOptions1);
console.log("Microsoft Excel 97‑2003 workbook opened successfully!");
```

### **Open Microsoft Excel 2007/2010/2013/2016/2019 and Office 365 XLSX Files**

To open a Microsoft Excel 2007/2010/2013/2016/2019 or Office 365 file, such as XLSX or XLSB, specify the file path. You can also use [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) and set the appropriate options for the file to be loaded.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate LoadOptions specified by the LoadFormat.
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);

// Create a Workbook object and open the file from its path
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book_Excel2007.xlsx"), loadOptions);
console.log("Microsoft Excel 2007 – Office 365 workbook opened successfully!");
```

### **Open Encrypted Excel Files**

It's possible to create encrypted Excel files using Microsoft Excel. To open an encrypted file, use [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) and set its attributes and options (for example, provide a password) for the file to be loaded. A sample file for testing this feature can be downloaded from the following link:

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

// Create a Workbook object and open the file from its path
const wbEncrypted = new AsposeCells.Workbook(filePath, loadOptions);
console.log("Encrypted Excel file opened successfully!");
```

Aspose.Cells also supports opening password‑protected Microsoft Excel 2007, 2010, 2013, 2016, 2019, and Office 365 files.

{{< app/cells/assistant language="nodejs-cpp" >}}
