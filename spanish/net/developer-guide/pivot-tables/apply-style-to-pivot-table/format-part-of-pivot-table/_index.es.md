---
title: Formatear parte de una Tabla Dinámica
description: Formatear parte de una tabla dinámica en Aspose.Cells for .NET aplicando estilos a regiones semánticas PivotArea o rectángulos CellArea mediante PivotTable.Format, con formatos almacenados en PivotTable.PivotFormats y preservados cuando se actualiza la tabla dinámica.
linktitle: Format Part of a Pivot Table
keywords: Aspose.Cells, tabla dinámica, formato, PivotArea, CellArea, PivotTable.Format, PivotFormats, PivotTableSelectionType, LabelOnly, DataOnly, SelectField, FormatAll, C#
type: docs
weight: 20
url: /es/net/format-part-of-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Posibles escenarios de uso**
`PivotTable.FormatAll` aplica un único estilo a toda la tabla dinámica y está cubierto en la página principal. No distingue entre etiquetas, valores, totales ni regiones específicas del informe.  
En la práctica, solo una parte de una tabla dinámica suele necesitar resaltarse. Los objetivos habituales incluyen las etiquetas que pertenecen a un campo de fila, las celdas de valor generadas por un campo, la fila de total general, o un rectángulo arbitrario como las dos primeras filas de elementos.  
La aplicación de un estilo directamente a las celdas de la hoja de cálculo de una tabla dinámica no es equivalente. Excel almacena el formato de la tabla dinámica como regiones semánticas `PivotArea` en lugar de como registros de estilo de celda ordinarios. Un formato de `PivotArea` permanece asociado a una región, como las etiquetas de un campo o los valores de datos, y se vuelve a resolver cuando la tabla dinámica se recalcula, se actualiza o se expande. Por otro lado, un estilo escrito directamente en una celda pertenece a esa posición de celda y no es rastreado por el modelo de tabla dinámica.  
Aspose.Cells expone la familia completa de sobrecargas de `PivotTable.Format` para que estén disponibles ambos tipos de formato:
- `Format(PivotArea, Style)` ancla un estilo a una región semántica que se construye con `PivotArea.Select` o `PivotArea.SelectField`.
- `Format(CellArea, Style)` ancla un estilo a un rectángulo de hoja de cálculo dentro de la tabla dinámica.
- `Format(int row, int column, Style)` dirige el formato a una celda.
- `FormatAll(Style)` formatea toda la tabla dinámica.

## **Formatear un Área Pivot**
El flujo de trabajo basado en áreas semánticas es el enfoque recomendado cuando un resaltado debe seguir a un campo o a una región del informe.
1. Cree un `PivotArea` con `new PivotArea(pivotTable)`. El objeto describe una región semántica que pertenece a esa tabla dinámica específica.
1. Seleccione un campo por su posición basada en cero en un eje dado con `PivotArea.Select(PivotFieldType axisType, int fieldPosition, PivotTableSelectionType selectionType)`.
   - `PivotTableSelectionType.DataAndLabel` selecciona tanto las etiquetas como los datos del campo.
   - `PivotTableSelectionType.LabelOnly` selecciona solo las etiquetas del campo.
   - `PivotTableSelectionType.DataOnly` selecciona solo las celdas de datos del campo.
1. Seleccione un campo por nombre con `PivotArea.SelectField(PivotFieldType axisType, string fieldName)`. Cuando se selecciona un campo de fila por nombre, la región se resuelve en las celdas de valor producidas por los elementos de ese campo.
1. Cree un `Style` con `Workbook.CreateStyle()`, configure su fuente, color de primer plano y patrón de fondo sólido, y pase el estilo a `PivotTable.Format(area, style)`.
1. Cada llamada a la sobrecarga `PivotArea` agrega una entrada `PivotTableFormat` a `PivotTable.PivotFormats`.
1. Los formatos anclados a campos se aplican cuando se calculan los datos de la tabla dinámica. Por lo tanto, llame a `PivotTable.CalculateData()` después de aplicar los formatos para que los estilos sean visibles.  
El siguiente ejemplo crea una pequeña tabla dinámica de ventas de frutas, aplica estilo a las etiquetas de fila `Fruit` con `PivotArea.Select` y `PivotTableSelectionType.LabelOnly`, aplica estilo a las celdas de valor generadas por ese mismo campo de fila con `PivotArea.SelectField`, y luego recalcula la tabla dinámica para que ambos estilos se apliquen.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Fruit sales data
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
// Pivot table with its top-left corner at E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Bold yellow fill on the row field's label cells
Style labelStyle = workbook.CreateStyle();
labelStyle.Font.IsBold = true;
labelStyle.ForegroundColor = Color.Yellow;
labelStyle.Pattern = BackgroundType.Solid;
PivotArea labelArea = new PivotArea(pivotTable);
labelArea.Select(PivotFieldType.Row, 0, PivotTableSelectionType.LabelOnly);
pivotTable.Format(labelArea, labelStyle);
// Light green fill on the value cells the row field produces
Style valueStyle = workbook.CreateStyle();
valueStyle.ForegroundColor = Color.LightGreen;
valueStyle.Pattern = BackgroundType.Solid;
PivotArea valueArea = new PivotArea(pivotTable);
valueArea.SelectField(PivotFieldType.Row, "Fruit");
pivotTable.Format(valueArea, valueStyle);
// Field-anchored formats are painted when the data is calculated
pivotTable.CalculateData();
// Label cells E4:E6 are now bold on yellow, value cells F4:F6 are light green
workbook.Save("FormatPivotArea.xlsx");
```

## **Formatear un Área de Celdas de la Tabla Dinámica**
Utilice `PivotTable.Format(CellArea, Style)` cuando la región de interés sea un simple rectángulo de hoja de cálculo en lugar de una región pivot semántica.  
Un `CellArea` se describe mediante las propiedades `StartRow`, `StartColumn`, `EndRow` y `EndColumn`. Los valores son coordenadas de hoja de cálculo basadas en cero, y las coordenadas finales identifican la última fila y columna incluidas en el rectángulo, por lo que el área cubre las celdas desde la posición inicial hasta la posición final inclusive.  
A diferencia de un formato anclado a un campo, un formato `CellArea` se aplica a las celdas inmediatamente. No se necesita otra llamada a `CalculateData()` para que el estilo aparezca.  
Un rectángulo `CellArea` puede contener celdas de etiqueta y celdas de valor juntas. La siguiente sección describe cómo Aspose.Cells y Excel representan internamente ese rectángulo.  
El siguiente ejemplo formatea el rectángulo `E4:F5` de la tabla dinámica con un estilo cursiva, azul claro y guarda el libro de trabajo sin ninguna recalculación adicional.

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
// Highlight the first two fruit rows (the rectangle E4:F5)
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// E4:F5 is italic on light blue immediately, no recalculation needed
workbook.Save("FormatPivotCellArea.xlsx");
```

## **Cómo se asignan los Áreas Pivot y Cell Areas**
Excel almacena el formato de la tabla dinámica como registros `pivotArea` en lugar de registros de estilo de celda ordinarios. Aspose.Cells utiliza el mismo modelo, por lo que una solicitud de formato se traduce en áreas pivot cuando se registra.  
La relación entre el `CellArea` proporcionado por el usuario y las áreas pivot almacenadas internamente es de muchos a muchos en ambas direcciones.  
- Un `CellArea` puede generar varias áreas pivot. Si el rectángulo abarca tanto celdas de etiqueta como celdas de valor, se descompone en reglas separadas de etiqueta y datos, porque el modelo pivot trata el formato de etiquetas y el de datos de forma independiente.  
- Una área pivot puede resolverse en varias instancias `CellArea` disjuntas. Una región semántica como una fila de total general, o un campo cuyos elementos no son contiguos, puede cubrir múltiples rectángulos. Por eso `PivotArea.GetCellAreas()` devuelve una colección en lugar de un único rectángulo.  
Cada operación de formato realizada a través de `PivotTable.Format` se registra en `PivotTable.PivotFormats`. Cada entrada `PivotTableFormat` expone el `PivotArea` asociado y el `Style` que se le aplica. La sobrecarga `PivotArea` agrega exactamente una entrada por llamada, mientras que un `CellArea` que contiene diferentes regiones semánticas puede agregar múltiples entradas.  
Para distinguir las regiones almacenadas, cada `PivotArea` expone los indicadores `OnlyLabel` y `OnlyData`. El ejemplo a continuación formatea un único rectángulo que cubre tanto etiquetas como valores, inspecciona `PivotTable.PivotFormats` y muestra las coordenadas `CellArea` a las que se resuelve cada área pivot almacenada.

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
Style highlightStyle = workbook.CreateStyle();
highlightStyle.Font.IsItalic = true;
highlightStyle.ForegroundColor = Color.FromArgb(0xFF, 0x99, 0xCC, 0xFF);
highlightStyle.Pattern = BackgroundType.Solid;
// ONE rectangle in...
CellArea rectangle = new CellArea { StartRow = 3, StartColumn = 4, EndRow = 4, EndColumn = 5 };
pivotTable.Format(rectangle, highlightStyle);
// ...TWO semantic pivot areas out: the label part and the data part are stored separately
Console.WriteLine("Stored formats: " + pivotTable.PivotFormats.Count);
for (int i = 0; i < pivotTable.PivotFormats.Count; i++)
{
    PivotArea storedArea = pivotTable.PivotFormats[i].PivotArea;
    Console.WriteLine($"Format {i}: OnlyLabel={storedArea.OnlyLabel}, OnlyData={storedArea.OnlyData}");
    foreach (CellArea resolved in storedArea.GetCellAreas())
        Console.WriteLine($"    rows {resolved.StartRow + 1}-{resolved.EndRow + 1}, columns {resolved.StartColumn + 1}-{resolved.EndColumn + 1}");
}
// This prints:
// Stored formats: 2
// Format 0: OnlyLabel=True, OnlyData=False
//     rows 4-5, columns 5-5        (E4:E5, the label part)
// Format 1: OnlyLabel=False, OnlyData=True
//     rows 4-5, columns 6-6        (F4:F5, the data part)
workbook.Save("FormatPivotAreasMap.xlsx");
```

{{% alert color="primary" %}}
Porque los formatos se almacenan como áreas pivot en lugar de como estilos de celda ordinarios, sobreviven a la recalculación y actualización. Cuando la tabla dinámica se actualiza con `PivotTable.RefreshData`, se recalcula con `CalculateData`, o se guarda y se vuelve a cargar, cada área pivot almacenada se vuelve a resolver a la posición actual de su región y su estilo se vuelve a aplicar.
{{% /alert %}}

Utilice un `PivotArea` construido con `Select` o `SelectField` cuando un resaltado deba permanecer anclado a un campo o a una región semántica entre actualizaciones, y utilice un `CellArea` cuando sea suficiente formatear un rectángulo fijo en el diseño actual de la tabla dinámica. La sobrecarga de una sola celda `Format(int row, int column, Style)` dirige el formato a una celda individual. Use `FormatAll`, cubierto en la página principal, cuando toda la tabla dinámica deba restilizarse de una vez.

## **Artículos relacionados**
- [Aplicar estilo a tabla dinámica](/cells/es/net/apply-style-to-pivot-table/)
- [Agregar campos de fila y columna a la tabla dinámica](/cells/es/net/pivot-table-add-row-and-column-fields/)
- [Administrar campos de valor en la tabla dinámica](/cells/es/net/manage-value-fields/)
- [Actualizar tabla dinámica](/cells/es/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}