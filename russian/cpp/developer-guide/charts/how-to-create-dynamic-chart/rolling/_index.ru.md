---
title: Как создать динамический скользящий график с помощью C++
linktitle: Как создать динамическую катящуюся диаграмму
description: Узнайте, как создать динамический скользящий график, используя Aspose.Cells for C++. Наш гид продемонстрирует, как реализовать плавные переходы данных и скользящие средние для вашего графика для более непрерывного и актуального отображения.
keywords: Aspose.Cells for C++, Динамический скользящий график, Переходы данных, Плавные средние, Непрерывное отображение, Обновление визуализации.
type: docs
weight: 74
url: /ru/cpp/create-dynamic-rolling-chart/
---

## **Возможные сценарии использования**
Динамическая катящаяся диаграмма относится к графическому представлению данных, которое постоянно смещается и обновляется с течением времени. Это тип диаграммы, который постоянно обновляется, показывая катящееся окно последних данных, отбрасывая старые данные по мере поступления новых.

Динамические катящиеся диаграммы часто используются для визуализации тенденций и закономерностей в реальном времени или потоковых данных. Они особенно полезны в сценариях, где временные аспекты и изменения со временем критичны, таких как анализ фондового рынка, мониторинг погоды или отслеживание живой производительности.

Эти диаграммы обычно используют анимацию или автоматическую прокрутку, чтобы обеспечить обновление наиболее актуальной информации. Длина катящегося окна может быть настроена для отображения определенного временного периода, такого как последний час, день или неделя.

В заключение, динамическая катящаяся диаграмма представляет собой непрерывно обновляемое графическое представление, отображающее последние данные и отбрасывающее старые, что позволяет пользователям наблюдать тенденции и закономерности в реальном времени.

## **Используйте Aspose Cells для создания динамической катящейся диаграммы**
В следующих абзацах мы покажем вам, как создать динамическую катящуюся диаграмму с использованием Aspose.Cells. Мы покажем вам код для примера, а также созданный этим кодом файл Excel.

## **Образец кода**
Приведенный ниже образец кода сгенерирует файл [Динамической Карты Прокрутки](DynamicRollingChart.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Your local test path
    U16String LocalPath = u"";

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A1").PutValue(u"Month");
    sheet.GetCells().Get(u"A2").PutValue(1);
    sheet.GetCells().Get(u"A3").PutValue(2);
    sheet.GetCells().Get(u"A4").PutValue(3);
    sheet.GetCells().Get(u"A5").PutValue(4);
    sheet.GetCells().Get(u"A6").PutValue(5);
    sheet.GetCells().Get(u"A7").PutValue(6);
    sheet.GetCells().Get(u"A8").PutValue(7);

    sheet.GetCells().Get(u"B1").PutValue(u"Sales");
    sheet.GetCells().Get(u"B2").PutValue(50);
    sheet.GetCells().Get(u"B3").PutValue(45);
    sheet.GetCells().Get(u"B4").PutValue(55);
    sheet.GetCells().Get(u"B5").PutValue(60);
    sheet.GetCells().Get(u"B6").PutValue(55);
    sheet.GetCells().Get(u"B7").PutValue(65);
    sheet.GetCells().Get(u"B8").PutValue(70);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 10, 3, 25, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtLabels");

    // Save the workbook as an Excel file.
    workbook.Save(LocalPath + u"DynamicRollingChart.xlsx");

    std::cout << "Dynamic rolling chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Примечания**
В сгенерированном файле вы можете продолжать добавлять данные в столбцах A и B, в то время как диаграмма динамически подсчитывает последние 5 наборов данных. Это делается с использованием формулы "СМЕЩЕНИЕ" в образцовом коде:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Вы можете попробовать изменить число "-5" на "-10" в формуле, и динамическая диаграмма будет подсчитывать последние 10 наборов данных. Теперь мы успешно создали динамическую прокручивающуюся диаграмму с использованием Aspose.Cells.
