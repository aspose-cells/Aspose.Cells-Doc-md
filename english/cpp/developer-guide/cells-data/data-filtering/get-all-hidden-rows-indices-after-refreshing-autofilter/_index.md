---
title: Get All Hidden Rows Indices after Refreshing AutoFilter with C++
linktitle: Get All Hidden Rows Indices after Refreshing AutoFilter
type: docs
weight: 320
url: /cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Learn how to get all hidden rows indices after refreshing AutoFilter by using the Aspose.Cells for C++ API.
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter, Obtain All Hidden Rows Indices after Refreshing AutoFilter, Retrieve All Hidden Rows Indices after Refreshing AutoFilter
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

When you apply the AutoFilter on worksheet cells, some of the rows get hidden automatically. However, it might be the case that some rows are already hidden manually by the Excel end‑user and are not hidden by an AutoFilter. This makes it difficult to know which rows are hidden by the AutoFilter and which are hidden manually by the Excel end‑user. Aspose.Cells deals with this problem using the int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/) method. This method returns the row indices of all rows that are hidden by the AutoFilter and not manually by the Excel end‑user.

## **Get All Hidden Rows Indices after Refreshing AutoFilter**

Please see the following sample code that loads the [sample Excel file](64716909.xlsx) which contains some rows hidden manually by the Excel end‑user. The code applies the AutoFilter and refreshes it using the int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/) method that returns the row indices of all rows hidden by the AutoFilter. It then prints the indices of the hidden rows on the console along with cell names and values.

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + U16String(u"sampleGetAllHiddenRowsIndicesAfterRefreshingAutoFilter.xlsx");
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    AutoFilter autoFilter = worksheet.GetAutoFilter();
    autoFilter.AddFilter(0, u"Orange");

    Vector<int32_t> rowIndices = autoFilter.Refresh(true);

    std::cout << "Printing Rows Indices, Cell Names and Values Hidden By AutoFilter." << std::endl;
    std::cout << "--------------------------" << std::endl;

    for (int32_t i = 0; i < rowIndices.GetLength(); i++)
    {
        int32_t r = rowIndices[i];
        Cell cell = worksheet.GetCells().Get(r, 0);
        std::cout << r << "\t" << cell.GetName().ToUtf8() << "\t" << cell.GetStringValue().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Console Output**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
