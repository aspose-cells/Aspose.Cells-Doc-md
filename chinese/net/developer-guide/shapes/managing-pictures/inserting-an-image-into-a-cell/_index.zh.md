---
title: 在单元格中插入图片
linktitle: 在单元格中插入图片
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库。本文介绍如何将图片精确适配到单个单元格，可以通过在单元格上方放置浮动图片，也可以直接将图片嵌入到单元格中。
keywords: Aspose.Cells, .NET 库, 电子表格, 插入图片, 嵌入图片, 单元格中的图片, 将图片适配到单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/net/inserting-an-image-into-a-cell/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了两种不同的方式将图片与单个单元格关联。浮动图片是工作表绘图层上的一个形状，它在视觉上覆盖一个单元格区域，而嵌入图片则存储在单元格内部，并会自动缩放到单元格的显示区域。请根据您的布局需求选择最适合的方式。

## **简介**
在设计作为可视化报表、产品目录、员工通讯录、仪表板或库存清单的电子表格时，将图片精确适配到单个单元格是一项常见需求。与其将图片拉伸到多个单元格或随意放置在工作表上，您可能希望获得一个干净的、与单元格绑定的图片，并保持与所属单元格的对齐。
Aspose.Cells 以两种互补的方式支持此场景：
- **方法 1 — 在单元格上方放置浮动图片。** 向工作表添加一个 `Picture`，将其 `Placement` 设置为 `MoveAndSize`，并调整其锚定单元格（`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`），使图片恰好覆盖一个单元格。
- **方法 2 — 将图片直接嵌入到单元格中。** 将图片字节赋值给单元格的 `EmbeddedImage` 属性。图片会自动缩放以适配单元格的显示区域，并随单元格一起移动。
本文的其余部分将逐一讲解这两种方法，介绍相关的 API，并展示如何在代码中使用它们。

## **方法 1：在单元格上方放置图片**
浮动图片是位于工作表绘图层上的 `Picture` 对象。尽管它不属于任何单个单元格，但它锚定在一个单元格区域上。图片的锚定单元格——其左上角和右下角——决定了其在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。
若要使浮动图片恰好覆盖**单个单元格**，您需要：
1. 使用 `Worksheet.Pictures.Add(int row, int column, Stream stream)` 添加图片，该方法会将新图片锚定到指定单元格。
2. 设置四个锚定属性，使图片的边界矩形与目标单元格重合。
3. 将 `Picture.Placement` 设置为 `PlacementType.MoveAndSize`，以便在用户更改列宽或行高时，图片能够随底层单元格一起移动和调整大小。

### **将图片锚定到单个单元格**
图片的锚点由四个从零开始的索引属性定义：
- `Picture.UpperLeftRow` — 图片顶边所在的行索引。
- `Picture.UpperLeftColumn` — 图片左边所在的列索引。
- `Picture.LowerRightRow` — 图片底边所在的行索引。若要将图片底边对齐到行 `r` 的底部，需将其设置为 `r + 1`。
- `Picture.LowerRightColumn` — 图片右边所在的列索引。若要将图片右边对齐到列 `c` 的右侧，需将其设置为 `c + 1`。

{{% alert color="primary" %}}
Aspose.Cells 中的行和列索引**从零开始**。单元格 C6 的行索引为 5，列索引为 2。右下角锚点的差一错误是导致图片看似溢出到相邻单元格的最常见原因。

### **控制放置行为**
`Picture.Placement` 是 `PlacementType` 类型的枚举，用于控制当用户调整底层行高或列宽时图片的行为。对于单个单元格的图片，推荐值为 `PlacementType.MoveAndSize`，它会使图片与其底层单元格一起移动和调整大小，从而保持精确适配。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开一个已有的工作簿）。
2. 通过 `workbook.Worksheets[0]` 访问目标 `Worksheet`。
3. 使用 `using` 块将磁盘上的图片文件打开到 `FileStream` 中，以确保流被正确释放。
4. 调用 `worksheet.Pictures.Add(5, 2, stream)` 将图片添加到单元格 C6 上，并捕获返回的 `Picture` 引用。
5. 设置四个锚定坐标，使图片仅覆盖单元格 C6：`UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. 将 `picture.Placement = PlacementType.MoveAndSize` 设置为在调整列或行时使图片与 C6 保持对齐。
7. （可选）向周围的单元格添加示例文本，以演示只有单元格 C6 包含图片。
8. 将工作簿以 `.xlsx` 格式保存到磁盘。
以下代码演示了完整的方法。

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

## **方法 2：将图片直接嵌入到单元格中**
Aspose.Cells 还提供了一种更简单的单元格绑定图片机制：`Cell.EmbeddedImage` 属性。将图片字节赋值给此属性后，图片将作为内联内容附加到单元格本身。

### **嵌入图片的工作原理**
- 图片作为单元格内容的一部分存储，而不是作为绘图层上的形状。
- 图片会自动缩放以适应单元格的渲染边界。无需锚定坐标或放置设置。
- 单元格仍然是一个具有真实地址的真实单元格，可以被公式引用、作为行的一部分排序，或用于其他单元格级别的操作。
当您的目标仅仅是"一张位于此单元格内的图片"时，`Cell.EmbeddedImage` 是最简洁的选择。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开一个已有的工作簿）。
2. 通过 `workbook.Worksheets[0]` 访问目标 `Worksheet`。
3. 将磁盘上的图片文件读取到 `byte[]` 数组中（例如，使用 `File.ReadAllBytes`）。
4. 获取目标单元格的引用 —— 可以通过 `worksheet.Cells["C6"]` 或 `worksheet.Cells[5, 2]`。
5. 将字节数组赋值给单元格的 `EmbeddedImage` 属性。
6. （可选）调整目标行和列的行高与列宽，使嵌入的图片显示效果更突出。
7. 将工作簿以 `.xlsx` 格式保存到磁盘。
以下代码演示了完整的方法。

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// 获取目标单元格 C6
var cell = worksheet.Cells["C6"];
// 将图像文件读取到字节数组中
byte[] imageData = File.ReadAllBytes("logo.png");
// 将图像直接嵌入到单元格中
cell.EmbeddedImage = imageData;
// 可选地调整行高和列宽，以便嵌入的图像更清晰可见
worksheet.Cells.SetColumnWidth(2, 30);   // C 列（索引 2）
worksheet.Cells.SetRowHeight(5, 100);     // 第 6 行（索引 5）
// 将生成的工作簿保存为 .xlsx 文件
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **选择合适的方法**
两种方法都可以生成适合单个单元格的图片，但它们在图片的存储方式和行为上有所不同：
- **在以下情况下使用浮动图片（方法 1）：**
  - 您需要对放置、图层顺序或与其他绘图对象的对齐进行更精细的控制。
  - 您希望图片作为形状表现，可以被选中、重新排序或与其他形状分组。
  - 您需要与已经支持 `PictureCollection` 的代码保持向后兼容。
  - 您需要根据工作表布局动态计算锚定坐标。
- **在以下情况下使用嵌入图片（方法 2）：**
  - 您希望以最简单的方式将图片插入到单元格中。
  - 图片应像其他单元格内容一样随单元格一起移动。
  - 您不需要将图片作为形状进行操作。
{{% /alert %}}

{{% /alert %}}

## 相关文章
- [Aspose.Cells for .NET 中的 Excel 照相机](/cells/zh/net/excel-camera/)
- [Aspose.Cells for .NET 中向数据透视表添加筛选字段](/cells/zh/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET 中对数据透视表应用样式](/cells/zh/net/apply-style-to-pivot-table/)
- [修改数据透视表的页面字段布局](/cells/zh/net/change-page-field-layout/)
- [Aspose.Cells for .NET 中将迷你图转换为图片和 HTML](/cells/zh/net/convert-sparkline-to-image-and-html/)csharp

{{< app/cells/assistant language="csharp" >}}