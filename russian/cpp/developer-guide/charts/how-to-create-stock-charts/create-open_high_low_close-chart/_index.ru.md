---
title: Создайте график акций OHLC (Open High Low Close) с помощью C++
description: Узнайте, как создать график акций OHLC, используя Aspose.Cells for C++. Наш гид покажет, как наносить данные фондового рынка, включая цены открытия, максимума, минимума и закрытия, на график для лучшего анализа и визуализации.
keywords: Aspose.Cells for C++, График акций OHLC, Данные фондового рынка, Анализ, Визуализация.
type: docs
weight: 182
url: /ru/cpp/create-open-high-low-close-stock-chart/
---

## **Возможные сценарии использования**
График цен акций Open-High-Low-Close (OHLC) использует пять столбцов данных по порядку: категория, открытие, максимум, минимум и закрытие. Диапазон цен в каждой категории снова указан вертикальной линией, а интервал между открытием и закрытием отображается более широким плавающим баром; если цена увеличивается в категории (закрытие выше открытия), бар заполняется одним цветом, а если цена уменьшается, бар заполняется другим. Этот тип графика часто называется графиком свечей.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Улучшения видимости на графике**
Мы часто используем цвета, а не черно-белую палитру, чтобы обозначить рост и снижение цен. В первом наборе свечей ниже красный показывает рост, а зеленый — снижение цен.

![todo:image_alt_text](sample2.png)

## **Образец кода**
Нижеприведенный образец кода загружает [образец файла Excel](Open-High-Low-Close.xlsx) и генерирует [файл Excel вывода](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Open-High-Low-Close.xlsx");
    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockOpenHighLowClose, 5, 6, 20, 12);
    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);
    // Set the legend can be showed
    chart.SetShowLegend(true);
    // Set the chart title name
    chart.GetTitle().SetText(u"Open-High-Low-Close Stock");
    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);
    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);
    // Set category data
    chart.GetNSeries().GetCategoryData() = u"A2:A9";
    // Set the DownBars and UpBars with different color
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Red());
    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);
    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
