---
title: Aplicar estilos a tablas dinámicas en Aspose.Cells for Node.js via Java
description: Aprenda a aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for Node.js via Java, incluyendo autoformatos heredados de XLS, estilos con nombre modernos de Excel 2007+, estilos personalizados de tabla dinámica y el acceso directo formatAll.
linktitle: Aplicar estilos a tablas dinámicas
keywords: estilos de tabla dinámica Aspose.Cells Node.js via Java, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite tanto autoformatos de tablas dinámicas heredados (diseñados para archivos `.xls`) como estilos de tabla dinámica personalizados o con nombre modernos (diseñados para archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe usar depende del formato de archivo en el que se guarda el libro, no del formato desde el que se cargó.
{{% /alert %}}

## **Introducción**
Aspose.Cells expone dos API de estilos paralelas para tablas dinámicas. La decisión entre ellas depende del formato de archivo en el que guarda el libro, no del formato desde el que lo lee. Un libro cargado desde un archivo `.xls` se puede volver a guardar como `.xlsx`, y en ese caso se aplica la API de estilos moderna en lugar de la heredada.
- `PivotTable.pivotTableStyleType` selecciona uno de los estilos con nombre integrados (temas claros y oscuros, incluidos los estilos añadidos en Excel 2017). Estos preajustes son de solo lectura.
- `PivotTable.pivotTableStyleName` selecciona un estilo personalizado que usted mismo define mediante `Worksheets.getTableStyles().addPivotTableStyle(...)`. Los estilos personalizados son necesarios siempre que desee modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.
Además, `PivotTable.formatAll(Style)` es un acceso directo que aplica un único objeto `Style` a cada celda de la tabla dinámica, sobrescribiendo lo establecido mediante cualquiera de las API de nombre de estilo anteriores. Esto resulta útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato preestablecido XLS heredado**
`PivotTable.autoFormatType` acepta un valor de la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Los valores disponibles son `Report1` a `Report10`, `Classic` y `Table1` a `Table10`.
El siguiente ejemplo carga un libro nuevo, rellena los datos de muestra Fruit/Year/Amount, añade una tabla dinámica, aplica `PivotTableAutoFormatType.Report5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}
**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) fueron diseñados en Excel clásico para **tablas dinámicas de una sola dimensión**, con únicamente campos de fila y valores, ya que no incluyen estilo integrado para los encabezados de campos de columna. Si su tabla dinámica necesita campos de columna, utilice en su lugar los preajustes modernos de `PivotTableStyleType` del [Escenario 2](#apply-a-modern-named-preset-pivot-table-style), que están diseñados para el diseño bidimensional que emplea el Excel moderno.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Obtener la primera hoja de cálculo
let sheet = workbook.getWorksheets().get(0);
// Poblar los datos fuente con la fila de encabezado (Fruit, Year, Amount)
// y 9 filas de datos que cubren grape, blueberry, kiwi, cherry entre 2020 y 2021
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
// Agregar una tabla dinámica en la celda destino E3, llamada, usando el rango fuente A1:C10
let pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4);
// Asignar campos: Fruit -> Filas, Amount -> Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Aplicar el formato automático preestablecido heredado de XLS "Report5"
// Nota: Esta propiedad solo tiene significado al guardar como .xls.
// Cuando se guarda como .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
// y utiliza lo que especifiquen PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);
// Guardar el libro en formato .xls heredado
workbook.save("output.xls");
```

## **Aplicar un estilo preestablecido de tabla dinámica con nombre moderno**
`PivotTable.setPivotTableStyleType(int)` selecciona uno de los estilos predefinidos con nombre que Excel 2007 introdujo para tablas dinámicas. La enumeración `PivotTableStyleType` expone tres familias de temas: la familia clara, desde `PIVOT_TABLE_STYLE_LIGHT1` hasta `PIVOT_TABLE_STYLE_LIGHT28`; la familia media, desde `PIVOT_TABLE_STYLE_MEDIUM1` hasta `PIVOT_TABLE_STYLE_MEDIUM28`; y la familia oscura, desde `PIVOT_TABLE_STYLE_DARK1` hasta `PIVOT_TABLE_STYLE_DARK_28`. Además, define `None` y `Custom`. Los miembros de número más alto de cada familia son los estilos añadidos en Excel 2017.
Estas predefiniciones son de solo lectura. Tan pronto como necesite cambiar colores, bordes o fuentes más allá de lo que una predefinición proporciona, deberá definir un estilo de tabla dinámica personalizado, como se muestra en el [Escenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**¿Por qué utilizar las predefiniciones modernas y no los autoformateos de la serie Report?** Los valores `Report1` hasta `Report10` y `Table1` hasta `Table10` de `PivotTableAutoFormatType` preceden a los campos de columna de tabla dinámica, por lo que no incluyen estilos para las cabeceras de los campos de columna, y Excel representa dichas cabeceras sin estilizar. Las predefiniciones `PivotTableStyleType` se diseñaron para la disposición bidimensional que utiliza Excel moderno y aplican estilo tanto a las cabeceras de los campos de fila como a las de los campos de columna.
{{% /alert %}}

Este escenario reutiliza el conjunto de datos Fruta/Año/Cantidad del Escenario 1, añade `Year` al área de columnas junto con el campo de fila `Fruit` mediante `PivotFieldType.COLUMN`, aplica la predefinición de tema oscuro `PIVOT_TABLE_STYLE_DARK1` con `pivotTable.setPivotTableStyleType`, y guarda el resultado como `.xlsx` —el formato para el cual `PivotTableStyleType` tiene significado.

```javascript
const AsposeCells = require("aspose.cells");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);
// Save as modern .xlsx -- this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```

## **Definir y aplicar un estilo personalizado de tabla dinámica**
Los preajustes integrados no se pueden modificar. Siempre que deba sobrescribir colores, bordes o fuentes, es necesario definir un estilo de tabla dinámica personalizado. El flujo de trabajo consta de tres pasos:
1. Añada un estilo personalizado a la colección `TableStyles` del libro mediante `Worksheets.getTableStyles().addPivotTableStyle(String name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WholeTable` o `GrandTotalRow`) mediante `TableStyle.tableStyleElements.add(TableStyleElementType)` y, a continuación, asigne un `Style` a cada elemento mediante `TableStyleElement.setElementStyle(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica estableciendo `PivotTable.pivotTableStyleName` en el nombre del estilo. No use aquí `pivotTableStyleType`, ya que esa propiedad selecciona los preajustes integrados.

{{% alert color="primary" %}}
`pivotTableStyleName` y `pivotTableStyleType` no son intercambiables. Use `pivotTableStyleType` para los preajustes integrados, y `pivotTableStyleName` para los estilos personalizados que haya definido mediante `addPivotTableStyle`. Establecer ambos resulta inofensivo, pero solo se representará el que coincida con el origen previsto.
Los valores disponibles de `TableStyleElementType` incluyen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` y `PageFieldValues`.
El siguiente ejemplo define un estilo personalizado de tabla dinámica con un borde negro fino en `WholeTable` y una fuente roja en negrita en `GrandTotalRow`, luego lo aplica mediante `pivotTableStyleName` y guarda como `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Rellenar datos de origen: fila de encabezado + 9 filas de datos (A1:C10)
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
// Agregar tabla dinámica con origen en A1:C10, anclada en E3, llamada
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Paso 1: registrar un nuevo estilo de tabla dinámica personalizado y capturar su índice
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Paso 2: agregar un elemento WholeTable y aplicar bordes negros finos en los cuatro lados
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.getBlack());
let bottomBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.getBlack());
let leftBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.getBlack());
let rightBorder = wholeTableStyle.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// Paso 3: agregar un elemento GrandTotalRow y aplicar fuente roja en negrita
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Paso 4: aplicar el estilo personalizado por nombre (NO por PivotTableStyleType, que es para estilos preestablecidos)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Aplicar un único estilo a cada celda de la tabla dinámica con formatAll**
`PivotTable.formatAll(Style)` es un acceso directo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluidas el área de datos, los encabezados de filas y columnas, y los totales. Todo lo establecido previamente mediante `pivotTableStyleType` o `pivotTableStyleName` queda sobrescrito.

{{% alert color="primary" %}}
`formatAll` sobrescribe tanto `pivotTableStyleType` como `pivotTableStyleName`. Utilícelo solo cuando se requiera una apariencia uniforme e independiente del tema en toda la tabla dinámica.
El siguiente ejemplo crea un `Style` con un relleno sólido amarillo, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, luego lo aplica con `formatAll` y guarda como `.xlsx`.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
// Poblar datos fuente: fila de encabezado (fila 1) + 9 filas de datos (filas 2-10)
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
// Agregar tabla dinámica: rango fuente A1:C10, celda de destino E3, nombre
let pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4);
// Asignar campos dinámicos: Fruit -> área de Fila, Year -> área de Columna, Amount -> área de Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
// Crear un Estilo que será forzado en cada celda de la tabla dinámica
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.getYellow());
style.setPattern(AsposeCells.BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(AsposeCells.Color.getDarkBlue());
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.TOP_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.BOTTOM_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.LEFT_BORDER).setColor(AsposeCells.Color.getBlack());
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setLineStyle(AsposeCells.CellBorderType.THIN);
style.getBorders().getByBorderType(AsposeCells.BorderType.RIGHT_BORDER).setColor(AsposeCells.Color.getBlack());
// Aplicar formatAll: fuerza este único estilo en cada celda de la tabla dinámica,
// sobrescribiendo cualquier PivotTableStyleType / PivotTableStyleName establecido previamente
pivotTable.formatAll(style);
// Guardar el libro en el formato moderno .xlsx
workbook.save("output.xlsx");
```

## **¿Qué API de estilos debo usar?**
La elección de la API de estilos depende del formato de archivo en el que va a guardar. Utilice la tabla siguiente como referencia rápida.
| Formato de archivo de destino | API a usar | Notas |
|---|---|---|
| `.xls` (heredado) | `PivotTable.autoFormatType` | Valores de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (por ejemplo, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Se ignora al guardar como formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `PivotTable.pivotTableStyleType` | Valores de `Aspose.Cells.PivotTableStyleType` (temas claros y oscuros, incluidas las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | Úselo cuando los preajustes integrados no sean suficientes. Configure mediante `TableStyleElement.setElementStyle(...)`. |
| Cualquier formato (anulación uniforme) | `PivotTable.formatAll(Style)` | Acceso directo que sobrescribe cualquier otra configuración de estilo en toda la tabla dinámica. |
En caso de duda, guarde como `.xlsx` y use `pivotTableStyleType` para los temas integrados, o `pivotTableStyleName` para los temas personalizados.

{{< app/cells/assistant language="nodejs-java" >}}