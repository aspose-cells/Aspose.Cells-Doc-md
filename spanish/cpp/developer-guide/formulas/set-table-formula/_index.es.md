---
title: Propagar automáticamente fórmulas en tablas u objetos de lista al ingresar datos en nuevas filas con C++
linktitle: Establecer fórmula de tabla
type: docs
weight: 260
url: /es/cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Aprende cómo propagar fórmulas en tablas u objetos de lista automáticamente al ingresar nuevos datos usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**
A veces, deseas que una fórmula en tu Tabla u Objeto de Lista se propague automáticamente a filas nuevas al ingresar nuevos datos. Este es el comportamiento predeterminado de Microsoft Excel. Para lograr la misma funcionalidad con Aspose.Cells, usa el método [ListColumn::GetFormula](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listcolumn/getformula/)

## **Propagar fórmula en tabla u objeto de lista automáticamente al ingresar datos en nuevas filas**
El siguiente código de ejemplo crea una Tabla u Objeto de Lista de tal manera que la fórmula en la columna B se propagará automáticamente a filas nuevas cuando ingreses nuevos datos. Por favor, revisa el [archivo Excel de salida](5115469.xlsx) generado con este código. Si ingresas cualquier número en la celda A3, verás que la fórmula en la celda B2 se propagará automáticamente a la celda B3.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add column headings in cell A1 and B1
    sheet.GetCells().Get(0, 0).PutValue(u"Column A");
    sheet.GetCells().Get(0, 1).PutValue(u"Column B");

    // Add list object, set its name and style
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(0, 0, 1, sheet.GetCells().GetMaxColumn(), true));
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium2);
    listObject.SetDisplayName(u"Table");

    // Set the formula of second column so that it propagates to new rows automatically while entering data
    listObject.GetListColumns().Get(1).SetFormula(u"=[Column A] + 1");

    // Save the workbook in xlsx format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
