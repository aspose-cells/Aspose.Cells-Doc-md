---
title: 用C++设置填充效果
linktitle: 填充设置
description: Aspose.Cells是一个用于处理电子表格文件的C++库。它支持设置单元格的填充效果，允许用户自定义单元格的背景和样式。本文将介绍如何使用Aspose.Cells库设置单元格的填充效果。
keywords: Aspose.Cells，Cells，填充设置，背景，样式
type: docs
weight: 50
url: /zh/cpp/cells-fill-settings/
---

## **颜色和背景图案**

Microsoft Excel可以设置单元格的前景（轮廓）和背景（填充）颜色以及背景图案。

Aspose.Cells还以灵活的方式支持这些功能。在本主题中，我们将学习如何使用Aspose.Cells来使用这些功能。

### **设置颜色和背景图案**

Aspose.Cells提供了一个表示Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含一个[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供一个[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合。[**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)集合中的每个项都表示[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的对象。

[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)具有[**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/)和[**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/)方法，用于获取和设置单元格的格式。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)类提供了设置单元格前景色和背景色的属性。Aspose.Cells提供一个[**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/)枚举，其中包含一组预定义的背景图案类型，如下所示。

|**背景图案**|**描述**|
| :- | :- |
|DiagonalCrosshatch|代表对角线交叉图案
|DiagonalStripe|代表对角线条纹图案
|Gray6|代表6.25%灰色图案
|Gray12|代表12.5%灰色图案
|Gray25|代表25%灰色图案
|Gray50|代表50%灰色图案
|Gray75|代表75%灰色图案
|HorizontalStripe|代表水平条纹图案
|None|代表无背景
|ReverseDiagonalStripe|代表反对角线条纹图案
|Solid|代表实线图案
|ThickDiagonalCrosshatch|代表粗对角线交叉图案
|ThinDiagonalCrosshatch|代表细对角线交叉图案
|ThinDiagonalStripe|代表细对角线条纹图案
|ThinHorizontalCrosshatch|代表细水平交叉图案
|ThinHorizontalStripe|代表细水平条纹图案
|ThinReverseDiagonalStripe|代表细反对角线条纹图案
|ThinVerticalStripe|代表细竖条纹图案|
|VerticalStripe|代表竖条纹图案|

在下面的示例中，A1单元格的前景色已设置，但A2配置为具有前景色和背景色的垂直条纹背景模式。

```c++
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

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Define a Style and get the A1 cell style
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    // Setting the foreground color to yellow
    style.SetForegroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A1 cell
    worksheet.GetCells().Get(u"A1").SetStyle(style);

    // Get the A2 cell style
    style = worksheet.GetCells().Get(u"A2").GetStyle();

    // Setting the foreground color to blue
    style.SetForegroundColor(Color::Blue());

    // Setting the background color to yellow
    style.SetBackgroundColor(Color::Yellow());

    // Setting the background pattern to vertical stripe
    style.SetPattern(BackgroundType::VerticalStripe);

    // Apply the style to A2 cell
    worksheet.GetCells().Get(u"A2").SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **重要知识**

{{% alert color="primary" %}}

- 若要设置单元格的前景色或背景色，请使用 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 对象的 [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) 或 [**GetBackgroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundcolor/) 属性。只有当 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 对象的 [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) 属性配置好时，这两个属性才会生效。
- [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) 属性设置单元格的阴影颜色。
  [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) 属性指定用于前景色或背景色的背景图案类型。Aspose.Cells 提供一个称为 [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) 的枚举，其中包含一组预定义的背景图案类型。
- 如果从 [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) 枚举中选择 *BackgroundType.None* 值，则不会应用前景色。
  同样，如果选择 *BackgroundType.None* 或 *BackgroundType.Solid* 值，则不会应用背景色。
- 在检索单元格的阴影/填充颜色时，如果 [**Style.GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) 是 *BackgroundType.None*，[**Style.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) 将返回 *Color.Empty*。

{{% /alert %}}

### **应用梯度填充效果**

要将期望的渐变填充效果应用于单元格，相应地使用 [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 对象的 [**SetTwoColorGradient**](https://reference.aspose.com/cells/cpp/aspose.cells/style/settwocolorgradient/) 方法。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::System;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(2, 1).PutValue(u"test");

    Cell cell = worksheet.GetCells().Get(u"B3");
    Style style = cell.GetStyle();
    style.SetIsGradient(true);
    style.SetTwoColorGradient(
        Color{ 0xFF, 0xFF, 0xFF, 0xFF },
        Color{ 0xFF, 0x4F, 0x81, 0xBD },
        GradientStyleType::Horizontal,
        1
    );

    style.GetFont().SetColor(Color::Red());
    style.SetHorizontalAlignment(TextAlignmentType::Center);
    style.SetVerticalAlignment(TextAlignmentType::Center);

    cell.SetStyle(style);

    worksheet.GetCells().SetRowHeightPixel(2, 53);
    worksheet.GetCells().Merge(2, 1, 1, 2);

    workbook.Save(outDir + u"output.xlsx");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **颜色和调色板**

调色板是在创建图像时可用的颜色数量。在演示文稿中使用标准调色板可以让用户创建一致的外观。每个Microsoft Excel（97-2003）文件都有一个包含可应用于单元格、字体、网格线、图形对象、填充和图表中的线条的56种颜色的调色板。

使用 Aspose.Cells 不仅可以使用调色板的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，首先将其添加到调色板中。

本主题讨论如何向调色板中添加自定义颜色。

### **向调色板中添加自定义颜色**

Aspose.Cells 支持 Microsoft Excel 的 56 种颜色调色板。要使用在调色板中未定义的自定义颜色，需要将颜色添加到调色板中。

Aspose.Cells 提供了一个名为 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 的类，用于表示 Microsoft Excel 文件。 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类提供了一个 [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) 方法，接受以下参数来添加自定义颜色以修改调色板：

- Custom Color，要添加的自定义颜色。
- Index，自定义颜色在调色板中的索引，将替换指定的颜色。应该在 0-55 之间。

下面的示例在应用于字体之前向调色板中添加了自定义颜色（兰花紫）。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid color is now in the palette
    std::cout << "Is Orchid in palette after change: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

调色板只能容纳 56 种颜色。当向调色板中添加自定义颜色时，调色板会改变，文件中用先前颜色格式化的任何元素也会发生变化。因此，在更改调色板时，请务必小心。此外，在 XLS（Excel 97 - 2003）文件格式中，这是唯一的限制，XLSX 或其他高级 MS Excel（2007/2010 或 2013）文件格式则没有这种限制。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
