---
title: Insert Timeline with C++
linktitle: Timelines
type: docs
weight: 170
url: /cpp/create-timeline/
description: Learn how to create a timeline with Aspose.Cells using C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Instead of adjusting filters to show dates, you can use a PivotTable Timeline—a dynamic filter option that lets you easily filter by date/time and zoom in on the period you want with a slider control. Microsoft Excel allows you to create a timeline by selecting a pivot table and then clicking *Insert > Timeline*. Aspose.Cells also allows you to create a timeline using the [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.timelines/timelinecollection/add/) method.

## **Create a Timeline for a Pivot Table**

Please see the following sample code. It loads the [sample Excel file](input.xlsx) that contains the pivot table. It then creates the timeline based on the first base pivot field. Finally, it saves the workbook in the [output XLSX](output.xlsx) file. The following screenshot shows the timeline created by Aspose.Cells in the output Excel file.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing pivot table
    U16String inputFilePath = u"input.xlsx";
    Workbook wb(inputFilePath);

    // Access second worksheet (index 1)
    Worksheet sheet = wb.GetWorksheets().Get(1);

    // Access first pivot table inside the worksheet
    PivotTable pivot = sheet.GetPivotTables().Get(0);

    // Add timeline relating to pivot table
    int index = sheet.GetTimelines().Add(pivot, 15, 1, u"Ship Date");

    // Access the newly added timeline from timeline collection
    Timeline timeline = sheet.GetTimelines().Get(index);

    // Save the modified workbook
    U16String outputFilePath = u"output.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Timeline added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
