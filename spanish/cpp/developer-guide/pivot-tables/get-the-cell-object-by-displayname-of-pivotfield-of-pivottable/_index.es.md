---
title: Obtener el objeto de celda por el nombre visible del campo de pivote en una tabla dinámica con C++
linktitle: Obtener el objeto de celda por el nombre visible del campo de pivote en una tabla dinámica
type: docs
weight: 70
url: /es/cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: Aprenda cómo recuperar el objeto de celda por el nombre visible de un campo dinámico y aplicar formato usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells proporciona el método [**PivotTable::GetCellByDisplayName()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getcellbydisplayname/), que puede usar para acceder al objeto de celda por el nombre visible de un campo de pivote. Este método es útil cuando desea resaltar o dar formato a la cabecera de su campo dinámico. Este artículo explica cómo recuperar el objeto de celda por el nombre visible de un campo de datos y luego aplicar formato a este.

{{% /alert %}}

## **Obtener el objeto de celda por el nombre visible del campo de pivote en una tabla dinámica**

El siguiente código accede a la primera tabla dinámica de la hoja de trabajo y luego recupera la celda por el nombre visible del segundo campo de datos de la tabla dinámica. Luego, cambia el color de relleno y el color de fuente de la celda a azul claro y negro, respectivamente. A continuación, se muestran capturas de pantalla de cómo se ve la tabla dinámica antes y después de la ejecución del código.

|**Tabla Dinámica - Antes**|
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

|**Tabla Dinámica - Después**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
