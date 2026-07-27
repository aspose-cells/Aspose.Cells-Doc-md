---
title: Agregar campos de fila y columna a una tabla dinámica en Aspose.Cells para .NET
linktitle: Campos de fila y columna
description: Aprenda a agregar campos base a las regiones de fila y columna de una tabla dinámica y a controlar los subtotales de los campos dinámicos con PivotField.SetSubtotals en Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET, tabla dinámica, campo de fila, campo de columna, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotales
type: docs
weight: 220
url: /es/net/pivot-table-add-row-column-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Agregar un campo a la región de fila o columna**

El método `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` mueve un campo base desde los datos de origen a una de las cuatro regiones de la tabla dinámica. El argumento `fieldType` acepta uno de los siguientes valores de `PivotFieldType`.

- `Row` — campos colocados verticalmente a la izquierda
- `Column` — campos colocados horizontalmente en la parte superior
- `Data` — campos cuyos valores se agregan
- `Page` — campos utilizados como filtros de informe

Después de agregar los campos, puede acceder a ellos a través de las propiedades `PivotTable.RowFields` y `PivotTable.ColumnFields`. Cada propiedad devuelve un `PivotFieldCollection`. El campo en el índice 0 de `RowFields` es el campo de fila más externo, y los índices siguientes representan campos anidados dentro de él. La misma convención de indexación se aplica a `ColumnFields`.

El orden de anidamiento de los campos es importante. Si se agrega primero `Category` a la región de fila y luego `Item`, se obtiene una tabla dinámica cuya agrupación externa es `Category` y cuya agrupación interna es `Item`. Si se invierte el orden, se invierte la jerarquía.

## **Subtotales de campos dinámicos**

El método `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` controla qué filas de subtotal aparecen para un campo dinámico. Cada llamada activa o desactiva un único tipo de subtotal de forma independiente. Si se pasa `shown = true` se muestra el subtotal, mientras que `shown = false` lo oculta. Dado que cada llamada solo afecta a un tipo, llamar al método varias veces con distintos valores de `subtotalType` construye un subconjunto personalizado de subtotales.

La enumeración `PivotFieldSubtotalType` define los tipos de subtotal disponibles.

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
Los subtotales solo se renderizan cuando hay dos o más campos dinámicos en la región de fila (o en la región de columna). Un solo campo no tiene nada significativo entre lo que calcular un subtotal, por lo que las llamadas a `SetSubtotals` no tienen ningún efecto visible en ese caso. Por este motivo, este artículo coloca dos campos de fila (`Category` externo, `Item` interno) en cada ejemplo, de modo que el límite de subtotal entre cada grupo `Category` sea visible.
{{% /alert %}}

## **Escenario 1 — Subtotales automáticos (predeterminados)**

Cuando no se llama a `SetSubtotals` en absoluto, Aspose.Cells aplica la selección `Automatic` a los campos numéricos. El siguiente ejemplo confirma explícitamente este comportamiento al llamar a `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` sobre el campo de fila `Category` externo.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Automatic, true);

pivotTable.CalculateData();

workbook.Save("output_automatic.xlsx");
```

## **Escenario 2 — Suprimir todos los subtotales (None)**

Llamar a `SetSubtotals(PivotFieldSubtotalType.None, true)` elimina todas las filas de subtotal de la tabla dinámica, dejando solo las filas de los campos y el total general en la parte inferior. Esto resulta útil cuando se desean los datos agrupados en bruto sin ninguna fila de resumen.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

string[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.Length; j++)
{
    worksheet.Cells[0, j].PutValue(headers[j]);
}

object[,] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.None, true);
pivotTable.CalculateData();

workbook.Save("output_none.xlsx");
```

## **Escenario 3 — Subconjunto personalizado de subtotales (Sum + Average)**

No se limita a un único tipo de subtotal. Cada llamada a `SetSubtotals` opera de forma independiente sobre un tipo, por lo que llamar al método dos veces — una con `Sum` y otra con `Average` — produce un subconjunto personalizado de dos filas de subtotal para cada grupo `Category`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells["A1"].PutValue("Category");
worksheet.Cells["B1"].PutValue("Item");
worksheet.Cells["C1"].PutValue("Year");
worksheet.Cells["D1"].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

PivotTableCollection pivotTables = worksheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Sum, true);
categoryField.SetSubtotals(PivotFieldSubtotalType.Average, true);

pivotTable.CalculateData();

workbook.Save("output_custom.xlsx");
```

## **Resumen**

Los tres escenarios anteriores comparten el mismo conjunto de datos y la misma estructura de tabla dinámica. La única diferencia entre ellos es la llamada a `SetSubtotals` aplicada al campo de fila `Category` externo. Recuerde la regla de los dos campos: un solo campo en una región no tiene nada entre lo que calcular un subtotal, así que coloque siempre al menos dos campos en la región de fila o de columna cuando desee que `SetSubtotals` tenga un efecto visible.

## **Artículos relacionados**

- [Campos de página en tablas dinámicas](/cells/es/net/add-page-field-in-pivot-table/)
- [Actualizar tablas dinámicas en Aspose.Cells for .NET](/cells/es/net/refresh-pivot-table/)
- [Aplicar estilos a las tablas dinámicas](/cells/es/net/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
