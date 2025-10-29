---
title: 用C++获取图表所在工作表
linktitle: 获取图表的工作表
description: 了解如何使用Aspose.Cells for C++检索与Excel图表关联的工作表。我们的指南将展示如何访问工作表并对其执行操作，以操作图表的底层数据。
keywords: Aspose.Cells for C++、Excel图表、工作表、数据操作、底层数据、操作。
type: docs
weight: 1000
url: /zh/cpp/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

有时，您希望从图表引用中访问工作表。Aspose.Cells提供了[**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/)方法，可以返回包含图表的工作表的引用。

{{% /alert %}}

以下示例展示如何使用[**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/)方法。代码首先输出工作表的名称，然后访问工作表上的第一个图表，再次打印工作表名，使用[**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/)方法。

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

    // Create workbook from sample Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print worksheet name
    cout << "Sheet Name: " << worksheet.GetName().ToUtf8() << endl;

    // Access the first chart inside this worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the chart's sheet and display its name again
    cout << "Chart's Sheet Name: " << chart.GetWorksheet().GetName().ToUtf8() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

以下是示例代码产生的控制台输出。您可以看到，它两次打印了相同的工作表名称。

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
