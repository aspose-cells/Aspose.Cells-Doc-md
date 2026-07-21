---
title: Aplicar estilos a tablas dinámicas
linktitle: Aplicar estilos a tablas dinámicas
description: Aprenda a aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for Node.js via Java, cubriendo autoformatos XLS heredados, estilos con nombre modernos de Excel 2007+, estilos personalizados de tablas dinámicas y el atajo FormatAll.
keywords: Aspose.Cells Node.js via Java estilo de tabla dinámica, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la aplicación tanto de autoformatos heredados para tablas dinámicas (destinados a archivos `.xls`) como de estilos modernos con nombre o personalizados para tablas dinámicas (destinados a archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe llamar depende del formato de archivo en el que se guarda el libro de trabajo, no del formato desde el que se cargó.

{{% /alert %}}

## **Introducción**

Aspose.Cells expone dos API de estilos paralelas para tablas dinámicas. La decisión entre ellas depende del formato de archivo en el que guarde el libro de trabajo, no del formato desde el que lo lee. Un libro de trabajo cargado desde un archivo `.xls` puede volver a guardarse como `.xlsx`, y en ese caso se aplica la API de estilos moderna en lugar de la heredada.

Para la salida `.xls` heredada, use la propiedad `PivotTable.autoFormatType` junto con la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Esta API corresponde al selector de autoformato que el Excel clásico ofrecía para las tablas dinámicas.

Para la salida moderna `.xlsx`, `.xlsm` y `.xlsb`, hay dos variantes de API de estilos disponibles:

- `PivotTable.pivotTableStyleType` selecciona uno de los estilos con nombre integrados (temas claros y oscuros, incluidos los estilos añadidos en Excel 2017). Estos preajustes son de solo lectura.
- `PivotTable.pivotTableStyleName` selecciona un estilo personalizado que usted mismo define mediante `Worksheets.getTableStyles().addPivotTableStyle(...)`. Los estilos personalizados son necesarios siempre que quiera modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.

Además, `PivotTable.formatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, anulando lo que se haya establecido mediante cualquiera de las API de nombre de estilo anteriores. Esto es útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato preestablecido XLS heredado**

`PivotTable.autoFormatType` acepta un valor de la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Los valores disponibles son `Report1` a `Report10`, `Classic`, y `Table1` a `Table10`.

{{% alert color="primary" %}}

`autoFormatType` solo se respeta cuando el libro de trabajo se guarda como `.xls`. Cuando el mismo libro de trabajo se guarda como `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora esta propiedad y recurre a la configuración de `pivotTableStyleType` y `pivotTableStyleName`.

{{% /alert %}}

El siguiente ejemplo carga un libro de trabajo nuevo, rellena los datos de muestra de Fruta/Año/Importe, añade una tabla dinámica, aplica `PivotTableAutoFormatType.Report5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}

**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas unidimensionales** con solo campos de fila y valores — no tienen estilo integrado para los encabezados de campos de columna. Si tu tabla dinámica necesita campos de columna, usa los preajustes modernos `PivotTableStyleType` del Escenario 2 a continuación, que están diseñados para el diseño bidimensional que usa el Excel moderno.

{{% /alert %}}

```javascript
let workbook = new AsposeCells.Workbook();

// Obtener la primera hoja de cálculo
let sheet = workbook.getWorksheets().get(0);

// Poblar los datos de origen con la fila de encabezado (Fruta, Año, Cantidad)
// y 9 filas de datos que cubren uva, arándano, kiwi, cereza en 2020 y 2021
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
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Asignar campos: Fruta -> Filas, Año -> Columnas, Cantidad -> Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Aplicar el formato automático preestablecido heredado de XLS "Report5"
// Nota: Esta propiedad solo tiene significado al guardar como .xls.
// Al guardar como .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
// y usa lo que especifique PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);

// Guardar el libro en formato .xls heredado
workbook.save("output.xls");
```

## **Aplicar un estilo preestablecido con nombre moderno de tabla dinámica**

`PivotTable.pivotTableStyleType` acepta un valor de la enumeración `Aspose.Cells.PivotTableStyleType`. La enumeración cubre los temas claros `PivotTableStyleLight1` a `PivotTableStyleLight28` y los temas oscuros `PivotTableStyleDark1` a `PivotTableStyleDark28`. Los estilos añadidos en Excel 2017 (la segunda oleada de temas claros y oscuros) son accesibles a través de la misma enumeración.

Esta es la API recomendada para cualquier formato de archivo moderno. A diferencia del autoformato heredado, el estilo seleccionado aquí se renderiza fielmente por Excel y sobrevive a idas y vueltas a través de otras herramientas de Office.

El siguiente ejemplo usa los mismos datos de Fruta/Año/Importe, crea una tabla dinámica idéntica, aplica `PivotTableStyleDark1` y guarda el libro de trabajo como `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Fila de encabezado: Fruta / Año / Cantidad
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 filas de datos de Fruta / Año / Cantidad
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

// Agrega una tabla dinámica en E3 llamada "Pivot1", con origen en A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Asigna los campos dinámicos: Fruta -> área de filas, Año -> área de columnas, Cantidad -> área de datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Aplica un estilo de tabla dinámica preestablecido y moderno de Excel 2007+.
// PivotTableStyleType es la API correcta para archivos .xlsx / .xlsm / .xlsb; AutoFormatType
// es ignorado por Excel para esos formatos. PivotTableStyleDark1 pertenece a la familia de
// temas oscuros (PivotTableStyleDark1..PivotTableStyleDark28), y la misma enumeración también expone
// los temas claros/oscuros más nuevos de Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// Guarda como .xlsx moderno — este es el formato para el cual PivotTableStyleType tiene significado.
workbook.save("output.xlsx");
```

## **Definir y aplicar un estilo personalizado de tabla dinámica**

Los preajustes integrados no se pueden modificar. Siempre que necesite anular colores, bordes o fuentes, debe definir un estilo de tabla dinámica personalizado. El flujo de trabajo consta de tres pasos:

1. Añada un estilo personalizado a la colección `TableStyles` del libro de trabajo mediante `Worksheets.getTableStyles().addPivotTableStyle(String name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WholeTable` o `GrandTotalRow`) mediante `TableStyle.tableStyleElements.add(TableStyleElementType)`, luego asigne un `Style` a cada elemento mediante `TableStyleElement.setElementStyle(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica estableciendo `PivotTable.pivotTableStyleName` con el nombre del estilo. No use `pivotTableStyleType` aquí, ya que esa propiedad selecciona preajustes integrados.

{{% alert color="primary" %}}

`pivotTableStyleName` y `pivotTableStyleType` no son intercambiables. Use `pivotTableStyleType` para preajustes integrados y `pivotTableStyleName` para estilos personalizados que haya definido mediante `addPivotTableStyle`. Establecer ambos es inofensivo, pero solo se renderiza el que coincida con la fuente prevista.

{{% /alert %}}

Los valores disponibles de `TableStyleElementType` incluyen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` y `PageFieldValues`.

El siguiente ejemplo define un estilo personalizado de tabla dinámica con un borde negro fino en `WholeTable` y una fuente roja en negrita en `GrandTotalRow`, luego lo aplica mediante `pivotTableStyleName` y guarda como `.xlsx`.

```javascript
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

// Agregar tabla dinámica con origen en A1:C10, anclada en E3, llamada "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Paso 1: registrar un nuevo estilo personalizado de tabla dinámica y capturar su índice
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Paso 2: agregar un elemento WholeTable y aplicar bordes negros finos en los cuatro lados
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.BLACK);

let bottomBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.BLACK);

let leftBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.BLACK);

let rightBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.BLACK);

wholeTableElement.setElementStyle(wholeTableStyle);

// Paso 3: agregar un elemento GrandTotalRow y aplicar fuente roja en negrita
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.RED);
grandTotalElement.setElementStyle(grandTotalStyle);

// Paso 4: aplicar el estilo personalizado por nombre (NO por PivotTableStyleType, que es para estilos predefinidos)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Aplicar un estilo a cada celda de la tabla dinámica con FormatAll**

`PivotTable.formatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluyendo el área de datos, los encabezados de fila y columna, y los totales. Todo lo establecido previamente mediante `pivotTableStyleType` o `pivotTableStyleName` queda anulado.

{{% alert color="primary" %}}

`formatAll` anula tanto `pivotTableStyleType` como `pivotTableStyleName`. Use esta opción solo cuando se requiera una apariencia uniforme e independiente del tema en toda la tabla dinámica.

{{% /alert %}}

El siguiente ejemplo crea un `Style` con un relleno sólido amarillo, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, luego lo aplica con `formatAll` y guarda como `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Llenar datos de origen: fila de encabezado (fila 1) + 9 filas de datos (filas 2-10)
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

// Asignar campos dinámicos: Fruit -> área de fila, Year -> área de columna, Amount -> área de datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Crear un Estilo que se aplicará forzosamente a cada celda de la tabla dinámica
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

// Aplicar FormatAll: aplica forzosamente este único estilo a cada celda de la tabla dinámica,
// anulando cualquier PivotTableStyleType / PivotTableStyleName establecido previamente
pivotTable.formatAll(style);

// Guardar el libro en el formato moderno .xlsx
workbook.save("output.xlsx");
```

## **¿Qué API de estilos debo usar?**

La elección de la API de estilos depende del formato de archivo en el que está guardando. Use la tabla siguiente como referencia rápida.

| Formato de archivo de destino | API a usar | Notas |
|---|---|---|
| `.xls` (heredado) | `PivotTable.autoFormatType` | Valores de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (p. ej. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `PivotTable.pivotTableStyleType` | Valores de `Aspose.Cells.PivotTableStyleType` (temas claros/oscuros, incluidas las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | Use cuando los preajustes integrados no sean suficientes. Configure mediante `TableStyleElement.setElementStyle(...)`. |
| Cualquier formato (anulación uniforme) | `PivotTable.formatAll(Style)` | Atajo que anula cualquier otra configuración de estilo en toda la tabla dinámica. |

En caso de duda, guarde como `.xlsx` y use `pivotTableStyleType` para temas integrados, o `pivotTableStyleName` para temas personalizados.

{{< app/cells/assistant language="javascript" >}}