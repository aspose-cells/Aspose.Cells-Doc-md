---
title: 通过 C++ 在 Node.js 中导入 HTML 时删除换行后的多余空格
linktitle: 导入HTML时删除换行后多余空格
type: docs
weight: 20
url: /zh/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: 学习如何在导入 HTML 时使用 Aspose.Cells for Node.js via C++ 删除换行后多余的空格。
---

{{% alert color="primary" %}}

 请使用[**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--)属性，并将其设置为**true**，以删除换行标签后的所有多余空格。默认情况下，此属性为**false**，在输出Excel文件时会保留多余空格。

{{% /alert %}}

## 设置 HTMLLoadOptions.deleteRedundantSpaces 属性为 false 和 true 的效果

以下截图显示了将此属性设置为**false**和**true**的效果。

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

在导入HTML时删除换行后的多余空格

###编程示例

以下示例代码展示了 [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) 属性的用法。请将其设置为 **true** 或 **false**，以获得上方截图所示的输出。

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Sample Html containing redundant spaces after <br> tag
const html = "<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

// Convert Html to byte array
const byteArray = Buffer.from(html, 'utf-8');

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setDeleteRedundantSpaces(true);

// Convert byte array into stream
const stream = Uint8Array.from(byteArray);

// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Auto fit the sheet columns
sheet.autoFitColumns();

// Save the workbook
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
