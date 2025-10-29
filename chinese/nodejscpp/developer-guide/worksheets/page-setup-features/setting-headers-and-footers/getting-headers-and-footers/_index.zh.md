---
title: 通过 C++ 使用 Node.js 获取标题或页脚
linktitle: 获取页眉或页脚
type: docs
weight: 30
url: /zh/nodejs-cpp/get-headers-or-footers/
description: 本文介绍了如何使用 C++ API 通过 Node.js 编程方式从 Excel 或 OpenOffice 文件中获取标题和页脚。
---

{{% alert color="primary" %}}

页眉和页脚只出现在页面布局视图、打印预览和打印页面上。 

如果要同时查看多个工作表的页眉或页脚，也可以使用页面设置对话框。 

对于其他工作表类型，如图表工作表或图表，只能通过使用页面设置对话框来插入页眉和页脚。

{{% /alert %}}

## **在MS Excel中获取页眉和页脚**
1. 单击要查看或更改页眉或页脚的工作表。
2. 在“视图”选项卡的“工作簿视图”组中，点击“页面布局”。
   Excel会以页面布局视图显示工作表。
3. 要查看或编辑页眉或页脚，请单击工作表页面顶部或底部的左侧、中间或右侧页眉或页脚文本框（在页眉下方或在页脚上方）。


## **使用 Aspose.Cells for Node.js via C++ 获取标题和页脚**
借助 [**PageSetup.getHeader(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getHeader-number-) 和 [**PageSetup.getFooter(number)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getFooter-number-) 方法，Node.js 开发者可以轻松从文件中获取标题或页脚。

1. 构建一个工作簿以打开文件。
2. 获取包含你要获取标题或页脚的工作表。
3. 使用特定节ID获取标题或页脚。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
console.log(sheet.getPageSetup().getHeader(0));
// Gets center section of header
console.log(sheet.getPageSetup().getHeader(1));
// Gets right section of header
console.log(sheet.getPageSetup().getHeader(2));
// Gets center section of footer
console.log(sheet.getPageSetup().getFooter(1));
```

## **解析页眉和页脚为命令列表**
标题或页脚文本可以包含特殊命令，例如用于页码、当前日期或文本格式属性的占位符。

特殊命令由带有前导“&”的单个字母表示。

标题和页脚字符串采用 ABNF 语法构建。不使用查看器很难理解。

Aspose.Cells for Node.js via C++ 提供 [**PageSetup.getCommands(string)**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getCommands-string-) 方法将标题和页脚解析为命令列表。

以下代码展示了如何将标题或页脚解析为命令列表并处理命令：

```javascript
try {
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "HeaderFooter.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

// Gets left section of header
const headerSection = sheet.getPageSetup().getHeader(0);
const commands = sheet.getPageSetup().getCommands(headerSection) || [];

commands.forEach(c => {
switch (c.getType()) {
case AsposeCells.HeaderFooterCommandType.SheetName:
// embedded the name of the sheet to header or footer
break;
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
