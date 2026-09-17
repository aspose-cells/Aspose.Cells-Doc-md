---
title: Aplicar estilos a tablas dinámicas en Aspose.Cells for Python via .NET
description: Aprenda a aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for Python via .NET, abarcando autoformatos heredados de XLS, estilos con nombre modernos de Excel 2007+, estilos personalizados para tablas dinámicas y el atajo FormatAll.
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
El siguiente ejemplo carga un libro nuevo, rellena los datos de ejemplo de Fruta/Año/Importe, añade una tabla dinámica, aplica `PivotTableAutoFormatType.REPORT_5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}
**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas de una sola dimensión** con campos de fila y valores únicamente; no cuentan con estilos integrados para los encabezados de campos de columna. Si su tabla dinámica necesita campos de columna, utilice en su lugar los preajustes modernos `PivotTableStyleType` del [Escenario 2](#apply-a-modern-named-preset-pivot-table-style), que están diseñados para el diseño bidimensional que utiliza el Excel moderno.
{{% /alert %}}

```python
import aspose.cells as ac
# Escenario 1: Aplicar un autoformato preestablecido de XLS heredado
# API en uso: PivotTable.AutoFormatType
# Formato de archivo de destino: .xls (heredado)
# Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Crear un nuevo libro de trabajo
workbook = ac.Workbook()
# Obtener la primera hoja de cálculo
sheet = workbook.worksheets[0]
# Llenar los datos de origen con la fila de encabezado (Fruta, Año, Cantidad)
# y 9 filas de datos que cubren uva, arándano, kiwi, cereza entre 2020 y 2021
sheet.cells[0, 0].put_value("Fruit")
sheet.cells[0, 1].put_value("Year")
sheet.cells[0, 2].put_value("Amount")
sheet.cells[1, 0].put_value("grape")
sheet.cells[1, 1].put_value(2020)
sheet.cells[1, 2].put_value(50)
sheet.cells[2, 0].put_value("blueberry")
sheet.cells[2, 1].put_value(2020)
sheet.cells[2, 2].put_value(30)
sheet.cells[3, 0].put_value("kiwi")
sheet.cells[3, 1].put_value(2020)
sheet.cells[3, 2].put_value(25)
sheet.cells[4, 0].put_value("cherry")
sheet.cells[4, 1].put_value(2020)
sheet.cells[4, 2].put_value(40)
sheet.cells[5, 0].put_value("grape")
sheet.cells[5, 1].put_value(2021)
sheet.cells[5, 2].put_value(60)
sheet.cells[6, 0].put_value("blueberry")
sheet.cells[6, 1].put_value(2021)
sheet.cells[6, 2].put_value(35)
sheet.cells[7, 0].put_value("kiwi")
sheet.cells[7, 1].put_value(2021)
sheet.cells[7, 2].put_value(28)
sheet.cells[8, 0].put_value("cherry")
sheet.cells[8, 1].put_value(2021)
sheet.cells[8, 2].put_value(45)
sheet.cells[9, 0].put_value("grape")
sheet.cells[9, 1].put_value(2020)
sheet.cells[9, 2].put_value(45)
# Agregar una tabla dinámica en la celda de destino E3, llamada "Pivot1", usando el rango de origen A1:C10
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]
# Asignar campos: Fruta -> Filas, Cantidad -> Datos
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# Aplicar el autoformato preestablecido "Report5" de XLS heredado
# Nota: Esta propiedad solo es significativa al guardar como .xls.
# Al guardar como .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
# y usa lo que especifique PivotTableStyleType / PivotTableStyleName.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5
# Guardar el libro de trabajo en formato .xls heredado
workbook.save("output.xls")
```

## **Aplicar un estilo de tabla dinámica preestablecido moderno con nombre**

## **Definir y aplicar un estilo personalizado de tabla dinámica**
Los preajustes integrados no se pueden modificar. Siempre que necesite anular colores, bordes o fuentes, debe definir un estilo personalizado para tablas dinámicas. El flujo de trabajo consta de tres pasos:
1. Añada un estilo personalizado a la colección `table_styles` del libro mediante `workbook.worksheets.table_styles.add_pivot_table_style(name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WHOLE_TABLE` o `GRAND_TOTAL_ROW`) mediante `table_style.table_style_elements.add(TableStyleElementType)` y, a continuación, asigne un `Style` a cada elemento con `table_style_element.set_element_style(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica asignando a `PivotTable.pivot_table_style_name` el nombre del estilo. No use aquí `pivot_table_style_type`, ya que esa propiedad selecciona los preajustes integrados.

{{% alert color="primary" %}}
`pivot_table_style_name` y `pivot_table_style_type` no son intercambiables. Use `pivot_table_style_type` para los preajustes integrados y `pivot_table_style_name` para los estilos personalizados que haya definido mediante `add_pivot_table_style`. Establecer ambas es inofensivo, pero solo se representa la que coincida con el origen previsto.
{{% /alert %}}

Los valores disponibles de `TableStyleElementType` incluyen `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` y `PAGE_FIELD_VALUES`.
El siguiente ejemplo define un estilo personalizado para tablas dinámicas con un borde negro fino en `WHOLE_TABLE` y una fuente roja en negrita en `GRAND_TOTAL_ROW`, lo aplica mediante `pivot_table_style_name` y guarda como `.xlsx`.

```python
import aspose.cells as ac
import System.Drawing
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Poblar datos de origen: fila de encabezado + 9 filas de datos (A1:C10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)
worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)
worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)
worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)
worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)
worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)
worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)
worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)
worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)
# Agregar tabla dinámica desde A1:C10, anclada en E3, llamada "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# Paso 1: registrar un nuevo estilo personalizado de tabla dinámica y capturar su índice
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]
# Paso 2: agregar un elemento WholeTable y aplicar bordes negros finos en los cuatro lados
whole_table_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.TOP_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.LEFT_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].color = System.Drawing.Color.Black
whole_table_element.set_element_style(whole_table_style)
# Paso 3: agregar un elemento GrandTotalRow y aplicar fuente roja en negrita
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)
# Paso 4: aplicar el estilo personalizado por nombre (NO por PivotTableStyleType, que es para ajustes preestablecidos integrados)
pivot_table.pivot_table_style_name = "CustomPivotStyle"
workbook.save("output.xlsx")
```

## **Aplicar un único estilo a todas las celdas de la tabla dinámica con FormatAll**
`PivotTable.format_all(Style)` es un atajo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluido el área de datos, los encabezados de filas y columnas y los totales. Todo lo establecido previamente mediante `pivot_table_style_type` o `pivot_table_style_name` queda anulado.

{{% alert color="primary" %}}
`format_all` anula tanto `pivot_table_style_type` como `pivot_table_style_name`. Úselo solo cuando se requiera una apariencia uniforme e independiente del tema en toda la tabla dinámica.
{{% /alert %}}

El siguiente ejemplo crea un `Style` con un relleno amarillo sólido, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, lo aplica con `format_all` y guarda como `.xlsx`.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType
# Escenario 4: Aplicar un único Estilo a cada celda de la tabla dinámica usando FormatAll
# API en uso: PivotTable.FormatAll(Style)
# Formato de destino: .xlsx
# Referencia de GitHub: ver repositorio Aspose.Cells-for-.NET — ejemplos de estilo de tabla dinámica
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Poblar datos de origen: fila de encabezado (fila 1) + 9 filas de datos (filas 2-10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)
worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)
worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)
worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)
worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)
worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)
worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)
worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)
worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)
# Agregar tabla dinámica: rango de origen A1:C10, celda de destino E3, nombre "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Asignar campos de tabla dinámica: Fruit -> área de Fila, Year -> área de Columna, Amount -> área de Datos
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Construir un Estilo que será forzado en cada celda de la tabla dinámica
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black
# Aplicar FormatAll: fuerza este único estilo en cada celda de la tabla dinámica,
# anulando cualquier PivotTableStyleType / PivotTableStyleName establecido previamente
pivot_table.format_all(style)
# Guardar el libro en el formato moderno .xlsx
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