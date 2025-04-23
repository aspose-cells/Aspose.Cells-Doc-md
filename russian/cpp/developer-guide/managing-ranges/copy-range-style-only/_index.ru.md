---
title: Копирование только стиля диапазона с C++
linktitle: Копировать только стиль диапазона
type: docs
weight: 620
url: /ru/cpp/copy-range-style-only/
description: Узнайте, как копировать только стиль диапазона в Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

[Только копирование данных диапазона](/cells/ru/cpp/copy-range-data-only/) и [Копирование данных диапазона с стилем](/cells/ru/cpp/copy-range-data-with-style/) объясняют, как копировать данные из одного диапазона в другой самостоятельно или полностью с форматированием. Также возможно скопировать только форматирование. В этой статье показано как.

{{% /alert %}} 

Этот пример создает рабочую книгу, заполняет ее данными и копирует только стиль диапазона.

1. Создать диапазон.
1. Создайте объект [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) с указанными атрибутами форматирования.
1. Применить форматирование стиля к диапазону.
1. Создать второй диапазон ячеек.
1. Скопируйте формат первого диапазона во второй диапазон.

```c++
#include <iostream>
#include <string>
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

    Range range2 = cells.CreateRange(u"C10", u"E13");
    range2.CopyStyle(range);

    U16String outputPath = outDir + u"copyrangestyle.out.xls";
    workbook.Save(outputPath);

    std::cout << "Range style copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
