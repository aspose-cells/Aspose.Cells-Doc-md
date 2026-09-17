---
title: 将图片插入单元格
linktitle: 将图片插入单元格
description: Aspose.Cells 是用于处理电子表格文件的 Node.js via Java 库。本文介绍如何将图片精确放入单个单元格，可以通过在单元格上方放置浮动图片或将图片直接嵌入单元格两种方式实现。
keywords: Aspose.Cells, Node.js via Java 库, 电子表格, 插入图片, 嵌入图片, 单元格图片, 图片适配单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/nodejs-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了两种不同的方式将图片与单个单元格关联。浮动图片是工作表绘图层上的一个形状，它在视觉上覆盖在单元格区域之上；而嵌入图片则存储在单元格内部，并自动缩放以适应单元格的显示区域。请根据您的布局需求选择最合适的方式。
{{% /alert %}}

## **简介**
在设计用作可视化报表、产品目录、员工通讯录、仪表板或库存清单的电子表格时，将图片精确放入单个单元格是一项常见需求。与其将图片拉伸跨越多个单元格或随意放置在工作表上，您可能希望获得一个干净的、与单元格绑定的图片，使其始终与所属单元格保持对齐。
Aspose.Cells 通过两种互补的方式支持此场景：
- **方式 1 — 在单元格上方放置浮动图片。** 向工作表添加 `Picture`，将其 `Placement` 设置为 `MoveAndSize`，并调整其锚定单元格（`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`），使图片恰好覆盖一个单元格。
- **方式 2 — 将图片直接嵌入单元格。** 将图片字节赋值给单元格的 `EmbeddedImage` 属性。图片会自动缩放以适应单元格的显示区域，并随单元格一起移动。
本文其余部分将逐步讲解这两种方式，介绍相关的 API，并展示如何在代码中使用它们。

## **方式 1：在单元格上方放置图片**
浮动图片是驻留在工作表绘图层上的 `Picture` 对象。虽然它不属于任何单个单元格，但它会被锚定到一个单元格区域。图片的锚定单元格（左上角和右下角）决定了其在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。
要使浮动图片恰好覆盖**一个单元格**，您需要：
1. 使用 `worksheet.getPictures().add(int row, int column, InputStream stream)` 添加图片，该方法将新图片锚定到指定单元格。
2. 设置四个锚定属性，使图片的边界矩形与目标单元格重合。
3. 设置 `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`，以便在用户更改列宽或行高时，图片随底层单元格一起移动和调整大小。

### **将图片锚定到单个单元格**
图片的锚定由四个从零开始的索引属性定义：
- `picture.setUpperLeftRow(int)` — 图片顶部边缘的行索引。
- `picture.setUpperLeftColumn(int)` — 图片左侧边缘的列索引。
- `picture.setLowerRightRow(int)` — 图片底部边缘的行索引。若要使图片的底部边缘位于行 `r` 的底部，请将其设置为 `r + 1`。
- `picture.setLowerRightColumn(int)` — 图片右侧边缘的列索引。若要使图片的右侧边缘位于列 `c` 的右侧，请将其设置为 `c + 1`。

{{% alert color="primary" %}}
Aspose.Cells 中的行和列索引**从零开始**。单元格 C6 的行索引为 5，列索引为 2。右下角锚定上的差一错误是图片看起来与相邻单元格重叠的最常见原因。

### **控制放置行为**
`Picture.Placement` 是 `PlacementType` 类型的枚举，用于控制当用户调整底层行或列的大小时图片的行为。对于单个单元格的图片，推荐的值是 `PlacementType.MoveAndSize`，它会使图片随底层单元格一起移动和调整大小，从而保持精确的适配。

### **逐步操作说明**
1. 创建一个新的 `Workbook`（或打开现有的工作簿）。
2. 通过 `workbook.getWorksheets().get(0)` 访问目标 `Worksheet`。
3. 使用 `InputStream` 从磁盘打开图像文件（例如，使用 `FileInputStream`），以便正确关闭流。
4. 调用 `worksheet.getPictures().add(5, 2, stream)` 添加锚定到单元格 C6 的图片。捕获返回的 `Picture` 引用。
5. 设置四个锚定坐标，使图片仅覆盖单元格 C6：`UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. 设置 `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`，以便在调整列或行大小时图片保持与 C6 对齐。
7. 可选地向周围单元格添加示例文本，以演示只有单元格 C6 包含该图片。
8. 将工作簿保存为磁盘上的 `.xlsx` 文件。
以下代码演示了完整的实现方式。

```javascript
const AsposeCells = require("aspose.cells-node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
var picIndex = worksheet.getPictures().add(5, 2, "logo.png");
var picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **方式 2：将图片直接嵌入单元格**
Aspose.Cells 还为单元格绑定图片提供了一种更简单的机制：`Cell.EmbeddedImage` 属性。将图片字节赋值给此属性即可将图片附加到单元格本身，就像内联内容一样。

### **嵌入图片的工作原理**
- 图片作为单元格内容的一部分存储，而不是作为绘图层上的形状。
- 图片会自动缩放以适应单元格的渲染边界。无需设置锚定坐标或放置选项。
- 该单元格仍然是具有真实地址的真实单元格，可被公式引用、作为行的一部分进行排序，或用于其他单元格级别的操作。
当您的目标仅仅是"在此单元格内放置一张图片"时，`Cell.EmbeddedImage` 是最简洁的选择。

### **逐步操作说明**
1. 创建一个新的 `Workbook`（或打开现有的工作簿）。
2. 通过 `workbook.getWorksheets().get(0)` 访问目标 `Worksheet`。
3. 将图像文件从磁盘读入字节数组（例如，使用 `java.nio.file.Files` 中的 `Files.readAllBytes`）。
4. 获取目标单元格的引用 —— 可以通过 `worksheet.getCells().get("C6")` 或 `worksheet.getCells().get(5, 2)`。
5. 通过 `cell.setEmbeddedImage(bytes)` 将字节数组赋值给单元格的 `EmbeddedImage` 属性。
6. 可选地调整目标行和列的行高与列宽，使嵌入的图片更加突出。
7. 将工作簿保存为磁盘上的 `.xlsx` 文件。
以下代码演示了完整的实现方式。

```javascript
const AsposeCells = require("aspose.cells-node");
const fs = require("fs");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// 获取目标单元格 C6
var cell = worksheet.getCells().get("C6");
// 将图片文件读取为字节数组
var imageData = fs.readFileSync("logo.png");
// 将图片直接嵌入到单元格中
cell.setEmbeddedImage(imageData);
// 可选地调整行高和列宽，使嵌入的图片更明显
worksheet.getCells().setColumnWidth(2, 30);   // 列 C（索引 2）
worksheet.getCells().setRowHeight(5, 100);     // 第 6 行（索引 5）
// 将生成的工作簿保存为 .xlsx 文件
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **选择合适的方式**
两种方式都可以生成适合放入单个单元格的图片，但它们在图片存储方式和行为表现上有所不同：
- **在以下情况下使用浮动图片（方式 1）：**
  - 您需要对放置、图层堆叠或与其他绘图对象的对齐进行更精细的控制。
  - 您希望图片表现为一种形状，可以被选中、重新排序或与其他形状分组。
  - 您需要与已经使用 `PictureCollection` 的代码保持向后兼容性。
  - 您需要根据工作表布局动态计算锚定坐标。
- **在以下情况下使用嵌入图片（方式 2）：**
  - 您希望以最简单的方式将图片插入单元格。
  - 图片应像其他单元格内容一样随单元格一起移动。
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}