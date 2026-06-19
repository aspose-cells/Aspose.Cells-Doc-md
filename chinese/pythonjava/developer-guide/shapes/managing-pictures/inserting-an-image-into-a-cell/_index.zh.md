---
title: 在单元格中插入图片
description: Aspose.Cells for Python via Java 是一个用于处理电子表格文件的库。本文介绍如何通过两种不同的方法将图片精确地适配到单个单元格大小：在单元格上方放置浮动图片，或将图片直接嵌入单元格中。
keywords: Aspose.Cells, Python via Java 库, 电子表格, 插入图片, 嵌入图片, 单元格中的图片, 图片适配单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/python-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells 提供了两种不同的方式将图片与单个单元格关联。浮动图片是工作表绘图图层上的一个形状，它在视觉上覆盖某个单元格区域；而嵌入图片则存储在单元格内部，并会自动缩放以适应单元格的显示区域。请根据您的布局需求选择最适合的方式。

{{% /alert %}}

## **简介**

在设计作为可视化报表、产品目录、员工名录、仪表板或库存清单的电子表格时，将图片精确适配到单个单元格是一项常见需求。您可能希望获得一个干净、与单元格绑定的图片，使其与所属单元格保持对齐，而不是将图片拉伸到多个单元格中或松散地放置在工作表上。

Aspose.Cells 通过两种互补的方式支持此场景：

- **方法一 —— 在单元格上方放置浮动图片。** 向工作表添加一个 `Picture`，将其 `setPlacement` 设置为 `MOVE_AND_SIZE`，并调整其锚定单元格（`setUpperLeftRow`、`setUpperLeftColumn`、`setLowerRightRow`、`setLowerRightColumn`），使图片恰好覆盖一个单元格。
- **方法二 —— 将图片直接嵌入单元格。** 将图片字节赋值给单元格的 `setEmbeddedImage` 属性。图片会自动缩放以适应单元格的显示区域，并随单元格一起移动。

本文后续内容将逐步讲解这两种方法，介绍相关的 API，并展示如何在代码中使用它们。

## **方法一：在单元格上方放置图片**

浮动图片是位于工作表绘图图层上的一个 `Picture` 对象。尽管它不属于任何单个单元格，但它锚定在一个单元格区域上。图片的锚定单元格（即左上角和右下角）决定了它在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。

要使浮动图片恰好覆盖 **一个单元格**，您需要：

1. 使用 `Worksheet.getPictures().add(int row, int column, InputStream stream)` 添加图片，该方法会将新图片锚定到指定的单元格。
2. 设置四个锚定属性，使图片的边界矩形与目标单元格重合。
3. 将 `Picture.setPlacement` 设置为 `PlacementType.MOVE_AND_SIZE`，这样当用户更改列宽或行高时，图片会随底层单元格一起移动和调整大小。

### **将图片锚定到单个单元格**

图片的锚点由四个从零开始的索引属性定义：

- `setUpperLeftRow` —— 图片上边缘所在的行索引。
- `setUpperLeftColumn` —— 图片左边缘所在的列索引。
- `setLowerRightRow` —— 图片下边缘所在的行索引。要使图片的下边缘位于行 `r` 的底部，需将其设置为 `r + 1`。
- `setLowerRightColumn` —— 图片右边缘所在的列索引。要使图片的右边缘位于列 `c` 的右侧，需将其设置为 `c + 1`。

例如，要将图片精确适配到单元格 **C6**（行索引 `5`，列索引 `2`），可设置 `setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)` 和 `setLowerRightColumn(3)`。

{{% alert color="primary" %}}

Aspose.Cells 中的行和列索引都是 **从零开始** 的。单元格 C6 的行索引为 5，列索引为 2。在右下角锚点上的差一错误是图片看似溢出到相邻单元格的最常见原因。

{{% /alert %}}

### **控制放置行为**

`getPlacement` 是 `PlacementType` 类型的枚举，用于控制当用户调整其下方行或列的大小时图片的行为方式。对于单单元格图片，推荐的值为 `PlacementType.MOVE_AND_SIZE`，它会使图片与其底层单元格一起移动和调整大小，从而保持精确适配。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开一个已有的工作簿）。
2. 从 `workbook.getWorksheets().get(0)` 获取目标 `Worksheet`。
3. 将磁盘上的图片文件打开到 `InputStream` 中（通常是 `FileInputStream`），以确保流被正确关闭。
4. 调用 `worksheet.getPictures().add(5, 2, stream)` 向工作表添加锚定到单元格 C6 的图片，并获取返回的 `Picture` 引用。
5. 设置四个锚定坐标，使图片仅覆盖单元格 C6：`setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)`、`setLowerRightColumn(3)`。
6. 设置 `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`，以便在调整列宽或行高时图片始终与 C6 保持对齐。
7. 可选地向周围单元格添加示例文本，以演示只有单元格 C6 包含该图片。
8. 将工作簿以 `.xlsx` 文件格式保存到磁盘。

以下代码演示了完整的实现方式。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat, PlacementType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

FileInputStream = jpype.JClass("java.io.FileInputStream")
fs = FileInputStream("logo.png")
try:
    picIndex = worksheet.getPictures().add(5, 2, fs)
    picture = worksheet.getPictures().get(picIndex)
    picture.setUpperLeftRow(5)
    picture.setUpperLeftColumn(2)
    picture.setLowerRightRow(6)
    picture.setLowerRightColumn(3)
    picture.setPlacement(PlacementType.MoveAndSize)
finally:
    fs.close()

workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **方法二：将图片直接嵌入单元格**

Aspose.Cells 还提供了一种更简单的单元格绑定图片机制：`Cell.setEmbeddedImage` 属性。将图片字节赋值给该属性后，图片就会被附加到单元格本身，就像内联内容一样。

### **嵌入图片的工作原理**

- 图片作为单元格内容的一部分存储，而不是作为绘图图层上的形状存储。
- 图片会自动缩放以适应单元格渲染后的边界。无需设置锚定坐标或放置属性。
- 该单元格仍然是一个具有真实地址的真实单元格，可以通过公式引用、作为一行的一部分进行排序，或用于其他单元格级别的操作。

当您的目标仅仅是"一张存在于该单元格内的图片"时，`Cell.setEmbeddedImage` 是最简洁的选择。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开一个已有的工作簿）。
2. 从 `workbook.getWorksheets().get(0)` 获取目标 `Worksheet`。
3. 将磁盘上的图片文件读取到一个 `byte[]` 数组中（例如通过 `java.nio.file.Files` 的 `Files.readAllBytes` 调用）。
4. 获取目标单元格的引用 —— 可以通过 `worksheet.getCells().get("C6")` 或 `worksheet.getCells().get(5, 2)`。
5. 将字节数组赋值给单元格的 `setEmbeddedImage` 属性。
6. 可选地调整目标行和列的行高与列宽，以使嵌入的图片更加醒目。
7. 将工作簿以 `.xlsx` 文件格式保存到磁盘。

以下代码演示了完整的实现方式。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# 移植的代码在此处
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# 获取目标单元格 C6
cell = worksheet.getCells().get("C6")

# 将图像文件读入字节数组
imageData = open("logo.png", "rb").read()

# 将图像直接嵌入单元格
cell.setEmbeddedImage(imageData)

# 可选地调整行高和列宽，使嵌入的图像更清晰可见
worksheet.getCells().setColumnWidth(2, 30)   # 列 C（索引 2）
worksheet.getCells().setRowHeight(5, 100)    # 行 6（索引 5）

# 将生成的工作簿保存为 .xlsx 文件
workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **选择合适的方法**

两种方法都能生成一个适配于单个单元格的图片，但它们在图片的存储方式和行为表现上有所不同：

- **在以下情况下使用浮动图片（方法一）：**
  - 您需要对放置、图层顺序或与其他绘图对象的对齐方式进行更精细的控制。
  - 您希望图片作为一个形状，能够被选中、重新排序或与其他形状进行分组。
  - 您需要与已使用 `PictureCollection` 的代码保持兼容性。
  - 您需要根据工作表布局动态计算锚定坐标。

- **在以下情况下使用嵌入图片（方法二）：**
  - 您希望以最简单的方式将图片插入单元格。
  - 图片应像其他单元格内容一样随单元格一起移动。
  - 您不需要将图片作为形状进行操作。

{{% alert color="primary" %}}

两种方法可以在同一个工作簿中共存。您可以将浮动图片放置在一组单元格上方，同时将图片直接嵌入其他单元格，因为这两种机制在文件中使用了不同的存储图层。

{{% /alert %}}



{{< app/cells/assistant language="python" >}}