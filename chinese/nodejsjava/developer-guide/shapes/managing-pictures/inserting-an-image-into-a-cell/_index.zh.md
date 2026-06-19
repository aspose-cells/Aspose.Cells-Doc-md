---
title: 在单元格中插入图片
description: Aspose.Cells 是一个通过 Java 使用的 Node.js 库，用于处理电子表格文件。本文介绍如何通过两种不同的方法将图片精确适配到单个单元格大小：将浮动图片放置在单元格上方，或将图片直接嵌入到单元格中。
keywords: Aspose.Cells, Node.js via Java 库, 电子表格, 插入图片, 嵌入图片, 单元格中的图片, 图片适配单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/nodejs-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells 提供了两种不同的方式将图片与单个单元格关联。浮动图片是工作表绘图图层上的一个形状，它在视觉上覆盖一个单元格区域；而嵌入图片则存储在单元格内部，并会自动缩放以适配单元格的显示区域。请选择最符合您布局需求的方法。

{{% /alert %}}

## **简介**

将图片精确适配到单个单元格，是在设计用作可视化报表、产品目录、员工名录、仪表板或库存清单的电子表格时常见的需求。您可能希望获得一个干净的、与单元格绑定的图片，并使其与所属单元格保持对齐，而不是将图片拉伸到多个单元格中或随意放置在工作表上。

Aspose.Cells 通过两种互补的方式支持此场景：

- **方法 1 — 将浮动图片放置在单元格上方。** 向工作表添加一个 `Picture`，将其 `Placement` 设置为 `MoveAndSize`，并调整其锚定单元格（`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`），使图片恰好覆盖一个单元格。
- **方法 2 — 将图片直接嵌入单元格。** 将图片字节数组赋值给单元格的 `EmbeddedImage` 属性。图片会自动缩放以适配单元格的显示区域，并随单元格一起移动。

本文的后续部分将逐步讲解这两种方法，解释相关的 API，并演示如何在代码中使用它们。

## **方法 1：将图片放置在单元格上方**

浮动图片是位于工作表绘图图层上的一个 `Picture` 对象。虽然它不属于任何单个单元格，但它锚定到一个单元格区域。图片的锚定单元格——即其左上角和右下角——决定了它在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。

要使浮动图片恰好覆盖**一个单元格**，您需要：

1. 使用 `worksheet.getPictures().add(int row, int column, InputStream stream)` 添加图片，该方法会将新图片锚定到指定的单元格。
2. 设置四个锚点属性，使图片的边界矩形与目标单元格重合。
3. 设置 `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`，以便当用户更改列宽或行高时，图片能够与其底层单元格一起移动并调整大小。

### **将图片锚定到单个单元格**

图片的锚点由四个从零开始的索引属性定义：

- `picture.setUpperLeftRow(int)` — 图片上边缘所在的行索引。
- `picture.setUpperLeftColumn(int)` — 图片左边缘所在的列索引。
- `picture.setLowerRightRow(int)` — 图片下边缘所在的行索引。要使图片的下边缘位于行 `r` 的底部，请将此值设置为 `r + 1`。
- `picture.setLowerRightColumn(int)` — 图片右边缘所在的列索引。要使图片的右边缘位于列 `c` 的右侧，请将此值设置为 `c + 1`。

例如，要将图片精确适配到单元格 **C6**（行索引为 `5`，列索引为 `2`），请设置 `UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6` 以及 `LowerRightColumn = 3`。

{{% alert color="primary" %}}

Aspose.Cells 中的行和列索引是**从零开始**的。单元格 C6 的行索引为 5，列索引为 2。右下角锚点上的差一错误是导致图片看起来溢出到相邻单元格的最常见原因。

{{% /alert %}}

### **控制放置行为**

`Picture.Placement` 是 `PlacementType` 类型的枚举，用于控制当用户调整底层行高或列宽时图片的行为。对于单元格中的图片，推荐的值为 `PlacementType.MoveAndSize`，它会使图片与其底层单元格一起移动并调整大小，从而保持精确的适配效果。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开现有的工作簿）。
2. 通过 `workbook.getWorksheets().get(0)` 访问目标 `Worksheet`。
3. 将磁盘上的图片文件打开到一个 `InputStream` 中（例如，通过使用 `FileInputStream`），以便正确关闭该流。
4. 调用 `worksheet.getPictures().add(5, 2, stream)` 将图片添加到锚定于单元格 C6 的位置。捕获返回的 `Picture` 引用。
5. 设置四个锚点坐标，使图片仅覆盖单元格 C6：`UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. 设置 `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`，以便在调整列宽或行高时图片仍能与 C6 保持对齐。
7. 可选地向周围单元格添加示例文本，以演示只有单元格 C6 包含该图片。
8. 将工作簿另存为 `.xlsx` 文件。

以下代码演示了完整的方法。

```javascript
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

## **方法 2：将图片直接嵌入单元格**

Aspose.Cells 还提供了一种更简单的机制来实现单元格绑定的图片：`Cell.EmbeddedImage` 属性。将图片字节数组赋值给该属性，即可将图片附加到单元格本身，就像内联内容一样。

### **嵌入图片的工作原理**

- 图片作为单元格内容的一部分存储，而不是作为绘图图层上的形状。
- 图片会自动缩放以适配单元格渲染的边界，无需任何锚点坐标或放置设置。
- 该单元格仍是一个具有真实地址的真实单元格，可以被公式引用、作为某行的一部分进行排序，或用于其他单元格级别的操作。

这使得 `Cell.EmbeddedImage` 成为当您的目标仅仅是"一张存在于该单元格内的图片"时最简洁的选择。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开现有的工作簿）。
2. 通过 `workbook.getWorksheets().get(0)` 访问目标 `Worksheet`。
3. 将磁盘上的图片文件读取到一个字节数组中（例如，使用 `java.nio.file.Files` 中的 `Files.readAllBytes`）。
4. 获取目标单元格的引用——可以通过 `worksheet.getCells().get("C6")` 或 `worksheet.getCells().get(5, 2)`。
5. 通过 `cell.setEmbeddedImage(bytes)` 将字节数组赋值给单元格的 `EmbeddedImage` 属性。
6. 可选地调整目标行和列的行高与列宽，使嵌入的图片具有更突出的显示效果。
7. 将工作簿另存为 `.xlsx` 文件。

以下代码演示了完整的方法。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// 获取目标单元格 C6
var cell = worksheet.getCells().get("C6");

// 将图片文件读取到字节数组中
var imageData = fs.readFileSync("logo.png");

// 将图片直接嵌入到单元格中
cell.setEmbeddedImage(imageData);

// 可选地调整行高和列宽，以便嵌入的图片更加清晰可见
worksheet.getCells().setColumnWidth(2, 30);   // C 列（索引 2）
worksheet.getCells().setRowHeight(5, 100);     // 第 6 行（索引 5）

// 将生成的工作簿保存为 .xlsx 文件
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **选择合适的方法**

两种方法都能生成适配单个单元格的图片，但它们在图片的存储方式和行为上有所不同：

- **在以下情况下使用浮动图片（方法 1）：**
  - 您需要对放置、图层叠放或与其他绘图对象的对齐方式进行更精细的控制。
  - 您希望图片表现得像一个可以被选中、重新排序或与其他形状组合的形状。
  - 您需要与已经使用 `PictureCollection` 的代码保持旧版兼容性。
  - 您需要根据工作表布局动态计算锚点坐标。

- **在以下情况下使用嵌入图片（方法 2）：**
  - 您希望以最简单的方式将图片插入到单元格中。
  - 图片应像其他单元格内容一样随单元格移动。
  - 您不需要将图片作为形状进行操作。

{{% alert color="primary" %}}

两种方法可以在同一工作簿中共存。您可以将浮动图片放置在一组单元格之上，同时将图片直接嵌入到其他单元格中，因为这两种机制在文件中使用不同的存储层。

{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}