---
title: Pivot Tabellenzellen mit C++ formatieren
linktitle: Formatieren von Pivottabellenzellen
type: docs
weight: 30
url: /de/cpp/format-pivot-table-cells/
description: Erfahren Sie, wie Sie Pivot Tabellenzellen mit Aspose.Cells und C++ formatieren.
---

{{% alert color="primary" %}}

Manchmal möchten Sie Pivottabellenzellen formatieren. Zum Beispiel möchten Sie Hintergrundfarbe auf Pivottabellenzellen anwenden. Aspose.Cells bietet zwei Methoden [**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) und [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/), die Sie zu diesem Zweck verwenden können.

[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) wendet den Stil auf die gesamte Pivot-Tabelle an, während [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) den Stil auf eine einzelne Zelle der Pivot-Tabelle anwendet.

{{% /alert %}}

Der folgende Beispielcode lädt die [Beispiel Excel-Datei](pivot_format.xlsx), die zwei Pivot-Tabellen enthält, und führt die Operation der Formatierung der gesamten Pivot-Tabelle und der einzelnen Zellen in der Pivot-Tabelle aus.

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

## Verwandte Artikel

- [Pivot-Tabelle formatieren](/cells/de/cpp/formatting-pivot-table/)
- [Arbeiten mit Datenanzeigeformaten von DataField im Pivot-Table](/cells/de/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
