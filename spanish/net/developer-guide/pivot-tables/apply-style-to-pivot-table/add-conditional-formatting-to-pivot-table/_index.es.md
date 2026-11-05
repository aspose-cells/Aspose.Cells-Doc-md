---
title: Agregar formato condicional a una Tabla Dinámica
linktitle: Agregar formato condicional a una Tabla Dinámica
description: Agregar formato condicional a una tabla dinámica en Aspose.Cells for .NET, anclar una regla a la región de datos con ApplyTo y un alcance PivotConditionFormatScopeType, o definir el objetivo con AddCellArea y PivotAreas, luego adjuntar reglas y estilos mediante FormatConditions.AddCondition.
keywords: Aspose.Cells, tabla dinámica, formato condicional, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C#
type: docs
weight: 30
url: /es/net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Escenarios de uso posibles**
Los estilos descritos en la página principal y en la página hermana son estáticos: una región `PivotArea` o `CellArea` se pinta una sola vez y mantiene su estilo sin importar los valores. **El formato condicional es la contraparte basada en reglas**: resaltar cada monto superior a 200, sombrear el cincuenta por ciento intermedio o marcar los elementos con menor rango, y el resaltado sigue a los valores siempre que la tabla dinámica se recalcula o actualiza.  
En Aspose.Cells, el formato condicional de una tabla dinámica reside en la colección `PivotTable.ConditionalFormats`. Cada entrada es un `PivotConditionalFormat` que responde a dos preguntas de forma independiente:
- **¿Dónde se aplica la regla?** La región objetivo se define ya sea mediante `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)`, que replica el selector de alcance de la interfaz de usuario de Excel, o mediante `AddCellArea(CellArea)` y la colección `PivotAreas`, que nombran la región de forma explícita.
- **¿Qué evalúa la regla?** Una o más condiciones se añaden a `FormatConditions` con `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)`, y cada condición lleva su propio `Style`.

{{% alert color="primary" %}}
No llame a `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` o `FormatConditionCollection.AddArea(CellArea)` en el objeto `FormatConditions` de un formato condicional de tabla dinámica. Estas dos sobrecargas se heredan de la API de formato condicional de hoja de cálculo ordinaria y no funcionan para tablas dinámicas: la zona de celdas nunca se convierte en una zona de pivote, por lo que la solicitud se ignora silenciosamente. Siempre defina la región en el propio `PivotConditionalFormat` (`ApplyTo`, `AddCellArea` o `PivotAreas`) y añada la regla con una de las sobrecargas de `AddCondition`.
{{% /alert %}}

## **Aplicar una regla con un alcance (modo de la interfaz de Excel)**
La primera forma posiciona la regla como lo hace la interfaz de usuario de Excel. Una celda de la tabla dinámica se nombra mediante sus coordenadas de hoja de cálculo basadas en cero, y un alcance `PivotConditionFormatScopeType` le indica an Aspose.Cells hasta dónde debe extenderse la regla desde esa celda:
- `PivotConditionFormatScopeType.Data` - todas las celdas de valores que produce la tabla dinámica, incluidos los totales generales.
- `PivotConditionFormatScopeType.Field` - las celdas de valores que pertenecen al campo que identifica la celda, excluyendo los totales generales. La celda debe ser una celda de campo, como una etiqueta de campo de fila; pasar una celda de valor genera una excepción.
- `PivotConditionFormatScopeType.Selection` - solo las celdas de valores en la intersección que la celda selecciona, típicamente una única celda de valor.  
El siguiente ejemplo crea una tabla dinámica de ventas de frutas cuya esquina superior izquierda está en E3, ancla un formato condicional en la celda F4 (fila 3, columna 5) con el alcance `Data`, y resalta cada monto mayor a 200 en blanco, en negrita, sobre rojo. Con los valores Manzana 220, Plátano 330, Cereza 200 y el total general 750, la regla colorea F4, F5 y F7; la región resultante es toda la columna de datos F4:F7, y solo las celdas cuyo valor cumple la regla se iluminan.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
// Tabla dinámica con su esquina superior izquierda en E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Anclar el formato condicional en F4 (fila 3, columna 5) con el alcance de Datos
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.ApplyTo(3, 5, PivotConditionFormatScopeType.Data);
// Regla - resaltar los montos mayores que 200
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
Style style = workbook.CreateStyle();
style.Font.IsBold = true;
style.Font.Color = Color.White;
style.ForegroundColor = Color.Red;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatData.xlsx");
```

Anclar la misma regla en la etiqueta de campo de fila E4 (fila 3, columna 4) con el alcance `Field` se resuelve en F4:F6 en su lugar—la misma columna de datos sin la fila de total general—porque el alcance ahora describe el campo `Fruit` en lugar de todo el área de valores. El alcance `Selection` anclado en F4 se resuelve solo en F4.

## **Definir la región manualmente**
La segunda forma omite el selector de alcance y nombra la región de forma explícita en el `PivotConditionalFormat`.

### **Un rectángulo de hoja de cálculo con AddCellArea**
`AddCellArea(CellArea)` registra el rectángulo proporcionado como objetivo de la regla. Las coordenadas son coordenadas de hoja de cálculo basadas en cero, y la región es exactamente el rectángulo suministrado —sin expansión a la columna de datos y sin lógica de total general. Úselo cuando las celdas de interés forman un rectángulo fijo conocido del diseño actual de la tabla dinámica.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Apuntar al rectángulo F4:F6 (las celdas de valor sin el total general)
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.AddCellArea(new CellArea { StartRow = 3, StartColumn = 5, EndRow = 5, EndColumn = 5 });
// Regla - cursiva en amarillo claro para montos entre 150 y 300
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.Between, "150", "300");
Style style = workbook.CreateStyle();
style.Font.IsItalic = true;
style.ForegroundColor = Color.LightYellow;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatCellArea.xlsx");
```

### **Una región semántica de pivote con PivotAreas**
`PivotAreas` es el mismo modelo de región semántica que la página hermana utiliza para estilos estáticos. Construya un `PivotArea`, seleccione un campo o región con `Select` o `SelectField`, y añádalo con `PivotAreas.AddPivotArea(PivotArea)`. Una región semántica permanece adjunta a su campo, por lo que el formato condicional sigue al campo cuando la tabla dinámica se actualiza y el diseño cambia. La sobrecarga `PivotAreas.Add(PivotArea)` todavía compila pero está marcada como obsoleta —prefiera `AddPivotArea`.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Adjuntar la regla al campo de datos Amount como una región semántica
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
PivotArea area = new PivotArea(pivotTable);
area.SelectField(PivotFieldType.Data, "Amount");
format.PivotAreas.AddPivotArea(area);
// Regla - texto gris para cantidades menores a 150
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
Style style = workbook.CreateStyle();
style.Font.Color = Color.Gray;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatPivotArea.xlsx");
```

## **Dónde se almacenan las reglas y cómo sobreviven a una recarga**
Cada llamada a `ConditionalFormats.Add()` agrega un `PivotConditionalFormat` a la tabla dinámica. Las condiciones, sus fórmulas y sus estilos se guardan con el libro de trabajo; volver a abrir el archivo en el ejemplo a continuación muestra la misma regla con su tipo, operador y fórmula intactos, y `GetCellAreas()` informa las mismas regiones. Las entradas que nunca recibieron una condición se eliminan al guardar el libro de trabajo, de la misma forma que Excel descarta un formato condicional sin regla.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
Console.WriteLine("Conditional formats: " + pivotTable.ConditionalFormats.Count);
for (int i = 0; i < pivotTable.ConditionalFormats.Count; i++)
{
    PivotConditionalFormat format = pivotTable.ConditionalFormats[i];
    for (int j = 0; j < format.FormatConditions.Count; j++)
    {
        FormatCondition condition = format.FormatConditions[j];
        Console.WriteLine($"Format {i}: {condition.Type} {condition.Operator} formula1={condition.Formula1}");
    }
    foreach (CellArea area in format.GetCellAreas())
        Console.WriteLine($"    rows {area.StartRow + 1}-{area.EndRow + 1}, columns {area.StartColumn + 1}-{area.EndColumn + 1}");
}
// Esto imprime:
// Conditional formats: 1
// Format 0: CellValue GreaterThan formula1==200
//     rows 4-7, columns 6-6        (F4:F7, the resolved data region)
```

## **Artículos relacionados**
- [Aplicar estilo a la tabla dinámica](/cells/es/net/apply-style-to-pivot-table/)
- [Formatear parte de la tabla dinámica](/cells/es/net/format-part-of-pivot-table/)
- [Top 10 mostrar o filtrar en tabla dinámica](/cells/es/net/top-10-show-or-filter-in-pivot-table/)
- [Filtrar tablas dinámicas por etiqueta o valor](/cells/es/net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="csharp" >}}