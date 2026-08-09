---
title: Administrar campos de valor de una tabla dinámica en Aspose.Cells para .NET
linktitle: Campos de valor
description: Aprenda a agregar campos base a la región de datos de una tabla dinámica, cambiar la función de resumen con PivotField.Function y representar el campo de valor en el eje de fila o columna en Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET, tabla dinámica, campo de valor, PivotField, PivotField.Function, campo de datos, PivotTable.ValuesField, Suma, Promedio
type: docs
weight: 230
url: /es/net/manage-value-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Agregar un campo a la región de datos

Agregar un campo base a la región de datos (valor) es el primer paso para dar forma a cómo una tabla dinámica agrega los datos de origen. Aspose.Cells expone `PivotTable.AddFieldToArea(PivotFieldType, string)`, una sobrecarga que acepta la constante `PivotFieldType.Data` y el nombre de la columna de origen. Una vez que se agrega un campo a la región de datos, la API lo expone a través de la colección `PivotTable.DataFields`, en el orden en que se agregaron los campos. Por defecto, una columna de origen numérica se resume con `ConsolidationFunction.Sum`, mientras que una columna no numérica toma por defecto `Count`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// Encabezados en A1:D1
worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

// Filas de datos A2:D9 usando bucles anidados que se ramifican en j
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 worksheet.Cells[i, j].PutValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.Cells[i, j].PutValue("Apple");
 else if (i == 3 || i == 4) worksheet.Cells[i, j].PutValue("Banana");
 else if (i == 5 || i == 6) worksheet.Cells[i, j].PutValue("Carrot");
 else worksheet.Cells[i, j].PutValue("Daikon");
 break;
 case 2:
 worksheet.Cells[i, j].PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.Cells[i, j].PutValue(100);
 else if (i == 2) worksheet.Cells[i, j].PutValue(150);
 else if (i == 3) worksheet.Cells[i, j].PutValue(80);
 else if (i == 4) worksheet.Cells[i, j].PutValue(90);
 else if (i == 5) worksheet.Cells[i, j].PutValue(50);
 else if (i == 6) worksheet.Cells[i, j].PutValue(60);
 else if (i == 7) worksheet.Cells[i, j].PutValue(40);
 else worksheet.Cells[i, j].PutValue(45);
 break;
 }
 }
}

// Agregar tabla dinámica en F3 con el nombre PivotTable1
int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Diseño de la tabla dinámica: Categoría e Ítem en Fila, Año en Columna, Monto como campo de datos
pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.CalculateData();
workbook.Save("output_drag.xlsx");
```

## Cambiar la función de resumen

Cada campo colocado en la región de datos se envuelve internamente como una instancia de `PivotField`, y su propiedad `Function` devuelve un valor de la enumeración `ConsolidationFunction`. El mismo setter de `Function` le permite cambiar entre los agregados disponibles, incluidos `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` y `Varp`.

{{% alert color="primary" %}}
Cambiar `Function` solo afecta al agregado, la columna de origen no cambia.
{{% /alert %}}

Por lo tanto, puede dejar un campo de datos como `Sum` mientras agrega un segundo campo de datos que apunte a la misma columna de origen pero que use `Count` o `Average`, todo en una sola tabla dinámica.

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

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0)
 {
 worksheet.Cells[i, j].PutValue(i <= 5 ? "Fruit" : "Vegetable");
 }
 else if (j == 1)
 {
 string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
 worksheet.Cells[i, j].PutValue(items[i - 1]);
 }
 else if (j == 2)
 {
 int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
 worksheet.Cells[i, j].PutValue(years[i - 1]);
 }
 else
 {
 int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };
 worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");

pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField countField = pivotTable.DataFields[1];
countField.Function = ConsolidationFunction.Count;

pivotTable.CalculateData();

workbook.Save("output_function.xlsx");
```

## Representar campos de valor en el eje de fila o columna

Cuando una tabla dinámica contiene dos o más campos de datos, Aspose.Cells expone un campo virtual adicional llamado `PivotTable.ValuesField`. Este campo virtual representa el agregado de cada campo de datos que se encuentra en la región de datos. Puede arrastrarlo a la región de fila o columna como un campo dinámico base, lo que resulta útil para disponer varias medidas una al lado de la otra.

{{% alert color="primary" %}}
`PivotTable.ValuesField` no funciona si no hay ningún campo de valor o si solo hay uno.
{{% /alert %}}

Los escenarios a continuación recorren tres ejemplos completos que demuestran cada capacidad descrita anteriormente sobre la misma estructura de tabla dinámica.

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

string[] categories = { "Fruit", "Fruit", "Fruit", "Fruit", "Vegetable", "Vegetable", "Vegetable", "Vegetable" };
string[] items = { "Apple", "Apple", "Banana", "Banana", "Carrot", "Carrot", "Daikon", "Daikon" };
int[] years = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
int[] amounts = { 100, 150, 80, 90, 50, 60, 40, 45 };

for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j <= 3; j++)
 {
 if (j == 0) worksheet.Cells[i, j].PutValue(categories[i - 1]);
 else if (j == 1) worksheet.Cells[i, j].PutValue(items[i - 1]);
 else if (j == 2) worksheet.Cells[i, j].PutValue(years[i - 1]);
 else worksheet.Cells[i, j].PutValue(amounts[i - 1]);
 }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

pivotTable.DataFields[1].Function = ConsolidationFunction.Count;

pivotTable.AddFieldToArea(PivotFieldType.Column, pivotTable.ValuesField.Name);

pivotTable.CalculateData();
workbook.Save("output_plot.xlsx");
```

{{< app/cells/assistant language="csharp" >}}