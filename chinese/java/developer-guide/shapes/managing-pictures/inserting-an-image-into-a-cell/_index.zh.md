---
title: 在单元格中插入图片
linktitle: Inserting an Image into a Cell
description: Aspose.Cells 是一款用于处理电子表格文件的 Java 库。本文介绍如何将图片精确地放入单个单元格，可以通过在单元格上方放置浮动图片，或将图片直接嵌入到单元格中。
keywords: Aspose.Cells, Java 库, 电子表格, 插入图片, 嵌入图片, 单元格中的图片, 图片适配单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/java/inserting-an-image-into-a-cell/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了两种不同的方式将图片与单个单元格关联。浮动图片是工作表绘图层上的一个图形，它在视觉上覆盖在单元格区域上方；而嵌入图片则存储在单元格内部，并会自动缩放以适应单元格的显示区域。请选择最适合您布局需求的方式。

## **简介**
在设计作为可视化报表、产品目录、员工通讯录、仪表板或库存清单的电子表格时，将图片精确地放入单个单元格是一个常见需求。与其让图片跨越多个单元格或松散地放置在工作表上，您可能更希望拥有一张干净、与单元格绑定、并始终与其所属单元格对齐的图片。
Aspose.Cells 通过两种互补的方式支持此场景：
- **方法 1 — 在单元格上方放置浮动图片。** 向工作表添加一个 `Picture`，将其 `Placement` 设置为 `MOVE_AND_SIZE`，并调整其锚定单元格（`getUpperLeftRow`、`getUpperLeftColumn`、`getLowerRightRow`、`getLowerRightColumn`），使图片恰好覆盖一个单元格。
- **方法 2 — 将图片直接嵌入单元格。** 将图片字节分配给单元格的 `getEmbeddedImage()` setter。图片会自动缩放以适应单元格的显示区域，并随单元格一起移动。
本文后续内容将逐步介绍这两种方法，解释相关的 API，并展示如何在代码中使用它们。

## **方法 1：在单元格上方放置图片**
浮动图片是位于工作表绘图层上的 `Picture` 对象。虽然它不属于任何一个单元格，但它锚定在一个单元格区域上。图片的锚定单元格——即其左上角和右下角——决定了图片在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。
若要使浮动图片恰好覆盖**一个单元格**，您需要：
1. 使用 `Worksheet.getPictures().add(int row, int column, InputStream stream)` 添加图片，该方法会将新图片锚定到指定的单元格。
2. 设置四个锚点属性，使图片的边界矩形与目标单元格重合。
3. 将 `Picture.setPlacement()` 设置为 `PlacementType.MOVE_AND_SIZE`，以便在用户更改列宽或行高时，图片能够随其下方的单元格一起移动和调整大小。

### **将图片锚定到单个单元格**
图片的锚点由四个从零开始的索引属性定义：
- `Picture.getUpperLeftRow()` — 图片顶部边缘的行索引。
- `Picture.getUpperLeftColumn()` — 图片左侧边缘的列索引。
- `Picture.getLowerRightRow()` — 图片底部边缘的行索引。若希望图片的底部边缘位于第 `r` 行的底部，请将此值设置为 `r + 1`。
- `Picture.getLowerRightColumn()` — 图片右侧边缘的列索引。若希望图片的右侧边缘位于第 `c` 列的右侧，请将此值设置为 `c + 1`。

{{% alert color="primary" %}}
Aspose.Cells 中的行和列索引**从零开始**。单元格 C6 的行索引为 5，列索引为 2。在右下角锚点上出现差一错误是导致图片看似与相邻单元格重叠的最常见原因。

### **控制放置行为**
`Picture.getPlacement()` 返回一个 `PlacementType` 类型的枚举，用于控制当用户调整图片下方行高或列宽时图片的行为。对于单个单元格的图片，推荐的取值是 `PlacementType.MOVE_AND_SIZE`，它会使图片与其下方的单元格一起移动和调整大小，从而保持精确的适配。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开现有的工作簿）。
2. 通过 `workbook.getWorksheets().get(0)` 获取目标 `Worksheet`。
3. 使用 try-with-resources 语句将磁盘上的图片文件打开为 `InputStream`（例如 `FileInputStream`），以确保流被正确关闭。
4. 调用 `worksheet.getPictures().add(5, 2, stream)` 添加一张锚定到 C6 单元格的图片，并捕获返回的 `Picture` 引用。
5. 设置四个锚点坐标，使图片仅覆盖 C6 单元格：`setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)`、`setLowerRightColumn(3)`。
6. 设置 `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`，以便在调整列宽或行高时图片始终与 C6 单元格保持对齐。
7. 可选择在周围单元格中添加示例文本，以演示仅 C6 单元格包含图片。
8. 将工作簿保存为磁盘上的 `.xlsx` 文件。
以下代码演示了完整的方法。

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
try (FileInputStream fs = new FileInputStream("logo.png"))
{
    int picIndex = worksheet.getPictures().add(5, 2, fs);
    Picture picture = worksheet.getPictures().get(picIndex);
    picture.setUpperLeftRow(5);
    picture.setUpperLeftColumn(2);
    picture.setLowerRightRow(6);
    picture.setLowerRightColumn(3);
    picture.setPlacement(PlacementType.MOVE_AND_SIZE);
}
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **方法 2：将图片直接嵌入单元格**
Aspose.Cells 还提供了一种更简单的机制来实现与单元格绑定的图片：`Cell.setEmbeddedImage(byte[])` 方法。将图片字节分配给此属性，会将图片附加到单元格本身，就像它是内联内容一样。

### **嵌入图片的工作原理**
- 图片作为单元格内容的一部分进行存储，而不是作为绘图层上的图形。
- 图片会自动缩放以适应单元格的渲染边界，无需任何锚点坐标或放置设置。
- 该单元格仍然是一个真实的单元格，具有真实的地址，可供公式引用、随行排序或用于其他单元格级操作。
因此，当您的目标仅仅是「一张位于该单元格内部的图片」时，`setEmbeddedImage()` 是最简洁的选择。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开现有的工作簿）。
2. 通过 `workbook.getWorksheets().get(0)` 获取目标 `Worksheet`。
3. 将磁盘上的图片文件读取到 `byte[]` 数组中（例如，使用 `java.nio.file` 中的 `Files.readAllBytes()` 读取文件）。
4. 获取目标单元格的引用——可以通过 `worksheet.getCells().get("C6")` 或 `worksheet.getCells().get(5, 2)`。
5. 使用 `cell.setEmbeddedImage(bytes)` 将字节数组分配给单元格。
6. 可选择调整目标行和列的行高与列宽，以使嵌入的图片更加醒目。
7. 将工作簿保存为磁盘上的 `.xlsx` 文件。
以下代码演示了完整的方法。

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Get the target cell C6
Cell cell = worksheet.getCells().get("C6");
// Read the image file into a byte array
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));
// Embed the image directly into the cell
cell.setEmbeddedImage(imageData);
// Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30);   // Column C (index 2)
worksheet.getCells().setRowHeight(5, 100);     // Row 6 (index 5)
// Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **选择合适的方法**
两种方法都能生成一张恰好放入单个单元格的图片，但它们在图片的存储方式和行为上有所不同：
- **在以下情况下使用浮动图片（方法 1）：**
  - 您需要对放置、图层顺序或与其他绘图对象的对齐方式进行更精细的控制。
  - 您希望图片表现为一个图形，可以被选中、重新排序或与其他图形分组。
  - 您需要与已使用 `PictureCollection` 的代码保持向后兼容。
  - 您需要根据工作表布局动态计算锚点坐标。
- **在以下情况下使用嵌入图片（方法 2）：**
  - 您希望以最简单的方式将图片插入单元格。
  - 图片应像其他单元格内容一样随单元格移动。
  - 您不需要将图片作为图形进行操作。
{{% /alert %}}

{{% /alert %}}

## 相关文章
- [Aspose.Cells for Java 中的 Excel 照相机](/cells/zh/java/excel-camera/)
- [在 Aspose.Cells for Java 中向数据透视表添加筛选字段](/cells/zh/java/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Java 中为数据透视表应用样式](/cells/zh/java/apply-style-to-pivot-table/)
- [修改数据透视表的页面字段布局](/cells/zh/java/change-page-field-layout/)
- [在 Aspose.Cells for Java 中将迷你图转换为图片和 HTML](/cells/zh/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}