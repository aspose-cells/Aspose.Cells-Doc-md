---
title: Aplicar estilos a tablas dinámicas
linktitle: Aplicar estilos a tablas dinámicas
description: Aprenda cómo aplicar estilos integrados y personalizados a tablas dinámicas en Aspose.Cells for Python via .NET, incluyendo autoformatos heredados de XLS, estilos con nombre modernos de Excel 2007+, estilos personalizados de tablas dinámicas y el acceso directo FormatAll.
keywords: Aspose.Cells Python via .NET estilo de tabla dinámica, PivotTableStyleType, AutoFormatType, FormatAll, estilo personalizado, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /es/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la aplicación tanto de autoformatos heredados de tablas dinámicas (diseñados para archivos `.xls`) como de estilos modernos con nombre o personalizados para tablas dinámicas (diseñados para archivos `.xlsx`, `.xlsm` y `.xlsb`). La API que debe llamar depende del formato de archivo en el que se guarda el libro de trabajo, no del formato del que se cargó.

{{% /alert %}}

## **Introducción**

Aspose.Cells expone dos API de estilo paralelas para tablas dinámicas. La decisión entre ellas está determinada por el formato de archivo en el que guarda el libro de trabajo, no por el formato del que lo lee. Un libro de trabajo cargado desde un archivo `.xls` puede volver a guardarse como `.xlsx`, y en ese caso se aplica la API de estilo moderna en lugar de la heredada.

Para la salida heredada `.xls`, use la propiedad `PivotTable.auto_format_type` junto con la enumeración `aspose.cells.pivot.PivotTableAutoFormatType`. Esta API corresponde al selector de autoformato que Excel clásico ofrecía para las tablas dinámicas.

Para la salida moderna `.xlsx`, `.xlsm` y `.xlsb`, hay disponibles dos variantes de la API de estilo:

- `PivotTable.pivot_table_style_type` selecciona uno de los estilos con nombre integrados (temas claros y oscuros, incluidos los estilos añadidos en Excel 2017). Estos preajustes son de solo lectura.
- `PivotTable.pivot_table_style_name` selecciona un estilo personalizado que usted mismo define mediante `workbook.worksheets.table_styles.add_pivot_table_style(...)`. Los estilos personalizados son obligatorios cuando desea modificar colores, bordes o fuentes más allá de lo que ofrecen los preajustes.

Además, `PivotTable.format_all(Style)` es un acceso directo que aplica un único objeto `Style` a cada celda de la tabla dinámica, sobrescribiendo cualquier configuración establecida mediante cualquiera de las API de nombre de estilo anteriores. Esto es útil cuando se requiere una apariencia uniforme independientemente del tema subyacente.

## **Aplicar un autoformato preestablecido heredado de XLS**

`PivotTable.auto_format_type` acepta un valor de la enumeración `aspose.cells.pivot.PivotTableAutoFormatType`. Los valores disponibles son `REPORT_1` a `REPORT_10`, `CLASSIC` y `TABLE_1` a `TABLE_10`.

{{% alert color="primary" %}}

`auto_format_type` solo se respeta cuando el libro de trabajo se guarda como `.xls`. Cuando el mismo libro de trabajo se guarda como `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora esta propiedad y recurre a las configuraciones de `pivot_table_style_type` y `pivot_table_style_name`.

{{% /alert %}}

El siguiente ejemplo carga un libro de trabajo nuevo, rellena los datos de ejemplo Fruit/Year/Amount, añade una tabla dinámica, aplica `PivotTableAutoFormatType.REPORT_5` y guarda el resultado como `.xls`.

{{% alert color="primary" %}}

**¿Por qué no hay campos de columna?** Los autoformatos de la serie Report (`Report1` a `Report10`, `Table1` a `Table10`) se diseñaron en el Excel clásico para **tablas dinámicas unidimensionales** con solo campos de fila y valores — no tienen estilo integrado para los encabezados de campos de columna. Si tu tabla dinámica necesita campos de columna, usa los preajustes modernos `PivotTableStyleType` del Escenario 2 a continuación, que están diseñados para el diseño bidimensional que usa el Excel moderno.

{{% /alert %}}

```python
import aspose.cells as ac

# Escenario 1: Aplicar un autoformato preestablecido de XLS heredado
# API en uso: PivotTable.AutoFormatType
# Formato de archivo de destino: .xls (heredado)
# Para ver ejemplos completos y archivos de datos, visite https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Crear un nuevo libro de trabajo
workbook = ac.Workbook()

# Obtener la primera hoja de trabajo
sheet = workbook.worksheets[0]

# Rellenar los datos de origen con la fila de encabezado (Fruta, Año, Monto)
# y 9 filas de datos que abarcan uva, arándano, kiwi, cereza en 2020 y 2021
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

# Agregar una tabla dinámica en la celda de destino E3, con el nombre "Pivot1", usando el rango de origen A1:C10
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]

# Asignar campos: Fruta -> Filas, Año -> Columnas, Monto -> Datos
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")

# Aplicar el autoformato preestablecido heredado de XLS "Report5"
# Nota: Esta propiedad solo es significativa cuando se guarda como .xls.
# Cuando se guarda como .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
# y usa lo que especifiquen PivotTableStyleType / PivotTableStyleName.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5

# Guardar el libro de trabajo en formato .xls heredado
workbook.save("output.xls")
```

## **Aplicar un estilo preestablecido con nombre moderno de tabla dinámica**

`PivotTable.pivot_table_style_type` acepta un valor de la enumeración `aspose.cells.PivotTableStyleType`. La enumeración cubre los temas claros `PIVOT_TABLE_STYLE_LIGHT_1` a `PIVOT_TABLE_STYLE_LIGHT_28` y los temas oscuros `PIVOT_TABLE_STYLE_DARK_1` a `PIVOT_TABLE_STYLE_DARK_28`. Los estilos añadidos en Excel 2017 (la segunda oleada de temas claros y oscuros) se pueden acceder a través de la misma enumeración.

Esta es la API recomendada para cualquier formato de archivo moderno. A diferencia del autoformato heredado, el estilo seleccionado aquí es renderizado fielmente por Excel y sobrevive a las idas y vueltas a través de otras herramientas de Office.

El siguiente ejemplo utiliza los mismos datos Fruit/Year/Amount, crea una tabla dinámica idéntica, aplica `PIVOT_TABLE_STYLE_DARK_1` y guarda el libro de trabajo como `.xlsx`.

```python
import aspose.cells as ac

# Escenario 2: Aplicar un estilo preestablecido con nombre de Excel 2007+ usando PivotTableStyleType.
# Formato de archivo de destino: .xlsx. La enumeración PivotTableStyleType reside en el espacio de nombres Aspose.Cells
# (no en Aspose.Cells.Pivot); es por eso que no necesitamos ningún using adicional.
# Referencia de GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Fila de encabezado: Fruit / Year / Amount
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")

# 9 filas de datos de Fruit / Year / Amount
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)

worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(150)

worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(200)

worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(180)

worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(120)

worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(170)

worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(210)

worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(190)

worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(130)

# Agregar una tabla dinámica en E3 con el nombre "Pivot1", con origen en A1:C10
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Asignar campos de la tabla dinámica: Fruit -> área de fila, Year -> área de columna, Amount -> área de datos
pivot_table.add_field_to_area(ac.PivotFieldType.Row, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.Column, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.Data, "Amount")

# Aplicar un estilo preestablecido con nombre de tabla dinámica moderno de Excel 2007+.
# PivotTableStyleType es la API correcta para archivos .xlsx / .xlsm / .xlsb; AutoFormatType
# es ignorado por Excel para esos formatos. PivotTableStyleDark1 pertenece a la familia de temas oscuros
# (PivotTableStyleDark1..PivotTableStyleDark28), y la misma enumeración también expone los
# temas más nuevos claros/oscuros de Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivot_table.pivot_table_style_type = ac.PivotTableStyleType.PivotTableStyleDark1

# Guardar como .xlsx moderno; este es el formato para el cual PivotTableStyleType es significativo.
workbook.save("output.xlsx")
```

## **Definir y aplicar un estilo personalizado de tabla dinámica**

Los preajustes integrados no se pueden modificar. Siempre que necesite anular colores, bordes o fuentes, debe definir un estilo personalizado de tabla dinámica. El flujo de trabajo tiene tres pasos:

1. Añada un estilo personalizado a la colección `table_styles` del libro de trabajo mediante `workbook.worksheets.table_styles.add_pivot_table_style(name)`. Esto devuelve el índice del estilo recién creado.
2. Configure el estilo añadiendo elementos (como `WHOLE_TABLE` o `GRAND_TOTAL_ROW`) mediante `table_style.table_style_elements.add(TableStyleElementType)` y luego asigne un `Style` a cada elemento mediante `table_style_element.set_element_style(Style)`.
3. Aplique el estilo personalizado a la tabla dinámica estableciendo `PivotTable.pivot_table_style_name` con el nombre del estilo. No use `pivot_table_style_type` aquí, ya que esa propiedad selecciona los preajustes integrados.

{{% alert color="primary" %}}

`pivot_table_style_name` y `pivot_table_style_type` no son intercambiables. Use `pivot_table_style_type` para los preajustes integrados y `pivot_table_style_name` para los estilos personalizados que haya definido mediante `add_pivot_table_style`. Establecer ambos es inofensivo, pero solo se renderiza el que coincide con la fuente prevista.

{{% /alert %}}

Los valores disponibles de `TableStyleElementType` incluyen `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` y `PAGE_FIELD_VALUES`.

El siguiente ejemplo define un estilo personalizado de tabla dinámica con un borde negro fino en `WHOLE_TABLE` y una fuente roja en negrita en `GRAND_TOTAL_ROW`, luego lo aplica mediante `pivot_table_style_name` y guarda como `.xlsx`.

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

# Agregar tabla dinámica con origen en A1:C10, anclada en E3, con nombre "Pivot1"
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

# Paso 4: aplicar el estilo personalizado por nombre (NO por PivotTableStyleType, que es para ajustes predefinidos)
pivot_table.pivot_table_style_name = "CustomPivotStyle"

workbook.save("output.xlsx")
```

## **Aplicar un estilo a cada celda de la tabla dinámica con FormatAll**

`PivotTable.format_all(Style)` es un acceso directo que aplica un único objeto `Style` a cada celda de la tabla dinámica, incluyendo el área de datos, los encabezados de fila y columna y los totales. Cualquier configuración establecida previamente mediante `pivot_table_style_type` o `pivot_table_style_name` queda anulada.

{{% alert color="primary" %}}

`format_all` anula tanto `pivot_table_style_type` como `pivot_table_style_name`. Úselo solo cuando se requiera una apariencia uniforme e independiente del tema en toda la tabla dinámica.

{{% /alert %}}

El siguiente ejemplo crea un `Style` con un relleno sólido amarillo, una fuente azul oscuro en negrita y bordes negros finos en todos los lados, luego lo aplica con `format_all` y guarda como `.xlsx`.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType

# Escenario 4: Aplicar un único Estilo a cada celda de tabla dinámica usando FormatAll
# API en uso: PivotTable.FormatAll(Style)
# Formato de destino: .xlsx
# Referencia de GitHub: ver repositorio Aspose.Cells-for-.NET — ejemplos de estilo de tabla dinámica

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Poblar datos fuente: fila de encabezado (fila 1) + 9 filas de datos (filas 2-10)
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

# Agregar tabla dinámica: rango fuente A1:C10, celda de destino E3, nombre "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]

# Asignar campos pivote: Fruit -> área de Fila, Year -> área de Columna, Amount -> área de Datos
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")

# Construir un Estilo que se forzará en cada celda de la tabla dinámica
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

## **¿Qué API de estilo debo usar?**

La elección de la API de estilo depende del formato de archivo en el que está guardando. Use la tabla siguiente como referencia rápida.

| Formato de archivo de destino | API a usar | Notas |
|---|---|---|
| `.xls` (heredado) | `PivotTable.auto_format_type` | Valores de `aspose.cells.pivot.PivotTableAutoFormatType` (p. ej. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Se ignora al guardar en formatos modernos. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo integrado) | `PivotTable.pivot_table_style_type` | Valores de `aspose.cells.PivotTableStyleType` (temas claros/oscuros, incluidas las adiciones de Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, estilo personalizado) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Use cuando los preajustes integrados no sean suficientes. Configure mediante `table_style_element.set_element_style(...)`. |
| Cualquier formato (anulación uniforme) | `PivotTable.format_all(Style)` | Acceso directo que anula cualquier otra configuración de estilo en toda la tabla dinámica. |

En caso de duda, guarde como `.xlsx` y use `pivot_table_style_type` para los temas integrados, o `pivot_table_style_name` para los temas personalizados.

{{< app/cells/assistant language="python" >}}