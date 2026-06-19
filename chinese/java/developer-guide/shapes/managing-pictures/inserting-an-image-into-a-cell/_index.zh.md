---
title: 将图片插入单元格
description: Aspose.Cells 是一个用于处理电子表格文件的 Java 库。本文介绍如何通过两种不同的方式将图片精确地适应单个单元格大小：将浮动图片放置在单元格上方，或者将图片直接嵌入到单元格中。
keywords: Aspose.Cells, Java 库, 电子表格, 插入图片, 嵌入图片, 单元格中的图片, 图片适应单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells 提供了两种不同的方式将图片与单个单元格关联。浮动图片是工作表绘图层上的一个形状，视觉上覆盖一个单元格区域，而嵌入图片则存储在单元格内部，并会自动缩放以适应单元格的显示区域。请根据您的布局需求选择最适合的方法。

{{% /alert %}}

## **介绍**

将图片精确地适应单个单元格是设计作为可视化报表、产品目录、员工目录、仪表板或库存清单的电子表格时的常见需求。您可能希望拥有一张整洁的、与单元格绑定的图片，使其与所属单元格保持对齐，而不是将图片拉伸到多个单元格中或松散地放置在工作表上。

Aspose.Cells 通过两种互补的方式支持此场景：

- **方法 1 — 将浮动图片放置在单元格上方。** 向工作表添加一个 `Picture`，将其 `Placement` 设置为 `MOVE_AND_SIZE`，并调整其锚定单元格（`getUpperLeftRow`、`getUpperLeftColumn`、`getLowerRightRow`、`getLowerRightColumn`），使图片恰好覆盖一个单元格。
- **方法 2 — 将图片直接嵌入到单元格中。** 将图片字节赋值给单元格的 `getEmbeddedImage()` setter。图片会自动缩放以适应单元格的显示区域，并随单元格一起移动。

本文的其余部分将逐步介绍这两种方法，解释相关的 API，并展示如何在代码中使用它们。

## **方法 1：将图片放置在单元格上方**

浮动图片是一个 `Picture` 对象，它存在于工作表绘图层上。虽然它不属于任何单个单元格，但它被锚定在一个单元格区域。图片的锚定单元格（即其左上角和右下角）决定了其在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。

要使浮动图片恰好覆盖**一个单元格**，您需要：

1. 使用 `Worksheet.getPictures().add(int row, int column, InputStream stream)` 添加图片，该方法会将新图片锚定到给定的单元格。
2. 设置四个锚定属性，使图片的边界矩形与目标单元格重合。
3. 将 `Picture.setPlacement()` 设置为 `PlacementType.MOVE_AND_SIZE`，这样当用户更改列宽或行高时，图片会随其下方的单元格一起移动和调整大小。

### **将图片锚定到单个单元格**

图片的锚定由四个从零开始的索引属性定义：

- `Picture.getUpperLeftRow()` — 图片顶边的行索引。
- `Picture.getUpperLeftColumn()` — 图片左边的列索引。
- `Picture.getLowerRightRow()` — 图片底边的行索引。要使图片的底边位于行 `r` 的底部，请将其设置为 `r + 1`。
- `Picture.getLowerRightColumn()` — 图片右边的列索引。要使图片的右边位于列 `c` 的右侧，请将其设置为 `c + 1`。

例如，要将图片精确地适应单元格 **C6**（行索引为 `5`，列索引为 `2`），请设置 `setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)` 和 `setLowerRightColumn(3)`。

{{% alert color="primary" %}}

Aspose.Cells 中的行和列索引均为**从零开始**的。单元格 C6 的行索引为 5，列索引为 2。右下角锚定上的差一错误是图片看起来覆盖到相邻单元格的最常见原因。

{{% /alert %}}

### **控制放置行为**

`Picture.getPlacement()` 返回一个 `PlacementType` 类型的枚举，用于控制当用户调整图片下方行或列的大小时图片的行为方式。对于单单元格图片，推荐的值为 `PlacementType.MOVE_AND_SIZE`，它会使图片与其下方的单元格一起移动和调整大小，从而保持精确贴合。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开一个现有的工作簿）。
2. 通过 `workbook.getWorksheets().get(0)` 访问目标 `Worksheet`。
3. 使用 try-with-resources 块将磁盘上的图片文件作为 `InputStream`（例如 `FileInputStream`）打开，以确保流被正确关闭。
4. 调用 `worksheet.getPictures().add(5, 2, stream)` 添加一张锚定到单元格 C6 的图片。捕获返回的 `Picture` 引用。
5. 设置四个锚定坐标，使图片仅覆盖单元格 C6：`setUpperLeftRow(5)`、`setUpperLeftColumn(2)`、`setLowerRightRow(6)`、`setLowerRightColumn(3)`。
6. 设置 `picture.setPlacement(PlacementType.MOVE_AND_SIZE)`，以便在调整列或行大小时使图片与 C6 保持对齐。
7. 可选地向周围的单元格添加示例文本，以演示只有单元格 C6 包含图片。
8. 将工作簿作为 `.xlsx` 文件保存到磁盘。

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

## **方法 2：将图片直接嵌入到单元格中**

Aspose.Cells 还提供了一种更简单的机制用于单元格绑定的图片：`Cell.setEmbeddedImage(byte[])` 方法。将图片字节赋值给此属性会将图片附加到单元格本身，就像它是内联内容一样。

### **嵌入图片的工作原理**

- 图片作为单元格内容的一部分存储，而不是作为绘图层上的形状。
- 图片会自动缩放以适应单元格的渲染边界。无需锚定坐标或放置设置。
- 该单元格仍然是一个真正的单元格，具有真实地址，可以被公式引用、作为一行的一部分进行排序，或用于其他单元格级别的操作。

这使得 `setEmbeddedImage()` 成为当您的目标仅仅是"一张存在于该单元格中的图片"时最简洁的选项。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开一个现有的工作簿）。
2. 通过 `workbook.getWorksheets().get(0)` 访问目标 `Worksheet`。
3. 将磁盘上的图片文件读取到 `byte[]` 数组中（例如，通过 `java.nio.file` 中的 `Files.readAllBytes()` 读取文件）。
4. 获取目标单元格的引用 —— 可以通过 `worksheet.getCells().get("C6")` 或 `worksheet.getCells().get(5, 2)`。
5. 使用 `cell.setEmbeddedImage(bytes)` 将字节数组赋值给单元格。
6. 可选地调整目标行和列的行高和列宽，以使嵌入的图片更加醒目。
7. 将工作簿作为 `.xlsx` 文件保存到磁盘。

以下代码演示了完整的方法。

```java
import com.aspose.cells.*;
import java.nio.file.Files;
import java.nio.file.Paths;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// 获取目标单元格 C6
Cell cell = worksheet.getCells().get("C6");

// 将图像文件读取到字节数组中
byte[] imageData = Files.readAllBytes(Paths.get("logo.png"));

// 将图像直接嵌入到单元格中
cell.setEmbeddedImage(imageData);

// 可选地调整行高和列宽，使嵌入的图像更明显
worksheet.getCells().setColumnWidth(2, 30);   // C 列（索引 2）
worksheet.getCells().setRowHeight(5, 100);     // 第 6 行（索引 5）

// 将生成的工作簿保存为 .xlsx 文件
workbook.save("output.xlsx", SaveFormat.XLSX);
```

## **选择正确的方法**

两种方法都会生成适合在单个单元格内显示的图片，但它们在图片的存储方式和行为方式上有所不同：

- **在以下情况下使用浮动图片（方法 1）：**
  - 您需要对放置、图层或与其他绘图对象的对齐方式进行更精细的控制。
  - 您希望图片表现得像一个可以被选中、重新排序或与其他形状分组的形状。
  - 您需要与已经使用 `PictureCollection` 的代码保持旧版兼容性。
  - 您需要根据工作表布局动态计算锚定坐标。

- **在以下情况下使用嵌入图片（方法 2）：**
  - 您希望以最简单的方式将图片插入到单元格中。
  - 图片应像其他单元格内容一样随单元格移动。
  - 您不需要将图片作为形状进行操作。

{{% alert color="primary" %}}

两种方法可以在同一个工作簿中共存。您可以将浮动图片放置在一组单元格之上，同时将图片直接嵌入到其他单元格中，因为这两种机制在文件中使用不同的存储层。

{{% /alert %}}



{{< app/cells/assistant language="java" >}}