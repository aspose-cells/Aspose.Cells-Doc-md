---
title: 通过 Node.js 转换 Excel 工作簿为 Ods、Sxc 和 Fods（OpenOffice / LibreOffice Calc）
linktitle: Ods
type: docs
weight: 20
url: /zh/nodejs-cpp/convert-excel-to-ods/
description: 如何使用 Aspose.Cells for Node.js via C++ 将 Excel 转换为 Ods（OpenOffice / LibreOffice Calc）或将 Ods（OpenOffice / LibreOffice Calc）转换为 Excel。
---

## **关于OpenDocument**
[OpenDocument format (ODF)](https://en.wikipedia.org/wiki/OpenDocument)是一种免费开放的用于电子办公文档的文件格式，最初由Sun开发用于Open Office套件。 OpenDocument Spreadsheet (ODS)是Excel文档的文件格式。 OpenDocument目前是OASIS和ISO标准。

## **将Ods（OpenOffice / LibreOffice calc）转换为Excel**
Aspose.Cells for Node.js via C++ 支持加载由 OpenOffice / LibreOffice Calc 支持的 Ods、Sxc 和 Fods，并将 [Ods](book1.ods)、[Sxc](book1.sxc) 和 [Fods](book1.fods) 转换为 Excel 文件。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load Excel workbook
const excelFilePath = path.join(__dirname, "book1.xlsx");
let workbook = new AsposeCells.Workbook(excelFilePath);

// Save as ods file
workbook.save("ods_out.ods");

// Save as sxc file
workbook.save("sxc_out.sxc");

// Save as fods file
workbook.save("fods_out.fods");
```

## **将Excel转换为Ods（OpenOffice / LibreOffice Calc）**
Aspose.Cells for Node.js via C++ 支持将 Excel 文件转换为 Ods、Sxc 和 Fods 文件。以下代码示例演示如何将 [模板](book1.xlsx) 转换为 Ods、Sxc 和 Fods 文件。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath1 = path.join(dataDir, "book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath1);
// Save as ods file 
workbook.save("Out.ods");
// Save as sxc file 
workbook.save("Out.sxc");
// Save as fods file 
workbook.save("Out.fods");
```

## **高级主题**
- [按照ODF 1.1和1.2规范保存ODS文件](/cells/zh/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [在ODS文件中处理背景](/cells/zh/nodejs-cpp/working-with-background-in-ods-files/)
{{< app/cells/assistant language="nodejs-cpp" >}}
