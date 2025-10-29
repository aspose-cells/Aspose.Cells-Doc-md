---
title: 以ODF 1.1、1.2和1.3格式保存，使用Node.js via C++
linktitle: 以ODF 1.1、1.2和1.3格式保存ODS文件
description: 使用Aspose.Cells for Node.js via C++将Excel转换为ODF 1.1、1.2和1.3规范
type: docs
weight: 230
url: /zh/nodejs-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

 Aspose.Cells 支持将 ODS 文件（**OpenDocument Spreadsheet**）保存为符合 ODF（**OpenDocument Format**） 1.1、1.2 和 1.3 规格的文件。Aspose.Cells 有 [**OdsSaveOptions.getOdfStrictVersion()**](https://reference.aspose.com/cells/nodejs-cpp/odssaveoptions/#getOdfStrictVersion--) 属性，用于指定保存 ODS 文件的 ODF 版本。该属性默认值为 [**OpenDocumentFormatVersionType.odf12**](https://reference.aspose.com/cells/nodejs-cpp/opendocumentformatversiontype/)，因此未设置此属性保存的 ODS 文件默认使用 1.2 规范。

{{% /alert %}}

 以下示例代码创建了一个工作簿对象，向第一个工作表的单元格 A1 添加了一些值，然后以 ODF 1.1、1.2 和 1.3 规范保存 ODS 文件。默认情况下，ODS 文件以 ODF 1.2 规范保存。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Put some value in cell A1
const cell = worksheet.getCells().get("A1");
cell.putValue("Welcome to Aspose!");

// Save ODS in ODF 1.2 version which is default
let options = new AsposeCells.OdsSaveOptions();
workbook.save(path.join(dataDir, "ODF1.2_out.ods"), options);

// Save ODS in ODF 1.1 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf11);
workbook.save(path.join(dataDir, "ODF1.1_out.ods"), options);

// Save ODS in ODF 1.3 version
options.setOdfStrictVersion(AsposeCells.OpenDocumentFormatVersionType.Odf13);
workbook.save(path.join(dataDir, "ODF1.3_out.ods"), options);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
