---
title: Как создать диаграмму TreeMap с помощью C++
description: Узнайте, как создать диаграмму Treemap в Aspose.Cells for C++. Наше руководство поможет вам понять различные свойства и параметры форматирования для диаграмм Treemap, включая цвета, метки и отображение данных.
keywords: Aspose.Cells for C++, диаграмма Treemap, создание, свойства, форматирование, цвета, метки, представление данных, круговая диаграмма, иерархическое отображение.
type: docs
weight: 161
url: /ru/cpp/creating-treemap-chart/
---

## **Возможные сценарии использования**
Диаграмма древовидной карты обеспечивает иерархический обзор ваших данных и упрощает обнаружение шаблонов, таких как наиболее продаваемые товары в магазине. Ветки дерева представлены прямоугольниками, и каждая подветка отображается в виде меньшего прямоугольника. Диаграмма древовидной карты отображает категории цветом и близостью и легко позволяет отображать большое количество данных, что было бы сложно с другими типами диаграмм.

![todo:image_alt_text](sample.png)
## **Диаграмма древовидной карты**
После выполнения приведенного ниже кода вы увидите диаграмму древовидной карты, как показано ниже.

![todo:image_alt_text](result.png)
## **Образец кода**
Приведенный ниже образец кода загружает [образец файла Excel](treemap.xlsx) и генерирует [выходной файл Excel](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"treemap.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Treemap, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"TreeMap Chart");

    // Add series data range (D2:F13, actually)
    chart.GetNSeries().Add(u"D2:F13", true);

    // Set category data (A2:C13 is incorrect)
    chart.GetNSeries().SetCategoryData(u"A2:C13");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
