---
title: Копировать данные диапазона с стилями в C++
linktitle: Копировать данные диапазона со стилем
type: docs
weight: 610
url: /ru/cpp/copy-range-data-with-style/
description: Копировать данные диапазона, включая стили ячеек, в файлах Excel с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

[Только копирование данных диапазона](/cells/ru/cpp/copy-range-data-only/) объясняет, как копировать данные ячеек между диапазонами. Эта статья демонстрирует, как копировать диапазоны ячеек с сохранением их форматов с помощью Aspose.Cells for C++.

{{% /alert %}}

Aspose.Cells предоставляет классы и методы для работы с диапазонами, включая [**CreateRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/createrange/), [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) и [**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).

Этот пример демонстрирует, как:

1. Создать рабочую книгу
1. Заполнить ячейки данными
1. Создать [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/)
1. Создать и настроить объект [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)
1. Применить стили к диапазону
1. Создать второй диапазон
1. Копировать отформатированные данные между диапазонами

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
