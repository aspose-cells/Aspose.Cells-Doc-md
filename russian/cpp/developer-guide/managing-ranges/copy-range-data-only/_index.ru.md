---
title: Копировать только данные диапазона с помощью C++
linktitle: Копировать только данные диапазона
type: docs
weight: 600
url: /ru/cpp/copy-range-data-only/
description: Узнайте, как копировать только данные диапазона без форматирования с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Иногда вам нужно скопировать данные из одного диапазона ячеек в другой, скопируя только данные, а не форматирование. Aspose.Cells предлагает эту функцию.

Эта статья предоставляет пример кода, который использует Aspose.Cells для копирования диапазона данных.

{{% /alert %}}

Этот пример показывает, как:

1. Создать книгу.
1. Добавить данные в ячейки на первом листе.
1. Создайте [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/).
1. Создайте объект [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) с указанными атрибутами форматирования.
1. Применить форматирование стиля к диапазону.
1. Создайте другой диапазон ячеек.
1. Скопируйте данные из первого диапазона во второй диапазон.

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

    for (int i = 0; i < 50; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            std::wstring value = std::to_wstring(i) + L"," + std::to_wstring(j);
            cells.Get(i, j).PutValue(U16String(reinterpret_cast<const char16_t*>(value.c_str())));
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
    range2.CopyData(range);

    U16String outputPath = outDir + u"CopyRangeData.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Range data copied and styled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
