---
title: Вставка спарклайна с помощью C++
linktitle: Sparklines
type: docs
weight: 160
url: /ru/cpp/creating-sparklines/
description: Создание спарклайна для Excel с помощью Aspose.Cells в C++
---

## **Вставить спарклайн**
{{% alert color="primary" %}} 

Спарклайн — это крошечная диаграмма в ячейке листа, которая визуально отображает данные. Используйте спарклайны для отображения трендов в серии значений, таких как сезонное увеличение или снижение, экономические циклы или для выделения максимальных и минимальных значений. Разместите спарклайн возле своих данных для максимального эффекта. Существует три типа спарклайна: Линия, Столбец и Стек

{{% /alert %}} 

Создание спарклайна с помощью Aspose.Cells просто с помощью следующих примеров кода:

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

    // Create a new workbook
    Workbook book;
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set values in cells
    sheet.GetCells().Get(u"A1").PutValue(5);
    sheet.GetCells().Get(u"B1").PutValue(2);
    sheet.GetCells().Get(u"C1").PutValue(1);
    sheet.GetCells().Get(u"D1").PutValue(3);

    // Define the CellArea
    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 0;
    ca.EndRow = 0;

    // Add a sparkline group
    int idx = sheet.GetSparklineGroups().Add(SparklineType::Line, sheet.GetName() + u"!A1:D1", false, ca);

    // Get the sparkline group
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);
    group.GetSparklines().Add(sheet.GetName() + u"!A1:D1", 0, 4);

    // Customize Sparklines
    // Create CellsColor
    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    // Set the high points to green and low points to red
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.GetHighPointColor().SetColor(Color::Green());
    group.GetLowPointColor().SetColor(Color::Red());

    // Set line weight
    group.SetLineWeight(1.0);

    // Optionally, apply a preset style
    // group.SetPresetStyle(SparklinePresetStyleType::Style10);

    // Save the workbook
    book.Save(outDir + u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Продвинутые темы**
- [Использование мерных линий и настройка 3D-формата](/cells/ru/cpp/using-sparklines-and-settings-3d-format/)
