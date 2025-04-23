---
title: Читать подзаголовок графика из файла ODS с помощью C++
linktitle: Чтение подзаголовка диаграммы из файла ODS
description: Узнайте, как использовать Aspose.Cells for C++ для чтения подзаголовка графика из файла OpenDocument Spreadsheet (ODS). Наше руководство покажет, как извлекать и получать доступ к подзаголовкам графика для дальнейшего анализа или отображения.
keywords: Aspose.Cells for C++, Чтение подзаголовка графика, OpenDocument Spreadsheet, ODS файл, Извлечение графика, Анализ данных.
type: docs
weight: 160
url: /ru/cpp/read-chart-subtitle-from-ods-file/
---

## **Чтение подзаголовка диаграммы из файла ODS**

Aspose.Cells предоставляет возможность читать подзаголовки диаграмм в файлах ODS с помощью свойства [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/). Нижеприведенный образец кода загружает [образец файла ODS](89620481.ods) и читает подзаголовок диаграммы, используя свойство [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/), а затем выводит его в окне консоли. См. ниже вывод консоли для справки.

## **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load excel file containing charts
    Workbook workbook(srcDir + u"SampleChart.ods");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Print chart subtitle
    cout << "Chart Subtitle: " << chart.GetSubTitle().GetText().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод в консоль**

{{< highlight java >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
