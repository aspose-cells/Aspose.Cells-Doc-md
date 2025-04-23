---
title: 通过Node.js和C++在保存为HTML时防止导出隐藏工作表内容
linktitle: 在保存为 HTML 时阻止导出隐藏的工作表内容
type: docs
weight: 210
url: /zh/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: 了解如何在将Excel文件保存为HTML时防止导出隐藏工作表内容，使用Aspose.Cells for Node.js via C++。
---

{{% alert color="primary" %}}

您可以将 Excel 工作簿保存为 HTML。但是，如果工作簿包含隐藏的工作表，则 Aspose.Cells 默认情况下会将隐藏的工作表内容导出到 HTML 输出的 (_files) 目录中，该目录包含诸如工作表、图像、tabstrip.htm、stylesheet.css 等文件。有时，以这种方式导出隐藏的工作表内容是不合适的。例如，如果隐藏的工作表包含不应导出到 _files 目录的图像。

{{% /alert %}}

Aspose.Cells for Node.js via C++提供了[**HtmlSaveOptions.getExportHiddenWorksheet()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getExportHiddenWorksheet--)属性。默认情况下，它设置为**true**，导出隐藏工作表为HTML。如果设置为**false**，Aspose.Cells将不会导出隐藏工作表内容。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "WorkbookWithHiddenContent.xlsx"));

// Do not export hidden worksheet contents
const options = new AsposeCells.HtmlSaveOptions();
options.setExportHiddenWorksheet(false);

// Save the workbook
workbook.save(path.join(dataDir, "HtmlWithoutHiddenContent_out.html"), options);
```

