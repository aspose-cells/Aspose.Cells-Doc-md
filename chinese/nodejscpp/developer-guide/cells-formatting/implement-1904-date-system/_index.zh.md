---
title: 使用 Node.js 通过 C++ 实现 1904 日期系统
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js 库。它支持实现1904日期系统，允许用户基于1904年1月1日的日期进行计算和格式化。本文介绍如何使用 Aspose.Cells 库实现1904日期系统。
keywords: Aspose.Cells、1904日期系统、电子表格、计算、格式化、Node.js 通过 C++
type: docs
weight: 7000
url: /zh/nodejs-cpp/implement-1904-date-system/
---

{{% alert color="primary" %}} 

微软Excel支持两种日期系统：1900日期系统（Windows版Excel的默认日期系统）和1904日期系统。1904日期系统通常用于与Mac版Excel文件的兼容性，并且如果你使用苹果电脑的Excel，这是默认系统。你可以使用Aspose.Cells for Node.js via C++为Excel文件设置1904日期系统。 

{{% /alert %}} 

在Microsoft Excel中实现1904日期系统（例如，Microsoft Excel 2003）的方法：

1. 从“工具”菜单中选择“选项”，并选择“计算”选项卡。
1. 选择“1904日期系统”选项。
1. 点击**确定**。

|**在Microsoft Excel中选择1904日期系统**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|

请参阅以下示例代码，了解如何使用Aspose.Cells API 实现此功能。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Initialize a new Workbook
// Open an excel file
const workbook = new AsposeCells.Workbook(filePath);

// Implement 1904 date system
workbook.getSettings().setDate1904(true);

// Save the excel file
workbook.save(path.join(dataDir, "Mybook.out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
