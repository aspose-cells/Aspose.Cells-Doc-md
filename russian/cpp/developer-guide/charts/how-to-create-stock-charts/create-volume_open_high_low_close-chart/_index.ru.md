---
title: Создайте график акции Объем Открытие Максимум Минимум Закрытие (VOHLC) с помощью C++
description: Узнайте, как создать график акций объем открытие максимум мининум закрытие, используя Aspose.Cells for C++. Наше руководство покажет, как наносить данные фондового рынка, включая объем, открытие, максимум, минимум и цены закрытия, на график для лучшего анализа и визуализации.
keywords: Aspose.Cells for C++, График фондового рынка Объем Открытие Максимум Мининум Закрытие, Анализ данных, Визуализация.
type: docs
weight: 184
url: /ru/cpp/create-volume-open-high-low-close-stock-chart/
---

## **Возможные сценарии использования**
Четвертый график акций — это график Volume Open High Low Close. Опять же, важно повторить, что данные должны быть в правильном порядке. Если необходимо переставить таблицу данных, сделайте это до настройки графика. Этот график включает столбец для объема сразу после первого (категорийного) столбца, а графики включают столбчатую диаграмму по первичной оси, показывающую этот объем, в то время как цены перемещены на вторичную ось.

![todo:image_alt_text](data.png)

## **График объема-открытия-максимума-минимума-закрытия (VHLC)**

![todo:image_alt_text](sample.png)

## **Образец кода**
Следующий образец кода загружает [образец excel-файла](Volume-Open-High-Low-Close.xlsx) и создает [выходной excel-файл](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-Open-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeOpenHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-Open-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:F9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{0xff, 79, 129, 189});

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
