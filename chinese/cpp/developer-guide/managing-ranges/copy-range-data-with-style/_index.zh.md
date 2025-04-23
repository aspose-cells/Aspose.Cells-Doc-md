---
title: 使用C++复制范围数据并保持样式
linktitle: 仅复制范围数据和样式
type: docs
weight: 610
url: /zh/cpp/copy-range-data-with-style/
description: 使用Aspose.Cells for C++在Excel文件中复制范围数据，包括单元格样式
---

{{% alert color="primary" %}}

[仅复制范围数据](/cells/zh/cpp/copy-range-data-only/) 说明如何在范围之间复制单元格数据。本文展示如何在复制单元格范围时同时保持其格式样式，使用Aspose.Cells for C++。

{{% /alert %}}

Aspose.Cells提供可以操作范围的类和方法，包括[**CreateRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/)、[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)和[**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)。

本示例演示了如何：

1. 创建一个工作簿
1. 填充单元格数据
1. 创建一个[**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)
1. 创建并配置一个[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)对象
1. 对范围应用样式
1. 创建第二个范围
1. 在范围之间复制格式化数据

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
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    for (int i = 0; i < 50; ++i)
    {
        for (int j = 0; j < 10; ++j)
        {
            cells.Get(i, j).PutValue((std::to_wstring(i) + L"," + std::to_wstring(j)).c_str());
        }
    }

    Range range = cells.CreateRange(u"A1", u"D3");
    Style style = workbook.CreateStyle();

    style.GetFont().SetName(u"Calibri");
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Blue());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Blue());

    StyleFlag flag1;
    flag1.SetFontName(true);
    flag1.SetCellShading(true);
    flag1.SetBorders(true);

    range.ApplyStyle(style, flag1);

    Range range2 = cells.CreateRange(u"C10", u"F12");
    range2.Copy(range);

    U16String outputPath = outDir + u"CopyRange.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Range copied with formatting successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
