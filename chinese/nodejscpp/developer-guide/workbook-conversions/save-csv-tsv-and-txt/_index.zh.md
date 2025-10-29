---
title: 通过 Node.js 结合 C++ 转换 Excel 为 CSV、TSV 和 Txt
linktitle: 另存为 CSV、TSV 和 Txt
type: docs
weight: 40
url: /zh/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 将Excel文件转换为CSV、TSV和TXT格式。
---

{{% alert color="primary" %}}

Aspose.Cells支持将Excel、ODS、JSON及其他格式文件转换为CSV、TSV和TXT。

{{% /alert %}}

## **将工作簿保存为文本或CSV格式**

 有时，你想将带有多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel 和 Aspose.Cells 只会保存活动工作表的内容。

以下代码示例说明如何将整个工作簿保存为文本格式。加载源工作簿，它可以是任何Microsoft Excel或OpenOffice电子表格文件（如XLS、XLSX、XLSM、XLSB、ODS等），包含任意数量的工作表。

执行代码后，将会将工作簿中所有工作表的数据转换为TXT格式。

您可以修改相同的示例以将文件保存为CSV。默认情况下，[**TxtSaveOptions.getSeparator()**](https://reference.aspose.com/cells/nodejs-cpp/txtsaveoptions/#getSeparator--)是一个逗号，因此在保存为CSV格式时不要指定分隔符。

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

## **使用自定义分隔符保存文本文件**

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


## **高级主题**
- [在将电子表格导出为CSV格式时保留空行的分隔符](/cells/zh/nodejs-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [导出电子表格到CSV格式时修剪前导空白行和列](/cells/zh/nodejs-cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
{{< app/cells/assistant language="nodejs-cpp" >}}
