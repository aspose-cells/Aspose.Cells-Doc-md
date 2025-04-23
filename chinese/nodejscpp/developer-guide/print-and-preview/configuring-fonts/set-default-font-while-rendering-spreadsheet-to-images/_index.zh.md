---
title: 设置使用 C++ 和 Node.js 将电子表格渲染成图片时的默认字体
linktitle: 在将电子表格呈现为图像时设置默认字体
type: docs
weight: 360
url: /zh/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/
description: 学习如何在用 Aspose.Cells for Node.js via C++ 将电子表格渲染为图片时设置默认字体。 
---

{{% alert color="primary" %}}

请使用[**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)属性将默认字体设置为渲染电子表格为图像时的默认字体。仅当工作簿的默认字体无法呈现您的字符时，才会使用[**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)属性指定的默认字体。指定的默认字体将用于所有缺少或不存在的字体的单元格。

{{% /alert %}}

## 渲染电子表格为图像时设置默认字体

以下示例代码创建了一个工作簿，在第一个工作表的单元格 A4 中添加一些文本，并将其字体设置为无效或不存在的字体。然后，分别用 [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) 属性设置为 *Courier New* 和 [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) 属性设置为 *Times New Roman* 来获取两个电子表格图片。

这是将 [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) 属性设置为 *Courier New* 后的输出图片。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

这是将 [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--) 属性设置为 *Times New Roman* 后的输出图片。

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

## 示例代码

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Set default font of the workbook to none
let s = wb.getDefaultStyle();
s.getFont().setName("");
wb.setDefaultStyle(s);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access cell A4 and add some text inside it.
const cell = ws.getCells().get("A4");
cell.putValue("This text has some unknown or invalid font which does not exist.");

// Set the font of cell A4 which is unknown.
let st = cell.getStyle();
st.getFont().setName("UnknownNotExist");
st.getFont().setSize(20);
st.setIsTextWrapped(true);
cell.setStyle(st);

// Set first column width and fourth column height
ws.getCells().setColumnWidth(0, 80);
ws.getCells().setRowHeight(3, 60);

// Create image or print options.
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setOnePagePerSheet(true);
opts.setImageType(AsposeCells.ImageType.Png);

// Render worksheet image with Courier New as default font.
opts.setDefaultFont("Courier New");
let sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "out_courier_new_out.png");

// Render worksheet image again with Times New Roman as default font.
opts.setDefaultFont("Times New Roman");
sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, "times_new_roman_out.png");
```
