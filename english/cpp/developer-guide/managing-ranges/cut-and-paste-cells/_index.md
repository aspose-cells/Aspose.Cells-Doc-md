---
title: Cut and Paste Range with C++
linktitle: Cut and Paste Range
type: docs
weight: 130
url: /cpp/cut-and-paste-cells/
description: Learn how to cut and paste cells within a worksheet using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Cut and Paste Cells**

Aspose.Cells provides you with the ability to cut and paste cells within a worksheet by using the [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) method of the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. The [**InsertCutCells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcutcells/) method accepts the following parameters:

- [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/): The range of cells to be cut.
- Row Index: The index of the row to insert cells.
- Column Index: The index of the column to insert cells.
- [**ShiftType**](https://reference.aspose.com/cells/cpp/aspose.cells/shifttype/): The shift direction of the columns.

The following example shows how to cut and paste cells within a worksheet.

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(0, 2).SetValue(1);
    worksheet.GetCells().Get(1, 2).SetValue(2);
    worksheet.GetCells().Get(2, 2).SetValue(3);
    worksheet.GetCells().Get(2, 3).SetValue(4);

    Range namedRange = worksheet.GetCells().CreateRange(0, 2, 3, 1);
    namedRange.SetName(u"NamedRange");

    Range cut = worksheet.GetCells().CreateRange(u"C:C");

    worksheet.GetCells().InsertCutCells(cut, 0, 1, ShiftType::Right);

    workbook.Save(outDir + u"CutAndPasteCells.xlsx");

    std::cout << "Cells cut and pasted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
