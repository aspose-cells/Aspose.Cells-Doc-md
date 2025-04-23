---
title: Как создать торнадо диаграмму с помощью C++
linktitle: Создать торнадо диаграмму
type: docs
weight: 73
url: /ru/cpp/create-tornado-chart/
description: Узнайте, как создавать торнадо диаграмму с помощью API Aspose.Cells for C++.
keywords: Создайте торнадо диаграмму с помощью C++, добавьте торнадо диаграмму, вставьте торнадо диаграмму
---

## **Введение**
Гистограмма торнадо, также известная как диаграмма торнадо или торнадо-график, является видом визуализации данных, который часто используется для анализа чувствительности в Excel. Она помогает понять влияние изменения переменных на конкретный результат или результат.

## **Как создать гистограмму торнадо в Excel**
Вы можете создать гистограмму торнадо в Excel, следуя этим шагам:
1. Выберите данные и перейдите во вкладку Вставка --> Диаграммы --> Вставить столбцовую или гистограмму --> Столбчатая гистограмма. Нажмите на неё.
<br>
<img src="1.png" width=70% />
2. Измените ось Y: Щелкните правой кнопкой мыши по оси Y. Нажмите на формат оси. В метках нажмите на выпадающий список позиции метки и выберите Положение Лоу.
<br>
<img src="2.png" width=70% />
3. Выберите любой столбец и перейдите к форматированию. установите соответствующую ширину промежутка.
<br>
<img src="3.png" width=70% />
4. Удалим знак минус(-) с гистограммы торнадо. Выберите ось X. Перейдите к форматированию. В параметрах оси нажмите на номер. В категории выберите пользовательское. В поле формата напишите ###0,###0. Нажмите добавить.
<br>
<img src="4.png" width=70% />
5. Нажмите на y-ось и перейдите в параметры оси. В параметрах оси установите Категории в обратном порядке.
<br>
<img src="5.png" width=70% />

## **Как добавить гистограмму торнадо в Aspose.Cells**
Пожалуйста, ознакомьтесь с следующим образцом кода. Он загружает [образец электронной таблицы](sample.xlsx), который содержит некоторые тестовые данные. Затем он создает столбчатую диаграмму на основе исходных данных и настраивает соответствующие свойства. Наконец, он сохраняет книгу в [формате XLSX](out.xlsx). На следующем скриншоте показана гистограмма торнадо, созданная Aspose.Cells в выходном файле Excel.
<br>
<img src="6.png" width=70% />

### **Образец кода**

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Get the chart collection from the worksheet
    ChartCollection charts = sheet.GetCharts();

    // Add a bar chart
    int index = charts.Add(ChartType::BarStacked, 8, 1, 24, 8);
    Chart chart = charts.Get(index);

    // Set data for the bar chart
    chart.SetChartDataRange(u"A1:C7", true);

    // Set properties for the bar chart
    chart.GetTitle().SetText(u"Tornado chart");
    chart.SetStyle(2);
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetPlotArea().GetBorder().SetColor(Color::White());
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set properties for the category axis
    chart.GetCategoryAxis().SetTickLabelPosition(TickLabelPositionType::Low);
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set gap width
    chart.SetGapWidth(10);

    // Set properties for the value axis
    Axis valueAxis = chart.GetValueAxis();
    valueAxis.GetTickLabels().SetNumberFormat(u"#,##0;#,##0");

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
