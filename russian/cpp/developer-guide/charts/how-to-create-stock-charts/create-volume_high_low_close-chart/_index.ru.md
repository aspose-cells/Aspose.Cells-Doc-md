---
title: Создайте график акций VHL (Volume High Low) с помощью C++
linktitle: Создание графика цен акций по объему  высоким, низким и закрывающим(VHLC)
description: Узнайте, как создать график акций объем+максимум+минимум+закрытие, используя Aspose.Cells for C++. Наш гид продемонстрирует, как наносить данные фондового рынка, включая объем, максимальные, минимальные и закрывающие цены, на график для более глубокого анализа и визуализации.
keywords: Aspose.Cells for C++, График акций VHL, Данные фондового рынка, Анализ, Визуализация.
type: docs
weight: 183
url: /ru/cpp/create-volume-high-low-close-stock-chart/
---

## **Возможные сценарии использования**
График объемов с высоким и низким закрытием, который мы рассмотрим следующий, - это график Объем-Высокий_низкий-Закрытие. Еще раз важно повторить, что данные должны быть в правильном порядке. Если нужно, переставьте таблицу данных до создания графика. Этот график включает колонку объема сразу после первой (категориальной) колонки, и графики включают столбчатую диаграмму на основном осях, показывающую объем, в то время как цены перемещены на вторичные оси.

![todo:image_alt_text](data.png)
## **График акций объем-высокая-низкая-закрытие (VHLC)**

![todo:image_alt_text](sample.png)
## **Образец кода**
Приведенный ниже образец кода загружает [образец файла Excel](Volume-High-Low-Close.xlsx) и генерирует [выходной файл Excel](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);

    // Set category data 
    chart.GetNSeries().SetCategoryData(u"A2:A9");

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{ 79, 129, 189 });

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```


{{< app/cells/assistant language="cpp" >}}
