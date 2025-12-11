---
title: Copy Range Data with Style in C++
linktitle: Copy Range Data with Style
type: docs
weight: 610
url: /cpp/copy-range-data-with-style/
description: Copy range data including cell styles in Excel files using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

[Copy Range Data Only](/cells/cpp/copy-range-data-only/) **explains** how to copy cell data between ranges. This article demonstrates how to copy cell ranges while preserving their formatting styles using Aspose.Cells for C++.

{{% /alert %}}

Aspose.Cells provides classes and methods for working with ranges including [**CreateRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/), and [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

This example demonstrates how to:

1. Create a workbook
1. Populate cells with data
1. Create a [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)
1. Create and configure a [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object
1. Apply styles to the range
1. Create a second range
1. Copy formatted data between ranges

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
{{< app/cells/assistant language="cpp" >}}
