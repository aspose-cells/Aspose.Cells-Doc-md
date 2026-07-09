---
title: 在单元格中插入图片
description: Aspose.Cells 是一个用于处理电子表格文件的 C++ 库。本文介绍如何使用两种不同的方法使图片精确地适应单个单元格的大小，将浮动图片放置在单元格上方，或将图片直接嵌入到单元格中。
keywords: Aspose.Cells, C++ 库, 电子表格, 插入图片, 嵌入图片, 单元格中的图片, 图片适应单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells 提供了两种不同的方式将图片与单个单元格关联。浮动图片是工作表绘图层上的一个形状，视觉上覆盖一个单元格区域，而嵌入图片则存储在单元格本身内部，并自动缩放到单元格的显示区域。请根据您的布局需求选择最合适的方法。

{{% /alert %}}

## **介绍**

将图片精确地适应单个单元格是设计电子表格时的常见需求，例如视觉报表、产品目录、员工通讯录、仪表板或库存清单。与其将图片拉伸跨越多个单元格，或随意放置在工作表上，您可能希望拥有一张干净、与所属单元格保持对齐的单元格绑定图片。

Aspose.Cells 通过两种互补的方式支持此场景：

- **方法一 — 将浮动图片放置在单元格上方。** 向工作表添加一个 `Picture`，将其 `Placement` 设置为 `MoveAndSize`，并调整其锚定单元格（`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`），使图片恰好覆盖一个单元格。
- **方法二 — 将图片直接嵌入到单元格中。** 将图片字节赋值给单元格的 `EmbeddedImage` 属性。图片将自动缩放以适应单元格的显示区域，并随单元格一起移动。

本文其余部分将逐步讲解这两种方法，介绍相关的 API，并展示如何在代码中使用它们。

## **方法一：将图片放置在单元格上方**

浮动图片是位于工作表绘图层上的 `Picture` 对象。虽然它不属于任何单个单元格，但会被锚定到一个单元格区域。图片的锚定单元格——其左上角和右下角——决定了其在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。

要使浮动图片恰好覆盖**单个单元格**，您需要：

1. 使用 `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)` 添加图片，该方法会将新图片锚定到指定的单元格。
2. 设置四个锚定属性，使图片的边界矩形与目标单元格重合。
3. 将 `Picture.Placement` 设置为 `PlacementType.MoveAndSize`，以便在用户更改列宽或行高时，图片与底层单元格一起移动和调整大小。

### **将图片锚定到单个单元格**

图片的锚点由四个从零开始的索引属性定义：

- `Picture.UpperLeftRow` — 图片顶部边缘的行索引。
- `Picture.UpperLeftColumn` — 图片左边缘的列索引。
- `Picture.LowerRightRow` — 图片底部边缘的行索引。要使图片底部边缘位于行 `r` 的底部，请将此属性设置为 `r + 1`。
- `Picture.LowerRightColumn` — 图片右边缘的列索引。要使图片右边缘位于列 `c` 的右侧，请将此属性设置为 `c + 1`。

例如，要将图片精确地放入单元格 **C6**（行索引 `5`，列索引 `2`），请设置 `UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6` 和 `LowerRightColumn = 3`。

{{% alert color="primary" %}}

Aspose.Cells 中的行和列索引是**从零开始**的。单元格 C6 的行索引为 5，列索引为 2。右下角锚点的差一错误是导致图片看起来溢出到相邻单元格的最常见原因。

{{% /alert %}}

### **控制放置行为**

`Picture.Placement` 是一个 `PlacementType` 类型的枚举，用于控制当用户调整底层行或列大小时图片的行为方式。对于单个单元格图片，推荐的值为 `PlacementType.MoveAndSize`，它会使图片与其底层单元格一起移动和调整大小，从而保持精确的适配。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开现有的工作簿）。
2. 从 `workbook.Worksheets[0]` 访问目标 `Worksheet`。
3. 将磁盘上的图片文件读入 `Vector<uint8_t>` 字节缓冲区，以便 API 可以使用图片字节。
4. 调用 `worksheet.Pictures.Add(5, 2, imageData)` 添加锚定到单元格 C6 的图片。捕获返回的 `Picture` 引用。
5. 设置四个锚定坐标，使图片仅覆盖单元格 C6：`UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. 设置 `picture.Placement = PlacementType.MoveAndSize`，以便在调整列或行大小时图片保持与 C6 对齐。
7. 可选地向周围的单元格添加示例文本，以演示仅单元格 C6 包含该图片。
8. 将工作簿另存为 `.xlsx` 文件。

以下代码演示了完整的方法。

```cpp
#include "Aspose.Cells.h"
#include <fstream>
#include <vector>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::ifstream fs("logo.png", std::ios::binary);
    std::vector<uint8_t> stdData((std::istreambuf_iterator<char>(fs)),
                                  std::istreambuf_iterator<char>());
    fs.close();

    Vector<uint8_t> imageData(reinterpret_cast<const uint8_t*>(stdData.data()),
                              static_cast<int32_t>(stdData.size()));

    int picIndex = worksheet.GetPictures().Add(5, 2, imageData);
    Picture picture = worksheet.GetPictures().Get(picIndex);
    picture.SetUpperLeftRow(5);
    picture.SetUpperLeftColumn(2);
    picture.SetLowerRightRow(6);
    picture.SetLowerRightColumn(3);
    picture.SetPlacement(PlacementType::MoveAndSize);

    workbook.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **方法二：将图片直接嵌入到单元格中**

Aspose.Cells 还提供了一种更简单的机制来处理单元格绑定的图片：`Cell.EmbeddedImage` 属性。将图片字节赋值给此属性会将图片附加到单元格本身，就像它是内联内容一样。

### **嵌入图片的工作原理**

- 图片作为单元格内容的一部分存储，而不是作为绘图层上的形状。
- 图片会自动缩放以适应单元格的渲染边界。无需锚定坐标或放置设置。
- 该单元格仍然是一个真实的单元格，具有真实的地址，可被公式引用、作为行的一部分进行排序，或用于其他单元格级别的操作。

这使得 `Cell.EmbeddedImage` 成为目标仅仅是"一张位于此单元格内的图片"时最简洁的选项。

### **分步说明**

1. 创建一个新的 `Workbook`（或打开现有的工作簿）。
2. 从 `workbook.Worksheets[0]` 访问目标 `Worksheet`。
3. 将磁盘上的图片文件读入 `Vector<uint8_t>` 字节数组。
4. 获取目标单元格的引用 —— 可以通过 `worksheet.Cells["C6"]` 或 `worksheet.Cells[5, 2]`。
5. 将字节数组赋值给单元格的 `EmbeddedImage` 属性。
6. 可选地调整目标行和列的行高和列宽，以使嵌入的图片更加醒目。
7. 将工作簿另存为 `.xlsx` 文件。

以下代码演示了完整的方法。

```cpp
#include "Aspose.Cells.h"
#include <vector>
#include <fstream>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(u"C6");

    // 将图像文件读取到字节数组中
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    // 使用指针+大小构造函数将 std::vector 转换为 Aspose::Cells::Vector
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());

    // 将图像直接嵌入到单元格中
    cell.SetEmbeddedImage(imageData);

    // 可选地调整行高和列宽，以便更清晰地显示嵌入的图像
    worksheet.GetCells().SetColumnWidth(2, 30);   // 列 C（索引 2）
    worksheet.GetCells().SetRowHeight(5, 100);    // 行 6（索引 5）

    // 将生成的工作簿保存为 .xlsx 文件
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **选择合适的方法**

两种方法都可以生成一张适合单个单元格的图片，但它们在图片的存储方式和行为上有所不同：

- **在以下情况下使用浮动图片（方法一）：**
  - 您需要对放置、图层顺序或与其他绘图对象的对齐方式进行更精细的控制。
  - 您希望图片作为形状使用，可以被选中、重新排序或与其他形状组合。
  - 您需要与已使用 `PictureCollection` 的代码保持向后兼容性。
  - 您需要根据工作表布局动态计算锚定坐标。

- **在以下情况下使用嵌入图片（方法二）：**
  - 您希望以最简单的方式将图片插入到单元格中。
  - 图片应像其他单元格内容一样随单元格移动。
  - 您不需要将图片作为形状进行操作。

{{% alert color="primary" %}}

两种方法可以在同一工作簿中共存。您可以将浮动图片放置在一组单元格上方，并将图片直接嵌入到其他单元格中，因为这两种机制在文件中使用不同的存储层。

{{% /alert %}}

## **相关文章**

- [如何在单元格中插入图片](/cells/zh/cpp/how-to-place-image-to-cell/)
- [添加图片超链接](/cells/zh/cpp/add-image-hyperlinks/)
- [将网络图片从 URL 加载到 Excel 工作表中](/cells/zh/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [操作位置、大小和设计器图表](/cells/zh/cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="cpp" >}}