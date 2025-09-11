---
title: AutoFill Range of Excel File with C++
linktitle: AutoFill Range
type: docs
weight: 105
url: /cpp/autofill-ranges/
description: Learn how to perform an autofill operation in a specified range of an Excel file using Aspose.Cells with C++.
---

## **Perform an Autofill in the Specified Range in Excel**

In Excel, select a range, move the mouse to the right-bottom corner, and drag the "+" to autofill data.

## **Auto Fill Ranges with Aspose.Cells**

The following example shows how to perform an AutoFill operation on a Range. Here is the sample file which can be downloaded for testing this feature:

[range_autofill.xlsx](range_autofill.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"range_autofill.xlsx");

    // Get Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create Range
    Range src = cells.CreateRange(u"C3:C4");
    Range dest = cells.CreateRange(u"C5:C10");

    // AutoFill
    src.AutoFill(dest, AutoFillType::Series);

    // Save the Workbook
    workbook.Save(u"range_autofill_result.xlsx");

    std::cout << "Range auto-filled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}