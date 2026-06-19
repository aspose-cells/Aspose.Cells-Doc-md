---
title: 在单元格中插入图像
description: Aspose.Cells 是用于处理电子表格文件的 Python 库。本文介绍了通过两种不同方法将图片精确适配到单个单元格大小：放置一个浮动图片覆盖在单元格上，或直接将图像嵌入到单元格中。
keywords: Aspose.Cells, Python 库, 电子表格, 插入图像, 嵌入图像, 单元格中的图片, 适配图像到单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/python-net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells 提供了两种不同的方式将图像与单个单元格进行关联。浮动图片是工作表绘图层上的一个形状，可在视觉上叠加在单元格区域上，而嵌入图像则存储在单元格内部，并自动缩放以适应单元格的显示区域。请根据布局需求选择最合适的方式。

{{% /alert %}}

## **简介**

在设计用作可视化报表、产品目录、员工通讯录、仪表板或库存清单的电子表格时，将图片精确地适配到单个单元格是一项常见需求。与其将图像拉伸到多个单元格上或松散地放置在工作表中，您可能更希望使用一个干净的、与所属单元格保持对齐的、绑定到单元格的图像。

Aspose.Cells 通过两种互补的方式支持此场景：

- **方法 1 — 在单元格上放置浮动图片。** 将 `Picture` 添加到工作表，将其 `placement` 设置为 `MOVE_AND_SIZE`，并调整其锚定单元格（`upper_left_row`、`upper_left_column`、`lower_right_row`、`lower_right_column`），使图片恰好覆盖一个单元格。
- **方法 2 — 直接将图像嵌入到单元格中。** 将图像字节分配给单元格的 `embedded_image` 属性。图像会自动缩放以适应单元格的显示区域，并随单元格一起移动。

本文的其余部分将逐步介绍这两种方法，解释相关的 API，并展示如何在代码中使用它们。

## **方法 1：将图片放置在单元格上方**

浮动图片是驻留在工作表绘图层上的 `Picture` 对象。虽然它不属于任何单个单元格，但它会被锚定到某个单元格区域。图片的锚定单元格——其左上角和右下角——决定了其在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。

要使浮动图片恰好覆盖**一个单元格**，您需要：

1. 使用 `Worksheet.pictures.add(row, column, stream)` 添加图片，该方法会将新图片锚定到给定的单元格。
2. 设置四个锚定属性，使图片的边界矩形与目标单元格重合。
3. 将 `Picture.placement` 设置为 `PlacementType.MOVE_AND_SIZE`，以便当用户更改列宽或行高时，图片随其下方单元格一起移动和调整大小。

### **将图片锚定到单个单元格**

图片的锚点由四个零基索引属性定义：

- `Picture.upper_left_row` — 图片顶部边缘的行索引。
- `Picture.upper_left_column` — 图片左侧边缘的列索引。
- `Picture.lower_right_row` — 图片底部边缘的行索引。要使图片的底部边缘位于第 `r` 行的底部，请将其设置为 `r + 1`。
- `Picture.lower_right_column` — 图片右侧边缘的列索引。要使图片的右侧边缘位于第 `c` 列的右侧，请将其设置为 `c + 1`。

例如，要将图片精确地适配到单元格 **C6**（行索引 `5`，列索引 `2`），请设置 `upper_left_row = 5`、`upper_left_column = 2`、`lower_right_row = 6` 和 `lower_right_column = 3`。

{{% alert color="primary" %}}

Aspose.Cells 中的行和列索引是**零基的**。单元格 C6 的行索引为 5，列索引为 2。右下角锚点上的差一错误是导致图片看起来与相邻单元格重叠的最常见原因。

{{% /alert %}}

### **控制放置行为**

`Picture.placement` 是 `PlacementType` 类型的枚举，用于控制当用户调整其下方行或列的大小时图片的行为。对于单单元格图片，推荐的值为 `PlacementType.MOVE_AND_SIZE`，它会使图片与其下方单元格一起移动和调整大小，从而保持精确适配。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开一个现有的）。
2. 从 `workbook.worksheets[0]` 访问目标 `Worksheet`。
3. 使用 `with` 代码块将磁盘上的图像文件打开为文件流（或 `BytesIO` 对象），以便正确释放流。
4. 调用 `worksheet.pictures.add(5, 2, stream)` 添加锚定到单元格 C6 的图片。捕获返回的 `Picture` 引用。
5. 设置四个锚定坐标，使图片仅覆盖单元格 C6：`upper_left_row = 5`、`upper_left_column = 2`、`lower_right_row = 6`、`lower_right_column = 3`。
6. 设置 `picture.placement = PlacementType.MOVE_AND_SIZE`，以便在调整列或行大小时图片与 C6 保持对齐。
7. （可选）向周围单元格添加示例文本，以演示仅单元格 C6 包含图片。
8. 将工作簿作为 `.xlsx` 文件保存到磁盘。

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

## **方法 2：直接将图像嵌入单元格**

Aspose.Cells 还提供了一种更简单的机制用于绑定到单元格的图像：`Cell.embedded_image` 属性。将图像字节分配给此属性会将图像附加到单元格本身，就像它是内联内容一样。

### **嵌入图像的工作原理**

- 图像作为单元格内容的一部分存储，而不是作为绘图层上的形状存储。
- 图像会自动缩放以适应单元格的渲染边界。无需锚定坐标或放置设置。
- 该单元格仍然是具有真实地址的真实单元格，可被公式引用、作为行的一部分进行排序或用于其他单元格级操作。

当您的目标仅仅是"一张位于此单元格内的图像"时，这使得 `Cell.embedded_image` 成为最简洁的选择。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开一个现有的）。
2. 从 `workbook.worksheets[0]` 访问目标 `Worksheet`。
3. 将磁盘上的图像文件读入 `bytes` 对象（例如，通过以二进制模式打开文件并调用 `.read()`）。
4. 获取对目标单元格的引用——通过 `worksheet.cells["C6"]` 或 `worksheet.cells[5, 2]`。
5. 将字节对象分配给单元格的 `embedded_image` 属性。
6. （可选）调整目标行和列的行高和列宽，以使嵌入的图像看起来更突出。
7. 将工作簿作为 `.xlsx` 文件保存到磁盘。

以下代码演示了完整的方法。

```python
import aspose.cells as ac

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# 获取目标单元格 C6
cell = worksheet.cells["C6"]

# 将图像文件读取为字节数组
with open("logo.png", "rb") as f:
    imageData = f.read()

# 将图像直接嵌入到单元格中
cell.embedded_image = imageData

# 可选地调整行高和列宽，以便嵌入的图像更清晰可见
worksheet.cells.set_column_width(2, 30)   # 列 C（索引 2）
worksheet.cells.set_row_height(5, 100)     # 第 6 行（索引 5）

# 将生成的工作簿另存为 .xlsx 文件
workbook.save("output.xlsx", ac.SaveFormat.XLSX)
```

## **选择合适的方法**

两种方法都生成适合放在单个单元格内的图片，但它们在图片的存储方式和行为上有所不同：

- **在以下情况下使用浮动图片（方法 1）：**
  - 您需要对放置、图层顺序或与其他绘图对象的对齐方式进行更精细的控制。
  - 您希望图片表现为一个可以被选择、重新排序或与其他形状分组的形状。
  - 您需要与已经使用 `pictures` 集合的代码保持遗留兼容性。
  - 您需要根据工作表布局动态计算锚定坐标。

- **在以下情况下使用嵌入图像（方法 2）：**
  - 您希望以最简单的方式将图像插入到单元格中。
  - 图像应像任何其他单元格内容一样随单元格一起移动。
  - 您不需要将图像作为形状进行操作。

{{% alert color="primary" %}}

两种方法可以在同一工作簿中共存。您可以在一组单元格上放置浮动图片，并将图像直接嵌入其他单元格中，因为这两种机制在文件中使用不同的存储层。

{{% /alert %}}

## **相关文章**

- [如何在单元格中插入图片](/cells/zh/python-net/how-to-place-image-to-cell/)
- [添加图片超链接](/cells/zh/python-net/add-image-hyperlinks/)
- [从 URL 将网络图像加载到 Excel 工作表中](/cells/zh/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [操作位置、大小和设计器图表](/cells/zh/python-net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="python" >}}