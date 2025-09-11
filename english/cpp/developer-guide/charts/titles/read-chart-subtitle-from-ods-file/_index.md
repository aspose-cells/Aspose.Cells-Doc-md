---
title: Read Chart Subtitle from ODS File with C++
linktitle: Read Chart Subtitle from ODS File
description: Learn how to use Aspose.Cells for C++ to read the chart subtitle from an OpenDocument Spreadsheet (ODS) file. Our guide will demonstrate how to extract and access the subtitle of a chart for further analysis or display.
keywords: Aspose.Cells for C++, Read Chart Subtitle, OpenDocument Spreadsheet, ODS File, Chart Extraction, Data Analysis.
type: docs
weight: 160
url: /cpp/read-chart-subtitle-from-ods-file/
---

## **Read Chart Subtitle from ODS File**

Aspose.Cells provides you with the ability to read chart subtitles in ODS files by using the [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/) property. The following sample code loads the [sample ODS file](89620481.ods) and reads the chart subtitle using [**Chart.SubTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getsubtitle/) property and prints it in the Console Window. Please see the console output of the code given below for reference.

## **Sample Code**

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

## **Console Output**

{{< highlight java >}}

Chart Subtitle: Sample Chart Subtitle

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}