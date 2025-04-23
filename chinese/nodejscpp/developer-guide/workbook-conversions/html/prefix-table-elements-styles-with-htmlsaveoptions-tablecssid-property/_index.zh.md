---
title: 在Node.js中通过C++为HtmlSaveOptions.TableCssId属性前缀表格元素样式
linktitle: 使用 HtmlSaveOptions.TableCssId 属性为表格元素样式添加前缀
type: docs
weight: 110
url: /zh/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: 学习如何使用Aspose.Cells for Node.js via C++为HTML中的表格元素样式添加前缀。 
---

## **可能的使用场景**

Aspose.Cells允许你使用[**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--)属性为表格元素样式添加前缀。例如，如果你将此属性设置为**MyTest_TableCssId**，你将看到如下所示的表格元素样式：

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

以下屏幕截图显示了使用 [**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--) 属性对输出 HTML 的影响。

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **使用 HtmlSaveOptions.TableCssId 属性为表格元素样式添加前缀**

以下示例代码演示了如何利用[**HtmlSaveOptions.getTableCssId()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getTableCssId--)属性。请查看代码生成的[output HTML](60489790.zip) 以供参考。

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and put value inside it
const cell = ws.getCells().get("B5");
cell.putValue("This is some text.");

// Set the style of the cell - font color is Red
const st = cell.getStyle();
st.getFont().setColor(AsposeCells.Color.Red);
cell.setStyle(st);

// Specify html save options - specify table css id
const opts = new AsposeCells.HtmlSaveOptions();
opts.setTableCssId("MyTest_TableCssId");

// Save the workbook in html
wb.save("outputTableCssId.html", opts);
```
