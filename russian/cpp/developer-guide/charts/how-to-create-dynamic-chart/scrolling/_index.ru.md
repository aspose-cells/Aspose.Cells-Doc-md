---
title: Как создать динамический график с прокруткой на C++
linktitle: Создать график с прокруткой
description: Узнайте, как создать динамический график с прокруткой, используя Aspose.Cells for C++. Наш пошаговый гид покажет, как реализовать плавные переходы данных и автоматическую прокрутку для вашего графика для более непрерывного и актуального отображения.
keywords: Aspose.Cells for C++, Динамический график с прокруткой, Переходы данных, Плавная прокрутка, Непрерывное отображение, Обновление визуализации.
type: docs
weight: 75
url: /ru/cpp/create-dynamic-scrolling-chart/
---

## **Возможные сценарии использования**
Динамическая прокручивающаяся диаграмма - это тип графического представления, используемого для отображения данных, меняющихся со временем. Она предназначена для предоставления видео в реальном времени данных, позволяя пользователям отслеживать непрерывные обновления и тренды. Диаграмма непрерывно обновляется при добавлении новых данных, автоматически прокручиваясь, чтобы показывать самую последнюю информацию.

Динамические прокручивающиеся диаграммы широко используются в различных отраслях, таких как финансы, анализ фондового рынка, отслеживание погоды и аналитика социальных медиа. Они позволяют пользователям визуализировать и анализировать паттерны данных и принимать обоснованные решения на основе информации в реальном времени.

Эти диаграммы обычно интерактивны, позволяя пользователю увеличивать или уменьшать масштаб, прокручивать исторические данные и регулировать временные интервалы. Они часто поддерживают несколько серий данных, обеспечивая комплексный обзор различных метрик и их взаимосвязей.

В целом, динамические прокручивающиеся диаграммы - это ценные инструменты для мониторинга и анализа временных рядов данных, способствуя принятию решений в реальном времени и улучшая возможности визуализации данных.

## **Используйте Aspose Cells для создания динамического графика с прокруткой**
В следующих параграфах мы покажем, как создать динамический график с прокруткой с помощью Aspose.Cells. Мы предоставим пример кода, а также файл Excel, созданный с этим кодом.

## **Образец кода**
Приведенный ниже образец кода сгенерирует файл [Динамической Прокручивающейся Диаграммы](DynamicScrollingChart.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String localPath(u"");

    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Day");
    sheet.GetCells().Get(u"B1").PutValue(u"Sales");

    int allDays = 30;
    int showDays = 10;
    int currentDay = 1;

    Cells cells = sheet.GetCells();
    for (int i = 0; i < allDays; i++)
    {
        int row = i + 1;
        cells.Get(row, 0).PutValue(i + 1);
        cells.Get(row, 1).PutValue(50 * (i % 2) + 20 * (i % 3) + 10 * (i / 3));
    }

    sheet.GetCells().Get(u"G19").PutValue(u"Start Day");
    sheet.GetCells().Get(u"G20").PutValue(currentDay);
    sheet.GetCells().Get(u"H19").PutValue(u"Show Days");
    sheet.GetCells().Get(u"H20").PutValue(showDays);

    int index = sheets.GetNames().Add(u"Sheet1!ChtScrollData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    index = sheets.GetNames().Add(u"Sheet1!ChtScrollLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    ScrollBar bar = sheet.GetShapes().AddScrollBar(2, 0, 3, 0, 200, 30);
    bar.SetMin(0);
    bar.SetMax(allDays - showDays);
    bar.SetCurrentValue(currentDay);
    bar.SetLinkedCell(u"$G$20");

    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 2, 4, 15, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtScrollData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtScrollLabels");

    workbook.Save(localPath + u"DynamicScrollingChart.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Примечания**
В сгенерированном файле вы можете работать со строкой прокрутки, в то время как диаграмма динамически подсчитывает последние 10 наборов данных. Это делается с использованием формулы "СМЕЩЕНИЕ" в образцовом коде:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

Вы можете попробовать изменить число "10" на "15" в ячейке "Лист1!$H$20", и динамическая диаграмма будет подсчитывать последние 15 наборов данных. Теперь мы успешно создали динамическую прокручивающуюся диаграмму с использованием Aspose.Cells.
