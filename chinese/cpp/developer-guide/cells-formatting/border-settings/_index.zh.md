---
title: 用C++设置边框
linktitle: 边框设置
description: 如何在C++中使用Aspose.Cells库设置单元格的边框样式和颜色。通过调整边框宽度、样式和颜色，可以更好地控制单元格的外观。
keywords: Aspose.Cells，单元格边框设置，C++，边框宽度，边框样式，边框颜色
type: docs
weight: 40
url: /zh/cpp/cells-border-settings/
---

## **向单元格添加边框**

微软Excel允许用户为单元格添加边框。边框类型取决于添加的位置。例如，上边框是添加到单元格顶部的位置。用户还可以修改线条样式和颜色。

借助 Aspose.Cells，开发人员可以以与 Microsoft Excel 中相同的灵活方式添加边框并自定义其外观。

### **向单元格添加边框**

Aspose.Cells提供了[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，可访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供了[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合中的每个元素都代表一个[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的对象。

Aspose.Cells在[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类中提供了[**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)方法，用于设置单元格的格式样式。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)类还提供了添加边框的属性。

#### **向单元格添加边框**

开发者可以通过使用[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)对象的[**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/)集合为单元格添加边框。边框类型作为索引传入[**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/)集合。所有边框类型都在[**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/)枚举中预定义。

**边框枚举**

| **边框类型** | **描述** |
|------------------|-----------------|
| BottomBorder     | 底部边框线 |
| DiagonalDown     | 从左上到右下的斜线 |
| DiagonalUp       | 从左下到右上的斜线 |
| LeftBorder       | 左边框线 |
| RightBorder      | 右边框线 |
| TopBorder        | 顶部边框线 |

[**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/)集合存储所有边框。[**GetBorders()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getborders/)集合中的每个边框由[**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/)对象表示，提供两个属性，[**GetColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getcolor/)和[**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/)，分别设置边框的线色和线样式。

要设置边框的线色，可以使用Color枚举选择颜色，并将其赋值给Border对象的Color属性。

通过从 [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/) 枚举中选择线条样式来设置边框的线条样式。

**CellBorderType枚举**

| **线条样式** | **说明** |
|------------------------|-------------------------------|
| DashDot               | 细点划线                   |
| DashDotDot            | 细点点划线                 |
| Dashed                | 虚线                     |
| Dotted                | 点线                     |
| Double                | 双线                     |
| Hair                  | 细线                     |
| MediumDashDot         | 中等点划线                 |
| MediumDashDotDot      | 中等点点划线               |
| MediumDashed          | 中等虚线                   |
| None                  | 无线                     |
| Medium                | 中等线                   |
| SlantedDashDot        | 斜点划线（中等）          |
| Thick                 | 厚线                     |
| Thin                  | 薄线                     |

选择一种线条样式，然后将其分配给 [**Border**](https://reference.aspose.com/cells/cpp/aspose.cells/border/) 对象的 [**GetLineStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/border/getlinestyle/) 属性。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Visit Aspose!");

    Style style = cell.GetStyle();

    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());

    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thick);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    cell.SetStyle(style);

    workbook.Save(outDir + u"book1.out.xls");
    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

你应该同时设置线条样式和颜色。两个对角线边框线应具有相同的线条样式和颜色。

{{% /alert %}}

#### **向单元格范围添加边框**

也可以对一范围单元格添加边框，而不仅仅是单个单元格。首先，通过调用 [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) 集合的 [**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) 方法创建一个单元格范围。它接受以下参数：

- 第一行，范围的第一行。
- 第一列，表示范围的第一列。
- 行数，范围中的行数。
- 列数，范围中的列数。

[**CreateRange**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/) 方法返回一个 [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) 对象，其中包含指定范围的单元格。[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) 对象提供一个 [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) 方法，可以接受以下参数，为单元格范围添加边框：

- **边框类型**，选择自 [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/) 枚举的边框类型。
- **线条样式**，选择自 [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/) 枚举的边框线条样式。
- **颜色**，线条颜色，从Color枚举中选择。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Obtain the reference of the first (default) worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello World From Aspose");

    // Creating a range of cells starting from "A1" cell to 3rd column in a row
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 3);

    // Adding a thick top border with blue line
    range.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick bottom border with blue line
    range.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick left border with blue line
    range.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick right border with blue line
    range.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Thick, Color::Blue());

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
