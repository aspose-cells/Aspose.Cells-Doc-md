---
title: 用Node.js通过C++管理范围
linktitle: 范围
type: docs
weight: 105
url: /zh/nodejs-cpp/managing-ranges/
description: 学习如何使用Aspose.Cells for Node.js via C++管理Excel中的范围。创建区域、设置值、样式并执行各种操作。
---

## **介绍**

在Excel中，可以使用鼠标框选择多个单元格；所选的单元格集合称为“范围”。

例如，你可以在Excel中的单元格“ A1”点击鼠标左键，然后拖动到“ C4”。所选的矩形区域也可以通过Aspose.Cells for Node.js via C++轻松创建为对象。

以下是如何创建范围、放置值、设置样式以及在“范围”对象上执行更多操作的方法。

## **用Aspose.Cells for Node.js via C++管理区域**

Aspose.Cells提供了一个代表Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个[**Workbook.getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合。

### **创建范围**

当您想创建覆盖 A1:C4 的矩形区域时，您可以使用以下代码：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
```

### **将值放入范围单元格**

假设您有一个涵盖 A1:C4 的单元格范围。该矩阵形成 4 * 3 = 12 个单元格。单个范围单元格是按顺序排列的：Range[0,0]、Range[0,1]、Range[0,2]、Range[1,0]、Range[1,1]、Range[1,2]、Range[2,0]、Range[2,1]、Range[2,2]、Range[3,0]、Range[3,1]、Range[3,2]。

以下示例展示如何向范围单元格输入一些值。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "RangeValueTest.xlsx");

// Create a Workbook
const workbook = new AsposeCells.Workbook();
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const range = cells.createRange("A1:C4");
// Put value
range.get(0, 0).setValue("A1");
range.get(0, 1).setValue("B1");
range.get(0, 2).setValue("C1");
range.get(3, 0).setValue("A4");
range.get(3, 1).setValue("B4");
range.get(3, 2).setValue("C4");
// Save the Workbook
workbook.save(filePath);
```

### **设置范围单元格的样式**

以下示例演示了如何设置范围内单元格的样式。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Creates a Workbook
const workbook = new AsposeCells.Workbook();
// Gets Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Creates Range
const range = cells.createRange("A1:C4");
// Puts value
range.get(0, 0).setValue("A1");
range.get(3, 2).setValue("C4");
// Sets Style
let style00 = workbook.createStyle();
style00.setPattern(AsposeCells.BackgroundType.Solid);
style00.setForegroundColor(new AsposeCells.Color(255, 0, 0)); // Red
range.get(0, 0).setStyle(style00);
let style32 = workbook.createStyle();
style32.setPattern(AsposeCells.BackgroundType.HorizontalStripe);
style32.setForegroundColor(new AsposeCells.Color(0, 255, 0)); // Green
range.get(3, 2).setStyle(style32);
// Saves the Workbook
workbook.save("RangeStyleTest.xlsx");
```

### **获取范围的当前区域**

CurrentRegion 是一个返回代表当前区域的 Range 对象的属性。 

当前区域是由任意组合空行和空列所限定的范围。只读。

在Excel中，你可以通过以下方法获取当前区域：
1. 用鼠标框选一个区域（范围1）。
2. 点击“主页 - 编辑 - 查找和选择 - 转到特殊 - 当前区域”，或使用“Ctrl+Shift+*”，你会看到Excel自动帮你选择一个区域（范围2）。完成后，范围2即为范围1的当前区域。

请下载以下测试文件，在Excel中打开，用鼠标框选一个区域“A1:D7”，然后点击“Ctrl+Shift+*”，你将看到区域“A1:C3”被选中。

[current_region.xlsx](current_region.xlsx)

现在请运行以下示例，查看它在Aspose.Cells中的工作方式：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "current_region.xlsx");
// Create a Workbook
const workbook = new AsposeCells.Workbook(filePath);
// Get Cells
const cells = workbook.getWorksheets().get(0).getCells();
// Create Range
const src = cells.createRange("A1:D7");
// Get CurrentRegion
const A1C3 = src.getCurrentRegion();
```


## **高级主题**
- [Excel文件的自动填充范围](/cells/zh/nodejs-cpp/autofill-ranges/)
- [复制Excel的区域](/cells/zh/nodejs-cpp/copy-ranges-of-Excel/)
- [仅复制区域数据](/cells/zh/nodejs-cpp/copy-range-data-only/)
- [复制具有样式的区域数据](/cells/zh/nodejs-cpp/copy-range-data-with-style/)
- [仅复制区域样式](/cells/zh/nodejs-cpp/copy-range-style-only/)
- [创建联合范围](/cells/zh/nodejs-cpp/create-union-range/)
- [剪切和粘贴范围](/cells/zh/nodejs-cpp/cut-and-paste-cells/)
- [删除区域](/cells/zh/nodejs-cpp/delete-ranges-from-Excel/)
- [获取区域的地址、单元格计数、偏移、整行和整列](/cells/zh/nodejs-cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [插入范围](/cells/zh/nodejs-cpp/insert-ranges-to-Excel/)
- [合并或取消合并单元格范围](/cells/zh/nodejs-cpp/merge-or-unmerge-range-of-cells/)
- [在工作表中移动单元格范围](/cells/zh/nodejs-cpp/move-range-of-cells-in-a-worksheet/)
- [创建工作簿和工作表范围命名](/cells/zh/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [在范围内搜索和替换数据](/cells/zh/nodejs-cpp/search-and-replace-data-in-a-range/)
{{< app/cells/assistant language="nodejs-cpp" >}}
