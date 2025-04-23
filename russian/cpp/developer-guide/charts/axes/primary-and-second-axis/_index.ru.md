---
title: Основная и второстепенная ось с помощью C++
linktitle: Основная и вторичная оси
description: Узнайте, как понимать и работать с основными и второстепенными осями в Aspose.Cells for C++. Наш гид поможет вам понять различия между основными и второстепенными осями, а также как правильно их настраивать и использовать в ваших графиках.
keywords: Aspose.Cells for C++, основные оси, второстепенные оси, понимание, различия, настройка, использование.
type: docs
weight: 190
url: /ru/cpp/primary-and-second-axis/
---

## **Возможные сценарии использования**
Когда числа в диаграмме значительно различаются в разных рядах данных, или когда у вас есть смешанные типы данных (цена и объем), отображайте один или несколько рядов данных на вторичной вертикальной (значений) оси. Масштаб вторичной вертикальной оси показывает значения соответствующих рядов данных. Вторичная ось работает хорошо в диаграмме, которая показывает комбинацию гистограмм и линейных диаграмм.

## **Работа с первичной и вторичной осями, как в Microsoft Excel**
Пожалуйста, посмотрите следующий пример кода, который создает новый Excel файл и помещает значения диаграммы в первый рабочий лист. 
Затем мы добавляем диаграмму и отображаем вторую ось.

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

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a chart
    worksheet.GetCells().Get(u"A1").PutValue(u"Region");
    worksheet.GetCells().Get(u"A2").PutValue(u"Peking");
    worksheet.GetCells().Get(u"A3").PutValue(u"New York");
    worksheet.GetCells().Get(u"A4").PutValue(u"Paris");
    worksheet.GetCells().Get(u"B1").PutValue(u"Sales Volume");
    worksheet.GetCells().Get(u"C1").PutValue(u"Growth Rate");
    worksheet.GetCells().Get(u"B2").PutValue(100);
    worksheet.GetCells().Get(u"B3").PutValue(80);
    worksheet.GetCells().Get(u"B4").PutValue(140);
    worksheet.GetCells().Get(u"C2").PutValue(0.7);
    worksheet.GetCells().Get(u"C3").PutValue(0.8);
    worksheet.GetCells().Get(u"C4").PutValue(1.0);

    // Create a Scatter chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::Scatter, 6, 6, 15, 11);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:C4", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$4");

    // Set the Second-Axis
    chart.GetNSeries().Get(1).SetPlotOnSecondAxis(true);

    // Show the Second-Axis
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Set the second series ChartType to line
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Set the series name
    chart.GetNSeries().Get(0).SetName(u"Sales Volume");
    chart.GetNSeries().Get(1).SetName(u"Growth Rate");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the file
    workbook.Save(u"PrimaryandSecondaryAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
