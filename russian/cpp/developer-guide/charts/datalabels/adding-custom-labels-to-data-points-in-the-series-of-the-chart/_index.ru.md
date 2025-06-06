---
title: Добавление пользовательских меток к точкам данных в серии графика с помощью C++
linktitle: Добавление пользовательских меток к данным точек в серии диаграммы
description: Узнайте, как добавлять пользовательские метки к точкам данных в серии графика с помощью Aspose.Cells for C++. Наше руководство покажет, как изменять внешний вид, положение и формат меток, а также как связывать их с источником данных для точного отображения информации.
type: docs
weight: 100
url: /ru/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/
---

{{% alert color="primary" %}}

Вы можете добавлять пользовательские метки к точкам данных в серии графика. Aspose.Cells предоставляет метод [**DataLabel::getText()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/gettext/) для добавления таких пользовательских меток. В этой статье объясняется, как использовать этот метод для добавления пользовательских меток к точкам данных в серии графика.

{{% /alert %}}

В следующем коде создается **Диаграмма рассеяния, соединенная линиями с маркерами данных** и затем добавляются **пользовательские метки** к **точкам данных** в **серии** **диаграммы**. Каждая пользовательская метка показывает **Название серии** и **Имя точки**. Вы можете использовать любой другой текст вместо этого.

```c++
#include <iostream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String outputPath = outDir + u"output_out.xlsx";

    // Create workbook with XLSX format
    Workbook workbook(FileFormatType::Xlsx);
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Populate data cells
    sheet.GetCells().Get(0, 0).PutValue(1);
    sheet.GetCells().Get(0, 1).PutValue(2);
    sheet.GetCells().Get(0, 2).PutValue(3);

    sheet.GetCells().Get(1, 0).PutValue(4);
    sheet.GetCells().Get(1, 1).PutValue(5);
    sheet.GetCells().Get(1, 2).PutValue(6);

    sheet.GetCells().Get(2, 0).PutValue(7);
    sheet.GetCells().Get(2, 1).PutValue(8);
    sheet.GetCells().Get(2, 2).PutValue(9);

    // Create scatter chart
    int32_t chartIndex = sheet.GetCharts().Add(ChartType::ScatterConnectedByLinesWithDataMarker, 5, 1, 24, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Configure chart titles
    chart.GetTitle().SetText(u"Test");
    chart.GetCategoryAxis().GetTitle().SetText(u"X-Axis");
    chart.GetValueAxis().GetTitle().SetText(u"Y-Axis");

    // Set category data range
    chart.GetNSeries().SetCategoryData(u"A1:C1");

    // Add first data series
    chart.GetNSeries().Add(u"A2:C2", false);
    Series series = chart.GetNSeries().Get(0);
    int32_t pointCount = series.GetPoints().GetCount();

    // Configure data labels for first series
    for (int32_t i = 0; i < pointCount; i++)
    {
        ChartPoint point = series.GetPoints().Get(i);
        std::wstringstream ws;
        ws << L"Series 1\nPoint " << i;
        U16String labelText(reinterpret_cast<const char16_t*>(ws.str().c_str()));
        point.GetDataLabels().SetText(labelText);
    }

    // Add second data series
    chart.GetNSeries().Add(u"A3:C3", false);
    series = chart.GetNSeries().Get(1);
    pointCount = series.GetPoints().GetCount();

    // Configure data labels for second series
    for (int32_t i = 0; i < pointCount; i++)
    {
        ChartPoint point = series.GetPoints().Get(i);
        std::wstringstream ws;
        ws << L"Series 2\nPoint " << i;
        U16String labelText(reinterpret_cast<const char16_t*>(ws.str().c_str()));
        point.GetDataLabels().SetText(labelText);
    }

    // Save workbook
    workbook.Save(outputPath, SaveFormat::Xlsx);
    std::cout << "Chart created successfully with data labels!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

void AddCustomLabels() {
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add sample data
    worksheet.GetCells().Get(u"A1").PutValue(u"X");
    worksheet.GetCells().Get(u"A2").PutValue(1);
    worksheet.GetCells().Get(u"A3").PutValue(2);
    worksheet.GetCells().Get(u"A4").PutValue(3);
    worksheet.GetCells().Get(u"B1").PutValue(u"Y");
    worksheet.GetCells().Get(u"B2").PutValue(4);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"B4").PutValue(2);
    worksheet.GetCells().Get(u"C1").PutValue(u"Point Name");
    worksheet.GetCells().Get(u"C2").PutValue(u"Point A");
    worksheet.GetCells().Get(u"C3").PutValue(u"Point B");
    worksheet.GetCells().Get(u"C4").PutValue(u"Point C");

    // Add chart
    int chartIndex = worksheet.GetCharts().Add(ChartType::ScatterConnectedByLinesWithDataMarker, 5, 0, 20, 8);
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Set data source
    chart.GetNSeries().Add(u"=Sheet1!$B$2:$B$4", true);
    chart.GetNSeries().Get(0).SetXValues(u"=Sheet1!$A$2:$A$4");

    // Enable data labels
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();
    dataLabels.SetShowValue(true);

    // Add custom labels
    int pointCount = chart.GetNSeries().Get(0).GetPoints().GetCount();
    for (int i = 0; i < pointCount; i++) {
        ChartPoint point = chart.GetNSeries().Get(0).GetPoints().Get(i);
        DataLabels dataLabel = point.GetDataLabels();
        dataLabel.SetText(
            u"Series: " + chart.GetNSeries().Get(0).GetName() + 
            u"\nPoint: " + worksheet.GetCells().Get(i + 1, 2).GetStringValue()
        );
    }

    // Save workbook
    workbook.Save(u"output.xlsx");
}
```
