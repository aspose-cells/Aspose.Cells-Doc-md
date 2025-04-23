---
title: Как создать круговую диаграмму Sunburst с помощью C++
description: Узнайте, как создать диаграмму Sunburst в Aspose.Cells for C++ — диаграмму, которая представляет данные в виде круга. Наше руководство поможет вам настроить различные свойства и форматирование вашей диаграммы, включая метки данных, легенды, цвета и многое другое.
keywords: Aspose.Cells for C++, диаграмма Sunburst, создание, установка свойств, метки данных, легенда, форматирование, цвет, круг, визуализация данных.
type: docs
weight: 162
url: /ru/cpp/creating-sunburst-chart/
---

## **Возможные сценарии использования**
Диаграммы типа Treemap хорошо подходят для сравнения пропорций внутри иерархии, однако такие диаграммы не идеально показывают уровни иерархии между крупнейшими категориями и отдельными данными. Диаграмма Sunburst — гораздо лучший визуальный инструмент для отображения этого. Диаграмма Sunburst идеально подходит для отображения иерархических данных. Каждый уровень иерархии представлен одним кольцом или окружностью, при этом внутреннее кольцо — это вершина иерархии. Диаграмма Sunburst без иерархических данных (один уровень категорий) выглядит похоже на кольцевую диаграмму. Однако диаграмма Sunburst с несколькими уровнями показывает, как внешние кольца связаны с внутренними. Эффективность диаграммы Sunburst в том, что она показывает, как одно кольцо разбивается на составляющие части, в то время как другая иерархическая диаграмма, диаграмма Treemap, лучше подходит для сравнения относительных размеров.

![todo:image_alt_text](sample.png)
## **Диаграмма созвездия**
После выполнения приведенного ниже кода вы увидите диаграмму созвездия, как показано ниже.

![todo:image_alt_text](result.png)
## **Образец кода**
Приведенный ниже образец кода загружает [образец файла Excel](sunburst.xlsx) и генерирует [выходной файл Excel](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sunburst.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Sunburst, 5, 6, 25, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Sunburst Chart");

    // Add series data range
    chart.GetNSeries().Add(u"D2:D16", true);

    // Set category data (A2:A16 is incorrect, as hierarchical category)
    chart.GetNSeries().SetCategoryData(u"A2:C16");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
