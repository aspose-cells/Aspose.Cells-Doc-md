---
title: 在单元格中插入图片
linktitle: 在单元格中插入图片
description: Aspose.Cells 是一个用于处理电子表格文件的 C++ 库。本文介绍如何将图片精确地适配到单个单元格中，可以通过在单元格上方放置浮动图片或将图片直接嵌入单元格来实现。
keywords: Aspose.Cells, C++ 库, 电子表格, 插入图片, 嵌入图片, 单元格中的图片, 将图片适配到单元格, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /zh/cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 提供了两种不同的方式将图片与单个单元格关联。浮动图片是工作表绘图层上的一个形状，它在视觉上覆盖在某个单元格区域之上；而嵌入图片则存储在单元格内部，并会自动缩放以适应单元格的显示区域。请根据您的布局需求选择最合适的方式。

## **简介**
在设计用作可视化报表、产品目录、员工通讯录、仪表板或库存清单的电子表格时，将图片精确地适配到单个单元格是一项常见需求。与其将图片拉伸跨越多个单元格，或随意地放在工作表上，您可能希望获得一种简洁的、与单元格绑定的图片，使其与所属单元格保持对齐。
Aspose.Cells 通过两种互补的方式来支持此场景：
- **方法 1 — 在单元格上方放置浮动图片。** 向工作表添加一个 `Picture`，将其 `Placement` 设置为 `MoveAndSize`，并调整其锚定单元格（`UpperLeftRow`、`UpperLeftColumn`、`LowerRightRow`、`LowerRightColumn`），使图片恰好覆盖一个单元格。
- **方法 2 — 将图片直接嵌入单元格。** 将图片字节赋值给单元格的 `EmbeddedImage` 属性。图片会自动缩放以适应单元格的显示区域，并随单元格一起移动。
本文的其余部分将逐一介绍这两种方法，解释相关的 API，并展示如何在代码中使用它们。

## **方法 1：在单元格上方放置图片**
浮动图片是一个存在于工作表绘图层上的 `Picture` 对象。虽然它不属于任何单个单元格，但它锚定在一个单元格区域上。图片的锚定单元格——即其左上角和右下角——决定了它在工作表上的视觉范围。默认情况下，新添加的图片会跨越多个单元格。
若要让浮动图片恰好覆盖**一个单元格**，您需要：
1. 使用 `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)` 添加图片，该方法会将新图片锚定到指定单元格。
2. 设置四个锚定属性，使图片的边界矩形与目标单元格重合。
3. 将 `Picture.Placement` 设置为 `PlacementType.MoveAndSize`，以便在用户更改列宽或行高时，图片能够随其底层单元格一起移动和缩放。

### **将图片锚定到单个单元格**
图片的锚点由四个从零开始的索引属性定义：
- `Picture.UpperLeftRow` — 图片顶边所在的行索引。
- `Picture.UpperLeftColumn` — 图片左边所在的列索引。
- `Picture.LowerRightRow` — 图片底边所在的行索引。若希望图片的底边位于行 `r` 的底部，请将其设置为 `r + 1`。
- `Picture.LowerRightColumn` — 图片右边所在的列索引。若希望图片的右边位于列 `c` 的右侧，请将其设置为 `c + 1`。

{{% alert color="primary" %}}
Aspose.Cells 中的行和列索引**从零开始**。单元格 C6 的行索引为 5，列索引为 2。对右下角锚点的差一错误是导致图片看起来延伸到相邻单元格的最常见原因。

### **控制放置行为**
`Picture.Placement` 是 `PlacementType` 类型的枚举，用于控制当用户调整其下方行或列大小时图片的行为方式。对于单单元格图片，推荐的值为 `PlacementType.MoveAndSize`，它会使图片与其底层单元格一起移动和缩放，从而保持精确的适配。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开一个已有的工作簿）。
2. 通过 `workbook.GetWorksheets().Get(0]` 访问目标 `Worksheet`。
3. 将磁盘上的图片文件读入 `Vector<uint8_t>` 字节缓冲区，以便 API 能够访问图片字节。
4. 调用 `worksheet.Pictures.Add(5, 2, imageData)` 添加一张锚定到单元格 C6 的图片，并获取返回的 `Picture` 引用。
5. 设置四个锚定坐标，使图片仅覆盖单元格 C6：`UpperLeftRow = 5`、`UpperLeftColumn = 2`、`LowerRightRow = 6`、`LowerRightColumn = 3`。
6. 设置 `picture.Placement = PlacementType.MoveAndSize`，以在调整列宽或行高时保持图片与 C6 对齐。
7. 可选地在周围的单元格中添加示例文本，以演示只有单元格 C6 包含该图片。
8. 将工作簿另存为磁盘上的 `.xlsx` 文件。
以下代码演示了完整的实现方法。

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

## **方法 2：将图片直接嵌入单元格**
Aspose.Cells 还提供了一种更简单的、用于绑定单元格的图片机制：`Cell.EmbeddedImage` 属性。将图片字节赋值给该属性，即可将图片附加到该单元格本身，如同作为单元格的内嵌内容。

### **嵌入图片的工作原理**
- 图片作为单元格内容的一部分存储，而不是作为绘图层上的形状。
- 图片会自动缩放以适应单元格渲染后的边界，无需任何锚定坐标或放置设置。
- 该单元格仍然是一个真实的单元格，具有真实的地址，可以被公式引用、作为行的一部分进行排序，或用于其他单元格级别的操作。
这使得 `Cell.EmbeddedImage` 成为目标仅仅是"一张存在于此单元格中的图片"时最简洁的选择。

### **分步说明**
1. 创建一个新的 `Workbook`（或打开一个已有的工作簿）。
2. 通过 `workbook.GetWorksheets().Get(0]` 访问目标 `Worksheet`。
3. 将磁盘上的图片文件读入 `Vector<uint8_t>` 字节数组。
4. 获取目标单元格的引用 —— 可以通过 `worksheet.GetCells().Get("C6"]`，也可以通过 `worksheet.GetCells().Get(5, 2]`。
5. 将字节数组赋值给该单元格的 `EmbeddedImage` 属性。
6. 可选地调整目标行和列的行高与列宽，使嵌入的图片看起来更醒目。
7. 将工作簿另存为磁盘上的 `.xlsx` 文件。
以下代码演示了完整的实现方法。

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
    // 直接将图像嵌入到单元格中
    cell.SetEmbeddedImage(imageData);
    // 可选地调整行高和列宽，使嵌入的图像更明显
    worksheet.GetCells().SetColumnWidth(2, 30);   // 列 C（索引 2）
    worksheet.GetCells().SetRowHeight(5, 100);    // 行 6（索引 5）
    // 将生成的工作簿保存为 .xlsx 文件
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **选择合适的方法**
两种方法都可以生成一张适配在单个单元格中的图片，但它们在图片的存储方式和行为上有所不同：
- **在以下情况下使用浮动图片（方法 1）：**
  - 您需要对放置、图层或与其他绘图对象的对齐进行更精细的控制。
  - 您希望图片作为一种形状，可以被选中、重新排序或与其他形状组合。
  - 您需要与已经使用 `PictureCollection` 的代码保持向后兼容性。
  - 您需要根据工作表布局动态计算锚定坐标。
- **在以下情况下使用嵌入图片（方法 2）：**
  - 您希望以最简单的方式将图片插入单元格。
  - 图片应当像其他单元格内容一样随单元格一起移动。
  - 您不需要将图片作为形状进行操作。
{{% /alert %}}

{{% /alert %}}

## 相关文章
- [Aspose.Cells for C++ 中的 Excel 照相机](/cells/zh/cpp/excel-camera/)
- [在 Aspose.Cells for C++ 中向数据透视表添加筛选字段](/cells/zh/cpp/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for C++ 中对数据透视表应用样式](/cells/zh/cpp/apply-style-to-pivot-table/)
- [修改数据透视表中的页面字段布局](/cells/zh/cpp/change-page-field-layout/)
- [在 Aspose.Cells for C++ 中将迷你图转换为图片和 HTML](/cells/zh/cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="cpp" >}}