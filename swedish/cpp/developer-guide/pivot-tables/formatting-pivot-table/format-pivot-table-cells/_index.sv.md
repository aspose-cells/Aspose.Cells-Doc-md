---
title: Formatera Pivot Tabellceller med C++
linktitle: Formatera pivot tabellceller
type: docs
weight: 30
url: /sv/cpp/format-pivot-table-cells/
description: Lär dig hur man formaterar pivot tabellceller med Aspose.Cells med C++.
---

{{% alert color="primary" %}}

Ibland vill du formatera pivottabellceller. Till exempel vill du tillämpa bakgrundsfärg på pivottabellceller. Aspose.Cells tillhandahåller två metoder [**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) och [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/), som du kan använda för detta ändamål.

[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) tillämpar stilen på hela pivot-tabellen medan [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) tillämpar stilen på en enskild cell i pivot-tabellen.

{{% /alert %}}

Följande exempel kod laddar den [exempel fil](pivot_format.xlsx) som innehåller två pivot-tabeller, och utför operationen att formatera hela pivot-tabellen samt formatera individuella celler i pivot-tabellen.

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

## Relaterade artiklar

- [Formatering av Pivottabell](/cells/sv/cpp/formatting-pivot-table/)
- [Arbete med dataformat för DataField i pivot-tabell](/cells/sv/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
