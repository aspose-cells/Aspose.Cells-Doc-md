---
title: 在单元格中插入图像
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js via C++ 库。本文介绍如何使用两种不同的方法将图片精确地适配到单个单元格大小：在单元格上放置浮动图片，或将图像直接嵌入到单元格中。
keywords: Aspose.Cells, Node.js via C++ 库, 电子表格, 插入图像, 嵌入图像, 单元格中的图片, 图片适配单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/nodejs-cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells 提供两种不同的方式将图像与单个单元格关联。浮动图片是工作表绘图层上的一个形状，它在视觉上覆盖一个单元格区域，而嵌入图像则存储在单元格内部，并自动缩放以适应单元格的显示区域。选择最适合您布局要求的方法。

{{% /alert %}}

## **简介**

在设计充当可视化报表、产品目录、员工通讯录、仪表板或库存清单的电子表格时，将图片精确适配到单个单元格是一项常见需求。您可能不希望将图像拉伸跨越多个单元格或随意放置在工作表上，而是希望获得一个干净的、绑定单元格的图像，使其保持与所属单元格对齐。

Aspose.Cells 通过两种互补的方式支持此场景：

- **方法 1 — 在单元格上方放置浮动图片。** 将 `Picture` 添加到工作表，将其 `placement` 设置为 `MoveAndSize`，并调整其锚定单元格（`upperLeftRow`、`upperLeftColumn`、`lowerRightRow`、`lowerRightColumn`），使图片精确覆盖一个单元格。
- **方法 2 — 将图像直接嵌入单元格。** 将图像字节分配给单元格的 `embeddedImage` 属性。图像会自动缩放以适应单元格的显示区域，并随单元格一起移动。

本文的其余部分将详细介绍这两种方法，解释相关的 API，并展示如何在代码中使用它们。

## **方法 1：在单元格上方放置图片**

浮动图片是一个 `Picture` 对象，它位于工作表的绘图层上。虽然它不属于任何单个单元格，但它锚定到一个单元格区域。图片的锚定单元格——其左上角和右下角——决定其在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。

要使浮动图片精确覆盖**一个**单元格，您需要：

1. 使用 `worksheet.pictures.add(row, column, stream)` 添加图片，该方法会将新图片锚定到指定单元格。
2. 设置四个锚点属性，使图片的边界矩形与目标单元格重合。
3. 将 `picture.placement` 设置为 `PlacementType.MoveAndSize`，以便当用户更改列宽或行高时，图片能够与底层单元格一起移动和调整大小。

### **将图片锚定到单个单元格**

图片的锚点由四个基于零的索引属性定义：

- `picture.upperLeftRow` — 图片顶边的行索引。
- `picture.upperLeftColumn` — 图片左边的列索引。
- `picture.lowerRightRow` — 图片底边的行索引。要使图片底边位于行 `r` 的底部，请将其设置为 `r + 1`。
- `picture.lowerRightColumn` — 图片右边的列索引。要使图片右边位于列 `c` 的右侧，请将其设置为 `c + 1`。

例如，要将图片精确适配到单元格 **C6**（行索引 `5`，列索引 `2`），请设置 `upperLeftRow = 5`、`upperLeftColumn = 2`、`lowerRightRow = 6` 和 `lowerRightColumn = 3`。

{{% alert color="primary" %}}

Aspose.Cells 中的行和列索引是**基于零的**。单元格 C6 的行索引为 5，列索引为 2。右下锚点的差一错误是图片看起来与相邻单元格重叠的最常见原因。

{{% /alert %}}

### **控制放置行为**

`picture.placement` 是 `PlacementType` 类型的枚举，用于控制当用户调整其下方行或列大小时图片的行为。对于单单元格图片，推荐值为 `PlacementType.MoveAndSize`，它会使图片与其底层单元格一起移动和调整大小，从而保持精确适配。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开现有的）。
2. 从 `workbook.worksheets[0]` 访问目标 `Worksheet`。
3. 将图像文件从磁盘打开到流中，确保使用后正确关闭流。
4. 调用 `worksheet.pictures.add(5, 2, stream)` 将图片添加到锚定于单元格 C6 的位置。获取返回的 `Picture` 引用。
5. 设置四个锚点坐标，使图片仅覆盖单元格 C6：`upperLeftRow = 5`、`upperLeftColumn = 2`、`lowerRightRow = 6`、`lowerRightColumn = 3`。
6. 设置 `picture.placement = PlacementType.MoveAndSize`，以便在调整列或行大小时保持图片与 C6 对齐。
7. （可选）向周围的单元格添加示例文本，以演示只有单元格 C6 包含图片。
8. 将工作簿保存为 `.xlsx` 文件。

以下代码演示了完整的方法。

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

Aspose.Cells 还为单元格绑定图像提供了一种更简单的机制：`cell.embeddedImage` 属性。将图像字节分配给此属性会将图像附加到单元格本身，就好像它是内联内容一样。

### **嵌入图像的工作原理**

- 图像作为单元格内容的一部分存储，而不是作为绘图层上的形状。
- 图像自动缩放以适应单元格的渲染边界。无需锚点坐标或位置设置。
- 该单元格仍然是一个真实的单元格，具有真实的地址，可以被公式引用、作为行的一部分进行排序，或用于其他单元格级别的操作。

当您的目标仅仅是"一个驻留在单元格内的图像"时，这使得 `cell.embeddedImage` 成为最简洁的选择。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开现有的）。
2. 从 `workbook.worksheets[0]` 访问目标 `Worksheet`。
3. 使用 Node.js 文件系统 API（例如 `fs.readFileSync`）将图像文件从磁盘读取到 Buffer 或字节数组中。
4. 获取目标单元格的引用——通过 `worksheet.cells["C6"]` 或 `worksheet.cells[5, 2]`。
5. 将字节数组分配给单元格的 `embeddedImage` 属性。
6. （可选）调整目标行和列的行高和列宽，使嵌入的图像更加突出。
7. 将工作簿保存为 `.xlsx` 文件。

以下代码演示了完整的方法。

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// 获取目标单元格 C6
var cell = worksheet.getCells().get("C6");

// 将图像文件读取到字节数组中
var imageData = fs.readFileSync("logo.png");

// 将图像直接嵌入到单元格中
cell.setEmbeddedImage(imageData);

// 可选地调整行高和列宽,以便嵌入的图像更清晰可见
worksheet.getCells().setColumnWidth(2, 30);   // 列 C(索引 2)
worksheet.getCells().setRowHeight(5, 100);     // 第 6 行(索引 5)

// 将生成的工作簿保存为 .xlsx 文件
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **选择合适的方法**

两种方法都会生成一个适配在单个单元格内的图片，但它们在图片的存储方式和行为上有所不同：

- **在以下情况下使用浮动图片（方法 1）：**
  - 您需要对放置、图层或与其他绘图对象的对齐方式进行更精细的控制。
  - 您希望图片表现为一个可以被选中、重新排序或与其他形状分组的形状。
  - 您需要与已经使用图片集合的代码保持旧版兼容。
  - 您需要根据工作表布局动态计算锚点坐标。

- **在以下情况下使用嵌入图像（方法 2）：**
  - 您希望以最简单的方式将图像插入单元格。
  - 图像应该像其他单元格内容一样随单元格一起移动。
  - 您不需要将图像作为形状进行操作。

{{% alert color="primary" %}}

两种方法可以共存于同一个工作簿中。您可以在一组单元格上方放置浮动图片，并将图像直接嵌入到其他单元格中，因为这两种机制在文件中使用不同的存储层。

{{% /alert %}}

## **相关文章**

- [如何在单元格中插入图片](/cells/zh/nodejs-cpp/how-to-place-image-to-cell/)
- [添加图片超链接](/cells/zh/nodejs-cpp/add-image-hyperlinks/)
- [从 URL 将网络图像加载到 Excel 工作表](/cells/zh/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [操作位置、大小和设计器图表](/cells/zh/nodejs-cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="javascript" >}}