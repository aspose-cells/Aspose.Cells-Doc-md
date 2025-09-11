---
title: Get the Cell Object by DisplayName of PivotField of PivotTable with C++
linktitle: Get the Cell Object by DisplayName of PivotField of PivotTable
type: docs
weight: 70
url: /cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Learn how to retrieve the cell object by the display name of a pivot field and apply formatting using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells provides the [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getcellbydisplayname/) method, which you can use to access the cell object by the display name of a pivot field. This method is useful when you want to highlight or format your pivot field header. This article explains how to retrieve the cell object by the display name of a data field and then apply formatting to it.

{{% /alert %}}

## **Get the Cell Object by DisplayName of PivotField of PivotTable**

The following code accesses the first pivot table of the worksheet and then retrieves the cell by the display name of the second data field of the pivot table. It then changes the fill color and font color of the cell to light blue and black, respectively. Below are screenshots showing how the pivot table looks before and after the execution of the code.

|**Pivot Table - Before**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"source.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    Cell cell = pivotTable.GetCellByDisplayName(pivotTable.GetDataFields().Get(0).GetDisplayName());

    Style style = cell.GetStyle();
    style.SetForegroundColor(Color::LightBlue());
    style.GetFont().SetColor(Color::Black());

    pivotTable.Format(cell.GetRow(), cell.GetColumn(), style);
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Pivot table formatted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

|**Pivot Table - After**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="cpp" >}}