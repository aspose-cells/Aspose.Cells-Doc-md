---
title: Aplicar estilos a tablas dinámicas en Aspose.Cells for Node.js via C++
description: Aprenda a aplicar estilos predefinidos y personalizados a tablas dinámicas usando Aspose.Cells for Node.js via C++, incluyendo autoformatos XLS heredados, estilos con nombre modernos de Excel 2007+, estilos personalizados de tablas dinámicas y el atajo FormatAll.
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
- `PivotTable.PivotTableStyleName` selecciona un estilo personalizado que usted mismo define mediante `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Los estilos personalizados son necesarios siempre que desee modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.
Además, `PivotTable.FormatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, sobrescribiendo lo que se haya establecido mediante cualquiera de los APIs de nombre de estilo anteriores. Esto resulta útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato preestablecido XLS heredado**
`PivotTable.AutoFormatType` acepta un valor de la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Los valores disponibles son `Report1` a `Report10`, `Classic` y `Table1` a `Table10`.
El siguiente ejemplo carga un libro de trabajo nuevo, rellena los datos de muestra de Fruta/Año/Importe, añade una tabla dinámica, aplica `PivotTableAutoFormatType.Report5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}
**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas de una sola dimensión** con solo campos de fila y valores; no cuentan con estilos integrados para los encabezados de campos de columna. Si su tabla dinámica necesita campos de columna, use en su lugar los preajustes modernos `PivotTableStyleType` del [Escenario 2](#apply-a-modern-named-preset-pivot-table-style), que están diseñados para la disposición bidimensional que utiliza el Excel moderno.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// Escenario 1: Aplicar un formato automático preestablecido XLS heredado
// API en uso: PivotTable.AutoFormatType
// Formato de archivo de destino: .xls (heredado)
// Para ejemplos completos y archivos de datos, vaya a https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Crear un nuevo libro de trabajo
const workbook = new AsposeCells.Workbook();
// Obtener la primera hoja de cálculo
const sheet = workbook.getWorksheets().get(0);
// Rellenar los datos de origen con la fila de encabezado (Fruta, Año, Cantidad)
// y 9 filas de datos que cubren uva, arándano, kiwi, cereza entre 2020 y 2021
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
// Agregar una tabla dinámica en la celda de destino E3, llamada "Pivot1", usando el rango de origen A1:C10
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);
// Asignar campos: Fruta -> Filas, Cantidad -> Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Aplicar el formato automático preestablecido XLS heredado "Report5"
// Nota: Esta propiedad solo es significativa al guardar como .xls.
// Cuando se guarda como .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
// y usa lo que sea que especifique PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);
// Guardar el libro de trabajo en formato .xls heredado
workbook.save("output.xls");
```

## **Aplicar un estilo de tabla dinámica preestablecido con nombre moderno**

## **Definir y aplicar un estilo de tabla dinámica personalizado**
Los preajustes integrados no se pueden modificar. Siempre que necesite sobrescribir colores, bordes o fuentes, debe definir un estilo personalizado de tabla dinámica. El flujo de trabajo consta de tres pasos:
1. Añada un estilo personalizado a la colección `TableStyles` del libro de trabajo mediante `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WholeTable` o `GrandTotalRow`) mediante `TableStyle.TableStyleElements.Add(TableStyleElementType)`, y luego asigne un `Style` a cada elemento mediante `TableStyleElement.SetElementStyle(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica asignando a `PivotTable.PivotTableStyleName` el nombre del estilo. No use `PivotTableStyleType` aquí, ya que esa propiedad selecciona preajustes integrados.

{{% alert color="primary" %}}
`PivotTableStyleName` y `PivotTableStyleType` no son intercambiables. Use `PivotTableStyleType` para los preajustes integrados, y `PivotTableStyleName` para los estilos personalizados que haya definido mediante `AddPivotTableStyle`. Establecer ambos es inofensivo, pero solo se representa el que coincida con la fuente prevista.
{{% /alert %}}

Los valores disponibles de `TableStyleElementType` incluyen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` y `PageFieldValues`.
El siguiente ejemplo define un estilo personalizado de tabla dinámica con un borde negro fino en `WholeTable` y una fuente roja en negrita en `GrandTotalRow`, luego lo aplica mediante `PivotTableStyleName` y guarda como `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Poblar datos fuente: fila de encabezado + 9 filas de datos (A1:C10)
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
// Agregar tabla dinámica con origen en A1:C10, anclada en E3, llamada "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Paso 1: registrar un nuevo estilo personalizado de tabla dinámica y capturar su índice
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Paso 2: agregar un elemento WholeTable y aplicar bordes negros finos en los cuatro lados
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
// Paso 3: agregar un elemento GrandTotalRow y aplicar fuente roja en negrita
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);
// Paso 4: aplicar el estilo personalizado por nombre (NO por PivotTableStyleType, que es para preajustes integrados)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Aplicar un único estilo a cada celda de la tabla dinámica con FormatAll**
`PivotTable.FormatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluyendo el área de datos, los encabezados de filas y columnas y los totales. Lo que se haya establecido previamente mediante `PivotTableStyleType` o `PivotTableStyleName` se sobrescribe.

{{% alert color="primary" %}}
`FormatAll` sobrescribe tanto `PivotTableStyleType` como `PivotTableStyleName`. Use esta opción solo cuando se requiera una apariencia uniforme e independiente del tema en toda la tabla dinámica.
{{% /alert %}}

El siguiente ejemplo crea un `Style` con un relleno sólido amarillo, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, luego lo aplica con `FormatAll` y guarda como `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Poblar datos de origen: fila de encabezado (fila 1) + 9 filas de datos (filas 2-10)
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
// Agregar tabla dinámica: rango de origen A1:C10, celda de destino E3, nombre "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Asignar campos dinámicos: Fruit -> área de Fila, Year -> área de Columna, Amount -> área de Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
// Construir un Estilo que se forzará en cada celda de la tabla dinámica
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
// Aplicar FormatAll: fuerza este único estilo en cada celda de la tabla dinámica,
// anulando cualquier PivotTableStyleType / PivotTableStyleName establecido previamente
pivotTable.formatAll(style);
// Guardar el libro en el formato moderno .xlsx
workbook.save("output.xlsx");
```

## **¿Qué API de estilo debo usar?**
La elección del API de estilo depende del formato de archivo en el que va a guardar. Use la tabla siguiente como referencia rápida.
| Formato de archivo de destino | API a usar | Notas |
|---|---|---|
| `.xls` (heredado) | `PivotTable.AutoFormatType` | Valores de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (por ejemplo, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `PivotTable.PivotTableStyleType` | Valores de `Aspose.Cells.PivotTableStyleType` (temas claros y oscuros, incluyendo las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Se utiliza cuando los preajustes integrados no son suficientes. Configure mediante `TableStyleElement.SetElementStyle(...)`. |
| Cualquier formato (sobrescritura uniforme) | `PivotTable.FormatAll(Style)` | Atajo que sobrescribe cualquier otra configuración de estilo en toda la tabla dinámica. |
En caso de duda, guarde como `.xlsx` y use `PivotTableStyleType` para los temas integrados, o `PivotTableStyleName` para los temas personalizados.

{{< app/cells/assistant language="nodejs-cpp" >}}