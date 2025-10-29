---
title: Пользовательские цвета срезов или сегментов в круговой диаграмме с помощью C++
linktitle: Настройка цветов круговой диаграммы
description: Узнайте, как использовать Aspose.Cells for C++ для настройки цветов срезов и сегментов в круговой диаграмме. Наше руководство покажет, как назначить уникальные цвета каждому срезу, сегменту или колонне для улучшения визуальной привлекательности и представления данных.
keywords: Aspose.Cells for C++, Круговая диаграмма, Пользовательские цвета срезов, Пользовательские цвета сегментов, Визуальная привлекательность, Представление данных.
type: docs
weight: 60
url: /ru/cpp/custom-slice-or-sector-colors-in-pie-chart/
---

{{% alert color="primary" %}}

В этой статье объясняется, как добавить пользовательские цвета к сегментам/секторам круговой диаграммы. По умолчанию круговые диаграммы используют шаблон Microsoft Excel по умолчанию. Чтобы использовать другие цвета, перепределите цвета в диаграмме.

{{% /alert %}}

Чтобы установить пользоватский цвет для отдельных секторов или секторов круговой диаграммы:

1. Обратитесь к [**Series**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/) обьекту [**ChartPoint**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartpoint/).
1. Назначьте цвет вашего выбора, используя свойство [**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/area/getforegroundcolor/).

В этой статье также объясняется, как:

- Категорийные данные диаграммы.
- Заголовок диаграммы, связанный с ячейкой.
- Настройки шрифта заголовка диаграммы.
- Положение легенды.

{{% alert color="primary" %}}

[**ChartPoint.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/area/getforegroundcolor/) не является специфичным для круговых диаграмм, но может быть использован для всех типов диаграмм.

{{% /alert %}}

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook object
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a pie chart
    worksheet.GetCells().Get(u"C3").PutValue(u"India");
    worksheet.GetCells().Get(u"C4").PutValue(u"China");
    worksheet.GetCells().Get(u"C5").PutValue(u"United States");
    worksheet.GetCells().Get(u"C6").PutValue(u"Russia");
    worksheet.GetCells().Get(u"C7").PutValue(u"United Kingdom");
    worksheet.GetCells().Get(u"C8").PutValue(u"Others");

    // Put the sample values used in a pie chart
    worksheet.GetCells().Get(u"D2").PutValue(u"% of world population");
    worksheet.GetCells().Get(u"D3").PutValue(25);
    worksheet.GetCells().Get(u"D4").PutValue(30);
    worksheet.GetCells().Get(u"D5").PutValue(10);
    worksheet.GetCells().Get(u"D6").PutValue(13);
    worksheet.GetCells().Get(u"D7").PutValue(9);
    worksheet.GetCells().Get(u"D8").PutValue(13);

    // Create a pie chart with desired length and width
    int pieIdx = worksheet.GetCharts().Add(ChartType::Pie, 1, 6, 15, 14);

    // Access the pie chart
    Chart pie = worksheet.GetCharts().Get(pieIdx);

    // Set the pie chart series
    pie.GetNSeries().Add(u"D3:D8", true);

    // Set the category data
    pie.GetNSeries().SetCategoryData(u"=Sheet1!$C$3:$C$8");

    // Set the chart title that is linked to cell D2
    pie.GetTitle().SetLinkedSource(u"D2");

    // Set the legend position at the bottom
    pie.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set the chart title's font name and color
    pie.GetTitle().GetFont().SetName(u"Calibri");
    pie.GetTitle().GetFont().SetSize(18);

    // Access the chart series
    Series srs = pie.GetNSeries().Get(0);

    // Color the individual points with custom colors
    srs.GetPoints().Get(0).GetArea().SetForegroundColor(Color{0, 246, 22, 219});
    srs.GetPoints().Get(1).GetArea().SetForegroundColor(Color{0, 51, 34, 84});
    srs.GetPoints().Get(2).GetArea().SetForegroundColor(Color{0, 46, 74, 44});
    srs.GetPoints().Get(3).GetArea().SetForegroundColor(Color{0, 19, 99, 44});
    srs.GetPoints().Get(4).GetArea().SetForegroundColor(Color{0, 208, 223, 7});
    srs.GetPoints().Get(5).GetArea().SetForegroundColor(Color{0, 222, 69, 8});

    // Autofit all columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath, SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
