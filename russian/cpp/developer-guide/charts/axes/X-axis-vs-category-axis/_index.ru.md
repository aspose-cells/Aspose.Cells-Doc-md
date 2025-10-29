---
title: Ось X против категориальной оси с помощью C++
linktitle: Ось X против категориальной оси
description: Узнайте, как различать ось X и категориальную ось в Aspose.Cells for C++. Наш гид поможет понять различия в их использовании и свойствах, а также как их настраивать в соответствии с вашими потребностями.
keywords: Aspose.Cells for C++, ось X, категориальная ось, различие, использование, свойства, настройка.
type: docs
weight: 180
url: /ru/cpp/X-axis-vs-category-axis/
---

## **Возможные сценарии использования**
Существуют разные типы осей X. В то время как ось Y является осью типа значения, ось X может быть осью типа категории или осью типа значения. Используя ось значения, данные рассматриваются как непрерывно изменяющиеся числовые данные, и маркер располагается в точке вдоль оси, которая изменяется в соответствии с их числовым значением. Используя категориальную ось, данные рассматриваются как последовательность нечисловых текстовых меток, и маркер располагается в точке вдоль оси в соответствии с ее положением в последовательности. Приведенный ниже пример иллюстрирует разницу между осями значения и категории.
Наши примерные данные показаны в [файле примеров таблиц](sample.png) ниже. Первый столбец содержит наши данные оси X, которые могут рассматриваться как категории или как значения. Обратите внимание, что числа не равномерно распределены, и они даже не появляются в числовом порядке.

![todo:image_alt_text](sample.png)

## **Обрабатывайте ось X и категориальную ось, подобно Microsoft Excel**
Мы отобразим эти данные на двух типах диаграмм, первая - XY (точечная) с осью X как осью значений, вторая - линейная с осью X как категориальной.

![todo:image_alt_text](compare.png)

## **Образец кода**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in charts
    worksheet.GetCells().Get(u"A2").PutValue(1);
    worksheet.GetCells().Get(u"A3").PutValue(3);
    worksheet.GetCells().Get(u"A4").PutValue(2.5);
    worksheet.GetCells().Get(u"A5").PutValue(3.5);
    worksheet.GetCells().Get(u"B1").PutValue(u"Cats");
    worksheet.GetCells().Get(u"C1").PutValue(u"Dogs");
    worksheet.GetCells().Get(u"D1").PutValue(u"Fishes");
    worksheet.GetCells().Get(u"B2").PutValue(7);
    worksheet.GetCells().Get(u"B3").PutValue(6);
    worksheet.GetCells().Get(u"B4").PutValue(5);
    worksheet.GetCells().Get(u"B5").PutValue(4);
    worksheet.GetCells().Get(u"C2").PutValue(7);
    worksheet.GetCells().Get(u"C3").PutValue(5);
    worksheet.GetCells().Get(u"C4").PutValue(4);
    worksheet.GetCells().Get(u"C5").PutValue(3);
    worksheet.GetCells().Get(u"D2").PutValue(8);
    worksheet.GetCells().Get(u"D3").PutValue(7);
    worksheet.GetCells().Get(u"D4").PutValue(3);
    worksheet.GetCells().Get(u"D5").PutValue(2);

    // Create Line Chart: X as Category Axis
    int pieIdx = worksheet.GetCharts().Add(ChartType::LineWithDataMarkers, 6, 15, 20, 21);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:D5", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$5");

    // Set the first series name
    chart.GetNSeries().Get(0).SetName(u"Cats");

    // Set the second series name
    chart.GetNSeries().Get(1).SetName(u"Dogs");

    // Set the third series name
    chart.GetNSeries().Get(2).SetName(u"Fishes");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Create XY (Scatter) Chart: X as Value Axis
    pieIdx = worksheet.GetCharts().Add(ChartType::ScatterConnectedByLinesWithDataMarker, 6, 6, 20, 12);

    // Retrieve the Chart object
    chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:D5", true);

    // Set X values for series
    chart.GetNSeries().Get(0).SetXValues(u"{1,3,2.5,3.5}");
    chart.GetNSeries().Get(1).SetXValues(u"{1,3,2.5,3.5}");
    chart.GetNSeries().Get(2).SetXValues(u"{1,3,2.5,3.5}");

    // Set the first series name
    chart.GetNSeries().Get(0).SetName(u"Cats");

    // Set the second series name
    chart.GetNSeries().Get(1).SetName(u"Dogs");

    // Set the third series name
    chart.GetNSeries().Get(2).SetName(u"Fishes");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"XAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
