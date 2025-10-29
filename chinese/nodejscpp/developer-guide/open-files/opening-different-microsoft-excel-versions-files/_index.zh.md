---
title: 使用 C++ 通过 Node.js 打开不同版本的 Microsoft Excel 文件
linktitle: 打开不同的Microsoft Excel版本文件
type: docs
weight: 20
url: /zh/nodejs-cpp/opening-different-microsoft-excel-versions-files/
description: 本文介绍了如何使用 Aspose.Cells for Node.js via C++ 打开不同版本的 Excel 文件。
keywords: 通过 C++ 和 Node.js 打开不同的 Microsoft Excel 文件，如何打开加密的 Excel 文件？
---

{{% alert color="primary" %}}

Aspose.Cells 可以打开一系列不同版本的 Microsoft Excel 文件，例如 Microsoft Excel 95/97 - 2003、SpreadsheetML、打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 XLSX 或加密的 Excel 文件。

{{% /alert %}}

## **如何打开不同版本的Microsoft Excel文件**

 应用程序常常需要能够打开不同版本创建的 Microsoft Excel 文件，例如 Microsoft Excel 95、97，或 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365。您可能需要加载多种格式的文件，包括 XLS、XLSX、XLSM、XLSB、SpreadsheetML、TabDelimited 或 TSV、CSV、ODS 等。请使用构造函数，或指定 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类的 [**getFileFormat()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFileFormat--) 类型属性，利用 [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) 枚举指定格式。

 [**FileFormatType**](https://reference.aspose.com/cells/nodejs-cpp/fileformattype) 枚举包含许多预定义的文件格式，部分如下。

|**文件格式类型**|**描述**|
| :- | :- |
|Csv|表示CSV文件
|Excel97To2003|表示Excel 97-2003文件
|Xlsx|表示Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件
|Xlsm|代表Excel 2007/2010/2013/2016/2019和Office 365的XLSM文件|
|Xltx|代表Excel 2007/2010/2013/2016/2019和Office 365模板XLTX文件|
|Xltm|代表Excel 2007/2010/2013/2016/2019和Office 365宏启用的XLTM文件|
|Xlsb|代表Excel 2007/2010/2013/2016/2019和Office 365二进制XLSB文件|
|SpreadsheetML|代表SpreadsheetML文件|
|Tsv|代表分隔值文件|
|TabDelimited|代表分隔符文本文件|
|Ods|代表ODS文件|
|Html|代表HTML文件|
|Mhtml|代表MHTML文件|

### **打开Microsoft Excel 95/5.0文件**

 要打开 Microsoft Excel 95/5.0 文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)，并为要加载的模板文件的 [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) 类设置相关属性。可以从以下链接下载测试示例文件：

[Excel95文件](Excel95.xls)

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

### **打开Microsoft Excel 97 - 2003文件**

 要打开 Microsoft Excel 97-2003 文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)，并为要加载的模板文件的 [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) 类设置相关属性。

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

### **打开Microsoft Excel 2007/2010/2013/2016/2019和Office 365 XLSX文件**

 要打开 Microsoft Excel 2007/2010/2013/2016/2019 和 Office 365 格式（即 XLSX 或 XLSB），请指定文件路径。也可以使用 [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)，并为要加载的模板文件的 [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions) 类设置相关属性/选项。

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

### **打开加密的Excel文件**

 可以使用 Microsoft Excel 创建加密的 Excel 文件。要打开加密文件，请使用 [**LoadOptions**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions)，并为模板文件设置其属性和选项（例如，密码）。
您可以从以下链接下载测试此功能的示例文件：

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

Aspose.Cells还支持打开受密码保护的Microsoft Excel 2007、2010、2013、2016、2019、Office 365文件。


{{< app/cells/assistant language="nodejs-cpp" >}}
