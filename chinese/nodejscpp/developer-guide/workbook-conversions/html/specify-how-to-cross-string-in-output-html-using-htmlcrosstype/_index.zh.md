---
title: 指定在输出HTML中如何交叉字符串，使用HtmlCrossType参数
linktitle: 使用HtmlCrossType指定输出HTML中如何交叉字符串
type: docs
weight: 140
url: /zh/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: 学习如何通过指定HtmlCrossType参数控制HTML输出中的字符串溢出问题，使用Aspose.Cells for Node.js via C++。 
---

## **可能的使用场景**

当单元格含文本或字符串，但其长度超过单元格宽度时，如果下一列的单元格为空，字符串会溢出。保存Excel为HTML时，可以通过指定交叉类型（[**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)枚举）控制此溢出。其值包括：

- **HtmlCrossType.Default**：显示方式类似MS Excel；依赖下一单元格。如果下一单元格为空，字符串将会超出或被截断。

- **HtmlCrossType.MSExport**: 以MS Excel导出HTML的方式显示字符串.

- **HtmlCrossType.Cross**：显示 HTML 交叉字符串；创建大型 HTML 文件的性能比设置为 Default 或 FitToCell 快十倍以上。

- **HtmlCrossType.FitToCell**：仅在单元格宽度内显示字符串。

## **使用HtmlCrossType指定输出HTML中如何交叉字符串**

以下示例代码加载[示例Excel文件](51740732.xlsx)，并通过指定不同的[**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)将其保存为HTML格式。请下载由此代码生成的[输出HTML](51740734.zip)。示例Excel文件包含一个以红色边框标记的图片，如此截图所示，展示了[**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)值对输出HTML的影响。

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);

// Output Html
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
