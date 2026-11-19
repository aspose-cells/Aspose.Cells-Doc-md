---
title: Aplicar estilos a tablas dinámicas en Aspose.Cells for .NET
description: Aprenda a aplicar estilos predefinidos y personalizados a tablas dinámicas en Aspose.Cells for .NET, incluyendo autoformatos XLS heredados, estilos con nombre de Excel 2007+, estilos personalizados de tabla dinámica y el atajo FormatAll.
linktitle: Aplicar estilos a tablas dinámicas
keywords: Aspose.Cells .NET tabla dinámica estilo, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la aplicación tanto de autoformatos heredados de tablas dinámicas (diseñados para archivos `.xls`) como de estilos modernos con nombre o personalizados (diseñados para archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe llamar depende del formato de archivo en el que se guarda el libro, no del formato desde el que se cargó.
{{% /alert %}}

## **Introducción**
Aspose.Cells expone dos API de estilos paralelas para tablas dinámicas. La decisión entre ellas depende del formato de archivo en el que guarde el libro, no del formato desde el que lo lea. Un libro cargado desde un archivo `.xls` puede volver a guardarse como `.xlsx`, y en ese caso se aplica la API de estilos moderna en lugar de la heredada.
- `PivotTable.PivotTableStyleType` selecciona uno de los estilos con nombre predefinidos (temas claros y oscuros, incluidos los estilos añadidos en Excel 2017). Estos preajustes son de solo lectura.
- `PivotTable.PivotTableStyleName` selecciona un estilo personalizado que defina usted mismo mediante `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Los estilos personalizados son necesarios siempre que quiera modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.
Además, `PivotTable.FormatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, anulando todo lo establecido mediante cualquiera de las API de nombre de estilo anteriores. Esto resulta útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato predefinido XLS heredado**
`PivotTable.AutoFormatType` acepta un valor de la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Los valores disponibles son `Report1` a `Report10`, `Classic` y `Table1` a `Table10`.
El siguiente ejemplo carga un libro nuevo, rellena los datos de muestra de Fruta/Año/Cantidad, añade una tabla dinámica, aplica `PivotTableAutoFormatType.Report5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}
**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas de una sola dimensión** con campos de fila y valores únicamente — no tienen un estilo integrado para encabezados de campos de columna. Si su tabla dinámica necesita campos de columna, utilice en su lugar los preajustes modernos `PivotTableStyleType` del [Escenario 2](#apply-a-modern-named-preset-pivot-table-style), que están diseñados para la distribución bidimensional que utiliza el Excel moderno.
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scenario 1: Apply a legacy XLS preset autoformat
// API in use: PivotTable.AutoFormatType
// Target file format: .xls (legacy)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Create a new workbook
Workbook workbook = new Workbook();
// Get the first worksheet
Worksheet sheet = workbook.Worksheets[0];
// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.Cells[0, 0].PutValue("Fruit");
sheet.Cells[0, 1].PutValue("Year");
sheet.Cells[0, 2].PutValue("Amount");
sheet.Cells[1, 0].PutValue("grape");
sheet.Cells[1, 1].PutValue(2020);
sheet.Cells[1, 2].PutValue(50);
sheet.Cells[2, 0].PutValue("blueberry");
sheet.Cells[2, 1].PutValue(2020);
sheet.Cells[2, 2].PutValue(30);
sheet.Cells[3, 0].PutValue("kiwi");
sheet.Cells[3, 1].PutValue(2020);
sheet.Cells[3, 2].PutValue(25);
sheet.Cells[4, 0].PutValue("cherry");
sheet.Cells[4, 1].PutValue(2020);
sheet.Cells[4, 2].PutValue(40);
sheet.Cells[5, 0].PutValue("grape");
sheet.Cells[5, 1].PutValue(2021);
sheet.Cells[5, 2].PutValue(60);
sheet.Cells[6, 0].PutValue("blueberry");
sheet.Cells[6, 1].PutValue(2021);
sheet.Cells[6, 2].PutValue(35);
sheet.Cells[7, 0].PutValue("kiwi");
sheet.Cells[7, 1].PutValue(2021);
sheet.Cells[7, 2].PutValue(28);
sheet.Cells[8, 0].PutValue("cherry");
sheet.Cells[8, 1].PutValue(2021);
sheet.Cells[8, 2].PutValue(45);
sheet.Cells[9, 0].PutValue("grape");
sheet.Cells[9, 1].PutValue(2020);
sheet.Cells[9, 2].PutValue(45);
// Add a pivot table at destination cell E3, using source range A1:C10
PivotTable pivotTable = sheet.PivotTables.Add("A1:C10", 2, 4);
// Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;
// Save the workbook in legacy .xls format
workbook.Save("output.xls");
```

## **Aplicar un estilo de tabla dinámica predefinido con nombre moderno**
`PivotTable.PivotTableStyleType` selecciona uno de los estilos integrados con nombre que Excel 2007 introdujo para las tablas dinámicas. La enumeración `PivotTableStyleType` expone tres familias de temas: la familia clara, desde `PivotTableStyleLight1` hasta `PivotTableStyleLight28`; la familia media, desde `PivotTableStyleMedium1` hasta `PivotTableStyleMedium28`; y la familia oscura, desde `PivotTableStyleDark1` hasta `PivotTableStyleDark28`. También define `None` y `Custom`. Los miembros de mayor número dentro de cada familia corresponden a los estilos añadidos en Excel 2017.
Estas predefiniciones son de solo lectura. En cuanto necesite modificar colores, bordes o fuentes más allá de lo que una predefinición ofrece, deberá definir un estilo de tabla dinámica personalizado, como se muestra en el [Escenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**¿Por qué usar las predefiniciones modernas en lugar de los autoformateos de la serie Report?** Los valores `Report1` hasta `Report10` y `Table1` hasta `Table10` de `PivotTableAutoFormatType` son anteriores a los campos de columna en tablas dinámicas, por lo que no incluyen estilos para las cabeceras de los campos de columna, y Excel renderiza dichas cabeceras sin formato. Las predefiniciones `PivotTableStyleType` fueron diseñadas para el diseño bidimensional que utiliza la versión moderna de Excel y aplica estilo tanto a las cabeceras de los campos de fila como a las de los campos de columna.
{{% /alert %}}

Este escenario reutiliza el conjunto de datos Fruta/Año/Cantidad del Escenario 1, agrega `Year` al área de columnas junto con el campo de fila `Fruit` mediante `PivotFieldType.Column`, aplica la predefinición de tema oscuro `PivotTableStyleDark1` con `PivotTable.PivotTableStyleType` y guarda el resultado como `.xlsx` —el formato para el cual `PivotTableStyleType` tiene significado.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
// Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
// (not in Aspose.Cells.Pivot) -- that is why we do not need any extra using for it.
// GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Header row: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// 9 data rows of Fruit / Year / Amount
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(150);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(180);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(120);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(170);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(210);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(190);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(130);
// Add a pivot table at E3, sourced from A1:C10
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.Save("output.xlsx");
```

## **Definir y aplicar un estilo de tabla dinámica personalizado**
Los preajustes integrados no se pueden modificar. Siempre que necesite anular colores, bordes o fuentes, debe definir un estilo de tabla dinámica personalizado. El flujo de trabajo consta de tres pasos:
1. Añada un estilo personalizado a la colección `TableStyles` del libro mediante `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WholeTable` o `GrandTotalRow`) mediante `TableStyle.TableStyleElements.Add(TableStyleElementType)` y, a continuación, asigne un `Style` a cada elemento mediante `TableStyleElement.SetElementStyle(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica asignando a `PivotTable.PivotTableStyleName` el nombre del estilo. No utilice aquí `PivotTableStyleType`, ya que esa propiedad selecciona los preajustes integrados.

{{% alert color="primary" %}}
`PivotTableStyleName` y `PivotTableStyleType` no son intercambiables. Utilice `PivotTableStyleType` para los preajustes integrados y `PivotTableStyleName` para los estilos personalizados que haya definido mediante `AddPivotTableStyle`. Establecer ambos es inofensivo, pero solo se representa el que coincide con el origen previsto.
Los valores disponibles de `TableStyleElementType` incluyen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` y `PageFieldValues`.
El siguiente ejemplo define un estilo de tabla dinámica personalizado con un borde negro fino en `WholeTable` y una fuente roja en negrita en `GrandTotalRow`, luego lo aplica mediante `PivotTableStyleName` y guarda como `.xlsx`.
{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using System.Drawing;
using Aspose.Cells.Tables;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Populate source data: header row + 9 data rows (A1:C10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);
// Add pivot table sourced from A1:C10, anchored at E3
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Step 1: register a new custom pivot table style and capture its index
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];
// Step 2: add a WholeTable element and apply thin black borders on all four sides
int wholeTableElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.WholeTable);
TableStyleElement wholeTableElement = tableStyle.TableStyleElements[wholeTableElementIndex];
Style wholeTableStyle = workbook.CreateStyle();
wholeTableStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.TopBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.BottomBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.LeftBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.RightBorder].Color = Color.Black;
wholeTableElement.SetElementStyle(wholeTableStyle);
// Step 3: add a GrandTotalRow element and apply bold red font
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);
// Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.PivotTableStyleName = "CustomPivotStyle";
workbook.Save("output.xlsx");
```

## **Aplicar un único estilo a cada celda de la tabla dinámica con FormatAll**
`PivotTable.FormatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluido el área de datos, los encabezados de filas y columnas y los totales. Lo que se haya establecido previamente mediante `PivotTableStyleType` o `PivotTableStyleName` se anula.

{{% alert color="primary" %}}
`FormatAll` anula tanto `PivotTableStyleType` como `PivotTableStyleName`. Utilícelo únicamente cuando se requiera una apariencia uniforme e independiente del tema en toda la tabla dinámica.
El siguiente ejemplo crea un `Style` con un relleno sólido amarillo, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, luego lo aplica con `FormatAll` y guarda como `.xlsx`.
{{% /alert %}}

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Scenario 4: Apply a single Style to every pivot table cell using FormatAll
// API in use: PivotTable.FormatAll(Style)
// Target format: .xlsx
// GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(5000);
worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(3000);
worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(4000);
worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(2000);
worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(6000);
worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(3500);
worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(4500);
worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(2500);
worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(5500);
// Add pivot table: source range A1:C10, destination cell E3
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Build a Style that will be forced onto every cell of the pivot table
Style style = workbook.CreateStyle();
style.ForegroundColor = Color.Yellow;
style.Pattern = BackgroundType.Solid;
style.Font.IsBold = true;
style.Font.Color = Color.DarkBlue;
style.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.TopBorder].Color = Color.Black;
style.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.BottomBorder].Color = Color.Black;
style.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.LeftBorder].Color = Color.Black;
style.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.RightBorder].Color = Color.Black;
// Apply FormatAll: forces this single style onto every cell of the pivot table,
// overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.FormatAll(style);
// Save the workbook in the modern .xlsx format
workbook.Save("output.xlsx");
```

## **¿Qué API de estilo debo usar?**
La elección de la API de estilo depende del formato de archivo en el que está guardando. Utilice la tabla siguiente como referencia rápida.
| Formato de archivo de destino | API a utilizar | Notas |
|---|---|---|
| `.xls` (heredado) | `PivotTable.AutoFormatType` | Valores de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (por ejemplo, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `PivotTable.PivotTableStyleType` | Valores de `Aspose.Cells.PivotTableStyleType` (temas claros/oscuros, incluidas las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Úselo cuando los preajustes integrados no sean suficientes. Configure mediante `TableStyleElement.SetElementStyle(...)`. |
| Cualquier formato (anulación uniforme) | `PivotTable.FormatAll(Style)` | Atajo que anula cualquier otro ajuste de estilo en toda la tabla dinámica. |
En caso de duda, guarde como `.xlsx` y utilice `PivotTableStyleType` para los temas integrados, o `PivotTableStyleName` para los temas personalizados.

## Artículos relacionados
- [Add Pivot Table Row and Column Fields in Aspose.Cells for .NET](/cells/es/net/pivot-table-add-row-and-column-fields/)
- [Manage Pivot Table Value Fields in Aspose.Cells for .NET](/cells/es/net/manage-value-fields/)
- [Refreshing Pivot Tables in Aspose.Cells for .NET](/cells/es/net/refresh-pivot-table/)csharp

{{< app/cells/assistant language="csharp" >}}