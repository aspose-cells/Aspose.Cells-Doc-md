---
title: Ось даты с помощью C++
linktitle: Ось дат
description: Узнайте, как управлять осью даты в Aspose.Cells for C++. Наше руководство поможет вам понять, как работать с различными форматами дат, шкалами времени и частотой меток.
keywords: Aspose.Cells for C++, ось даты, управление, форматы дат, шкалы времени, частота меток.
type: docs
weight: 200
url: /ru/cpp/date-axis/
---

## **Возможные сценарии использования**
Когда создаёте диаграмму из данных листа с использованием дат, и даты отображаются вдоль горизонтальной (категорийной) оси на диаграмме, Aspose.Cells автоматически преобразует категориальную ось в ось дат (шкалу времени).
Ось дат отображает даты в хронологическом порядке с определенными интервалами или базовыми единицами, такими как количество дней, месяцев или лет, даже если даты на листе не расположены последовательно или в тех же базовых единицах.
По умолчанию Aspose.Cells определяет базовые единицы для оси дат на основе минимальной разницы между любыми двумя датами в данных листа. Например, если у вас есть данные о ценах акций, где минимальная разница между датами — семь дней, то базовая единица устанавливается в дни, но вы можете изменить её на месяцы или годы, чтобы отслеживать производительность акций за более долгий период.

## **Обработка оси дат, подобно Microsoft Excel**
Пожалуйста, посмотрите следующий пример кода, который создает новый Excel файл и помещает значения диаграммы в первый рабочий лист. 
Затем мы добавляем диаграмму и устанавливаем тип [**Axis**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) 
на [**TimeScale**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/categorytype/), а затем устанавливаем базовые единицы в Дни.

![todo:image_alt_text](excel.png)

## **Образец кода**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add the sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Date");

    // 14 means datetime format
    Style style = worksheet.GetCells().GetStyle();
    style.SetNumber(14);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A2").SetStyle(style);
    worksheet.GetCells().Get(u"A2").PutValue(Date{2022, 6, 26, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A3").SetStyle(style);
    worksheet.GetCells().Get(u"A3").PutValue(Date{2022, 5, 22, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A4").SetStyle(style);
    worksheet.GetCells().Get(u"A4").PutValue(Date{2022, 8, 3, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"B1").PutValue(u"Price");
    worksheet.GetCells().Get(u"B2").PutValue(40);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(60);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 9, 6, 21, 13);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Set the Axis type to Date time
    chart.GetCategoryAxis().SetCategoryType(CategoryType::TimeScale);

    // Set the base unit for CategoryAxis to days
    chart.GetCategoryAxis().SetBaseUnitScale(TimeUnit::Days);

    // Set the direction for the axis text to be vertical
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Vertical);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set max value of Y axis
    chart.GetValueAxis().SetMaxValue(70);

    // Set major unit
    chart.GetValueAxis().SetMajorUnit(10);

    // Save the file
    workbook.Save(u"DateAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
