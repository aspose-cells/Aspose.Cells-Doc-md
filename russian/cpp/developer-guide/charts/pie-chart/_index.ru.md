---
title: Создание круговой диаграммы с лидерными линиями с помощью C++
linktitle: Круговая диаграмма
description: Узнайте, как использовать Aspose.Cells for C++ для создания круговой диаграммы с лидерными линиями в Microsoft Excel. Наш гид покажет, как добавлять лидерные линии, соединяющие точки данных с легендой и улучшающие общую ясность вашей диаграммы.
keywords: Aspose.Cells for C++, Круговая диаграмма, Лидерные линии, Microsoft Excel, Визуализация данных, Настройка диаграммы.
type: docs
weight: 45
url: /ru/cpp/creating-pie-chart-with-leader-lines/
---

{{% alert color="primary" %}}

Эта статья объясняет, как создавать круговую диаграмму с лидерными линиями с нуля, используя API Aspose.Cells for C++. В Excel опция 'Показать лидерные линии' установлен по умолчанию, поэтому при создании круговой диаграммы в Excel лидерные линии отображаются. Однако при создании аналогичной диаграммы с помощью API Aspose.Cells необходимо явно установить свойство [**Series.GetHasLeaderLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/gethasleaderlines/).

{{% /alert %}}

Чтобы продемонстрировать использование API Aspose.Cells for C++ для создания круговой диаграммы с лидерными линиями, вначале создадим новую [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) и введем некоторые данные, которые послужат источником данных серии. После размещения данных мы добавим [**Chart**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/) типа [**ChartType.Pie**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) в коллекцию диаграмм и настроим его параметры для получения нужного вида диаграммы.

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

    // Create an instance of Workbook in XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add two columns of data
    worksheet.GetCells().Get(u"A1").PutValue(u"Retail");
    worksheet.GetCells().Get(u"A2").PutValue(u"Services");
    worksheet.GetCells().Get(u"A3").PutValue(u"Info & Communication");
    worksheet.GetCells().Get(u"A4").PutValue(u"Transport Equip");
    worksheet.GetCells().Get(u"A5").PutValue(u"Construction");
    worksheet.GetCells().Get(u"A6").PutValue(u"Other Products");
    worksheet.GetCells().Get(u"A7").PutValue(u"Wholesale");
    worksheet.GetCells().Get(u"A8").PutValue(u"Land Transport");
    worksheet.GetCells().Get(u"A9").PutValue(u"Air Transport");
    worksheet.GetCells().Get(u"A10").PutValue(u"Electric Appliances");
    worksheet.GetCells().Get(u"A11").PutValue(u"Securities");
    worksheet.GetCells().Get(u"A12").PutValue(u"Textiles & Apparel");
    worksheet.GetCells().Get(u"A13").PutValue(u"Machinery");
    worksheet.GetCells().Get(u"A14").PutValue(u"Metal Products");
    worksheet.GetCells().Get(u"A15").PutValue(u"Cash");
    worksheet.GetCells().Get(u"A16").PutValue(u"Banks");

    worksheet.GetCells().Get(u"B1").PutValue(10.4);
    worksheet.GetCells().Get(u"B2").PutValue(5.2);
    worksheet.GetCells().Get(u"B3").PutValue(6.4);
    worksheet.GetCells().Get(u"B4").PutValue(10.4);
    worksheet.GetCells().Get(u"B5").PutValue(7.9);
    worksheet.GetCells().Get(u"B6").PutValue(4.1);
    worksheet.GetCells().Get(u"B7").PutValue(3.5);
    worksheet.GetCells().Get(u"B8").PutValue(5.7);
    worksheet.GetCells().Get(u"B9").PutValue(3);
    worksheet.GetCells().Get(u"B10").PutValue(14.7);
    worksheet.GetCells().Get(u"B11").PutValue(3.6);
    worksheet.GetCells().Get(u"B12").PutValue(2.8);
    worksheet.GetCells().Get(u"B13").PutValue(7.8);
    worksheet.GetCells().Get(u"B14").PutValue(2.4);
    worksheet.GetCells().Get(u"B15").PutValue(1.8);
    worksheet.GetCells().Get(u"B16").PutValue(10.1);

    // Create a pie chart and add it to the collection of charts
    int id = worksheet.GetCharts().Add(ChartType::Pie, 3, 3, 23, 13);

    // Access newly created Chart instance
    Chart chart = worksheet.GetCharts().Get(id);

    // Set series data range
    chart.GetNSeries().Add(u"B1:B16", true);

    // Set category data range
    chart.GetNSeries().SetCategoryData(u"A1:A16");

    // Turn off legend
    chart.SetShowLegend(false);

    // Access data labels
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();

    // Turn on category names
    dataLabels.SetShowCategoryName(true);

    // Turn on percentage format
    dataLabels.SetShowPercentage(true);

    // Set position
    dataLabels.SetPosition(LabelPositionType::OutsideEnd);

    // Set separator
    dataLabels.SetSeparatorType(DataLabelsSeparatorType::Comma);

    // Save the workbook
    workbook.Save(outDir + u"PieChart_out.xlsx");

    std::cout << "Pie chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

До сих пор мы создали круговую диаграмму и установили различные ее аспекты. Теперь мы собираемся включить линии-проводники для диаграммы. Обратите внимание, чтобы показать линии-проводники, нужно немного переместить метки данных.

Следующий кусок кода включает линии-проводники, обновляет диаграмму, а затем рассчитывает позиции меток данных для их соответствующего перемещения.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook in XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add two columns of data
    worksheet.GetCells().Get(u"A1").PutValue(u"Retail");
    worksheet.GetCells().Get(u"A2").PutValue(u"Services");
    worksheet.GetCells().Get(u"A3").PutValue(u"Info & Communication");
    worksheet.GetCells().Get(u"A4").PutValue(u"Transport Equip");
    worksheet.GetCells().Get(u"A5").PutValue(u"Construction");
    worksheet.GetCells().Get(u"A6").PutValue(u"Other Products");
    worksheet.GetCells().Get(u"A7").PutValue(u"Wholesale");
    worksheet.GetCells().Get(u"A8").PutValue(u"Land Transport");
    worksheet.GetCells().Get(u"A9").PutValue(u"Air Transport");
    worksheet.GetCells().Get(u"A10").PutValue(u"Electric Appliances");
    worksheet.GetCells().Get(u"A11").PutValue(u"Securities");
    worksheet.GetCells().Get(u"A12").PutValue(u"Textiles & Apparel");
    worksheet.GetCells().Get(u"A13").PutValue(u"Machinery");
    worksheet.GetCells().Get(u"A14").PutValue(u"Metal Products");
    worksheet.GetCells().Get(u"A15").PutValue(u"Cash");
    worksheet.GetCells().Get(u"A16").PutValue(u"Banks");

    worksheet.GetCells().Get(u"B1").PutValue(10.4);
    worksheet.GetCells().Get(u"B2").PutValue(5.2);
    worksheet.GetCells().Get(u"B3").PutValue(6.4);
    worksheet.GetCells().Get(u"B4").PutValue(10.4);
    worksheet.GetCells().Get(u"B5").PutValue(7.9);
    worksheet.GetCells().Get(u"B6").PutValue(4.1);
    worksheet.GetCells().Get(u"B7").PutValue(3.5);
    worksheet.GetCells().Get(u"B8").PutValue(5.7);
    worksheet.GetCells().Get(u"B9").PutValue(3);
    worksheet.GetCells().Get(u"B10").PutValue(14.7);
    worksheet.GetCells().Get(u"B11").PutValue(3.6);
    worksheet.GetCells().Get(u"B12").PutValue(2.8);
    worksheet.GetCells().Get(u"B13").PutValue(7.8);
    worksheet.GetCells().Get(u"B14").PutValue(2.4);
    worksheet.GetCells().Get(u"B15").PutValue(1.8);
    worksheet.GetCells().Get(u"B16").PutValue(10.1);

    // Create a pie chart and add it to the collection of charts
    int id = worksheet.GetCharts().Add(ChartType::Pie, 3, 3, 23, 13);

    // Access newly created Chart instance
    Chart chart = worksheet.GetCharts().Get(id);

    // Set series data range
    chart.GetNSeries().Add(u"B1:B16", true);

    // Set category data range
    chart.GetNSeries().SetCategoryData(u"A1:A16");

    // Turn off legend
    chart.SetShowLegend(false);

    // Access data labels
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();

    // Turn on category names
    dataLabels.SetShowCategoryName(true);

    // Turn on percentage format
    dataLabels.SetShowPercentage(true);

    // Set position
    dataLabels.SetPosition(LabelPositionType::OutsideEnd);

    // Set separator
    dataLabels.SetSeparatorType(DataLabelsSeparatorType::Comma);

    // Turn on leader lines
    chart.GetNSeries().Get(0).SetHasLeaderLines(true);

    // Calculate chart
    chart.Calculate();

    // You need to move DataLabels a little leftward or rightward depending on their position to show leader lines
    int DELTA = 100;
    for (int i = 0; i < chart.GetNSeries().Get(0).GetPoints().GetCount(); i++)
    {
        int X = chart.GetNSeries().Get(0).GetPoints().Get(i).GetDataLabels().GetX();
        // If it is greater than 2000, then move the X position a little right otherwise move the X position a little left
        if (X > 2000)
            chart.GetNSeries().Get(0).GetPoints().Get(i).GetDataLabels().SetX(X + DELTA);
        else
            chart.GetNSeries().Get(0).GetPoints().Get(i).GetDataLabels().SetX(X - DELTA);
    }

    // Save the workbook
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
}
```

Наконец, следующий код сохраняет диаграмму в формате изображения и книгу в формате XLSX.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook in XLSX format
    Workbook workbook(FileFormatType::Xlsx);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add two columns of data
    worksheet.GetCells().Get(u"A1").PutValue(u"Retail");
    worksheet.GetCells().Get(u"A2").PutValue(u"Services");
    worksheet.GetCells().Get(u"A3").PutValue(u"Info & Communication");
    worksheet.GetCells().Get(u"A4").PutValue(u"Transport Equip");
    worksheet.GetCells().Get(u"A5").PutValue(u"Construction");
    worksheet.GetCells().Get(u"A6").PutValue(u"Other Products");
    worksheet.GetCells().Get(u"A7").PutValue(u"Wholesale");
    worksheet.GetCells().Get(u"A8").PutValue(u"Land Transport");
    worksheet.GetCells().Get(u"A9").PutValue(u"Air Transport");
    worksheet.GetCells().Get(u"A10").PutValue(u"Electric Appliances");
    worksheet.GetCells().Get(u"A11").PutValue(u"Securities");
    worksheet.GetCells().Get(u"A12").PutValue(u"Textiles & Apparel");
    worksheet.GetCells().Get(u"A13").PutValue(u"Machinery");
    worksheet.GetCells().Get(u"A14").PutValue(u"Metal Products");
    worksheet.GetCells().Get(u"A15").PutValue(u"Cash");
    worksheet.GetCells().Get(u"A16").PutValue(u"Banks");

    worksheet.GetCells().Get(u"B1").PutValue(10.4);
    worksheet.GetCells().Get(u"B2").PutValue(5.2);
    worksheet.GetCells().Get(u"B3").PutValue(6.4);
    worksheet.GetCells().Get(u"B4").PutValue(10.4);
    worksheet.GetCells().Get(u"B5").PutValue(7.9);
    worksheet.GetCells().Get(u"B6").PutValue(4.1);
    worksheet.GetCells().Get(u"B7").PutValue(3.5);
    worksheet.GetCells().Get(u"B8").PutValue(5.7);
    worksheet.GetCells().Get(u"B9").PutValue(3);
    worksheet.GetCells().Get(u"B10").PutValue(14.7);
    worksheet.GetCells().Get(u"B11").PutValue(3.6);
    worksheet.GetCells().Get(u"B12").PutValue(2.8);
    worksheet.GetCells().Get(u"B13").PutValue(7.8);
    worksheet.GetCells().Get(u"B14").PutValue(2.4);
    worksheet.GetCells().Get(u"B15").PutValue(1.8);
    worksheet.GetCells().Get(u"B16").PutValue(10.1);

    // Create a pie chart and add it to the collection of charts
    int id = worksheet.GetCharts().Add(ChartType::Pie, 3, 3, 23, 13);

    // Access newly created Chart instance
    Chart chart = worksheet.GetCharts().Get(id);

    // Set series data range
    chart.GetNSeries().Add(u"B1:B16", true);

    // Set category data range
    chart.GetNSeries().SetCategoryData(u"A1:A16");

    // Turn off legend
    chart.SetShowLegend(false);

    // Access data labels
    DataLabels dataLabels = chart.GetNSeries().Get(0).GetDataLabels();

    // Turn on category names
    dataLabels.SetShowCategoryName(true);

    // Turn on percentage format
    dataLabels.SetShowPercentage(true);

    // Set position
    dataLabels.SetPosition(LabelPositionType::OutsideEnd);

    // Set separator
    dataLabels.SetSeparatorType(DataLabelsSeparatorType::Comma);

    // In order to save the chart image, create an instance of ImageOrPrintOptions
    ImageOrPrintOptions anOption;

    // Set image format
    anOption.SetImageType(ImageType::Png);

    // Set resolution
    anOption.SetHorizontalResolution(200);
    anOption.SetVerticalResolution(200);

    // Render chart to image
    chart.ToImage(u"output_out.png", anOption);

    // Save the workbook to see chart inside the Excel
    workbook.Save(u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

|**Результирующая круговая диаграмма**|
| :- |
|![todo:image_alt_text](creating-pie-chart-with-leader-lines_1.png)|

## **Продвинутые темы**
- [Пользовательские цвета секторов в круговой диаграмме](/cells/ru/cpp/custom-slice-or-sector-colors-in-pie-chart/)
- [Определение того, находятся ли точки данных во втором сегменте или в столбце на круговой из кругов или столбчатой из кругов диаграмме](/cells/ru/cpp/find-if-data-points-are-in-the-second-pie-or-bar-on-a-pie-of-pie-or-bar-of-pie-chart/)

## Связанные статьи

- [Создание диаграмм](/cells/ru/cpp/creating-charts/)
- [Настройка диаграмм](/cells/ru/cpp/customizing-charts/)
- [Форматирование данных в диаграммах](/cells/ru/cpp/data-formatting-in-charts/)
- [Настройка внешнего вида диаграммы](/cells/ru/cpp/setting-chart-appearance/)
