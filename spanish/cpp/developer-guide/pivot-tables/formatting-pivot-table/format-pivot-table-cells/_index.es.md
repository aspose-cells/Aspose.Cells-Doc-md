---
title: Formato de celdas de tabla dinámica con C++
linktitle: Formato de celdas de tabla dinámica
type: docs
weight: 30
url: /es/cpp/format-pivot-table-cells/
description: Aprende a formatear celdas de tabla dinámica usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A veces, desea dar formato a las celdas de tabla dinámica. Por ejemplo, desea aplicar color de fondo a las celdas de tabla dinámica. Aspose.Cells proporciona dos métodos [**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) y [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/), que puede utilizar con este propósito.

[**PivotTable::FormatAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/formatall/) aplica el estilo a toda la tabla dinámica, mientras que [**PivotTable::Format()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/format/) aplica el estilo a una sola celda de la tabla dinámica.

{{% /alert %}}

El siguiente código de ejemplo carga el [archivo Excel de ejemplo](pivot_format.xlsx) que contiene dos tablas dinámicas, y realiza la operación de formatear toda la tabla dinámica y dar formato a celdas individuales en la tabla dinámica.

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

## Artículos relacionados

- [Dar formato a la tabla dinámica](/cells/es/cpp/formatting-pivot-table/)
- [Trabajar con formatos de visualización de datos del Campo de Datos en la Tabla Dinámica](/cells/es/cpp/working-with-data-display-formats-of-datafield-in-pivot-table/)
