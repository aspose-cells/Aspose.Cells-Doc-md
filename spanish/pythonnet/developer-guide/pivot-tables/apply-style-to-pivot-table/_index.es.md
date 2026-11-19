---
title: Aplicar estilos a tablas dinámicas en Aspose.Cells for Python via .NET
description: Aprenda a aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for Python via .NET, abarcando autoformatos heredados de XLS, estilos con nombre modernos de Excel 2007+, estilos personalizados para tablas dinámicas y el atajo _format_all.
linktitle: Aplicar estilos a tablas dinámicas
keywords: Aspose.Cells Python via .NET estilo de tabla dinámica, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la aplicación de autoformatos heredados para tablas dinámicas (diseñados para archivos `.xls`) y estilos modernos con nombre o personalizados para tablas dinámicas (diseñados para archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe utilizar depende del formato de archivo en el que se guarda el libro, no del formato desde el que se cargó.
{{% /alert %}}

## **Introducción**
Aspose.Cells expone dos API de estilos paralelas para tablas dinámicas. La decisión entre ellas depende del formato de archivo en el que guarda el libro, no del formato desde el que lo lee. Un libro cargado desde un archivo `.xls` puede guardarse de nuevo como `.xlsx`, y en ese caso se aplica la API de estilos moderna en lugar de la heredada.
- `PivotTable.pivot_table_style_type` selecciona uno de los estilos con nombre integrados (temas claros y oscuros, incluidos los estilos añadidos en Excel 2017). Estos preajustes son de solo lectura.
- `PivotTable.pivot_table_style_name` selecciona un estilo personalizado que usted mismo define mediante `workbook.worksheets.table_styles.add_pivot_table_style(...)`. Los estilos personalizados son obligatorios siempre que desee modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.
Además, `PivotTable.format_all(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, anulando lo establecido mediante cualquiera de las dos API de nombre de estilo anteriores. Esto resulta útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato preestablecido heredado de XLS**
`PivotTable.auto_format_type` acepta un valor de la enumeración `aspose.cells.pivot.PivotTableAutoFormatType`. Los valores disponibles son `REPORT_1` a `REPORT_10`, `CLASSIC` y `TABLE_1` a `TABLE_10`.
El siguiente ejemplo carga un libro nuevo, rellena los datos de ejemplo de Fruta/Año/Importe, añade una tabla dinámica, aplica `PivotTableAutoFormatType.REPORT5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}
**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas de una sola dimensión** con campos de fila y valores únicamente; no cuentan con estilos integrados para los encabezados de campos de columna. Si su tabla dinámica necesita campos de columna, utilice en su lugar los preajustes modernos `PivotTableStyleType` del [Escenario 2](#apply-a-modern-named-preset-pivot-table-style), que están diseñados para el diseño bidimensional que utiliza el Excel moderno.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotTableAutoFormatType
# Scenario 1: Apply a legacy XLS preset autoformat
# API in use: PivotTable.AutoFormatType
# Target file format: .xls (legacy)
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Create a new workbook
workbook = ac.Workbook()
# Get the first worksheet
sheet = workbook.worksheets[0]
# Populate the source data with header row (Fruit, Year, Amount)
# and 9 data rows covering grape, blueberry, kiwi, cherry across 2020 and 2021
sheet.cells.get(0, 0).put_value("Fruit")
sheet.cells.get(0, 1).put_value("Year")
sheet.cells.get(0, 2).put_value("Amount")
sheet.cells.get(1, 0).put_value("grape")
sheet.cells.get(1, 1).put_value(2020)
sheet.cells.get(1, 2).put_value(50)
sheet.cells.get(2, 0).put_value("blueberry")
sheet.cells.get(2, 1).put_value(2020)
sheet.cells.get(2, 2).put_value(30)
sheet.cells.get(3, 0).put_value("kiwi")
sheet.cells.get(3, 1).put_value(2020)
sheet.cells.get(3, 2).put_value(25)
sheet.cells.get(4, 0).put_value("cherry")
sheet.cells.get(4, 1).put_value(2020)
sheet.cells.get(4, 2).put_value(40)
sheet.cells.get(5, 0).put_value("grape")
sheet.cells.get(5, 1).put_value(2021)
sheet.cells.get(5, 2).put_value(60)
sheet.cells.get(6, 0).put_value("blueberry")
sheet.cells.get(6, 1).put_value(2021)
sheet.cells.get(6, 2).put_value(35)
sheet.cells.get(7, 0).put_value("kiwi")
sheet.cells.get(7, 1).put_value(2021)
sheet.cells.get(7, 2).put_value(28)
sheet.cells.get(8, 0).put_value("cherry")
sheet.cells.get(8, 1).put_value(2021)
sheet.cells.get(8, 2).put_value(45)
sheet.cells.get(9, 0).put_value("grape")
sheet.cells.get(9, 1).put_value(2020)
sheet.cells.get(9, 2).put_value(45)
# Add a pivot table at destination cell E3, using source range A1:C10
pivot_table = sheet.pivot_tables.add("A1:C10", 2, 4)
# Assign fields: Fruit -> Rows, Amount -> Data
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Apply the legacy XLS preset autoformat "Report5"
# Note: This property is only meaningful when saving as .xls.
# When saved as .xlsx/.xlsm/.xlsb, Excel ignores AutoFormatType
# and uses whatever PivotTableStyleType / PivotTableStyleName specifies.
pivot_table.auto_format_type = PivotTableAutoFormatType.REPORT5
# Save the workbook in legacy .xls format
workbook.save("output.xls")
```

## **Aplicar un estilo de tabla dinámica preestablecido moderno con nombre**
`pivot_table.pivot_table_style_type` selecciona uno de los estilos predefinidos con nombre que Excel 2007 introdujo para tablas dinámicas. La enumeración `PivotTableStyleType` expone tres familias de temas: la familia clara, desde `PIVOT_TABLE_STYLE_LIGHT1` hasta `PIVOT_TABLE_STYLE_LIGHT28`; la familia media, desde `PIVOT_TABLE_STYLE_MEDIUM1` hasta `PIVOT_TABLE_STYLE_MEDIUM28`; y la familia oscura, desde `PIVOT_TABLE_STYLE_DARK1` hasta `PIVOT_TABLE_STYLE_DARK28`. Además, define los valores `None` y `Custom`. Los miembros numerados más altamente de cada familia corresponden a los estilos añadidos en Excel 2017.
Estas predefiniciones son de solo lectura. En cuanto necesite cambiar colores, bordes o fuentes más allá de lo que una predefinición ofrece, debe definir un estilo de tabla dinámica personalizado, como se muestra en [Escenario 3](#define-and-apply-a-custom-pivot-table-style).

{{% alert color="primary" %}}
**¿Por qué usar las predefiniciones modernas y no los autoformateos de la serie Report?** Los valores `Report1` hasta `Report10` y `Table1` hasta `Table10` de `PivotTableAutoFormatType` son anteriores a los campos de columna de tabla dinámica, por lo que no contienen estilos para las cabeceras de campo de columna, y Excel las renderiza sin estilo. Las predefiniciones `PivotTableStyleType` fueron diseñadas para el diseño bidimensional que utiliza Excel moderno y aplican estilos tanto a las cabeceras de campo de fila como a las de campo de columna.
{{% /alert %}}

Este escenario reutiliza el conjunto de datos Fruta/Año/Cantidad del Escenario 1, añade `Year` al área de columnas junto al campo de fila `Fruit` mediante `PivotFieldType.COLUMN`, aplica la predefinición de tema oscuro `PIVOT_TABLE_STYLE_DARK1` con `pivot_table.pivot_table_style_type` y guarda el resultado como `.xlsx`, el formato para el cual `PivotTableStyleType` tiene sentido.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotTableStyleType
# Scenario 2: Apply a modern Excel 2007+ named preset style using PivotTableStyleType.
# Target file format: .xlsx. PivotTableStyleType lives in aspose.cells.pivot,
# so it is imported explicitly alongside PivotFieldType.
# GitHub reference: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Header row: Fruit / Year / Amount
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
# 9 data rows of Fruit / Year / Amount
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(150)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(200)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(180)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(120)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(170)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(210)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(190)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(130)
# Add a pivot table at E3, sourced from A1:C10
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Apply a modern Excel 2007+ named preset pivot style.
# PivotTableStyleType is the correct API for .xlsx / .xlsm / .xlsb files; AutoFormatType
# is ignored by Excel for those formats. PIVOT_TABLE_STYLE_DARK1 belongs to the dark-theme
# family (PIVOT_TABLE_STYLE_DARK1..PIVOT_TABLE_STYLE_DARK28), and the same enum also exposes
# the newer Excel 2017 themes (PIVOT_TABLE_STYLE_LIGHT1..LIGHT28 / DARK1..DARK28).
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_DARK1
# Save as modern .xlsx — this is the format for which PivotTableStyleType is meaningful.
workbook.save("output.xlsx")
```

## **Definir y aplicar un estilo personalizado de tabla dinámica**
Los preajustes integrados no se pueden modificar. Siempre que necesite anular colores, bordes o fuentes, debe definir un estilo personalizado para tablas dinámicas. El flujo de trabajo consta de tres pasos:
1. Añada un estilo personalizado a la colección `table_styles` del libro mediante `workbook.worksheets.table_styles.add_pivot_table_style(name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WHOLE_TABLE` o `GRAND_TOTAL_ROW`) mediante `table_style.table_style_elements.add(TableStyleElementType)` y, a continuación, asigne un `Style` a cada elemento con `table_style_element.set_element_style(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica asignando a `PivotTable.pivot_table_style_name` el nombre del estilo. No use aquí `pivot_table_style_type`, ya que esa propiedad selecciona los preajustes integrados.

{{% alert color="primary" %}}
`pivot_table_style_name` y `pivot_table_style_type` no son intercambiables. Use `pivot_table_style_type` para los preajustes integrados y `pivot_table_style_name` para los estilos personalizados que haya definido mediante `add_pivot_table_style`. Establecer ambas es inofensivo, pero solo se representa la que coincida con el origen previsto.
Los valores disponibles de `TableStyleElementType` incluyen `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` y `PAGE_FIELD_VALUES`.
El siguiente ejemplo define un estilo personalizado para tablas dinámicas con un borde negro fino en `WHOLE_TABLE` y una fuente roja en negrita en `GRAND_TOTAL_ROW`, lo aplica mediante `pivot_table_style_name` y guarda como `.xlsx`.
{{% /alert %}}

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.tables import TableStyleElementType
from aspose.pydrawing import Color
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Populate source data: header row + 9 data rows (A1:C10)
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(100)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(200)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(300)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(400)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(500)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(600)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(700)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(800)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(900)
# Add pivot table sourced from A1:C10, anchored at E3
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Step 1: register a new custom pivot table style and capture its index
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]
# Step 2: add a WholeTable element and apply thin black borders on all four sides
whole_table_element_index = table_style.table_style_elements.add(TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders.get(ac.BorderType.TOP_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.TOP_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.BOTTOM_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.BOTTOM_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.LEFT_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.LEFT_BORDER).color = Color.black
whole_table_style.borders.get(ac.BorderType.RIGHT_BORDER).line_style = ac.CellBorderType.THIN
whole_table_style.borders.get(ac.BorderType.RIGHT_BORDER).color = Color.black
whole_table_element.set_element_style(whole_table_style)
# Step 3: add a GrandTotalRow element and apply bold red font
grand_total_element_index = table_style.table_style_elements.add(TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = Color.red
grand_total_element.set_element_style(grand_total_style)
# Step 4: apply the custom style by name (NOT by PivotTableStyleType, which is for built-in presets)
pivot_table.pivot_table_style_name = "CustomPivotStyle"
workbook.save("output.xlsx")
```

## **Aplicar un único estilo a todas las celdas de la tabla dinámica con format_all**
`PivotTable.format_all(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluido el área de datos, los encabezados de filas y columnas y los totales. Todo lo establecido previamente mediante `pivot_table_style_type` o `pivot_table_style_name` queda anulado.

{{% alert color="primary" %}}
`format_all` anula tanto `pivot_table_style_type` como `pivot_table_style_name`. Úselo solo cuando se requiera una apariencia uniforme e independiente del tema en toda la tabla dinámica.
El siguiente ejemplo crea un `Style` con un relleno amarillo sólido, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, lo aplica con `format_all` y guarda como `.xlsx`.
{{% /alert %}}

```python
from aspose.pydrawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType
# Scenario 4: Apply a single Style to every pivot table cell using format_all
# API in use: PivotTable.format_all(Style)
# Target format: .xlsx
# GitHub reference: see Aspose.Cells-for-.NET repository — pivot table styling examples
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Populate source data: header row (row 1) + 9 data rows (rows 2-10)
worksheet.cells.get("A1").put_value("Fruit")
worksheet.cells.get("B1").put_value("Year")
worksheet.cells.get("C1").put_value("Amount")
worksheet.cells.get("A2").put_value("Grape")
worksheet.cells.get("B2").put_value(2020)
worksheet.cells.get("C2").put_value(5000)
worksheet.cells.get("A3").put_value("Blueberry")
worksheet.cells.get("B3").put_value(2020)
worksheet.cells.get("C3").put_value(3000)
worksheet.cells.get("A4").put_value("Kiwi")
worksheet.cells.get("B4").put_value(2020)
worksheet.cells.get("C4").put_value(4000)
worksheet.cells.get("A5").put_value("Cherry")
worksheet.cells.get("B5").put_value(2020)
worksheet.cells.get("C5").put_value(2000)
worksheet.cells.get("A6").put_value("Grape")
worksheet.cells.get("B6").put_value(2021)
worksheet.cells.get("C6").put_value(6000)
worksheet.cells.get("A7").put_value("Blueberry")
worksheet.cells.get("B7").put_value(2021)
worksheet.cells.get("C7").put_value(3500)
worksheet.cells.get("A8").put_value("Kiwi")
worksheet.cells.get("B8").put_value(2021)
worksheet.cells.get("C8").put_value(4500)
worksheet.cells.get("A9").put_value("Cherry")
worksheet.cells.get("B9").put_value(2021)
worksheet.cells.get("C9").put_value(2500)
worksheet.cells.get("A10").put_value("Grape")
worksheet.cells.get("B10").put_value(2021)
worksheet.cells.get("C10").put_value(5500)
# Add pivot table: source range A1:C10, destination cell E3
pivot_table = worksheet.pivot_tables.add("A1:C10", 2, 4)
# Assign pivot fields: Fruit -> Row area, Year -> Column area, Amount -> Data area
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Build a Style that will be forced onto every cell of the pivot table
style = workbook.create_style()
style.foreground_color = Color.yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.dark_blue
style.borders.get(BorderType.TOP_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.TOP_BORDER).color = Color.black
style.borders.get(BorderType.BOTTOM_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.BOTTOM_BORDER).color = Color.black
style.borders.get(BorderType.LEFT_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.LEFT_BORDER).color = Color.black
style.borders.get(BorderType.RIGHT_BORDER).line_style = CellBorderType.THIN
style.borders.get(BorderType.RIGHT_BORDER).color = Color.black
# Apply format_all: forces this single style onto every cell of the pivot table,
# overriding any PivotTableStyleType / PivotTableStyleName previously set
pivot_table.format_all(style)
# Save the workbook in the modern .xlsx format
workbook.save("output.xlsx")
```

## **¿Qué API de estilos debo usar?**
La elección de la API de estilos depende del formato de archivo en el que está guardando. Utilice la tabla siguiente como referencia rápida.
| Formato de archivo de destino | API que debe usar | Notas |
|---|---|---|
| `.xls` (heredado) | `PivotTable.auto_format_type` | Valores de `aspose.cells.pivot.PivotTableAutoFormatType` (por ejemplo, `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `PivotTable.pivot_table_style_type` | Valores de `aspose.cells.PivotTableStyleType` (temas claros y oscuros, incluidas las incorporaciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Úselo cuando los preajustes integrados no sean suficientes. Configúrelo mediante `table_style_element.set_element_style(...)`. |
| Cualquier formato (anulación uniforme) | `PivotTable.format_all(Style)` | Atajo que anula cualquier otra configuración de estilo en toda la tabla dinámica. |
En caso de duda, guarde como `.xlsx` y use `pivot_table_style_type` para los temas integrados, o `pivot_table_style_name` para los temas personalizados.

{{< app/cells/assistant language="python-net" >}}