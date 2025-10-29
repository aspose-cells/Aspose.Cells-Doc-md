---
title: 通过Node.js通过C++保存文件的不同方法
linktitle: 保存文件
type: docs
weight: 40
url: /zh/nodejs-cpp/different-ways-to-save-files/
description: Aspose.Cells for Node.js via C++可以将文件保存为不同的格式，包括PDF、HTML、DOCX、PPTX、JSON和MHTML。
keywords: Aspose.Cells使用Node.js通过C++将Excel保存为PDF、HTML、JSON、CSV、TXT、XML、DOCX、PPTX、MHT、MHTML等格式。
---

{{% alert color="primary" %}}

Aspose.Cells 可以创建和保存文件。本文介绍了可保存文件的各种方式。

{{% /alert %}}

## **不同的文件保存方式**

Aspose.Cells提供了[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表Microsoft Excel文件，具有操作Excel文件所需的属性和方法。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类提供用于保存Excel文件的[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)方法。[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)方法有多种重载，可以以不同方式保存文件。

保存文件的文件格式由[**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)枚举决定

|**文件格式类型**|**描述**|
| :- | :- |
|CSV|表示 CSV 文件|
|Excel97To2003|表示Excel 97-2003文件
|Xlsx|表示Excel 2007 XLSX文件|
|Xlsm|表示Excel 2007 XLSM文件|
|Xltx|表示Excel 2007模板XLTX文件|
|Xltm|表示Excel 2007启用宏的XLTM文件|
|Xlsb|表示Excel 2007二进制XLSB文件|
|SpreadsheetML|表示一种Spreadsheet XML文件|
|TSV|表示制表符分隔数值文件|
|TabDelimited|代表分隔符文本文件|
|ODS|表示 ODS 文件|
|Html|表示HTML文件|
|MHtml|表示一个MHTML文件|
|Pdf|表示一个PDF文件|
|XPS|表示一个XPS文档|
|TIFF|表示Tagged Image File Format (TIFF)|

## **如何将文件保存为不同的格式**

要将文件保存到存储位置，在调用[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)对象的[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)方法时，指定文件名（包括存储路径）和所需的文件格式（来自[**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)枚举）。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save in Excel 97 to 2003 format
workbook.save(path.join(dataDir, ".output.xls"));
// OR
workbook.save(path.join(dataDir, ".output.xls"), new AsposeCells.XlsSaveOptions());

// Save in Excel 2007 xlsx format
workbook.save(path.join(dataDir, ".output.xlsx"), AsposeCells.SaveFormat.Xlsx);

// Save in Excel 2007 xlsb format
workbook.save(path.join(dataDir, ".output.xlsb"), AsposeCells.SaveFormat.Xlsb);

// Save in ODS format
workbook.save(path.join(dataDir, ".output.ods"), AsposeCells.SaveFormat.Ods);

// Save in Pdf format
workbook.save(path.join(dataDir, ".output.pdf"), AsposeCells.SaveFormat.Pdf);

// Save in Html format
workbook.save(path.join(dataDir, ".output.html"), AsposeCells.SaveFormat.Html);

// Save in SpreadsheetML format
workbook.save(path.join(dataDir, ".output.xml"), AsposeCells.SaveFormat.SpreadsheetML);
```

## **如何将工作簿保存为PDF**
便携式文档格式（PDF）是由Adobe在1990年代创建的一种文档。该文件格式的目的是引入一种标准，用于以与应用软件、硬件及操作系统无关的格式表示文档和其他参考资料。PDF文件格式具有完整能力，包括文本、图像、超链接、表单字段、丰富媒体、数字签名、附件、元数据、地理空间特征和3D对象，且可以成为源文档的一部分。

以下代码展示了如何用Aspose.Cells将工作簿保存为PDF文件：
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Set value to Cell.
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World!");

const saveFilePath = path.join(dataDir, "pdf1.pdf");
workbook.save(saveFilePath);

// Save as Pdf format compatible with PDFA-1a
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

const pdfAFilePath = path.join(dataDir, "pdfa1a.pdf");
workbook.save(pdfAFilePath, saveOptions);
```

## **如何将工作簿保存为文本或CSV格式**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel和Aspose.Cells都仅保存活动工作表的内容。

以下示例说明如何将整个工作簿保存为文本格式。加载源工作簿，可以是任何Microsoft Excel或OpenOffice电子表格文件（如XLS、XLSX、XLSM、XLSB、ODS等），含有任意数量的工作表。

执行代码后，将会将工作簿中所有工作表的数据转换为TXT格式。

你可以修改相同的示例，将文件保存为CSV格式。默认情况下，[**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--)为逗号，因此在保存为CSV格式时无需指定分隔符。请注意：如果你使用评估版，即使设置了[**TxtSaveOptions.getExportAllSheets()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getExportAllSheets--)属性为true，程序仍只导出一个工作表。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xls"));

// Text save options. You can use any type of separator
const opts = new AsposeCells.TxtSaveOptions();
opts.setSeparator('\t');
opts.setExportAllSheets(true);

// Save entire workbook data into file
workbook.save(path.join(dataDir, "out.txt"), opts);
```

## **如何使用自定义分隔符将文件保存为文本文件**

文本文件包含无格式的电子表格数据。该文件是一种纯文本文件，可以在其数据之间具有一些自定义分隔符。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Create a Workbook object and opening the file from its path
const wb = new AsposeCells.Workbook(filePath);

// Instantiate Text File's Save Options
const options = new AsposeCells.TxtSaveOptions();

// Specify the separator
options.setSeparator(";");

// Save the file with the options
wb.save(path.join(dataDir, "output.csv"), options);
```

## **如何将文件保存到流中**

要将文件保存到流中，创建一个*MemoryStream*或*FileStream*对象，并通过调用[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)对象的[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)方法，将文件保存到该流对象中。在调用时，使用[**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)枚举指定所需的文件格式。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

async function downloadExcel(req, res) {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);
// Save the workbook to a memory stream
const stream = workbook.save(AsposeCells.SaveFormat.Xlsx);

// Set the content type and file name
const contentType = "application/octet-stream";
const fileName = "output.xlsx";

// Set the response headers
res.setHeader("Content-Disposition", `attachment; filename="${fileName}"`);
res.setHeader("Content-Type", contentType);

// Write the file contents to the response body stream
res.send(stream);
}
```

## **如何将Excel文件保存为Html和Mht文件**
Aspose.Cells可以轻松保存Excel文件、JSON、CSV或其他可以作为.html和.mht文件加载的文件。
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```


## **如何将Excel文件保存为OpenOffice（ODS，SXC，FODS，OTS）**
我们可以将文件保存为OpenOffice格式：ODS、SXC、FODS、OTS等。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **如何将Excel文件保存为JSON或XML**

JSON（JavaScript对象表示）是一种用于存储和传输数据的开放标准文件格式，它使用人类可读的文本。JSON文件存储为.json扩展名。JSON需要更少的格式化，是XML的一个很好的替代品。JSON源自JavaScript，但是是一种与语言无关的数据格式。许多现代编程语言都支持JSON的生成和解析。application/json是用于JSON的媒体类型。

Aspose.Cells支持将文件保存为JSON或XML。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```


## **高级主题**
- [调整工作簿压缩级别](/cells/zh/nodejs-cpp/adjust-workbook-compression-level/)
- [将工作簿保存为严格的 Open XML 电子表格格式](/cells/zh/nodejs-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/)
- [将文件保存到响应对象](/cells/zh/nodejs-cpp/saving-file-to-response-object/)
{{< app/cells/assistant language="nodejs-cpp" >}}
