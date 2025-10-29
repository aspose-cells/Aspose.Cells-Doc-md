---
title: Как создать динамический график с выпадающим списком на C++
linktitle: Создать динамический график с выпадающим списком
description: Узнайте, как создать динамический график, который обновляется в зависимости от выбранного в списке варианта, используя Aspose.Cells for C++. Наш пошаговый гид продемонстрирует, как интегрировать выпадающий список в ваш график для гибкой визуализации данных.
keywords: Aspose.Cells for C++, Динамический график, Выпадающий список, Визуализация данных, Интеграция, Гибкая визуализация.
type: docs
weight: 76
url: /ru/cpp/create-dynamic-chart-with-dropdownlist/
---

## **Возможные сценарии использования**
Динамическая диаграмма с выпадающим списком в Excel - мощный инструмент, позволяющий пользователям создавать интерактивные диаграммы, которые могут динамически обновляться на основе выбранных данных. Эта функция особенно полезна в ситуациях, где необходимо проанализировать несколько наборов данных или сравнить различные сценарии.

Одно из распространенных применений динамической диаграммы с выпадающим списком - в финансовом анализе. Например, компания может иметь несколько наборов финансовых данных для разных лет или отделов. Используя выпадающий список, пользователи могут выбрать конкретный набор данных, который они хотят проанализировать, и диаграмма автоматически обновится, чтобы отобразить соответствующую информацию. Это позволяет легко сравнивать и идентифицировать тенденции или закономерности.

Еще одно применение - в продажах и маркетинге. У компании может быть данные о продажах различных товаров или регионов. С помощью динамической диаграммы с выпадающим списком пользователи могут выбрать конкретный товар или регион из выпадающего списка, и диаграмма будет динамически обновляться, чтобы показать результаты продаж для выбранной опции. Это помогает определить лучшие области или продукты и принимать решения на основе данных.

В заключение, динамическая диаграмма с выпадающим списком в Excel обеспечивает гибкий и интерактивный способ визуализации и анализа данных. Он ценен в ситуациях, где необходимо сравнивать несколько наборов данных или изучать различные сценарии, что делает его универсальным инструментом для финансового анализа, продаж и маркетинга, а также многих других приложений.

## **Используйте Aspose Cells для создания динамического графика с выпадающим списком**
В следующих параграфах мы покажем, как создать динамический график с выпадающим списком, используя Aspose.Cells. Мы покажем пример кода, а также созданный с его помощью файл Excel.

## **Образец кода**
Следующий образец кода сгенерирует файл [Динамическая диаграмма с выпадающим списком](DynamicChartWithDropdownlist.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A3").PutValue(u"Tea");
    sheet.GetCells().Get(u"A4").PutValue(u"Coffee");
    sheet.GetCells().Get(u"A5").PutValue(u"Sugar");

    // In this example, we will add 12 months of data
    sheet.GetCells().Get(u"B2").PutValue(u"Jan");
    sheet.GetCells().Get(u"C2").PutValue(u"Feb");
    sheet.GetCells().Get(u"D2").PutValue(u"Mar");
    sheet.GetCells().Get(u"E2").PutValue(u"Apr");
    sheet.GetCells().Get(u"F2").PutValue(u"May");
    sheet.GetCells().Get(u"G2").PutValue(u"Jun");
    sheet.GetCells().Get(u"H2").PutValue(u"Jul");
    sheet.GetCells().Get(u"I2").PutValue(u"Aug");
    sheet.GetCells().Get(u"J2").PutValue(u"Sep");
    sheet.GetCells().Get(u"K2").PutValue(u"Oct");
    sheet.GetCells().Get(u"L2").PutValue(u"Nov");
    sheet.GetCells().Get(u"M2").PutValue(u"Dec");

    int allMonths = 12;
    int iCount = 3;
    for (int i = 0; i < iCount; i++)
    {
        for (int j = 0; j < allMonths; j++)
        {
            int _row = i + 2;
            int _column = j + 1;
            sheet.GetCells().Get(_row, _column).PutValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
        }
    }

    // This is the Dropdownlist for Dynamic Data
    CellArea ca = CellArea::CreateCellArea(9, 0, 9, 0);
    int _index = sheet.GetValidations().Add(ca);
    Validation _va = sheet.GetValidations().Get(_index);
    _va.SetType(ValidationType::List);
    _va.SetInCellDropDown(true);
    _va.SetFormula1(u"=$B$2:$M$2");

    sheet.GetCells().Get(u"A9").PutValue(u"Current Month");
    sheet.GetCells().Get(u"A10").PutValue(u"Jan");

    Style _style = sheet.GetCells().Get(u"A10").GetStyle();
    _style.GetFont().SetIsBold(true);
    _style.SetPattern(BackgroundType::Solid);
    _style.SetForegroundColor(Color::Yellow());
    sheet.GetCells().Get(u"A10").SetStyle(_style);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtMonthData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtXLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=Sheet1!$A$3:$A$5");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 8, 2, 20, 8);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"month", true);
    chart.GetNSeries().Get(0).SetName(u"=Sheet1!$A$10");
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtMonthData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtXLabels");

    // Save the workbook as an Excel file.
    workbook.Save(u"DynamicChartWithDropdownlist.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Примечания**
В сгенерированном файле диаграмма динамически будет подсчитывать данные для выбранного месяца. Это делается с помощью формулы "OFFSET" в образцовом коде:

```cpp
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Вы можете попробовать изменить значение выпадающего списка в ячейке "Лист1!$A$10", и вы увидите динамическое изменение диаграммы. Теперь мы успешно создали динамическую диаграмму с выпадающим списком с использованием Aspose.Cells.
{{< app/cells/assistant language="cpp" >}}
