---
title: 在单元格中插入图片
linktitle: 在单元格中插入图片
description: Aspose.Cells 是一个用于处理电子表格文件的 Python 库。本文介绍如何将图片精确适配到单个单元格，可以通过在单元格上放置浮动图片，也可以直接将图片嵌入到单元格中。
keywords: Aspose.Cells, Python 库, 电子表格, 插入图片, 嵌入图片, 单元格中的图片, 将图片适配到单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/python-net/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了两种不同的方式将图片与单个单元格关联。浮动图片是工作表绘图图层上的一个形状，它在视觉上覆盖一个单元格区域；而嵌入图片则存储在单元格内部，并会自动缩放以适应单元格的显示区域。请选择最符合您布局需求的方法。
{{% /alert %}}

## **简介**
在设计作为可视化报表、产品目录、员工通讯录、仪表板或库存清单的电子表格时，将图片精确适配到单个单元格是一项常见需求。与其将图片拉伸跨越多个单元格，或者松散地放置在工作表上，您可能更希望获得一张与所属单元格保持对齐的、整洁的、绑定到单元格的图片。
Aspose.Cells 通过两种互补的方式来支持这一场景：
- **方法一 — 在单元格上放置浮动图片。** 向工作表添加一个 `Picture`，将其 `placement` 设置为 `MOVE_AND_SIZE`，并调整其锚定单元格（`upper_left_row`、`upper_left_column`、`lower_right_row`、`lower_right_column`），使图片恰好覆盖一个单元格。
- **方法二 — 将图片直接嵌入单元格。** 将图片字节赋值给单元格的 `embedded_image` 属性。图片会自动缩放以适应单元格的显示区域，并随单元格一起移动。
本文后续章节将逐一介绍这两种方法，解释相关的 API，并展示如何在代码中使用它们。

## **方法一：将图片放置在单元格上**
浮动图片是一个 `Picture` 对象，位于工作表绘图图层上。虽然它不属于任何单个单元格，但它被锚定在一个单元格区域。图片的锚定单元格——左上角和右下角——决定了图片在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。
要使浮动图片恰好覆盖**一个单元格**，您需要：
1. 使用 `Worksheet.pictures.add(row, column, stream)` 添加图片，该方法会将新图片锚定到给定的单元格。
2. 设置四个锚定属性，使图片的边界矩形与目标单元格重合。
3. 将 `Picture.placement` 设置为 `PlacementType.MOVE_AND_SIZE`，这样在用户更改列宽或行高时，图片会与底层单元格一起移动并调整大小。

### **将图片锚定到单个单元格**
图片的锚点由四个从零开始的索引属性定义：
- `Picture.upper_left_row` — 图片顶边所在的行索引。
- `Picture.upper_left_column` — 图片左边所在的列索引。
- `Picture.lower_right_row` — 图片底边所在的行索引。要使图片的底边位于行 `r` 的底部，请将其设置为 `r + 1`。
- `Picture.lower_right_column` — 图片右边所在的列索引。要使图片的右边位于列 `c` 的右侧，请将其设置为 `c + 1`。

{{% alert color="primary" %}}
Aspose.Cells 中的行和列索引**从零开始**。单元格 C6 的行索引为 5，列索引为 2。在右下锚点上的差一错误是导致图片看起来重叠到相邻单元格的最常见原因。

### **控制放置行为**
`Picture.placement` 是 `PlacementType` 类型的枚举，用于控制当用户调整下方行高或列宽时图片的行为。对于单个单元格图片，推荐使用 `PlacementType.MOVE_AND_SIZE`，它会使图片与底层单元格一起移动和调整大小，从而保持精确的适配效果。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开一个已有的工作簿）。
2. 通过 `workbook.worksheets[0]` 访问目标 `Worksheet`。
3. 使用 `with` 语句将磁盘上的图片文件打开到文件流（或 `BytesIO` 对象）中，以确保流被正确释放。
4. 调用 `worksheet.pictures.add(5, 2, stream)` 添加一个锚定到单元格 C6 的图片，并捕获返回的 `Picture` 引用。
5. 设置四个锚点坐标，使图片仅覆盖单元格 C6：`upper_left_row = 5`，`upper_left_column = 2`，`lower_right_row = 6`，`lower_right_column = 3`。
6. 设置 `picture.placement = PlacementType.MOVE_AND_SIZE`，以便在调整列或行大小时保持图片与 C6 对齐。
7. 可选地向相邻单元格添加示例文本，以演示仅单元格 C6 包含该图片。
8. 将工作簿另存为 `.xlsx` 文件。
以下代码演示了完整的方法。

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
with open("logo.png", "rb") as fs:
    pic_index = worksheet.pictures.add(5, 2, fs)
    picture = worksheet.pictures[pic_index]
    picture.upper_left_row = 5
    picture.upper_left_column = 2
    picture.lower_right_row = 6
    picture.lower_right_column = 3
    picture.placement = ac.PlacementType.MOVE_AND_SIZE
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **方法二：将图片直接嵌入单元格**
Aspose.Cells 还提供了更简单的单元格绑定图片机制：`Cell.embedded_image` 属性。将图片字节赋值给该属性会将图片附加到单元格本身，就像行内内容一样。

### **嵌入图片的工作原理**
- 图片作为单元格内容的一部分存储，而不是作为绘图图层上的形状。
- 图片会自动缩放以适应单元格的渲染边界。无需设置锚点坐标或放置属性。
- 单元格仍然是具有真实地址的真实单元格，可以被公式引用、作为行的一部分进行排序，或用于其他单元格级操作。
当您的目标仅仅是"一张存在于该单元格中的图片"时，`Cell.embedded_image` 是最简洁的选择。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开一个已有的工作簿）。
2. 通过 `workbook.worksheets[0]` 访问目标 `Worksheet`。
3. 将磁盘上的图片文件读取到 `bytes` 对象中（例如，以二进制模式打开文件并调用 `.read()`）。
4. 获取目标单元格的引用——可以通过 `worksheet.cells["C6"]` 或 `worksheet.cells[5, 2]`。
5. 将 bytes 对象赋值给单元格的 `embedded_image` 属性。
6. 可选地调整目标行和列的行高与列宽，以使嵌入图片看起来更醒目。
7. 将工作簿另存为 `.xlsx` 文件。
以下代码演示了完整的方法。

```python
import aspose.cells as ac
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Get the target cell C6
cell = worksheet.cells["C6"]
# Read the image file into a byte array
with open("logo.png", "rb") as f:
    imageData = f.read()
# Embed the image directly into the cell
cell.embedded_image = imageData
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.cells.set_column_width(2, 30)   # Column C (index 2)
worksheet.cells.set_row_height(5, 100)     # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **选择合适的方法**
两种方法都可以生成一张适合放入单个单元格的图片，但它们在图片的存储方式和行为上有所不同：
- **在以下情况下使用浮动图片（方法一）：**
  - 您需要对放置、图层顺序或与其他绘图对象的对齐方式进行更精细的控制。
  - 您希望图片表现得像一个形状，可以被选中、重新排序或与其他形状分组。
  - 您需要与已使用 `pictures` 集合的代码保持旧版兼容性。
  - 您需要根据工作表布局动态计算锚点坐标。
- **在以下情况下使用嵌入图片（方法二）：**
  - 您希望以最简单的方式将图片插入到单元格中。
  - 图片应像其他单元格内容一样随单元格一起移动。
{{% /alert %}}

## 相关文章
- [Aspose.Cells for Python via .NET 中的 Excel 照相机](/cells/zh/python-net/excel-camera/)
- [在 Aspose.Cells for Python via .NET 中向数据透视表添加筛选字段](/cells/zh/python-net/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Python via .NET 中对数据透视表应用样式](/cells/zh/python-net/apply-style-to-pivot-table/)
- [修改数据透视表中的页面字段布局](/cells/zh/python-net/change-page-field-layout/)
- [在 Aspose.Cells for Python via .NET 中将迷你图转换为图像和 HTML](/cells/zh/python-net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="python" >}}