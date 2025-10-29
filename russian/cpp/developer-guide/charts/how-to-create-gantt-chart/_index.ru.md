---
title: Как создать диаграмму Ганта с помощью C++
linktitle: Как создать диаграмму Ганта
type: docs
weight: 72
url: /ru/cpp/how-to-create-gantt-chart/
description: Узнайте, как создавать диаграмму Ганта с помощью API Aspose.Cells for C++.
keywords: Создайте диаграмму Ганта с помощью C++, добавьте диаграмму Ганта, вставьте диаграмму Ганта
---

## **Что такое диаграмма Ганта**

Диаграмма Ганта — это тип графика в виде столбцовой диаграммы, которая иллюстрирует график проекта. Она показывает даты начала и окончания различных элементов проекта. Каждый элемент или задача представлена столбцом, длина которого соответствует его продолжительности. Диаграммы Ганта также показывают зависимости между задачами, позволяя менеджерам видеть последовательность выполнения задач. Они широко используются в управлении проектами для планирования, расписания и отслеживания проектов.

## **Как создать диаграмму Ганта в Excel**

Вы можете создать диаграмму Ганта в Excel, следуя этим шагам:
1. Добавьте данные для диаграммы Ганта. 
<br>
<img src="00.png" width=50% />
1. Выберите данные и перейдите в Вставка -> Графики -> Вставить столбчатую или линейчатую диаграмму -> Сложенная гистограмма. В нашем примере это B1:B7, затем вставьте **Сложенную гистограмму**.
<br>
<img src="1.png" width=50% />

1. Выберите диаграмму, **Выбор данных**->**Добавить**, установите **Имя серии** и **Значения серии** следующим образом.
<br>
<img src="2.png" width=50% />

1. Выберите диаграмму, отредактируйте **Метки горизонтальной (категорийной) оси**.
<br>
<img src="3.png" width=50% />

1. **Форматировать ось** по оси Y, выберите **Обратный порядок категорий**.
1. Выберите **синюю серию** и установите **Заливка->Без заливки**.
1. **Форматировать ось** по оси X, установите **Минимум** и **Максимум**(01.05.2019:43470, 30.01.2019:43494).
<br>
<img src="4.png" width=50% />

1. **Добавьте метки данных** для диаграммы, и вы получите диаграмму Ганта.
<br>
<img src="0.png" width=50% />


## **Как добавить диаграмму Ганта в Aspose.Cells**
Пожалуйста, посмотрите следующий пример кода. Он загружает [пробный Excel-файл](sample.xlsx), содержащий некоторые данные. Затем он создает сложенную столбчатую диаграмму на основе исходных данных и устанавливает соответствующие свойства. В конце он сохраняет рабочую книгу в [формате XLSX](result.xlsx). Следующий скриншот показывает созданную с помощью Aspose.Cells диаграмму Ганта в выходном Excel-файле.
<br>
<img src="5.png" width=60% />

### **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create BarStacked Chart
    int32_t chartIndex = worksheet.GetCharts().Add(ChartType::BarStacked, 5, 6, 20, 15);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Set the chart title name
    chart.GetTitle().SetText(u"Gantt Chart");

    // Set the chart title visibility
    chart.GetTitle().SetIsVisible(true);

    // Set data range
    chart.SetChartDataRange(u"B1:B6", true);

    // Add series data range
    chart.GetNSeries().Add(u"C2:C6", true);

    // No fill for one series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set the Horizontal(Category) Axis
    chart.GetNSeries().SetCategoryData(u"A2:A6");

    // Reverse the Horizontal(Category) Axis
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set the value axis's MinValue and MaxValue
    chart.GetValueAxis().SetMinValue(worksheet.GetCells().Get(u"B2").GetValue());
    chart.GetValueAxis().SetMaxValue(worksheet.GetCells().Get(u"D6").GetValue());

    // Set the PlotArea with no fill
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Show the DataLabels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowValue(true);

    // Disable the Legend
    chart.SetShowLegend(false);

    // Save the result
    workbook.Save(u"result.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
