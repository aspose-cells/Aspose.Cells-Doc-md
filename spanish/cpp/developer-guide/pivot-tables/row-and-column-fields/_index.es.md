---
title: Campos de fila y columna en Aspose.Cells for C++
linktitle: Campos de fila y columna
description: Aprenda cómo agregar campos base a las regiones de fila y columna de una tabla dinámica y cómo controlar los subtotales de los campos dinámicos mediante PivotField.SetSubtotals en Aspose.Cells for C++.
keywords: Aspose.Cells, C++, tabla dinámica, campo de fila, campo de columna, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotales
type: docs
weight: 220
url: /es/cpp/row-and-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Los campos de fila y columna son los bloques de construcción de una tabla dinámica. Un campo colocado en la región de fila aparece verticalmente a la izquierda de la tabla dinámica, mientras que un campo colocado en la región de columna aparece horizontalmente en la parte superior. Este artículo muestra cómo agregar campos base a esas regiones mediante programación y cómo controlar los subtotales que se renderizan entre los grupos de campos utilizando el método `PivotField.SetSubtotals`.

## **Agregar un campo a la región de fila o columna**

El método `PivotTable.AddFieldToArea(PivotFieldType fieldType, intrusive_ptr<Aspose::Cells::Systems::String> fieldName)` mueve un campo base desde los datos de origen a una de las cuatro regiones de la tabla dinámica. El argumento `fieldType` acepta uno de los siguientes valores de `PivotFieldType`.

- `Row` — campos colocados verticalmente a la izquierda
- `Column` — campos colocados horizontalmente en la parte superior
- `Data` — campos cuyos valores se agregan
- `Page` — campos utilizados como filtros de informe

Después de agregar los campos, puede acceder a ellos a través de las propiedades `PivotTable.RowFields` y `PivotTable.ColumnFields`. Cada propiedad devuelve un `PivotFieldCollection`. El campo en el índice 0 de `RowFields` es el campo de fila más externo, y los índices posteriores representan campos anidados dentro de él. La misma convención de indexación se aplica a `ColumnFields`.

El orden de anidamiento de los campos es importante. Agregar `Category` a la región de fila primero y luego `Item` produce una tabla dinámica cuya agrupación externa es `Category` y cuya agrupación interna es `Item`. Invertir el orden invierte la jerarquía.

## **Subtotales de campos dinámicos**

El método `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` controla qué filas de subtotal aparecen para un campo dinámico. Cada llamada activa o desactiva un único tipo de subtotal de forma independiente. Pasar `shown = true` muestra el subtotal, mientras que `shown = false` lo oculta. Dado que cada llamada solo afecta a un tipo, llamar al método varias veces con diferentes valores de `subtotalType` crea un subconjunto personalizado de subtotales.

La enumeración `PivotFieldSubtotalType` define los tipos de subtotales disponibles.

- `Automatic` — Aspose.Cells elige la selección predeterminada (normalmente `Sum` para campos numéricos)
- `None` — suprime todas las filas de subtotal
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Los subtotales solo se renderizan cuando hay dos o más campos dinámicos en la región de fila (o en la región de columna). Un único campo no tiene nada significativo que subtotalizar, por lo que las llamadas a `SetSubtotals` no tienen un efecto visible en ese caso. Por lo tanto, este artículo coloca dos campos de fila (`Category` externo, `Item` interno) en cada ejemplo para que el límite de subtotal entre cada grupo `Category` sea visible.
{{% /alert %}}

## **Escenario 1 — Subtotales automáticos (predeterminados)**

Si no llama a `SetSubtotals` en absoluto, Aspose.Cells aplica la selección `Automatic` a los campos numéricos. El siguiente ejemplo confirma explícitamente este comportamiento llamando a `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` en el campo de fila externo `Category`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Automatic, true);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output_automatic.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Escenario 2 — Suprimir todos los subtotales (None)**

Llamar a `SetSubtotals(PivotFieldSubtotalType.None, true)` elimina todas las filas de subtotal de la tabla dinámica, dejando solo las filas de campos y el total general en la parte inferior. Esto resulta útil cuando se desea obtener los datos agrupados sin procesar, sin ninguna fila de resumen.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.SetName(u"Data");

    U16String headers[] = { u"Category", u"Item", u"Year", u"Amount" };
    for (int j = 0; j < 4; j++) {
        sheet.GetCells().Get(0, j).PutValue(headers[j]);
    }

    U16String categories[] = { u"Fruit", u"Fruit", u"Fruit", u"Fruit",
                               u"Vegetable", u"Vegetable", u"Vegetable", u"Vegetable" };
    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana",
                          u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[]   = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = {  100,  150,   80,   90,   50,   60,   40,   45 };

    for (int i = 0; i < 8; i++) {
        sheet.GetCells().Get(i + 1, 0).PutValue(categories[i]);
        sheet.GetCells().Get(i + 1, 1).PutValue(items[i]);
        sheet.GetCells().Get(i + 1, 2).PutValue(years[i]);
        sheet.GetCells().Get(i + 1, 3).PutValue(amounts[i]);
    }

    int pivotIndex = sheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::None, true);
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    wb.Save(u"output_none.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Escenario 3 — Subconjunto personalizado de subtotales (Sum + Average)**

No está limitado a un solo tipo de subtotal. Cada llamada a `SetSubtotals` opera independientemente en un tipo, por lo que llamar al método dos veces, una vez con `Sum` y otra con `Average`, produce un subconjunto personalizado de dos filas de subtotal para cada grupo `Category`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(u"A1").PutValue(u"Category");
    worksheet.GetCells().Get(u"B1").PutValue(u"Item");
    worksheet.GetCells().Get(u"C1").PutValue(u"Year");
    worksheet.GetCells().Get(u"D1").PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Average, true);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output_custom.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Resumen**

Los tres escenarios anteriores comparten el mismo conjunto de datos y la misma estructura de tabla dinámica. La única diferencia entre ellos es la llamada a `SetSubtotals` aplicada al campo de fila externo `Category`. Recuerde la regla de los dos campos: un único campo en una región no tiene nada que subtotalizar, así que coloque siempre al menos dos campos en la región de fila o columna cuando desee que `SetSubtotals` tenga un efecto visible.

## **Artículos relacionados**

- [Campos de página en tablas dinámicas](/cells/es/cpp/add-page-field-in-pivot-table/)
- [Actualización de tablas dinámicas en Aspose.Cells for C++](/cells/es/cpp/refresh-pivot-table/)
- [Aplicar estilos a tablas dinámicas](/cells/es/cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
