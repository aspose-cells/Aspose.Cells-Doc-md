--- 
title: Создайте график акций с точками максимум, минимум и закрытием (HLC) на C++ 
linktitle: Создание диаграммы акций HLC (High Low Close) 
description: Узнайте, как создать график акций с точками максимум, минимум и закрытием с использованием Aspose.Cells for C++. Наш пошаговый гид покажет, как наносить данные фондового рынка, включая максимальные, минимальные и закрывающие цены, на график для лучшего анализа и визуализации. 
keywords: Aspose.Cells for C++, График акций HLC, Данные фондового рынка, Анализ, Визуализация. 
type: docs 
weight: 181 
url: /ru/cpp/create-high-low-close-stock-chart/ 
--- 

## **Возможные сценарии использования** 
График цен акций High-Low-Close (HLC) использует четыре столбца данных. Первый столбец представляет собой категорию, обычно дату, но также можно использовать имена акций. Следующие три столбца по порядку предназначены для отображения высокой, низкой и закрывающей цены. Диапазон цен для каждой категории указывается вертикальной линией, отображающей диапазон от низкой к высокой цене, а за закрытие отмечается метка, выходящая вправо от этой линии. 

![todo:image_alt_text](sample.png) 
## **Улучшения видимости на графике** 
Иногда, чтобы сделать график более интуитивно понятным, мы можем изменить внешний вид маркера (закрытия) или отображать его на вторичной оси. 

![todo:image_alt_text](sample2.png) 
## **Образец кода** 
Нижеприведенный образец кода загружает [образец файла Excel](High-Low-Close.xlsx) и генерирует [файл Excel вывода](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::StockHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:D9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set the marker with the built-in data 
    chart.GetNSeries().Get(2).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
    chart.GetNSeries().Get(2).GetMarker().SetMarkerSize(20);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetForegroundColor(Color::Maroon());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
