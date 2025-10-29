---
title: Три метода фильтрации данных диаграммы с помощью C++
linktitle: Три метода фильтрации данных диаграммы
description: Узнайте, как фильтровать диаграммы в Excel с помощью Aspose.Cells for C++. Наш всесторонний гид покажет, как применять фильтры к диаграммам, настраивать элементы диаграммы и использовать инструменты анализа данных для получения лучших инсайтов и принятия решений.
keywords: Aspose.Cells for C++, фильтрация диаграмм в Excel, анализ данных, принятие решений, визуализация
type: docs
weight: 2210
url: /ru/cpp/filtering-charts-in-excel/
---


## **1. Отфильтровать серии для отображения диаграммы**

### **Шаги по фильтрации серии с диаграммы в Excel**
В Excel мы можем фильтровать определённые серии на диаграмме, из-за чего эти фильтрованные серии не отображаются в диаграмме. Исходная диаграмма показана на **Рисунке 1**. Однако, когда мы фильтруем **Testseries2** и **Testseries4**, диаграмма будет выглядеть как на **Рисунке 2**.

В Aspose.Cells мы можем выполнить подобную операцию. Для файла [пример](seriesFiltered.xlsx) такого типа, если нужно фильтровать **Testseries2** и **Testseries4**, можно выполнить следующий код. Также мы будем держать два списка: один ([GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/)), чтобы хранить все выбранные серии, и другой ([GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)), чтобы хранить отфильтрованные серии.

Обратите **внимание**, что в коде, когда мы устанавливаем **chart->GetNSeries()->Get(0)->SetIsFiltered(true);**, первая серия в [GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/) будет удалена и размещена в соответствующей позиции внутри [GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/). Впоследствии, предыдущий **NSeries[1]** станет новым первым элементом списка, и все последующие серии сместятся вперед на одну позицию. Это означает, что если затем вызвать **chart->GetNSeries()->Get(1)->SetIsFiltered(true);**, мы фактически удаляем исходную третью серию. Это иногда вызывает путаницу, поэтому рекомендуется следовать операции в коде, которая удаляет серии с конца к началу.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Образец кода**
Приведенный ниже образец кода загружает [образец файла Excel](seriesFiltered.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of existing Workbook
    Workbook workbook(u"seriesFiltered.xlsx");

    // Get filtered series list
    SeriesCollection nSeriesFiltered = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetFilteredNSeries();

    // Get selected series list
    SeriesCollection nSeries = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetNSeries();

    // Should be 0
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 6
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Process from the end to the beginning
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Save the workbook
    workbook.Save(u"seriesFiltered-out.xlsx");

    // Reload the workbook
    workbook = Workbook(u"seriesFiltered-out.xlsx");

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **2. Отфильтруйте данные и дайте диаграмме измениться**

Фильтрация данных — отличный способ управлять фильтрами диаграмм с большим количеством данных. При фильтрации данные диаграммы изменяются. Одна из проблем — убедиться, что диаграмма остаётся на экране. Когда вы фильтруете, скрываются строки, и иногда диаграмма оказывается в скрытых строках.

![todo:image_alt_text](Figure3.png)

### **Шаги для использования фильтров данных для изменения диаграммы в Excel**

1. Щелкните внутри вашего диапазона данных.
2. Щелкните вкладку **Данные** и включите фильтры, щелкнув по кнопке Фильтры. Ваша строка заголовка будет иметь выпадающие стрелки.
3. Создайте диаграмму, перейдя на вкладку **Вставка** и выбрав столбчатую диаграмму.
4. Теперь отфильтруйте свои данные, используя выпадающие стрелки в данных. Не используйте фильтры диаграммы.

### **Образец кода**
Следующий пример кода показывает ту же функцию с использованием Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the First sheet.
    Worksheet sheet = workbook.GetWorksheets().Get(u"Sheet1");

    // Add data into details cells.
    sheet.GetCells().Get(0, 0).PutValue(u"Fruits Name");
    sheet.GetCells().Get(0, 1).PutValue(u"Fruits Price");
    sheet.GetCells().Get(1, 0).PutValue(u"Apples");
    sheet.GetCells().Get(2, 0).PutValue(u"Bananas");
    sheet.GetCells().Get(3, 0).PutValue(u"Grapes");
    sheet.GetCells().Get(4, 0).PutValue(u"Oranges");
    sheet.GetCells().Get(1, 1).PutValue(5);
    sheet.GetCells().Get(2, 1).PutValue(2);
    sheet.GetCells().Get(3, 1).PutValue(1);
    sheet.GetCells().Get(4, 1).PutValue(4);

    // Add a chart to the worksheet
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);

    // Access the instance of the newly added chart
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B5", true);

    // Set AutoFilter range
    sheet.GetAutoFilter().SetRange(u"A1:B5");

    // Add filters for a filter column.
    sheet.GetAutoFilter().AddFilter(0, u"Bananas");
    sheet.GetAutoFilter().AddFilter(0, u"Oranges");

    // Apply the filters
    sheet.GetAutoFilter().Refresh();

    // Save the chart as an image
    chart.ToImage(u"Autofilter.png");

    // Save the workbook
    workbook.Save(u"Autofilter.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3. Отфильтруйте данные с помощью таблицы и дайте измениться диаграмме**

Использование таблицы похоже на Метод 2, используя диапазон, но у вас есть преимущества таблиц перед диапазонами. Когда вы изменяете свой диапазон на таблицу и добавляете данные, диаграмма автоматически обновляется. С диапазоном вам придется изменять источник данных.

### **Форматирование как таблица в Excel**

Щелкните внутри ваших данных и используйте **CTRL+T** или используйте вкладку **Главная**, **Форматировать как таблицу**

![todo:image_alt_text](Figure4.png)

### **Образец кода**
Следующий пример кода загружает [пример Excel](TableFilters.xlsx), показывая ту же функцию с помощью Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Tables;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook
    Workbook workbook(u"TableFilters.xlsx");

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the instance of the newly added chart
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B7", true);

    // Convert the chart to image
    chart.ToImage(u"TableFilters.before.png");

    // Add a new List Object to the worksheet
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(u"A1", u"B7", true));

    // Add default style to the table
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium10);

    // Show Total
    listObject.SetShowTotals(false);

    // Add filters for a filter column
    listObject.GetAutoFilter().AddFilter(0, u"James");

    // Apply the filters
    listObject.GetAutoFilter().Refresh();

    // After adding new value the chart will change
    listObject.PutCellValue(7, 0, Object(u"Me"));
    listObject.PutCellValue(7, 1, Object(1000));

    // Check the changed images
    chart.ToImage(u"TableFilters.after.png");

    // Saving the Excel file
    workbook.Save(u"TableFilter.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
