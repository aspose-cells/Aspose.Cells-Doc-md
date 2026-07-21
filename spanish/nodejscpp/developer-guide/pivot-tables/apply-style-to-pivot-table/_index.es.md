---
title: Aplicar estilos a tablas dinámicas
linktitle: Aplicar estilos a tablas dinámicas
description: Aprenda a aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for Node.js via C++, incluyendo autoformatos XLS heredados, estilos con nombre de Excel 2007+, estilos personalizados para tablas dinámicas y el acceso directo FormatAll.
keywords: Aspose.Cells Node.js via C++ estilo de tabla dinámica, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejs_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells admite la aplicación tanto de autoformatos heredados de tablas dinámicas (diseñados para archivos `.xls`) como de estilos modernos con nombre o personalizados para tablas dinámicas (diseñados para archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe llamar depende del formato de archivo en el que se guarda el libro, no del formato desde el que se cargó.

{{% /alert %}}

## **Introducción**

Aspose.Cells expone dos APIs de estilo paralelas para tablas dinámicas. La decisión entre ellas depende del formato de archivo en el que guarda el libro, no del formato desde el que lo lee. Un libro cargado desde un archivo `.xls` puede volver a guardarse como `.xlsx`, y en ese caso se aplica la API de estilo moderna en lugar de la heredada.

Para la salida heredada en `.xls`, use la propiedad `PivotTable.AutoFormatType` junto con la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Esta API corresponde al selector de autoformato que el Excel clásico ofrecía para las tablas dinámicas.

Para la salida moderna en `.xlsx`, `.xlsm` y `.xlsb`, hay dos variantes de API de estilo disponibles:

- `PivotTable.PivotTableStyleType` selecciona uno de los estilos con nombre integrados (temas claros y oscuros, incluidos los estilos añadidos en Excel 2017). Estos valores preestablecidos son de solo lectura.
- `PivotTable.PivotTableStyleName` selecciona un estilo personalizado que usted mismo define mediante `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Los estilos personalizados son necesarios siempre que desee modificar colores, bordes o fuentes más allá de lo que ofrecen los valores preestablecidos.

Además, `PivotTable.FormatAll(Style)` es un acceso directo que aplica un único objeto `Style` a todas las celdas de la tabla dinámica, sobrescribiendo lo que se haya establecido mediante cualquiera de las APIs de nombre de estilo anteriores. Esto resulta útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato preestablecido heredado de XLS**

`PivotTable.AutoFormatType` acepta un valor de la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Los valores disponibles son `Report1` a `Report10`, `Classic`, y `Table1` a `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` solo se respeta cuando el libro se guarda como `.xls`. Cuando el mismo libro se guarda como `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora esta propiedad y recurre a la configuración de `PivotTableStyleType` y `PivotTableStyleName`.

{{% /alert %}}

El siguiente ejemplo carga un libro nuevo, completa los datos de muestra de Fruta/Año/Importe, añade una tabla dinámica, aplica `PivotTableAutoFormatType.Report5` y guarda el resultado como `.xls`.

```javascript
const AsposeCells = require("aspose.cells");

// Escenario 1: Aplicar un autoformato preestablecido XLS heredado
// API en uso: PivotTable.AutoFormatType
// Formato de archivo de destino: .xls (heredado)
// Para ejemplos completos y archivos de datos, vaya a https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Crear un nuevo libro
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

// Asignar campos: Fruta -> Filas, Año -> Columnas, Cantidad -> Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Aplicar el autoformato preestablecido "Report5" del XLS heredado
// Nota: Esta propiedad solo es significativa al guardar como .xls.
// Cuando se guarda como .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
// y usa lo que especifique PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);

// Guardar el libro en formato .xls heredado
workbook.save("output.xls");
```

## **Aplicar un estilo de tabla dinámica preestablecido con nombre moderno**

`PivotTable.PivotTableStyleType` acepta un valor de la enumeración `Aspose.Cells.PivotTableStyleType`. La enumeración cubre los temas claros `PivotTableStyleLight1` a `PivotTableStyleLight28` y los temas oscuros `PivotTableStyleDark1` a `PivotTableStyleDark28`. Los estilos añadidos en Excel 2017 (la segunda ola de temas claros y oscuros) son accesibles a través de la misma enumeración.

Esta es la API recomendada para cualquier formato de archivo moderno. A diferencia del autoformato heredado, el estilo seleccionado aquí se representa fielmente en Excel y sobrevive a idas y vueltas a través de otras herramientas de Office.

El siguiente ejemplo usa los mismos datos de Fruta/Año/Importe, crea una tabla dinámica idéntica, aplica `PivotTableStyleDark1` y guarda el libro como `.xlsx`.

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

// Agregar una tabla dinámica en E3 llamada "Pivot1", con origen en A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Asignar campos de la tabla dinámica: Fruta -> área de Filas, Año -> área de Columnas, Cantidad -> área de Datos
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Aplicar un estilo de tabla dinámica preestablecido con nombre moderno de Excel 2007+.
// PivotTableStyleType es la API correcta para archivos .xlsx / .xlsm / .xlsb; AutoFormatType
// es ignorado por Excel para esos formatos. PivotTableStyleDark1 pertenece a la familia del tema oscuro
// (PivotTableStyleDark1..PivotTableStyleDark28), y el mismo enum también expone los
// temas claros/oscuros más nuevos de Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleDark1);

// Guardar como .xlsx moderno — este es el formato para el cual PivotTableStyleType es significativo.
workbook.save("output.xlsx");
```

## **Definir y aplicar un estilo de tabla dinámica personalizado**

Los valores preestablecidos integrados no se pueden modificar. Siempre que necesite sobrescribir colores, bordes o fuentes, debe definir un estilo de tabla dinámica personalizado. El flujo de trabajo tiene tres pasos:

1. Añada un estilo personalizado a la colección `TableStyles` del libro mediante `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WholeTable` o `GrandTotalRow`) mediante `TableStyle.TableStyleElements.Add(TableStyleElementType)`, y luego asigne un `Style` a cada elemento mediante `TableStyleElement.SetElementStyle(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica estableciendo `PivotTable.PivotTableStyleName` con el nombre del estilo. No use `PivotTableStyleType` aquí, ya que esa propiedad selecciona los valores preestablecidos integrados.

{{% alert color="primary" %}}

`PivotTableStyleName` y `PivotTableStyleType` no son intercambiables. Use `PivotTableStyleType` para los valores preestablecidos integrados, y `PivotTableStyleName` para los estilos personalizados que haya definido mediante `AddPivotTableStyle`. Establecer ambos es inofensivo, pero solo se representa el que coincida con el origen previsto.

{{% /alert %}}

Los valores disponibles de `TableStyleElementType` incluyen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` y `PageFieldValues`.

El siguiente ejemplo define un estilo de tabla dinámica personalizado con un borde negro fino en `WholeTable` y una fuente roja en negrita en `GrandTotalRow`, luego lo aplica mediante `PivotTableStyleName` y guarda como `.xlsx`.

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

// Paso 1: registrar un nuevo estilo de tabla dinámica personalizado y capturar su índice
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

// Paso 4: aplicar el estilo personalizado por nombre (NO por PivotTableStyleType, que es para ajustes preestablecidos integrados)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Aplicar un único estilo a todas las celdas de la tabla dinámica con FormatAll**

`PivotTable.FormatAll(Style)` es un acceso directo que aplica un único objeto `Style` a todas las celdas de la tabla dinámica, incluyendo el área de datos, los encabezados de fila y columna, y los totales. Lo que se haya establecido previamente mediante `PivotTableStyleType` o `PivotTableStyleName` queda sobrescrito.

{{% alert color="primary" %}}

`FormatAll` sobrescribe tanto `PivotTableStyleType` como `PivotTableStyleName`. Úselo solo cuando se requiera una apariencia uniforme e independiente del tema en toda la tabla dinámica.

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

// Construir un Estilo que se forzará sobre cada celda de la tabla dinámica
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

// Aplicar FormatAll: fuerza este único estilo sobre cada celda de la tabla dinámica,
// anulando cualquier PivotTableStyleType / PivotTableStyleName establecido previamente
pivotTable.formatAll(style);

// Guardar el libro en el formato moderno .xlsx
workbook.save("output.xlsx");
```

## **¿Qué API de estilo debo usar?**

La elección de la API de estilo depende del formato de archivo en el que está guardando. Use la tabla siguiente como referencia rápida.

| Formato de archivo de destino | API a usar | Notas |
|---|---|---|
| `.xls` (heredado) | `PivotTable.AutoFormatType` | Valores de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (por ejemplo, `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `PivotTable.PivotTableStyleType` | Valores de `Aspose.Cells.PivotTableStyleType` (temas claros y oscuros, incluidas las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Use cuando los valores preestablecidos integrados no son suficientes. Configure mediante `TableStyleElement.SetElementStyle(...)`. |
| Cualquier formato (sobrescritura uniforme) | `PivotTable.FormatAll(Style)` | Acceso directo que sobrescribe cualquier otra configuración de estilo en toda la tabla dinámica. |

En caso de duda, guarde como `.xlsx` y use `PivotTableStyleType` para temas integrados, o `PivotTableStyleName` para temas personalizados.

{{< app/cells/assistant language="javascript" >}}
