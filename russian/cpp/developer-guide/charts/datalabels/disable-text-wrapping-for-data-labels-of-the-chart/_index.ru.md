---
title: Отключение переноса текста у меток данных графика с помощью C++
linktitle: Отключить перенос текста у меток данных
description: Узнайте, как отключить перенос текста для меток данных в графиках с помощью Aspose.Cells for C++. Наше руководство покажет, как предотвратить перекрытие длинных меток и обеспечить более читаемый и ясный отображение графиков.
keywords: Aspose.Cells for C++, построение графиков, метки данных, перенос текста, перекрытие, читаемость, отображения.
type: docs
weight: 70
url: /ru/cpp/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 позволяет пользователям включать или отключать перенос текста в метках данных диаграммы. По умолчанию текст в метках данных диаграммы находится в перенесенном состоянии.

Aspose.Cells предоставляет свойство [**DataLabels.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/istextwrapped/), которое можно установить в True или False для включения или отключения переноса текста меток данных соответственно.

{{% /alert %}}

Ниже приведен образец кода, показывающий, как отключить перенос текста для меток данных диаграммы.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Load the sample Excel file inside the workbook object
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Disable the Text Wrapping of Data Labels in all Series
    chart.GetNSeries().Get(0).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(1).GetDataLabels().SetIsTextWrapped(false);
    chart.GetNSeries().Get(2).GetDataLabels().SetIsTextWrapped(false);

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Text wrapping disabled successfully in data labels!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
