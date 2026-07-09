---
title: 在单元格中插入图片
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库。本文介绍如何通过两种不同的方法使图片恰好适配单个单元格大小，将浮动图片放置在单元格上方，或将图片直接嵌入到单元格中。
keywords: Aspose.Cells, NET 库, 电子表格, 插入图片, 嵌入图片, 单元格中的图片, 图片适配单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells 提供了两种不同的方式将图片与单个单元格关联。浮动图片是工作表绘图层上的一个形状，在视觉上覆盖一个单元格区域；而嵌入图片则存储在单元格内部，并自动按单元格的显示区域进行缩放。请根据您的布局需求选择最合适的方式。

{{% /alert %}}

## **简介**

在设计作为可视化报告、产品目录、员工通讯录、仪表板或库存清单的电子表格时，使图片恰好适配单个单元格是一项常见需求。与其将图片拉伸到多个单元格，或随意放置在工作表上，您可能希望获得一个干净的、与所属单元格对齐的单元格绑定图片。

Aspose.Cells 以两种互补的方式支持此场景：

- **方式 1 — 将浮动图片放置在单元格上方。** 向工作表添加一个 `Picture`，将其 `Placement` 设置为 `MoveAndSize`，并调整其锚定单元格（`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`），使图片恰好覆盖一个单元格。
- **方式 2 — 将图片直接嵌入到单元格中。** 将图片字节赋值给单元格的 `EmbeddedImage` 属性。图片将自动缩放以适配单元格的显示区域，并随单元格一起移动。

本文的其余部分将逐步讲解这两种方法，介绍相关的 API，并展示如何在代码中使用它们。

## **方式 1：将图片放置在单元格上方**

浮动图片是存在于工作表绘图层上的 `Picture` 对象。虽然它不属于任何单个单元格，但它被锚定到一个单元格区域。图片的锚定单元格——其左上角和右下角——决定了其在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。

若要使浮动图片恰好覆盖**一个单元格**，您需要：

1. 使用 `Worksheet.Pictures.Add(int row, int column, Stream stream)` 添加图片，该方法会将新图片锚定到指定的单元格。
2. 设置四个锚定属性，使图片的边界矩形与目标单元格重合。
3. 将 `Picture.Placement` 设置为 `PlacementType.MoveAndSize`，以便在用户更改列宽或行高时，图片与底层单元格一起移动和调整大小。

### **将图片锚定到单个单元格**

图片的锚点由四个从零开始的索引属性定义：

- `Picture.UpperLeftRow` — 图片上边缘的行索引。
- `Picture.UpperLeftColumn` — 图片左边缘的列索引。
- `Picture.LowerRightRow` — 图片下边缘的行索引。若要使图片下边缘位于第 `r` 行的底部，请将其设置为 `r + 1`。
- `Picture.LowerRightColumn` — 图片右边缘的列索引。若要使图片右边缘位于第 `c` 列的右侧，请将其设置为 `c + 1`。

例如，要使图片恰好适配单元格 **C6**（行索引 `5`，列索引 `2`），请设置 `UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`，以及 `LowerRightColumn = 3`。

{{% alert color="primary" %}}

Aspose.Cells 中的行和列索引**从零开始**。单元格 C6 的行索引为 5，列索引为 2。右下角锚点的差一错误（off-by-one error）是图片看起来延伸到相邻单元格的最常见原因。

{{% /alert %}}

### **控制放置行为**

`Picture.Placement` 是一个 `PlacementType` 类型的枚举，用于控制当用户调整其下方行或列的大小时图片的行为。对于单个单元格的图片，推荐的值为 `PlacementType.MoveAndSize`，它会使图片与其底层单元格一起移动和调整大小，从而保持精确适配。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开一个现有的工作簿）。
2. 从 `workbook.Worksheets[0]` 访问目标 `Worksheet`。
3. 使用 `using` 块将磁盘上的图像文件打开到 `FileStream` 中，以确保流被正确释放。
4. 调用 `worksheet.Pictures.Add(5, 2, stream)` 添加一个锚定到单元格 C6 的图片。保存返回的 `Picture` 引用。
5. 设置四个锚定坐标，使图片仅覆盖单元格 C6：`UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. 设置 `picture.Placement = PlacementType.MoveAndSize`，以便在调整列或行大小时图片仍与 C6 保持对齐。
7. （可选）向周围的单元格添加示例文本，以演示只有单元格 C6 包含该图片。
8. 将工作簿另存为磁盘上的 `.xlsx` 文件。

以下代码演示了完整的实现方式。

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

using (FileStream fs = new FileStream("logo.png", FileMode.Open, FileAccess.Read))
{
    int picIndex = worksheet.Pictures.Add(5, 2, fs);
    Picture picture = worksheet.Pictures[picIndex];
    picture.UpperLeftRow = 5;
    picture.UpperLeftColumn = 2;
    picture.LowerRightRow = 6;
    picture.LowerRightColumn = 3;
    picture.Placement = PlacementType.MoveAndSize;
}

workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **方式 2：将图片直接嵌入到单元格中**

Aspose.Cells 还提供了一种更简洁的单元格绑定图片机制：`Cell.EmbeddedImage` 属性。将图片字节赋值给此属性即可将图片附加到单元格本身，如同它是内联内容一样。

### **嵌入图片的工作原理**

- 图片作为单元格内容的一部分存储，而不是作为绘图层上的形状存储。
- 图片会自动缩放以适配单元格的渲染边界。无需任何锚定坐标或放置设置。
- 该单元格仍是一个具有真实地址的真实单元格，可被公式引用、作为行的一部分进行排序，或用于其他单元格级别的操作。

当您的目标仅仅是"一张存在于该单元格中的图片"时，`Cell.EmbeddedImage` 是最简洁的选项。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开一个现有的工作簿）。
2. 从 `workbook.Worksheets[0]` 访问目标 `Worksheet`。
3. 将磁盘上的图像文件读入到 `byte[]` 数组中（例如，使用 `File.ReadAllBytes`）。
4. 获取目标单元格的引用——可以通过 `worksheet.Cells["C6"]` 或 `worksheet.Cells[5, 2]`。
5. 将字节数组赋值给单元格的 `EmbeddedImage` 属性。
6. （可选）调整目标行和列的行高与列宽，以使嵌入的图片更加醒目。
7. 将工作簿另存为磁盘上的 `.xlsx` 文件。

以下代码演示了完整的实现方式。

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// 获取目标单元格 C6
var cell = worksheet.Cells["C6"];

// 将图片文件读取为字节数组
byte[] imageData = File.ReadAllBytes("logo.png");

// 将图片直接嵌入到单元格中
cell.EmbeddedImage = imageData;

// 可选地调整行高和列宽，使嵌入的图片更加清晰可见
worksheet.Cells.SetColumnWidth(2, 30);   // 列 C（索引 2）
worksheet.Cells.SetRowHeight(5, 100);     // 行 6（索引 5）

// 将生成的工作簿保存为 .xlsx 文件
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **选择合适的方式**

两种方法都能生成适配单个单元格的图片，但它们在图片的存储方式和行为上有所不同：

- **在以下情况下使用浮动图片（方式 1）：**
  - 您需要对放置、图层顺序或与其他绘图对象的对齐方式进行更精细的控制。
  - 您希望图片作为一个可以被选中、重新排序或与其他形状组合的形状来使用。
  - 您需要与已使用 `PictureCollection` 的现有代码保持兼容。
  - 您需要根据工作表布局动态计算锚定坐标。

- **在以下情况下使用嵌入图片（方式 2）：**
  - 您希望以最简单的方式将图片插入到单元格中。
  - 图片应像其他单元格内容一样随单元格一起移动。
  - 您无需将图片作为形状进行操作。

{{% alert color="primary" %}}

两种方法可以在同一个工作簿中共存。您可以在某些单元格上方放置浮动图片，同时在其他单元格中直接嵌入图片，因为这两种机制在文件中使用不同的存储层。

{{% /alert %}}

## **相关文章**

- [如何在单元格中插入图片](/cells/zh/net/how-to-place-image-to-cell/)
- [如何使图片适配单元格的宽度和高度](/cells/zh/net/how-to-fit-image-to-cell-width-height/)
- [添加图片超链接](/cells/zh/net/add-image-hyperlinks/)
- [将 URL 中的网络图片加载到 Excel 工作表](/cells/zh/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [操作位置、大小和设计器图表](/cells/zh/net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="csharp" >}}