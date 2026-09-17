---
title: 在单元格中插入图片
linktitle: 在单元格中插入图片
description: Aspose.Cells for Python via Java 是一个用于处理电子表格文件的库。本文介绍如何将图片精确地放入单个单元格中，方法是在单元格上方放置浮动图片，或将图片直接嵌入到单元格中。
keywords: Aspose.Cells, Python via Java 库, 电子表格, 插入图片, 嵌入图片, 单元格中的图片, 将图片适配到单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/python-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了两种不同的方式将图片与单个单元格关联。浮动图片是工作表绘图层上的一个形状，它在视觉上覆盖一个单元格区域；而嵌入图片则存储在单元格内部，并自动缩放以适配单元格的显示区域。请根据您的布局需求选择最合适的方法。

## **简介**
在设计用作可视化报表、产品目录、员工通讯录、仪表板或库存清单的电子表格时，将图片精确地放入单个单元格是一项常见需求。与其将图片拉伸到多个单元格或随意放置在工作表上，您可能更希望拥有一个干净的、与单元格绑定的图片，使其与所属单元格始终保持对齐。
Aspose.Cells 以两种互补的方式支持此场景：
- **方法一 — 在单元格上方放置浮动图片。** 向工作表添加一个 `Picture`，将其 `setPlacement` 设置为 `MOVE_AND_SIZE`，然后调整其锚定单元格（`setUpperLeftRow`、`setUpperLeftColumn`、`setLowerRightRow`、`setLowerRightColumn`），使图片恰好覆盖一个单元格。
- **方法二 — 将图片直接嵌入到单元格中。** 将图片字节分配给单元格的 `setEmbeddedImage` 属性。图片会自动缩放以适配单元格的显示区域，并随单元格一起移动。
本文的其余部分将详细介绍这两种方法，解释相关的 API，并展示如何在代码中使用它们。

## **方法一：在单元格上方放置图片**
浮动图片是工作表绘图层上的一个 `Picture` 对象。虽然它不属于任何单个单元格，但它锚定在一个单元格区域。图片的锚定单元格（即左上角和右下角）决定了它在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。
若要使浮动图片恰好覆盖 **一个单元格**，您需要：
1. 使用 `Worksheet.getPictures().add(int row, int column, InputStream stream)` 添加图片，该方法会将新图片锚定到指定的单元格。
2. 设置四个锚定属性，使图片的边界矩形与目标单元格重合。
3. 将 `Picture.setPlacement` 设置为 `PlacementType.MOVE_AND_SIZE`，这样当用户更改列宽或行高时，图片会随底层单元格一起移动和缩放。

### **将图片锚定到单个单元格**
图片的锚点由四个从零开始的索引属性定义：
- `setUpperLeftRow` — 图片顶边所在行的行索引。
- `setUpperLeftColumn` — 图片左边所在列的列索引。
- `setLowerRightRow` — 图片底边所在行的行索引。要使图片的底边位于行 `r` 的底部，请将其设置为 `r + 1`。
- `setLowerRightColumn` — 图片右边所在列的列索引。要使图片的右边位于列 `c` 的右侧，请将其设置为 `c + 1`。

{{% alert color="primary" %}}
Aspose.Cells 中的行和列索引均为 **从零开始**。单元格 C6 的行索引为 5，列索引为 2。右下角锚点处的差一错误是图片看起来覆盖到相邻单元格的常见原因。

### **控制放置行为**
`getPlacement` 是 `PlacementType` 类型的枚举，用于控制当用户调整其下方行高或列宽时图片的行为。对于单个单元格图片，推荐的值是 `PlacementType.MOVE_AND_SIZE`，它会使图片与其底层单元格一起移动和缩放，从而保持精确匹配。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开一个已有的工作簿）。
2. 通过 `workbook.getWorksheets().get(0)` 访问目标 `Worksheet`。
3. 将磁盘上的图片文件打开到 `InputStream` 中（通常使用 `FileInputStream`），以确保流被正确关闭。
4. 调用 `worksheet.getPictures().add(5, 2, stream)` 添加一张锚定到单元格 C6 的图片，并捕获返回的 `Picture` 引用。
5. 设置四个锚定坐标，使图片仅覆盖单元格 C6：`setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)`、`setLowerRightColumn(3)`。
6. 设置 `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`，以在调整列宽或行高时使图片与 C6 保持对齐。
7. 可选地，在周围的单元格中添加示例文本，以演示只有单元格 C6 包含该图片。
8. 将工作簿作为 `.xlsx` 文件保存到磁盘。
以下代码演示了完整的方法。

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

## **方法二：将图片直接嵌入到单元格中**
Aspose.Cells 还提供了一种更简单的机制来处理与单元格绑定的图片：`Cell.setEmbeddedImage` 属性。将图片字节分配给此属性即可将图片附加到单元格本身，就像内联内容一样。

### **嵌入图片的工作原理**
- 图片作为单元格内容的一部分存储，而不是作为绘图层上的形状存储。
- 图片会自动缩放以适配单元格的渲染边界，无需任何锚定坐标或放置设置。
- 该单元格仍是一个具有真实地址的真实单元格，可以被公式引用、作为行的一部分进行排序，或用于其他单元格级别的操作。
当您的目标仅仅是"一张位于此单元格内的图片"时，`Cell.setEmbeddedImage` 是最简洁的选项。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开一个已有的工作簿）。
2. 通过 `workbook.getWorksheets().get(0)` 访问目标 `Worksheet`。
3. 将磁盘上的图片文件读入 `byte[]` 数组（例如，通过 `java.nio.file.Files` 中的 `Files.readAllBytes` 调用）。
4. 获取目标单元格的引用 — 可以通过 `worksheet.getCells().get("C6")` 或 `worksheet.getCells().get(5, 2)`。
5. 将字节数组分配给单元格的 `setEmbeddedImage` 属性。
6. 可选地，调整目标行和列的行高与列宽，以使嵌入图片看起来更加突出。
7. 将工作簿作为 `.xlsx` 文件保存到磁盘。
以下代码演示了完整的方法。

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Get the target cell C6
cell = worksheet.getCells().get("C6")
# Read the image file into a byte array
imageData = open("logo.png", "rb").read()
# Embed the image directly into the cell
cell.setEmbeddedImage(imageData)
# Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30)   # Column C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Row 6 (index 5)
# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **选择合适的方法**
两种方法都会生成一张适合放入单个单元格的图片，但它们在图片的存储方式和行为上有所不同：
- **在以下情况下使用浮动图片（方法一）：**
  - 您需要对放置、图层顺序或与其他绘图对象的对齐方式进行更精细的控制。
  - 您希望图片表现得像一个形状，可以被选中、重新排序或与其他形状组合。
  - 您需要与已使用 `PictureCollection` 的代码保持向后兼容。
  - 您需要根据工作表布局动态计算锚定坐标。
- **在以下情况下使用嵌入图片（方法二）：**
  - 您希望以最简单的方式将图片插入到单元格中。
  - 图片应像其他单元格内容一样随单元格一起移动。
  - 您不需要将图片作为形状进行操作。
{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="python" >}}