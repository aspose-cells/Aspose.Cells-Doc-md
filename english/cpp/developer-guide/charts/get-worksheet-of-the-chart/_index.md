---
title: Get Worksheet of the Chart with C++
linktitle: Get Worksheet of the Chart
description: Learn how to retrieve the worksheet associated with an Excel chart using Aspose.Cells for C++. Our guide will show you how to access the worksheet and perform operations on it to manipulate the underlying data of the chart.
keywords: Aspose.Cells for C++, Excel charts, worksheets, data manipulation, underlying data, operations.
type: docs
weight: 1000
url: /cpp/get-worksheet-of-the-chart/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you want to access a worksheet from a chart's reference. Aspose.Cells provides the [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) method which returns the reference of the worksheet that contains the chart.

{{% /alert %}}

The following example shows how to use the [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) method. The code first prints the name of the worksheet, then accesses the first chart on the worksheet. It then prints the worksheet name again, using the [**Chart::GetWorksheet**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getworksheet/) method.

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

Below is the console output that the sample code results in. As you can see, it prints the same worksheet name both times.

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
