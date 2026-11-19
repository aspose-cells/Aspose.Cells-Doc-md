---
title: Aplicar estilos a tablas dinámicas en Aspose.Cells for Node.js via C++
description: Aprenda a aplicar estilos predefinidos y personalizados a tablas dinámicas usando Aspose.Cells for Node.js via C++, incluyendo autoformatos XLS heredados, estilos con nombre modernos de Excel 2007+, estilos personalizados de tablas dinámicas y el atajo formatAll.
linktitle: Aplicar estilos a tablas dinámicas
url: /es/nodejs-cpp/apply-style-to-pivot-table/
keywords: Aspose.Cells Node.js via C++ estilo de tabla dinámica, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la aplicación tanto de autoformatos heredados de tablas dinámicas (pensados para archivos `.xls`) como de estilos modernos con nombre o personalizados para tablas dinámicas (pensados para archivos `.xlsx`, `.xlsm` y `.xlsb`). El API que debe llamar depende del formato de archivo en el que se guarda el libro de trabajo, no del formato desde el que se cargó.
{{% /alert %}}

## **Introducción**
Aspose.Cells expone dos APIs de estilos paralelas para tablas dinámicas. La decisión entre ellas depende del formato de archivo en el que guarde el libro de trabajo, no del formato desde el que lo lee. Un libro de trabajo cargado desde un archivo `.xls` puede volver a guardarse como `.xlsx`, y en ese caso se aplica el API de estilos moderno en lugar del heredado.
- `PivotTable.PivotTableStyleType` selecciona uno de los estilos con nombre predefinidos (temas claros y oscuros, incluyendo los estilos añadidos en Excel 2017). Estos preajustes son de solo lectura.
- `PivotTable.PivotTableStyleName` selecciona un estilo personalizado que usted mismo define mediante `Workbook.Worksheets.TableStyles.addPivotTableStyle(...)`. Los estilos personalizados son necesarios siempre que desee modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.
Además, `PivotTable.formatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, sobrescribiendo lo que se haya establecido mediante cualquiera de los APIs de nombre de estilo anteriores. Esto resulta útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato preestablecido XLS heredado**
`PivotTable.AutoFormatType` acepta un valor de la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Los valores disponibles son `Report1` a `Report10`, `Classic` y `Table1` a `Table10`.
El siguiente ejemplo carga un libro de trabajo nuevo, rellena los datos de muestra de Fruta/Año/Importe, añade una tabla dinámica, aplica `PivotTableAutoFormatType.Report5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}
**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas de una sola dimensión** con solo campos de fila y valores; no cuentan con estilos integrados para los encabezados de campos de columna. Si su tabla dinámica necesita campos de columna, use en su lugar los preajustes modernos `PivotTableStyleType` del [Escenario 2](#apply-a-modern-named-preset-pivot-table-style), que están diseñados para la disposición bidimensional que utiliza el Excel moderno.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
// Scenario 1: Apply a legacy XLS preset autoformat
// API in use: PivotTable.AutoFormatType
// Target file format: .xls (legacy)
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Create a new workbook
const workbook = new AsposeCells.Workbook();
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Populate the source data with header row (Fruit, Year, Amount)
// and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");
sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);
sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);
sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);
sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);
sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);
sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);
sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);
sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);
sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);
// Add a pivot table at destination cell E3, using source range A1:C10
const pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Apply the legacy XLS preset autoformat "Report5"
// Note: This property is only meaningful when saving as .xls.
// When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
// and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);
// Save the workbook in legacy .xls format
workbook.save("output.xls");
```

## **Aplicar un estilo de tabla dinámica preestablecido con nombre moderno**
`PivotTable.pivotTableStyleType` selecciona uno de los estilos predefinidos con nombre que Excel 2007 introdujo para tablas dinámicas. La enumeración `PivotTableStyleType` expone tres familias temáticas: la familia clara, desde `PivotTableStyleLight1` hasta `PivotTableStyleLight28`; la familia media, desde `PivotTableStyleMedium1` hasta `PivotTableStyleMedium28`; y la familia oscura, desde `PivotTableStyleDark1` hasta `PivotTableStyleDark28`. También define `None` y `Custom`. Los miembros de numeración más alta de cada familia corresponden a los estilos añadidos en Excel 2017.
Estas opciones predefinidas son de solo lectura. En cuanto necesite modificar colores, bordes o fuentes más allá de lo que ofrece una opción predefinida, deberá definir un estilo de tabla dinámica personalizado, como se muestra en el [Escenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**¿Por qué usar las opciones modernas y no los autoformateos de la serie Report?** Los valores `Report1` a `Report10` y `Table1` a `Table10` de `PivotTableAutoFormatType` son anteriores a los campos de columna en tablas dinámicas, por lo que no incluyen estilización alguna para las cabeceras de los campos de columna, y Excel las renderiza sin estilizar. Las opciones predefinidas `PivotTableStyleType` se diseñaron específicamente para la disposición bidimensional que utiliza Excel actualmente, aplicando estilos tanto a las cabeceras de los campos de fila como de los campos de columna.
{{% /alert %}}

Este escenario reutiliza el conjunto de datos Fruta/Año/Cantidad del Escenario 1, añade `Year` al área de columnas junto con el campo de fila `Fruit` mediante `PivotFieldType.Column`, aplica la opción predefinida del tema oscuro `PivotTableStyleDark1` con `pivotTable.setPivotTableStyleType`, y guarda el resultado en formato `.xlsx`, único formato para el que `PivotTableStyleType` tiene significado.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
// 9 data rows of Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);
// Add a pivot table at E3, sourced from A1:C10
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleDark1);
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **Definir y aplicar un estilo de tabla dinámica personalizado**
Los preajustes integrados no se pueden modificar. Siempre que necesite sobrescribir colores, bordes o fuentes, debe definir un estilo personalizado de tabla dinámica. El flujo de trabajo consta de tres pasos:
1. Añada un estilo personalizado a la colección `TableStyles` del libro de trabajo mediante `Workbook.Worksheets.TableStyles.addPivotTableStyle(string name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WholeTable` o `GrandTotalRow`) mediante `TableStyle.TableStyleElements.Add(TableStyleElementType)`, y luego asigne un `Style` a cada elemento mediante `TableStyleElement.SetElementStyle(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica asignando a `PivotTable.PivotTableStyleName` el nombre del estilo. No use `PivotTableStyleType` aquí, ya que esa propiedad selecciona preajustes integrados.

{{% alert color="primary" %}}
`PivotTableStyleName` y `PivotTableStyleType` no son intercambiables. Use `PivotTableStyleType` para los preajustes integrados, y `PivotTableStyleName` para los estilos personalizados que haya definido mediante `addPivotTableStyle`. Establecer ambos es inofensivo, pero solo se representa el que coincida con la fuente prevista.
Los valores disponibles de `TableStyleElementType` incluyen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` y `PageFieldValues`.
El siguiente ejemplo define un estilo personalizado de tabla dinámica con un borde negro fino en `WholeTable` y una fuente roja en negrita en `GrandTotalRow`, luego lo aplica mediante `PivotTableStyleName` y guarda como `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Populate source data: header row + 9 data rows (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);
// Add pivot table sourced from A1:C10, anchored at E3
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Step 1: register a new custom pivot table style and capture its index
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Step 2: add a WholeTable element and apply thin black borders on all four sides
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WholeTable);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
wholeTableElement.setElementStyle(wholeTableStyle);
// Step 3: add a GrandTotalRow element and apply bold red font
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);
// Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Aplicar un único estilo a cada celda de la tabla dinámica con formatAll**
`PivotTable.formatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluyendo el área de datos, los encabezados de filas y columnas y los totales. Lo que se haya establecido previamente mediante `PivotTableStyleType` o `PivotTableStyleName` se sobrescribe.

{{% alert color="primary" %}}
`formatAll` sobrescribe tanto `PivotTableStyleType` como `PivotTableStyleName`. Use esta opción solo cuando se requiera una apariencia uniforme e independiente del tema en toda la tabla dinámica.
El siguiente ejemplo crea un `Style` con un relleno sólido amarillo, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, luego lo aplica con `formatAll` y guarda como `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);
worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);
worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);
worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);
worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);
worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);
worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);
worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);
worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);
// Add pivot table: source range A1:C10, destination cell E3
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Build a Style that will be forced onto every cell of the pivot table
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.DarkBlue);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
// Apply formatAll: forces this single style onto every cell of the pivot table,
// overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.formatAll(style);
// Save the workbook in the modern .xlsx format
workbook.save("output.xlsx");
```

## **¿Qué API de estilo debo usar?**
La elección del API de estilo depende del formato de archivo en el que va a guardar. Use la tabla siguiente como referencia rápida.
| Formato de archivo de destino | API a usar | Notas |
|---|---|---|
| `.xls` (heredado) | `PivotTable.AutoFormatType` | Valores de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (por ejemplo, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `PivotTable.PivotTableStyleType` | Valores de `Aspose.Cells.PivotTableStyleType` (temas claros y oscuros, incluyendo las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | Se utiliza cuando los preajustes integrados no son suficientes. Configure mediante `TableStyleElement.SetElementStyle(...)`. |
| Cualquier formato (sobrescritura uniforme) | `PivotTable.formatAll(Style)` | Atajo que sobrescribe cualquier otra configuración de estilo en toda la tabla dinámica. |
En caso de duda, guarde como `.xlsx` y use `PivotTableStyleType` para los temas integrados, o `PivotTableStyleName` para los temas personalizados.

{{< app/cells/assistant language="nodejs-cpp" >}}