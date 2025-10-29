---
title: Как сделать серию невидимой с помощью C++
linktitle: Как сделать серию невидимой
description: В диаграмме Excel вам может понадобиться сделать серию невидимой. В этой статье описывается, как использовать Aspose.Cells с C++ для этого.
keywords: Диаграмма Excel, Серия, Невидимая, Фильтрация.
type: docs
weight: 74
url: /ru/cpp/how-to-set-series-invisible/
---

## Как сделать серию невидимой в диаграмме Excel

В Excel можно щёлкнуть правой кнопкой по диаграмме, выбрать "Выбрать данные", и в появившемся окне проверить или снять выделение с серии, чтобы сделать её невидимой. Вы можете скачать [пример файла](SeriesFiltered.xlsx) и работать с ним в Excel, как показано на рисунке, чтобы реализовать эту функцию. Далее мы расскажем, как достичь этого с помощью библиотеки Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Как сделать серию невидимой с помощью Aspose.Cells 

Мы используем следующий код, чтобы сделать серию невидимой с помощью Aspose.Cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // File path for the input and output Excel files
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file
    Workbook workbook(filePath + u"SeriesFiltered.xlsx");

    // Access the charts collection of the first worksheet
    ChartCollection charts = workbook.GetWorksheets().Get(0).GetCharts();

    // Access a specific chart by name
    Chart chart = charts.Get(u"Chart 1");

    // Access filtered and non-filtered series collections
    SeriesCollection nSeriesFiltered = chart.GetFilteredNSeries();
    SeriesCollection nSeries = chart.GetNSeries();

    // Set the visibility of the first two series to be filtered
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Save the modified Excel file
    workbook.Save(filePath + u"output.xlsx");

    std::cout << "Series filtered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Вы можете получить следующий [входной файл](SeriesFiltered.xlsx) и [выходной файл](output.xlsx).

Как показано на рисунке ниже, первые две серии, которые изначально были видимы, стали невидимыми в выходном файле.  
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="cpp" >}}
