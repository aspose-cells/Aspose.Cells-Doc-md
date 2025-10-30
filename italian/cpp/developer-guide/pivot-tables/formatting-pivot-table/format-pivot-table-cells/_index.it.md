---
title: Formatta celle di tabella pivot con C++
linktitle: Formattare le celle della tabella pivot
type: docs
weight: 30
url: /it/cpp/format-pivot-table-cells/
description: Impara come formattare celle di tabella pivot usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte vuoi formattare le celle della tabella pivot. Ad esempio, vuoi applicare un colore di sfondo alle celle della tabella pivot. Aspose.Cells fornisce due metodi [**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) e [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/), che puoi utilizzare a questo scopo.

[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) applica lo stile all'intera tabella pivot mentre [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) applica lo stile a una singola cella della tabella pivot.

{{% /alert %}}

Il codice di esempio seguente carica il [file Excel di esempio](pivot_format.xlsx) che contiene due tabelle pivot, e realizza l'operazione di formattare l'intera tabella pivot e di formattare singole celle nella tabella pivot.

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

## Articoli correlati

- [Formattazione tabella pivot](/cells/it/cpp/formatting-pivot-table/)
- [Lavorare con i formati di visualizzazione dei dati dei campi dati nella tabella pivot](/cells/it/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="cpp" >}}
