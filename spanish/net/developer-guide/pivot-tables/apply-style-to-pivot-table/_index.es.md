---
title: Aplicar estilos a tablas dinámicas
linktitle: Aplicar estilos a tablas dinámicas
description: Aprenda a aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for .NET, incluyendo autoformatos XLS heredados, estilos con nombre de Excel 2007+, estilos personalizados para tablas dinámicas y el acceso directo FormatAll.
keywords: Aspose.Cells .NET estilo de tabla dinámica, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la aplicación tanto de autoformatos heredados para tablas dinámicas (diseñados para archivos `.xls`) como de estilos modernos con nombre o personalizados para tablas dinámicas (diseñados para archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe llamar depende del formato de archivo en el que se guarda el libro, no del formato desde el que se cargó.

{{% /alert %}}

## **Introducción**

Aspose.Cells expone dos APIs de estilo paralelas para tablas dinámicas. La decisión entre ellas depende del formato de archivo en el que guarde el libro, no del formato desde el que lo lea. Un libro cargado desde un archivo `.xls` puede volver a guardarse como `.xlsx`, y en ese caso se aplica la API de estilo moderna en lugar de la heredada.

Para la salida heredada en formato `.xls`, utilice la propiedad `PivotTable.AutoFormatType` junto con la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Esta API corresponde al selector de autoformato que el Excel clásico ofrecía para las tablas dinámicas.

Para la salida moderna en formatos `.xlsx`, `.xlsm` y `.xlsb`, están disponibles dos variantes de la API de estilo:

- `PivotTable.PivotTableStyleType` selecciona uno de los estilos con nombre integrados (temas claros y oscuros, incluidos los estilos añadidos en Excel 2017). Estos preajustes son de solo lectura.
- `PivotTable.PivotTableStyleName` selecciona un estilo personalizado que usted mismo define mediante `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)`. Los estilos personalizados son obligatorios cuando se desea modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.

Además, `PivotTable.FormatAll(Style)` es un acceso directo que aplica un único objeto `Style` a cada celda de la tabla dinámica, anulando todo lo establecido mediante cualquiera de las APIs de nombre de estilo anteriores. Esto resulta útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato predefinido heredado de XLS**

`PivotTable.AutoFormatType` acepta un valor de la enumeración `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Los valores disponibles son `Report1` a `Report10`, `Classic` y `Table1` a `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` solo se respeta cuando el libro se guarda como `.xls`. Cuando el mismo libro se guarda como `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora esta propiedad y recurre a la configuración de `PivotTableStyleType` y `PivotTableStyleName`.

{{% /alert %}}

El siguiente ejemplo carga un libro nuevo, rellena los datos de muestra de Fruta/Año/Importe, añade una tabla dinámica, aplica `PivotTableAutoFormatType.Report5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}

**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas unidimensionales** con solo campos de fila y valores — no tienen estilo integrado para los encabezados de campos de columna. Si tu tabla dinámica necesita campos de columna, usa los preajustes modernos `PivotTableStyleType` del Escenario 2 a continuación, que están diseñados para el diseño bidimensional que usa el Excel moderno.

{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Escenario 1: Aplicar un autoformato preestablecido XLS heredado
// API en uso: PivotTable.AutoFormatType
// Formato de archivo de destino: .xls (heredado)
// Para ejemplos completos y archivos de datos, vaya a https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Crear un nuevo libro de trabajo
Workbook workbook = new Workbook();

// Obtener la primera hoja de trabajo
Worksheet sheet = workbook.Worksheets[0];

// Rellenar los datos de origen con la fila de encabezado (Fruit, Year, Amount)
// y 9 filas de datos que cubren grape, blueberry, kiwi, cherry entre 2020 y 2021
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

// Agregar una tabla dinámica en la celda de destino E3, llamada "Pivot1", usando el rango de origen A1:C10
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Asignar campos: Fruit -> Filas, Year -> Columnas, Amount -> Datos
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Aplicar el autoformato preestablecido XLS heredado "Report5"
// Nota: Esta propiedad solo tiene sentido al guardar como .xls.
// Cuando se guarda como .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
// y usa lo que especifique PivotTableStyleType / PivotTableStyleName.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;

// Guardar el libro en formato .xls heredado
workbook.Save("output.xls");
```

## **Aplicar un estilo predefinido moderno con nombre para tablas dinámicas**

`PivotTable.PivotTableStyleType` acepta un valor de la enumeración `Aspose.Cells.PivotTableStyleType`. La enumeración cubre los temas claros `PivotTableStyleLight1` a `PivotTableStyleLight28` y los temas oscuros `PivotTableStyleDark1` a `PivotTableStyleDark28`. Los estilos añadidos en Excel 2017 (la segunda oleada de temas claros y oscuros) están disponibles a través de la misma enumeración.

Esta es la API recomendada para cualquier formato de archivo moderno. A diferencia del autoformato heredado, el estilo seleccionado aquí se representa fielmente en Excel y sobrevive a los intercambios con otras herramientas de Office.

El siguiente ejemplo utiliza los mismos datos de Fruta/Año/Importe, crea una tabla dinámica idéntica, aplica `PivotTableStyleDark1` y guarda el libro como `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Escenario 2: Aplicar un estilo preestablecido con nombre de Excel 2007+ moderno usando PivotTableStyleType.
// Formato de archivo de destino: .xlsx. La enumeración PivotTableStyleType reside en el espacio de nombres Aspose.Cells
// (no en Aspose.Cells.Pivot) — es por eso que no necesitamos ninguna cláusula using adicional para ello.
// Referencia en GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Fila de encabezado: Fruta / Año / Monto
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 filas de datos de Fruta / Año / Monto
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

// Añadir una tabla dinámica en E3 con el nombre "Pivot1", con origen en A1:C10
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Asignar campos dinámicos: Fruta -> área de fila, Año -> área de columna, Monto -> área de datos
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Aplicar un estilo de tabla dinámica preestablecido con nombre de Excel 2007+ moderno.
// PivotTableStyleType es la API correcta para archivos .xlsx / .xlsm / .xlsb; AutoFormatType
// es ignorado por Excel para esos formatos. PivotTableStyleDark1 pertenece a la familia del tema oscuro
// (PivotTableStyleDark1..PivotTableStyleDark28), y la misma enumeración también expone los
// temas más recientes de Excel 2017 claro/oscuro (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;

// Guardar como .xlsx moderno — este es el formato para el cual PivotTableStyleType es significativo.
workbook.Save("output.xlsx");
```

## **Definir y aplicar un estilo personalizado para tablas dinámicas**

Los preajustes integrados no se pueden modificar. Cuando necesite anular colores, bordes o fuentes, debe definir un estilo personalizado para tablas dinámicas. El flujo de trabajo consta de tres pasos:

1. Añada un estilo personalizado a la colección `TableStyles` del libro mediante `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WholeTable` o `GrandTotalRow`) mediante `TableStyle.TableStyleElements.Add(TableStyleElementType)` y, a continuación, asigne un `Style` a cada elemento mediante `TableStyleElement.SetElementStyle(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica asignando a `PivotTable.PivotTableStyleName` el nombre del estilo. No utilice `PivotTableStyleType` aquí, ya que esa propiedad selecciona los preajustes integrados.

{{% alert color="primary" %}}

`PivotTableStyleName` y `PivotTableStyleType` no son intercambiables. Utilice `PivotTableStyleType` para los preajustes integrados y `PivotTableStyleName` para los estilos personalizados que haya definido mediante `AddPivotTableStyle`. Establecer ambos no causa problemas, pero solo se representa el que coincida con el origen previsto.

{{% /alert %}}

Los valores disponibles de `TableStyleElementType` incluyen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` y `PageFieldValues`.

El siguiente ejemplo define un estilo personalizado para tablas dinámicas con un borde negro fino en `WholeTable` y una fuente roja en negrita en `GrandTotalRow`, lo aplica mediante `PivotTableStyleName` y guarda como `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using Aspose.Cells.Tables;
using System.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Poblar datos de origen: fila de encabezado + 9 filas de datos (A1:C10)
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

// Agregar tabla dinámica con origen en A1:C10, anclada en E3, llamada "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Paso 1: registrar un nuevo estilo de tabla dinámica personalizado y capturar su índice
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];

// Paso 2: agregar un elemento WholeTable y aplicar bordes negros finos en los cuatro lados
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

// Paso 3: agregar un elemento GrandTotalRow y aplicar fuente roja en negrita
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);

// Paso 4: aplicar el estilo personalizado por nombre (NO por PivotTableStyleType, que es para estilos predefinidos)
pivotTable.PivotTableStyleName = "CustomPivotStyle";

workbook.Save("output.xlsx");
```

## **Aplicar un solo estilo a cada celda de la tabla dinámica con FormatAll**

`PivotTable.FormatAll(Style)` es un acceso directo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluidas el área de datos, los encabezados de filas y columnas y los totales. Todo lo establecido previamente mediante `PivotTableStyleType` o `PivotTableStyleName` queda anulado.

{{% alert color="primary" %}}

`FormatAll` anula tanto `PivotTableStyleType` como `PivotTableStyleName`. Utilícelo solo cuando se requiera una apariencia uniforme e independiente del tema en toda la tabla dinámica.

{{% /alert %}}

El siguiente ejemplo crea un `Style` con un relleno sólido amarillo, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, lo aplica con `FormatAll` y guarda como `.xlsx`.

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Escenario 4: Aplicar un único Estilo a cada celda de la tabla dinámica usando FormatAll
// API en uso: PivotTable.FormatAll(Style)
// Formato de destino: .xlsx
// Referencia de GitHub: ver el repositorio Aspose.Cells-for-.NET — ejemplos de estilo de tablas dinámicas

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Rellenar datos de origen: fila de encabezado (fila 1) + 9 filas de datos (filas 2-10)
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

// Agregar tabla dinámica: rango de origen A1:C10, celda de destino E3, nombre "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Asignar campos dinámicos: Fruit -> área de Filas, Year -> área de Columnas, Amount -> área de Datos
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Construir un Estilo que se forzará sobre cada celda de la tabla dinámica
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

// Aplicar FormatAll: fuerza este único estilo sobre cada celda de la tabla dinámica,
// anulando cualquier PivotTableStyleType / PivotTableStyleName establecido previamente
pivotTable.FormatAll(style);

// Guardar el libro en el formato moderno .xlsx
workbook.Save("output.xlsx");
```

## **¿Qué API de estilo debo usar?**

La elección de la API de estilo depende del formato de archivo en el que va a guardar. Utilice la tabla siguiente como referencia rápida.

| Formato de archivo de destino | API a utilizar | Notas |
|---|---|---|
| `.xls` (heredado) | `PivotTable.AutoFormatType` | Valores de `Aspose.Cells.Pivot.PivotTableAutoFormatType` (p. ej., `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `PivotTable.PivotTableStyleType` | Valores de `Aspose.Cells.PivotTableStyleType` (temas claros y oscuros, incluidas las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Utilícelo cuando los preajustes integrados no sean suficientes. Configurar mediante `TableStyleElement.SetElementStyle(...)`. |
| Cualquier formato (anulación uniforme) | `PivotTable.FormatAll(Style)` | Acceso directo que anula cualquier otra configuración de estilo en toda la tabla dinámica. |

En caso de duda, guarde como `.xlsx` y utilice `PivotTableStyleType` para los temas integrados, o `PivotTableStyleName` para los temas personalizados.

{{< app/cells/assistant language="csharp" >}}