---
title: Настройка графиков с C++
linktitle: Настройка диаграмм
description: Узнайте, как настраивать графики в Aspose.Cells for C++. Наш гид покажет, как изменять макеты графиков, добавлять и форматировать серии данных, настраивать оси и применять различные параметры форматирования для улучшения внешнего вида и удобства использования ваших графиков.
keywords: Aspose.Cells for C++, построение графиков, настройка, макеты, серии данных, оси, форматирование, внешний вид, удобство.
type: docs
weight: 40
url: /ru/cpp/customizing-charts/
---


## **Создание настраиваемых диаграмм**

На данный момент, когда мы говорим о графиках, мы рассматриваем стандартные графики с их стандартными настройками форматирования. Мы только указываем источник данных, задаем несколько свойств, и график создается с настройками по умолчанию. Но API Aspose.Cells также поддерживают создание настраиваемых графиков, позволяющих разработчикам создавать графики со своими собственными настроить.

Разработчики могут создавать пользовательские графики во время выполнения с использованием Aspose.Cells.

График состоит из серии данных. Каждая серия данных в Aspose.Cells представлена объектом [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/), в то время как объект [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) служит коллекцией объектов [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/). При создании пользовательского графика разработчики имеют свободу использовать различные типы графиков для различных серий данных (собранных в объекте [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/)).

Приведенный ниже пример кода демонстрирует, как создать пользовательские графики. В этом примере мы собираемся использовать столбчатую диаграмму для первой серии данных и линейную диаграмму для второй серии. Результатом будет добавление столбчатой диаграммы, объединенной с линейной диаграммой, на лист.

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtain the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(110);
    worksheet.GetCells().Get(u"B1").PutValue(260);
    worksheet.GetCells().Get(u"B2").PutValue(12);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(100);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add NSeries (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the chart type of 2nd NSeries to display as line chart
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

В настоящее время Aspose.Cells поддерживает только пользовательские графики, сочетающие диаграммы типа pie, line, column и column stack, однако в будущих версиях будет поддержано больше типов графиков.

{{% /alert %}}
