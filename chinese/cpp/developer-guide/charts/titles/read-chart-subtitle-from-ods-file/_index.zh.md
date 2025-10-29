---
title: 用 C++ 从 ODS 文件读取图表字幕
linktitle: 从ODS文件中读取图表副标题
description: 学习如何使用 Aspose.Cells for C++ 从 OpenDocument Spreadsheet (ODS) 文件中读取图表字幕。我们的指南将演示如何提取和访问图表字幕以进行进一步分析或显示。
keywords: Aspose.Cells for C++，读取图表字幕，OpenDocument 电子表格，ODS 文件，图表提取，数据分析。
type: docs
weight: 160
url: /zh/cpp/read-chart-subtitle-from-ods-file/
---

## **从ODS文件中读取图表副标题**

Aspose.Cells通过使用[**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/)属性为您提供了读取ODS文件中图表副标题的能力。以下示例代码加载了[sample ODS file](89620481.ods)，使用[**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/)属性读取图表副标题，并在控制台窗口中打印。请参考下面给出的代码控制台输出。

## **示例代码**

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

## **控制台输出**

{{< highlight java >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
