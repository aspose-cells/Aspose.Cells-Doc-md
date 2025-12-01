---
title: Get Address, Cell Count, Offset, Entire Column, and Entire Row of the Range with C++
linktitle: Get Address, Cell Count, Offset, Entire Column, and Entire Row of the Range
type: docs
weight: 330
url: /cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/
description: Learn how to get address, cell count, offset, entire column, and entire row of a range using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Aspose.Cells provides the `Range` object, which has various utility methods that facilitate working with Excel ranges easily. This article illustrates the usage of the following methods or properties of the `Range` object:

- **Address**

  Gets the address of the range.

- **Cell Count**

  Gets the total cell count in the range.

- **Offset**

  Gets a range by offset.

- **Entire Column**

  Gets a `Range` object that represents the entire column (or columns) that contains the specified range.

- **Entire Row**

  Gets a `Range` object that represents the entire row (or rows) that contains the specified range.

## **Get Address, Cell Count, Offset, Entire Column, and Entire Row of the Range**
The following sample code explains the usage of the methods and properties as discussed above. Please see the console output of the code given below for reference.

## **Sample Code**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Create range A1:B3
    cout << "Creating Range A1:B3" << endl;
    Range rng = ws.GetCells().CreateRange(u"A1:B3");

    // Print range address and cell count
    cout << "Range Address: " << rng.GetAddress().ToUtf8() << endl;
    cout << "Range row Count: " << rng.GetRowCount() << endl;
    cout << "Range column Count: " << rng.GetColumnCount() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    // Create range A1
    cout << "Creating Range A1" << endl;
    rng = ws.GetCells().CreateRange(u"A1");

    // Print range offset, entire column and entire row
    cout << "Offset: " << rng.GetOffset(2, 2).GetAddress().ToUtf8() << endl;
    cout << "Entire Column: " << rng.GetEntireColumn().GetAddress().ToUtf8() << endl;
    cout << "Entire Row: " << rng.GetEntireRow().GetAddress().ToUtf8() << endl;

    // Formatting console output
    cout << "----------------------" << endl;
    cout << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Console Output**
{{< highlight java >}}

Creating Range A1:B3

Range Address: A1:B3

Cell Count: 6

\----------------------

Creating Range A1

Offset: C3

Entire Column: A:A

Entire Row: 1:1

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
