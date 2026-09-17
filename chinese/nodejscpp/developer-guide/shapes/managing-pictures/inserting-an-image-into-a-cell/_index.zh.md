---
title: 在单元格中插入图片
linktitle: 在单元格中插入图片
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js via C++ 库。本文介绍如何将图片精确地适配到单个单元格，包括将浮动图片放置在单元格上方，或将图像直接嵌入单元格中。
keywords: Aspose.Cells, Node.js via C++ 库, 电子表格, 插入图片, 嵌入图像, 单元格中的图片, 将图片适配到单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/nodejs-cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了两种不同的方式将图像与单个单元格关联。浮动图片是工作表绘图层上的一个形状，它在视觉上覆盖一个单元格区域，而嵌入图像则存储在单元格内部，并会自动缩放以适应单元格的显示区域。请根据您的布局需求选择最合适的方法。
{{% /alert %}}

## **简介**
在设计作为可视化报表、产品目录、员工通讯录、仪表板或库存清单的电子表格时，将图片精确地适配到单个单元格是一个常见需求。与其将图像拉伸到多个单元格或随意放置在工作表上，您可能希望图片与所在单元格保持清晰、整齐的绑定关系。
Aspose.Cells 通过两种互补的方式支持此场景：
- **方法 1 — 将浮动图片放置在单元格上方。** 将 `Picture` 添加到工作表，将其 `placement` 设置为 `MoveAndSize`，并调整其锚定单元格（`upperLeftRow`、`upperLeftColumn`、`lowerRightRow`、`lowerRightColumn`），使图片恰好覆盖一个单元格。
- **方法 2 — 将图像直接嵌入单元格中。** 将图像字节赋值给单元格的 `embeddedImage` 属性。图像会自动缩放以适应单元格的显示区域，并随单元格一起移动。
本文接下来的部分将逐步讲解这两种方法，介绍相关的 API，并展示如何在代码中使用它们。

## **方法 1：将图片放置在单元格上方**
浮动图片是驻留在工作表绘图层上的 `Picture` 对象。虽然它不属于任何单个单元格，但会被锚定到一个单元格区域。图片的锚定单元格（左上角和右下角）决定了它在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。
若要让浮动图片恰好覆盖 **一个单元格**，您需要：
1. 使用 `worksheet.pictures.add(row, column, stream)` 添加图片，该调用会将新图片锚定到指定的单元格。
2. 设置四个锚定属性，使图片的边界矩形与目标单元格重合。
3. 将 `picture.placement` 设置为 `PlacementType.MoveAndSize`，以便当用户更改列宽或行高时，图片会随其下方单元格一起移动和缩放。

### **将图片锚定到单个单元格**
图片的锚定由四个从零开始的索引属性定义：
- `picture.upperLeftRow` — 图片顶边所在的行索引。
- `picture.upperLeftColumn` — 图片左边所在的列索引。
- `picture.lowerRightRow` — 图片底边所在的行索引。要使图片的底边位于行 `r` 的底部，请将其设置为 `r + 1`。
- `picture.lowerRightColumn` — 图片右边所在的列索引。要使图片的右边位于列 `c` 的右侧，请将其设置为 `c + 1`。

{{% alert color="primary" %}}
Aspose.Cells 中的行和列索引采用 **从零开始** 的编号方式。单元格 C6 的行索引为 5，列索引为 2。右下角锚定的差一错误是导致图片看似溢出到相邻单元格的最常见原因。

### **控制放置行为**
`picture.placement` 是 `PlacementType` 类型的枚举，用于控制当用户调整图片下方行或列时图片的行为。对于单单元格图片，推荐的取值是 `PlacementType.MoveAndSize`，它会使图片与其下方单元格一起移动和缩放，从而保持精确的适配效果。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开现有的工作簿）。
2. 通过 `workbook.worksheets[0]` 访问目标 `Worksheet`。
3. 将磁盘上的图像文件打开到流中，并确保使用完毕后正确关闭该流。
4. 调用 `worksheet.pictures.add(5, 2, stream)` 添加锚定到单元格 C6 的图片，并接收返回的 `Picture` 引用。
5. 设置四个锚定坐标，使图片仅覆盖单元格 C6：`upperLeftRow = 5`，`upperLeftColumn = 2`，`lowerRightRow = 6`，`lowerRightColumn = 3`。
6. 将 `picture.placement = PlacementType.MoveAndSize`，以确保在调整列宽或行高时图片始终与 C6 对齐。
7. 可选择在周围单元格中添加示例文本，以演示只有单元格 C6 包含此图片。
8. 将工作簿以 `.xlsx` 文件格式保存到磁盘。
下面的代码演示了完整的实现方法。

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const fs_stream = fs.createReadStream("logo.png");
const picIndex = worksheet.getPictures().add(5, 2, fs_stream);
const picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **方法 2：将图像直接嵌入单元格**
Aspose.Cells 还提供了一种更简单的单元格绑定图像机制：`cell.embeddedImage` 属性。将图像字节赋值给该属性即可将图像附加到单元格本身，就像内联内容一样。

### **嵌入图像的工作原理**
- 图像作为单元格内容的一部分存储，而不是作为绘图层上的形状。
- 图像会自动缩放以适应单元格的渲染边界。无需任何锚定坐标或放置设置。
- 该单元格仍然是具有真实地址的真实单元格，可以被公式引用、作为某一行的一部分参与排序，或用于其他单元格级别的操作。
这使得 `cell.embeddedImage` 成为"在该单元格内嵌入一张图像"这一目标最简洁的选项。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开现有的工作簿）。
2. 通过 `workbook.worksheets[0]` 访问目标 `Worksheet`。
3. 使用 Node.js 文件系统 API（例如 `fs.readFileSync`）将磁盘上的图像文件读取到 Buffer 或字节数组中。
4. 获取目标单元格的引用——可以通过 `worksheet.cells["C6"]` 或 `worksheet.cells[5, 2]`。
5. 将字节数组赋值给该单元格的 `embeddedImage` 属性。
6. 可选择调整目标行和列的行高与列宽，使嵌入图像看起来更加突出。
7. 将工作簿以 `.xlsx` 文件格式保存到磁盘。
下面的代码演示了完整的实现方法。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// 获取目标单元格 C6
var cell = worksheet.getCells().get("C6");
// 将图像文件读取到字节数组中
var imageData = fs.readFileSync("logo.png");
// 将图像直接嵌入到单元格中
cell.setEmbeddedImage(imageData);
// 可选地调整行高和列宽，使嵌入的图像更清晰可见
worksheet.getCells().setColumnWidth(2, 30);   // C 列（索引 2）
worksheet.getCells().setRowHeight(5, 100);     // 第 6 行（索引 5）
// 将生成的工作簿保存为 .xlsx 文件
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **选择合适的方法**
两种方法都可以生成一张适配在单个单元格内的图片，但它们在图片的存储方式和行为表现上有所不同：
- **在以下情况下使用浮动图片（方法 1）：**
  - 您需要对放置、图层顺序或与其他绘图对象的对齐方式进行更精细的控制。
  - 您希望图片作为可被选中、重新排序或与其他形状分组的形状。
  - 您需要与已有的图片集合相关代码保持兼容性。
  - 您需要根据工作表布局动态计算锚定坐标。
- **在以下情况下使用嵌入图像（方法 2）：**
  - 您希望以最简单的方式将图像插入单元格。
  - 图像应当像其他单元格内容一样随单元格一起移动。
{{% /alert %}}

## 相关文章
- [Aspose.Cells for Node.js via C++ 中的 Excel 照相机](/cells/zh/nodejs-cpp/excel-camera/)
- [Aspose.Cells for Node.js via C++ 中向数据透视表添加筛选字段](/cells/zh/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via C++ 中对数据透视表应用样式](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)
- [修改数据透视表中的页面字段布局](/cells/zh/nodejs-cpp/change-page-field-layout/)
- [Aspose.Cells for Node.js via C++ 中将迷你图转换为图像和 HTML](/cells/zh/nodejs-cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="javascript" >}}