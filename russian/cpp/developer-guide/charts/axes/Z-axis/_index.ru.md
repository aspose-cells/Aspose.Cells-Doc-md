---
title: Ось Z с помощью C++
linktitle: Ось Z
description: Узнайте, как работать с осью Z в Aspose.Cells for C++. Наш гид поможет вам понять, как настраивать и модифицировать ось Z, включая масштаб и подписи, чтобы улучшить ваши графики.
keywords: Aspose.Cells for C++, ось Z, построение графиков, настройка, модификация, масштаб, подписи.
type: docs
weight: 210
url: /ru/cpp/z-axis/
---

## **Возможные сценарии использования**
Для некоторых 3D-графиков, таких как 3D-столбец, 3D-конус или 3D-пирамида, у которых есть ось глубины (ряда), также известная как ось Z, можно изменить. Вы можете указать интервал между метками делений, подписями оси и другими операциями.

## **Работа с первичной и вторичной осями, как в Microsoft Excel**
Посмотрите следующий пример кода, создающего новый файл Excel и вставляющего значения графика в первый лист. Затем добавляется график и устанавливается тип графика Column3D, после чего вы увидите также ось Z, называемую глубиной. 

![todo:image_alt_text](excel.png)

## **Образец кода**
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A1").PutValue(u"A");
    worksheet.GetCells().Get(u"B1").PutValue(u"B");
    worksheet.GetCells().Get(u"C1").PutValue(u"C");
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(1);
    worksheet.GetCells().Get(u"B2").PutValue(2);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"C2").PutValue(2);
    worksheet.GetCells().Get(u"C3").PutValue(3);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column3D, 9, 6, 25, 16);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Calculate the chart
    chart.Calculate();

    // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
    chart.SetChartDataRange(u"A2:C3", true);

    // Hide the CategoryAxis axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Hide the ValueAxis axis
    chart.GetValueAxis().SetIsVisible(false);

    // Save the file
    workbook.Save(u"ZAxis.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
