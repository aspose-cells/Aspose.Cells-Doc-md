---
title: Aplicar estilos a tablas dinámicas en Aspose.Cells for Java
description: Aprenda a aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for Java, incluyendo autoformatos XLS heredados, estilos con nombre modernos de Excel 2007+, estilos personalizados de tablas dinámicas y el atajo FormatAll.
linktitle: Aplicar estilos a tablas dinámicas
keywords: Aspose.Cells Java estilo de tabla dinámica, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la aplicación de autoformatos heredados para tablas dinámicas (diseñados para archivos `.xls`) y estilos modernos con nombre o personalizados para tablas dinámicas (diseñados para archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe llamar depende del formato de archivo al que se guarda el libro, no del formato desde el que se cargó.
{{% /alert %}}

## **Introducción**
Aspose.Cells expone dos API de estilos paralelas para tablas dinámicas. La decisión entre ellas depende del formato de archivo al que guarde el libro, no del formato desde el que lo lea. Un libro cargado desde un archivo `.xls` puede volver a guardarse como `.xlsx`, y en ese caso se aplica la API de estilos moderna en lugar de la heredada.
- `PivotTable.PivotTableStyleType` selecciona uno de los estilos con nombre integrados (temas claros y oscuros, incluidos los estilos añadidos en Excel 2017). Estos preajustes son de solo lectura.
- `PivotTable.PivotTableStyleName` selecciona un estilo personalizado que usted mismo define mediante `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)`. Los estilos personalizados son obligatorios siempre que desee modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.
Además, `PivotTable.formatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, anulando lo que se haya configurado a través de cualquiera de las API de nombres de estilo anteriores. Esto resulta útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato predefinido XLS heredado**
`PivotTable.AutoFormatType` acepta un valor de la enumeración `com.aspose.cells.PivotTableAutoFormatType`. Los valores disponibles son `REPORT_1` hasta `REPORT_10`, `CLASSIC` y `TABLE_1` hasta `TABLE_10`.
El siguiente ejemplo carga un libro nuevo, completa los datos de muestra de Fruta/Año/Cantidad, añade una tabla dinámica, aplica `PivotTableAutoFormatType.REPORT_5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}
**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas de una sola dimensión**, solo con campos de fila y valores, ya que no incluyen estilo integrado para los encabezados de campos de columna. Si su tabla dinámica necesita campos de columna, utilice en su lugar los preajustes modernos de `PivotTableStyleType` del [Escenario 2](#apply-a-modern-named-preset-pivot-table-style), que están diseñados para el diseño bidimensional que utiliza el Excel moderno.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Escenario 1: Aplicar un formato automático preestablecido de XLS heredado
// API en uso: PivotTable.AutoFormatType
// Formato de archivo de destino: .xls (heredado)
// Para ejemplos completos y archivos de datos, vaya a https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Crear un nuevo libro
Workbook workbook = new Workbook();
// Obtener la primera hoja de cálculo
Worksheet sheet = workbook.getWorksheets().get(0);
// Rellenar los datos de origen con la fila de encabezado (Fruit, Year, Amount)
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
// Agregar una tabla dinámica en la celda de destino E3, llamada "Pivot1", usando el rango de origen A1:C10
int pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// Asignar campos: Fruit -> Filas, Amount -> Datos
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Aplicar el formato automático preestablecido "Report5" de XLS heredado
// Nota: Esta propiedad solo es significativa al guardar como .xls.
// Al guardar como .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
// y usa lo que especifiquen PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);
// Guardar el libro en formato .xls heredado
workbook.save("output.xls");
```

## **Aplicar un estilo predefinido moderno con nombre a una tabla dinámica**

`PivotTable.setPivotTableStyleType(int)` selecciona uno de los estilos predefinidos con nombre que Excel 2007 introdujo para tablas dinámicas. La enumeración `PivotTableStyleType` expone tres familias de temas: la familia clara, desde `PIVOT_TABLE_STYLE_LIGHT1` hasta `PIVOT_TABLE_STYLE_LIGHT28`, la familia media, desde `PIVOT_TABLE_STYLE_MEDIUM1` hasta `PIVOT_TABLE_STYLE_MEDIUM28`, y la familia oscura, desde `PIVOT_TABLE_STYLE_DARK1` hasta `PIVOT_TABLE_STYLE_DARK_28`. También define `None` y `Custom`. Los miembros de número más alto de cada familia corresponden a los estilos agregados en Excel 2017.
Estas predefiniciones son de solo lectura. Tan pronto como necesite cambiar colores, bordes o fuentes más allá de lo que una predefinición ofrece, deberá definir un estilo de tabla dinámica personalizado, como se muestra en el [Escenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**¿Por qué usar las predefiniciones modernas y no los autoformateos de la serie Report?** Los valores `Report1` hasta `Report10` y `Table1` hasta `Table10` de `PivotTableAutoFormatType` son anteriores a los campos de columna en tablas dinámicas, por lo que no incluyen estilos para las cabeceras de los campos de columna, y Excel las renderiza sin estilo. Las predefiniciones `PivotTableStyleType` se diseñaron para el diseño bidimensional que utiliza Excel en las versiones modernas, aplicando estilos tanto a las cabeceras de los campos de fila como a las de los campos de columna.
{{% /alert %}}

Este escenario reutiliza el conjunto de datos Fruta/Año/Cantidad del Escenario 1, agrega `Year` al área de columnas junto con el campo de fila `Fruit` mediante `PivotFieldType.COLUMN`, aplica la predefinición de tema oscuro `PIVOT_TABLE_STYLE_DARK1` con `pivotTable.setPivotTableStyleType`, y guarda el resultado como `.xlsx` —el formato para el cual `PivotTableStyleType` tiene sentido.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
// Add a pivot table at E3 named "Pivot1", sourced from A1:C10
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Apply a modern Excel 2007+ named preset pivot style.
// PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
// is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
// family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
// newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);
// Save as modern .xlsx - this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx");
```
## **Definir y aplicar un estilo personalizado a una tabla dinámica**
Los preajustes integrados no se pueden modificar. Siempre que necesite sobrescribir colores, bordes o fuentes, debe definir un estilo personalizado para la tabla dinámica. El flujo de trabajo consta de tres pasos:
1. Añada un estilo personalizado a la colección `TableStyles` del libro mediante `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WholeTable` o `GrandTotalRow`) mediante `TableStyle.getTableStyleElements().add(TableStyleElementType)`, y luego asigne un `Style` a cada elemento mediante `TableStyleElement.setElementStyle(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica asignando `PivotTable.PivotTableStyleName` al nombre del estilo. No utilice aquí `PivotTableStyleType`, ya que esa propiedad selecciona los preajustes integrados.

{{% alert color="primary" %}}
`PivotTableStyleName` y `PivotTableStyleType` no son intercambiables. Use `PivotTableStyleType` para los preajustes integrados, y `PivotTableStyleName` para los estilos personalizados que haya definido mediante `addPivotTableStyle`. Configurar ambas no causa problemas, pero solo se representa la que coincide con el origen previsto.
Los valores disponibles de `TableStyleElementType` incluyen `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` y `PAGE_FIELD_VALUES`.
El siguiente ejemplo define un estilo personalizado de tabla dinámica con un borde negro fino en `WholeTable` y una fuente roja en negrita en `GrandTotalRow`, lo aplica mediante `PivotTableStyleName` y guarda como `.xlsx`.
{{% /alert %}}

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Llenar datos fuente: fila de encabezado + 9 filas de datos (A1:C10)
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
// Agregar tabla dinámica con origen A1:C10, anclada en E3, llamada "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Paso 1: registrar un nuevo estilo personalizado de tabla dinámica y capturar su índice
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Paso 2: agregar un elemento WholeTable y aplicar bordes negros finos en los cuatro lados
int wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE);
TableStyleElement wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
Style wholeTableStyle = workbook.createStyle();
BorderCollection borders = wholeTableStyle.getBorders();
Border borderTop = borders.getByBorderType(BorderType.TOP_BORDER);
borderTop.setLineStyle(CellBorderType.THIN);
borderTop.setColor(Color.getBlack());
Border borderBottom = borders.getByBorderType(BorderType.BOTTOM_BORDER);
borderBottom.setLineStyle(CellBorderType.THIN);
borderBottom.setColor(Color.getBlack());
Border borderLeft = borders.getByBorderType(BorderType.LEFT_BORDER);
borderLeft.setLineStyle(CellBorderType.THIN);
borderLeft.setColor(Color.getBlack());
Border borderRight = borders.getByBorderType(BorderType.RIGHT_BORDER);
borderRight.setLineStyle(CellBorderType.THIN);
borderRight.setColor(Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// Paso 3: agregar un elemento GrandTotalRow y aplicar fuente roja en negrita
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Paso 4: aplicar el estilo personalizado por nombre (NO por PivotTableStyleType, que es para estilos preestablecidos)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Aplicar un estilo a cada celda de la tabla dinámica con formatAll**
`PivotTable.formatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluyendo el área de datos, los encabezados de filas y columnas, y los totales. Lo que se haya configurado previamente mediante `PivotTableStyleType` o `PivotTableStyleName` queda sobrescrito.

{{% alert color="primary" %}}
`formatAll` sobrescribe tanto `PivotTableStyleType` como `PivotTableStyleName`. Úselo solo cuando se requiera una apariencia uniforme, independiente del tema, en toda la tabla dinámica.
El siguiente ejemplo crea un `Style` con relleno sólido amarillo, fuente azul oscuro en negrita y bordes negros finos en todos los lados, lo aplica con `formatAll` y guarda como `.xlsx`.
{{% /alert %}}

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
// Rellenar datos de origen: fila de encabezado (fila 1) + 9 filas de datos (filas 2-10)
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
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Asignar campos dinámicos: Fruit -> área de fila, Year -> área de columna, Amount -> área de datos
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Construir un Style que se aplicará a cada celda de la tabla dinámica
Style style = workbook.createStyle();
style.setForegroundColor(Color.getYellow());
style.setPattern(BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(Color.getDarkBlue());
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack());
// Aplicar formatAll: fuerza este único estilo sobre cada celda de la tabla dinámica,
// anulando cualquier PivotTableStyleType / PivotTableStyleName establecido previamente
pivotTable.formatAll(style);
// Guardar el workbook en el formato moderno .xlsx
workbook.save("output.xlsx");
```

## **¿Qué API de estilos debo usar?**
La elección de la API de estilos depende del formato de archivo al que está guardando. Utilice la tabla siguiente como referencia rápida.
| Formato de archivo de destino | API a utilizar | Notas |
|---|---|---|
| `.xls` (heredado) | `PivotTable.AutoFormatType` | Valores de `com.aspose.cells.PivotTableAutoFormatType` (p. ej. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `PivotTable.PivotTableStyleType` | Valores de `com.aspose.cells.PivotTableStyleType` (temas claros/oscuros, incluidas las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | Úselo cuando los preajustes integrados no sean suficientes. Configúrelo mediante `TableStyleElement.setElementStyle(...)`. |
| Cualquier formato (anulación uniforme) | `PivotTable.formatAll(Style)` | Atajo que sobrescribe cualquier otra configuración de estilo en toda la tabla dinámica. |
En caso de duda, guarde como `.xlsx` y use `PivotTableStyleType` para los temas integrados, o `PivotTableStyleName` para los temas personalizados.


{{< app/cells/assistant language="java" >}}