---
title: Agregar campos de fila y columna en una tabla dinámica en Aspose.Cells for .NET
description: Aprenda cómo agregar campos de fila y columna a una tabla dinámica y controlar los subtotales de los campos dinámicos usando PivotField.SetSubtotals con PivotFieldSubtotalType en Aspose.Cells for .NET.
linktitle: Campos de fila y columna
keywords: Aspose.Cells, .NET, tabla dinámica, campo de fila, campo de columna, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotales, C#, tabla dinámica de Excel
type: docs
weight: 220
url: /es/net/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Agregar un campo a la región de filas o columnas**
El método `PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` mueve un campo base desde los datos de origen hacia una de las cuatro regiones de la tabla dinámica. El argumento `fieldType` acepta uno de los siguientes valores de `PivotFieldType`.
- `Row` — campos colocados verticalmente a la izquierda
- `Column` — campos colocados horizontalmente en la parte superior
- `Data` — campos cuyos valores se agregan
- `Page` — campos utilizados como filtros del informe
El orden de anidación de los campos es importante. Si agrega `Category` a la región de filas primero y luego `Item`, obtendrá una tabla dinámica cuya agrupación externa es `Category` y cuya agrupación interna es `Item`. Si invierte el orden, se invierte la jerarquía.

## **Subtotales de campos dinámicos**
El método `PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` controla qué filas de subtotal aparecen para un campo dinámico. Cada llamada activa o desactiva un único tipo de subtotal de forma independiente. Pasar `shown = true` muestra el subtotal, mientras que `shown = false` lo oculta. Dado que cada llamada solo afecta a un tipo, llamar al método varias veces con diferentes valores de `subtotalType` permite construir un subconjunto personalizado de subtotales.
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
Los subtotales solo se representan cuando hay dos o más campos dinámicos en la región de filas (o en la región de columnas). Un solo campo no tiene nada significativo entre lo que subtotalizar, por lo que las llamadas a `SetSubtotals` no tienen ningún efecto visible en ese caso. Por ello, este artículo coloca dos campos de fila (`Category` externo, `Item` interno) en cada ejemplo para que el límite de subtotal entre cada grupo de `Category` sea visible.
{{% /alert %}}

## **Escenario 1 — Subtotales automáticos (predeterminados)**
Si no llama en absoluto a `SetSubtotals`, Aspose.Cells aplica la selección `Automatic` a los campos numéricos. El siguiente ejemplo confirma explícitamente este comportamiento llamando a `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` en el campo de fila externo `Category`.

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
PivotTable pivotTable = worksheet.PivotTables.Add("A1:D9", 2, 5);
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
Llamar a `SetSubtotals(PivotFieldSubtotalType.None, true)` elimina todas las filas de subtotal de la tabla dinámica, dejando solo las filas de los campos y el total general en la parte inferior. Esto resulta útil cuando se desea obtener los datos agrupados sin filas de resumen.

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
PivotTable pivotTable = worksheet.PivotTables.Add("A1:D9", 2, 5);
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
No está limitado a un solo tipo de subtotal. Cada llamada a `SetSubtotals` opera de forma independiente sobre un tipo, por lo que llamar al método dos veces — una con `Sum` y otra con `Average` — produce un subconjunto personalizado de dos filas de subtotal para cada grupo de `Category`.

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
PivotTable pivotTable = pivotTables.Add("A1:D9", 2, 5);
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
Los tres escenarios difieren únicamente en las llamadas a `SetSubtotals`. Todo lo demás —el conjunto de datos, los campos y las áreas a las que se asignan— es idéntico, lo que permite una comparación directa entre los diseños.
- **Colocación de campos.** `PivotTable.AddFieldToArea(PivotFieldType.Row, fieldName)` mueve una columna de origen a una región. Dentro de una misma región, el orden de las llamadas determina el orden de visualización; por lo tanto, la primera llamada genera el grupo más externo. Para calcular subtotales se requieren dos o más campos en la misma región: con un único campo no existe ningún elemento entre los grupos sobre el cual calcular el subtotal.
- **Escenario 1 — subtotales automáticos.** Si se omite la llamada a `SetSubtotals`, Excel decide automáticamente aplicar su subtotal predeterminado a los campos numéricos. Llamar a `SetSubtotals` con `PivotFieldSubtotalType.Automatic` registra explícitamente dicha decisión, en lugar de dejarla implícita.
- **Escenario 2 — sin subtotales.** `SetSubtotals` con `PivotFieldSubtotalType.None` desactiva el subtotal predeterminado, de modo que la tabla dinámica conserva las filas de campos y el total general, pero omite las filas de subtotal que de otro modo Excel insertaría entre ellas.
- **Escenario 3 — un subconjunto seleccionado.** Cada llamada activa o desactiva exactamente un tipo de subtotal, y las llamadas se acumulan en lugar de anularse mutuamente. Por lo tanto, llamarlo una vez con `PivotFieldSubtotalType.Sum` y otra vez con `PivotFieldSubtotalType.Average` deja ambos habilitados, y la tabla dinámica muestra un subtotal de `Sum`, un subtotal de `Average` y el total general.

{{% alert color="primary" %}}
Nada en lo relativo a los subtotales es específico de la región de fila. Las mismas llamadas a `SetSubtotals` aplicadas a un campo obtenido de `PivotTable.ColumnFields` producen los mismos tres diseños en el eje de columna, puesto que la configuración pertenece al campo dinámico y no al eje en el que se ubica.
{{% /alert %}}

## **Artículos relacionados**
- [Campos de página en tablas dinámicas](/cells/es/net/add-page-field-in-pivot-table/)
- [Actualizar tablas dinámicas en Aspose.Cells for .NET](/cells/es/net/refresh-pivot-table/)
- [Aplicar estilos a las tablas dinámicas](/cells/es/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}