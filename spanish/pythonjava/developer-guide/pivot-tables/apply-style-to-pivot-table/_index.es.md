---
title: Aplicar estilos a tablas dinámicas en Aspose.Cells for Python via Java
description: Aprenda a aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for Python via Java, incluyendo autoformatos heredados de XLS, estilos con nombre modernos de Excel 2007+, estilos personalizados de tabla dinámica y el atajo formatAll.
linktitle: Aplicar estilos a tablas dinámicas
keywords: Aspose.Cells Python via Java estilo de tabla dinámica, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la aplicación tanto de autoformatos heredados para tablas dinámicas (pensados para archivos `.xls`) como de estilos con nombre modernos o personalizados para tablas dinámicas (pensados para archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe llamar depende del formato de archivo en el que se guarde el libro, no del formato desde el que se haya cargado.
{{% /alert %}}

## **Introducción**
Aspose.Cells expone dos API de estilos paralelas para tablas dinámicas. La decisión entre ellas depende del formato de archivo en el que guarde el libro, no del formato desde el que lo lea. Un libro cargado desde un archivo `.xls` puede volver a guardarse como `.xlsx`, y en ese caso se aplica la API de estilos moderna en lugar de la heredada.
- `pivotTable.setPivotTableStyleType(int)` selecciona uno de los estilos con nombre integrados (temas claros y oscuros, incluidos los estilos añadidos en Excel 2017). Estos preajustes son de solo lectura.
- `pivotTable.setPivotTableStyleName(String)` selecciona un estilo personalizado que usted mismo define mediante `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. Los estilos personalizados son necesarios cuando desea modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.
Además, `pivotTable.formatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, anulando lo que se haya establecido mediante cualquiera de las API de nombres de estilo anteriores. Esto resulta útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato preestablecido heredado de XLS**
El método `setAutoFormatType` en una tabla dinámica acepta un valor de la enumeración `com.aspose.cells.pivot.PivotTableAutoFormatType`. Los valores disponibles son `REPORT_1` a `REPORT_10`, `CLASSIC` y `TABLE_1` a `TABLE_10`.
El siguiente ejemplo carga un libro nuevo, rellena los datos de muestra Fruta/Año/Importe, agrega una tabla dinámica, aplica `PivotTableAutoFormatType.REPORT_5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}
**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para tablas dinámicas **unidimensionales** con solo campos de fila y valores, ya que no disponen de estilos integrados para los encabezados de campos de columna. Si su tabla dinámica necesita campos de columna, utilice en su lugar los preajustes modernos `PivotTableStyleType` del [Escenario 2](#apply-a-modern-named-preset-pivot-table-style), que están diseñados para el diseño bidimensional que utiliza el Excel moderno.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType
# Scenario 1: Apply a legacy XLS preset autoformat
# API in use: PivotTable.AutoFormatType
# Target file format: .xls (legacy)
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Create a new workbook
workbook = Workbook()
# Get the first worksheet
sheet = workbook.getWorksheets().get(0)
# Populate the source data with header row (Fruit, Year, Amount)
# and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")
sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)
sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)
sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)
sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)
sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)
sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)
sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)
sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)
sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)
# Add a pivot table at destination cell E3, using source range A1:C10
pivotTable = sheet.getPivotTables().add("A1:C10", 2, 4)
# Assign fields: Fruit -> Rows, Amount -> Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Apply the legacy XLS preset autoformat "Report5"
# Note: This property is only meaningful when saving as .xls.
# When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
# and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5)
# Save the workbook in legacy .xls format
workbook.save("output.xls")
jpype.shutdownJVM()
```

## **Aplicar un estilo de tabla dinámica preestablecido con nombre moderno**
`pivotTable.setPivotTableStyleType(int)` selecciona uno de los estilos integrados con nombre que Excel 2007 introdujo para las tablas dinámicas. La enumeración `PivotTableStyleType` expone tres familias de temas: la familia clara desde `PIVOT_TABLE_STYLE_LIGHT1` hasta `PIVOT_TABLE_STYLE_LIGHT28`, la familia media desde `PIVOT_TABLE_STYLE_MEDIUM1` hasta `PIVOT_TABLE_STYLE_MEDIUM28` y la familia oscura desde `PIVOT_TABLE_STYLE_DARK1` hasta `PIVOT_TABLE_STYLE_DARK_28`. También define `None` y `Custom`. Los miembros con números más altos de cada familia son los estilos agregados en Excel 2017.
Estos preajustes son de solo lectura. En cuanto necesite cambiar los colores, los bordes o las fuentes más allá de lo que ofrece un preajuste, tendrá que definir un estilo personalizado de tabla dinámica, como se muestra en [Escenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**¿Por qué los preajustes modernos y no los autoformatos de la serie de informes?** Los valores `Report1` a `Report10` y `Table1` a `Table10` de `PivotTableAutoFormatType` son anteriores a los campos de columna de las tablas dinámicas, por lo que no incluyen estilos para los encabezados de los campos de columna y Excel representa esos encabezados sin estilo. Los preajustes de `PivotTableStyleType` se diseñaron para la disposición bidimensional que utiliza Excel moderno y dan estilo tanto a los encabezados de los campos de fila como a los de los campos de columna.
{{% /alert %}}

Este escenario reutiliza el conjunto de datos Fruit/Year/Amount del Escenario 1, agrega `Year` al área de columnas junto con el campo de fila `Fruit` mediante `PivotFieldType.COLUMN`, aplica el preajuste del tema oscuro `PIVOT_TABLE_STYLE_DARK1` con `pivotTable.setPivotTableStyleType` y guarda el resultado como `.xlsx`, el formato para el que `PivotTableStyleType` es relevante.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. The PivotTableStyleType enum lives in the Aspose.Cells namespace
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Header row: Fruit / Year / Amount
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
# 9 data rows of Fruit / Year / Amount
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(150)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(180)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(120)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(170)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(210)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(190)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(130)
# Add a pivot table at E3, sourced from A1:C10
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PivotTableStyleDark1 belongs to the dark-theme
# family (PivotTableStyleDark1..PivotTableStyleDark28), and the same enum also exposes the
# newer Excel 2017 light/dark themes (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1)
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Definir y aplicar un estilo personalizado de tabla dinámica**
Los preajustes integrados no se pueden modificar. Siempre que necesite anular colores, bordes o fuentes, debe definir un estilo personalizado para tabla dinámica. El flujo de trabajo consta de tres pasos:
1. Agregue un estilo personalizado a la colección `TableStyles` del libro mediante `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WHOLE_TABLE` o `GRAND_TOTAL_ROW`) mediante `tableStyle.getTableStyleElements().add(TableStyleElementType)` y, a continuación, asigne un `Style` a cada elemento con `tableStyleElement.setElementStyle(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica llamando a `pivotTable.setPivotTableStyleName(String)` con el nombre del estilo. No utilice aquí `setPivotTableStyleType`, ya que ese método selecciona preajustes integrados.

{{% alert color="primary" %}}
`setPivotTableStyleName` y `setPivotTableStyleType` no son intercambiables. Utilice `setPivotTableStyleType` para preajustes integrados y `setPivotTableStyleName` para estilos personalizados que haya definido mediante `addPivotTableStyle`. Establecer ambos es inofensivo, pero solo se representa el que coincide con el origen previsto.
Los valores disponibles de `TableStyleElementType` incluyen `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` y `PAGE_FIELD_VALUES`.
El siguiente ejemplo define un estilo personalizado para tabla dinámica con un borde negro fino en `WHOLE_TABLE` y una fuente roja en negrita en `GRAND_TOTAL_ROW`, lo aplica mediante `setPivotTableStyleName` y guarda como `.xlsx`.
{{% /alert %}}

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from asposecells.api import Color
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Populate source data: header row + 9 data rows (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)
# Add pivot table sourced from A1:C10, anchored at E3
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Step 1: register a new custom pivot table style and capture its index
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)
# Step 2: add a WholeTable element and apply thin black borders on all four sides
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
wholeTableElement.setElementStyle(wholeTableStyle)
# Step 3: add a GrandTotalRow element and apply bold red font
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.getRed())
grandTotalElement.setElementStyle(grandTotalStyle)
# Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivotTable.setPivotTableStyleName("CustomPivotStyle")
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Aplicar un único estilo a cada celda de la tabla dinámica con formatAll**
`pivotTable.formatAll(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluyendo el área de datos, los encabezados de fila y columna y los totales. Todo lo establecido previamente mediante `setPivotTableStyleType` o `setPivotTableStyleName` queda anulado.

{{% alert color="primary" %}}
`formatAll` anula tanto `setPivotTableStyleType` como `setPivotTableStyleName`. Utilícelo solo cuando se requiera una apariencia uniforme e independiente del tema en toda la tabla dinámica.
El siguiente ejemplo crea un `Style` con un relleno sólido amarillo, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, lo aplica con `formatAll` y guarda como `.xlsx`.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType
# Scenario 4: Apply a single Style to every pivot table cell using formatAll
# API in use: PivotTable.formatAll(Style)
# Target format: .xlsx
# GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)
# Add pivot table: source range A1:C10, destination cell E3
pivotTable = worksheet.getPivotTables().add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Build a Style that will be forced onto every cell of the pivot table
style = workbook.createStyle()
style.setForegroundColor(Color.fromArgb(70, 130, 180))
style.setPattern(BackgroundType.SOLID)
style.getFont().setBold(True)
style.getFont().setColor(Color.getDarkBlue())
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack())
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack())
# Apply formatAll: forces this single style onto every cell of the pivot table,
# overriding any PivotTableStyleType / PivotTableStyleName previously set
pivotTable.formatAll(style)
# Save the workbook in the modern .xlsx format
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **¿Qué API de estilo debo utilizar?**
La elección de la API de estilo depende del formato de archivo en el que esté guardando. Utilice la tabla siguiente como referencia rápida.
| Formato de archivo de destino | API a utilizar | Notas |
|---|---|---|
| `.xls` (heredado) | `pivotTable.setAutoFormatType(int)` | Valores de `com.aspose.cells.pivot.PivotTableAutoFormatType` (p. ej., `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `pivotTable.setPivotTableStyleType(int)` | Valores de `com.aspose.cells.PivotTableStyleType` (temas claros/oscuros, incluidas las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Utilícelo cuando los preajustes integrados no sean suficientes. Configure mediante `tableStyleElement.setElementStyle(Style)`. |
| Cualquier formato (anulación uniforme) | `pivotTable.formatAll(Style)` | Atajo que anula cualquier otra configuración de estilo en toda la tabla dinámica. |
En caso de duda, guarde como `.xlsx` y utilice `setPivotTableStyleType` para temas integrados, o `setPivotTableStyleName` para temas personalizados.

{{< app/cells/assistant language="python" >}}