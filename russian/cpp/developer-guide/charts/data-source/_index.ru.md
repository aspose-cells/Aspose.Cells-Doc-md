---
title: Задать источник данных для графика с C++
linktitle: Источник данных
type: docs
weight: 10
url: /ru/cpp/data-formatting-in-charts/
description: Узнайте о различных поддерживаемых источниках данных в Aspose.Cells for C++. Наш гид проведет вас по различным типам источников данных и покажет, как подключаться к ним и получать данные для заполнения ваших листов.
keywords: Aspose.Cells for C++, построение графиков, форматирование данных, метки, цвета, шрифты, внешний вид, удобство.
---

В наших предыдущих темах мы уже предоставили много примеров, показывающих, как установить источник данных для вашего графика. В этой теме мы предоставим больше деталей о типах данных, которые могут быть установлены для графика.

## **Установка данных графика**

При работе с графиками с использованием Aspose.Cells есть два типа данных, с которыми нужно работать, следующие:

- Данные графика.
- Данные категорий.

### **Данные графика**

Данные графика - это данные, которые мы используем в качестве источника данных для построения наших графиков. Мы можем добавить диапазон ячеек (содержащих данные графика), вызвав метод [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/add/) объекта [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(300);
    worksheet.GetCells().Get(u"B1").PutValue(160);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Adding sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Данные категорий**

Данные категорий используются для маркировки данных графика и могут быть добавлены к [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) с использованием его свойства [**GetCategoryData()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/getcategorydata/). Приведен ниже полный пример для демонстрации использования данных графика и категорий. После выполнения приведенного выше примера кода на лист будет добавлена столбчатая диаграмма, как показано ниже.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(200);
    worksheet.GetCells().Get(u"B1").PutValue(120);
    worksheet.GetCells().Get(u"B2").PutValue(320);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Add sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the data source for the category data of SeriesCollection
    chart.GetNSeries().SetCategoryData(u"C1:C4");

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Дополнительные темы**
- [Изменение источника данных диаграммы на целевой лист при копировании строк или диапазона](/cells/ru/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Создание динамических диаграмм](/cells/ru/cpp/create-dynamic-charts/)
- [Простой способ настройки диаграммы с использованием метода Chart.SetChartDataRange](/cells/ru/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Найдите тип значений X и Y точек в серии графика](/cells/ru/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
{{< app/cells/assistant language="cpp" >}}
