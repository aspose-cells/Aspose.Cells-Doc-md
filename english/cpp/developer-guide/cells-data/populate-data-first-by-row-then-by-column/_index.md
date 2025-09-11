---
title: Populate Data First by Row then by Column with C++
linktitle: Populate Data First by Row then by Column
type: docs
weight: 1000
url: /cpp/populate-data-first-by-row-then-by-column/
description: Learn how to Populate Data First by Row then by Column through the Aspose.Cells for C++ API.
keywords: Populate Data First by Row then by Column, Insert Data First by Row then by Column, Add Data First by Row then by Column, High performance data insertion, High performance data addition
---

{{% alert color="primary" %}} 

Populating a spreadsheet with data first by row and then by column improves the overall performance.

{{% /alert %}} 

Putting data in the sequence A1, B1, A2, B2 is faster than A1, A2, B1, B2. If there are many cells in a worksheet and you follow the second sequence, that is, you're filling the data row by row, this tip can make the program much faster.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook workbook;

    // Populate Data into Cells
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();
    cells.Get(u"A1").PutValue(U"data1");
    cells.Get(u"B1").PutValue(U"data2");
    cells.Get(u"A2").PutValue(U"data3");
    cells.Get(u"B2").PutValue(U"data4");

    // Save workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}