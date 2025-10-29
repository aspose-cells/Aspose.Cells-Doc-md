---
title: 使用Node.js通过C++隐藏叠加内容CrossHideRight，保存为HTML
linktitle: 使用 CrossHideRight 在保存为 HTML 时隐藏重叠内容
type: docs
weight: 100
url: /zh/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---


## **可能的使用场景**

将Excel文件保存为HTML时，可以为单元格字符串指定不同的交叉类型。默认情况下，Aspose.Cells会按Microsoft Excel生成HTML，但当更改交叉类型为[**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)时，覆盖或与单元格字符串重叠的所有字符串将被隐藏。

## **在保存为Html时使用CrossHideRight隐藏重叠内容**

以下示例代码加载[示例Excel文件](64716894.xlsx)，并在将[**HtmlSaveOptions.getHtmlCrossStringType()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getHtmlCrossStringType--)设置为[**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)后，将其保存为[输出HTML](64716893.zip)。截图说明了[**CrossHideRight**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype)如何影响默认输出的HTML。

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Load sample Excel file
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.CrossHideRight);

// Save to HTML with HtmlSaveOptions
workbook.save(path.join(dataDir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html"), opts);
``` 
{{< app/cells/assistant language="nodejs-cpp" >}}
