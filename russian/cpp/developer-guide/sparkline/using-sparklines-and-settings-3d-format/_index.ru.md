---
title: Использование Sparklines и настройки 3D форматирования в C++
linktitle: Использование мини графиков и настройки 3D формата
type: docs
weight: 40
url: /ru/cpp/using-sparklines-and-settings-3d-format/
description: Узнайте, как использовать sparklines и применять 3D форматирование в файлах Excel с помощью Aspose.Cells и C++.
---

## **Использование мини-графиков**
Microsoft Excel 2010 позволяет анализировать информацию более чем когда-либо прежде. С его помощью пользователи могут отслеживать и выделять важные тенденции данных с помощью новых средств анализа и визуализации. Мини-графики - это миниатюрные графики, которые можно разместить внутри ячеек, чтобы одновременно просматривать данные и диаграмму на одной и той же таблице. При правильном использовании мини-графиков анализ данных становится более быстрым и точным. Они также обеспечивают простой просмотр информации, избегая переполненных листов с множеством занятых диаграмм.

Aspose.Cells предоставляет API для обработки мини-графиков в электронных таблицах.
### **Мини-графики в Microsoft Excel**
Для вставки мини-графиков в Microsoft Excel 2010:

1. Выберите ячейки, где вы хотите разместить мини-графики. Чтобы упростить их просмотр, выберите ячейки сбоку от данных.
1. Нажмите **Вставка** на ленте и затем выберите **столбец** в группе **Мини-графики**.
1. Выберите или введите диапазон ячеек на листе, который содержит исходные данные. Диаграммы появятся.

Мини-графики помогают видеть тенденции, например, победы или поражения в лиге по софтболу. Мини-графики могут даже подвести итоги всего сезона каждой команды в лиге.
### **Мини-графики с использованием Aspose.Cells**
Разработчики могут создавать, удалять или читать sparklines (в шаблонных файлах) с помощью API Aspose.Cells. Классы, управляющие sparklines, находятся в пространстве имен [Aspose.Cells.Charts](https://reference.aspose.com/cells/cpp/aspose.cells.charts/), поэтому перед использованием этих функций необходимо импортировать это пространство имен.

Добавляя пользовательские графики для определенного диапазона данных, разработчики имеют возможность добавлять различные типы маленьких диаграмм в выбранные области ячеек.

Приведенный ниже пример демонстрирует функцию мини-графиков. Пример показывает, как:

1. Открыть простой файл шаблона.
1. Прочитать информацию о мини-графиках для листа.
1. Добавьте новые искры для определенного диапазона данных в область ячейки.
1. Сохраните файл Excel на диск.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    Workbook book(inputFilePath);
    Worksheet sheet = book.GetWorksheets().Get(0);

    SparklineGroupCollection sparklineGroups = sheet.GetSparklineGroups();
    for (int i = 0; i < sparklineGroups.GetCount(); ++i)
    {
        SparklineGroup g = sparklineGroups.Get(i);
        std::cout << "sparkline group: type:" << static_cast<int>(g.GetType()) << ", sparkline items count:" << g.GetSparklines().GetCount() << std::endl;
        for (int j = 0; j < g.GetSparklines().GetCount(); ++j)
        {
            Sparkline s = g.GetSparklines().Get(j);
            std::cout << "sparkline: row:" << s.GetRow() << ", col:" << s.GetColumn() << ", dataRange:" << s.GetDataRange().ToUtf8() << std::endl;
        }
    }

    CellArea ca;
    ca.StartColumn = 4;
    ca.EndColumn = 4;
    ca.StartRow = 1;
    ca.EndRow = 7;

    int idx = sheet.GetSparklineGroups().Add(SparklineType::Column, u"Sheet1!B2:D8", false, ca);
    SparklineGroup group = sheet.GetSparklineGroups().Get(idx);

    CellsColor clr = book.CreateCellsColor();
    clr.SetColor(Color::Orange());
    group.SetSeriesColor(clr);

    book.Save(outDir + u"Book1.out.xlsx");
    std::cout << "Sparklines added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Настройка 3D формата**
Вам может потребоваться стили 3D-графиков, чтобы получить результаты для вашего сценария. Aspose.Cells предоставляет соответствующий API для применения форматирования 3D Microsoft Excel 2007.

Ниже приведен полный пример для демонстрации того, как создать диаграмму и применить форматирование 3D Microsoft Excel 2007. После выполнения примерного кода на листе будет добавлена столбчатая диаграмма (с 3D эффектами).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook book;

    // Add a Data Worksheet
    Worksheet dataSheet = book.GetWorksheets().Add(u"DataSheet");

    // Add Chart Worksheet
    Worksheet sheet = book.GetWorksheets().Add(u"MyChart");

    // Put some values into the cells in the data worksheet
    dataSheet.GetCells().Get(u"B1").PutValue(1);
    dataSheet.GetCells().Get(u"B2").PutValue(2);
    dataSheet.GetCells().Get(u"B3").PutValue(3);
    dataSheet.GetCells().Get(u"A1").PutValue(u"A");
    dataSheet.GetCells().Get(u"A2").PutValue(u"B");
    dataSheet.GetCells().Get(u"A3").PutValue(u"C");

    // Define the Chart Collection
    ChartCollection charts = sheet.GetCharts();

    // Add a Column chart to the Chart Worksheet
    int chartSheetIdx = charts.Add(ChartType::Column, 5, 0, 25, 15);

    // Get the newly added Chart
    Chart chart = book.GetWorksheets().Get(2).GetCharts().Get(0);

    // Set the background/foreground color for PlotArea/ChartArea
    chart.GetPlotArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetChartArea().GetArea().SetBackgroundColor(Color::White());
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetChartArea().GetArea().SetForegroundColor(Color::White());

    // Hide the Legend
    chart.SetShowLegend(false);

    // Add Data Series for the Chart
    chart.GetNSeries().Add(u"DataSheet!B1:B3", true);

    // Specify the Category Data
    chart.GetNSeries().SetCategoryData(u"DataSheet!A1:A3");

    // Get the Data Series
    Series ser = chart.GetNSeries().Get(0);

    // Apply the 3-D formatting
    ShapePropertyCollection spPr = ser.GetShapeProperties();
    Format3D fmt3d = spPr.GetFormat3D();

    // Specify Bevel with its height/width
    Bevel bevel = fmt3d.GetTopBevel();
    bevel.SetType(BevelPresetType::Circle);
    bevel.SetHeight(2);
    bevel.SetWidth(5);

    // Specify Surface material type
    fmt3d.SetSurfaceMaterialType(PresetMaterialType::WarmMatte);

    // Specify surface lighting type
    fmt3d.SetSurfaceLightingType(LightRigType::ThreePoint);

    // Specify lighting angle
    fmt3d.SetLightingAngle(20);

    // Specify Series background/foreground and line color
    ser.GetArea().SetBackgroundColor(Color::Maroon());
    ser.GetArea().SetForegroundColor(Color::Maroon());
    ser.GetBorder().SetColor(Color::Maroon());

    // Save the Excel file
    book.Save(outDir + u"3d_format.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
