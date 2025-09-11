---
title: Format Pivot Table Cells with C++
linktitle: Format Pivot Table Cells
type: docs
weight: 30
url: /cpp/format-pivot-table-cells/
description: Learn how to format pivot table cells using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

Sometimes, you want to format pivot table cells. For example, you want to apply background color to pivot table cells. Aspose.Cells provides two methods [**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) and [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/), which you can use for this purpose.

[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) applies the style to the entire pivot table while [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) applies the style to a single cell of the pivot table.

{{% /alert %}}

The following sample code loads the [sample Excel file](pivot_format.xlsx) that contains two pivot tables, and achieves the operation of formatting the entire pivot table and formatting individual cells in the pivot table.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook(u"pivot_format.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(u"Sheet1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(1);

    Style style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::LightBlue());
    pivotTable.FormatAll(style);

    style = workbook.CreateStyle();
    style.SetPattern(BackgroundType::Solid);
    style.SetBackgroundColor(Color::Yellow());

    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(0);
    pivotTable2.Format(16, 5, style);

    workbook.Save(u"out.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Related Articles

- [Formatting Pivot Table](/cells/cpp/formatting-pivot-table/)
- [Working with data display formats of DataField in Pivot Table](/cells/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="cpp" >}}